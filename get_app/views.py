from typing import Any
from django.shortcuts import redirect
from .models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')      #By applying the `@login_required` decorator to the `dispatch` method of the `PostListView`, the view will only be accessible to authenticated users. If an unauthenticated user tries to access the view, they will be redirected to the login page.
class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        search_words = self.request.GET.get("search_words")
        search_field = self.request.GET.get("search_field")
        search_date = self.request.GET.get("search_date")
        
        if search_words:
            if search_field == "title":
                queryset = queryset.filter(title__icontains = search_words)
            elif search_field == "description":
                queryset = queryset.filter(description__icontains = search_words)
        
        if search_date:
            queryset = queryset.filter(created_at__gte = search_date)
        
        if not search_words and not search_date:
            queryset = self.model.objects.all()
            
        return queryset
    

@method_decorator(login_required, name='dispatch')
class PostCreateView(CreateView):
    model = Post
    fields = ["title", "description", "image"]
    template_name = "post_create.html"
    success_url = reverse_lazy("post-list")
    
    def form_valid(self, form):
        
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def post(self, request, *args, **kwargs):

        form = self.get_form()
        if "add_image" in request.FILES:
            form.files["image"] = request.FILES["add_image"]
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(lambda u: u.is_staff or u == u.object.author), name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    fields = ["title", "description", "image"]
    template_name = "post_update.html"
    
    def get_success_url(self):

        return reverse_lazy("post-detail", kwargs={'pk':self.object.pk})
    
    def form_valid(self, form):

        if form.cleaned_data.get("remove_image", False):
            if form.instance.image:
                form.instance.image.delete()
            form.instance.image = None
        elif "replace_image" in self.request.FILES:
            form.instance.image = self.request.FILES["replace_image"]
        return super().form_valid(form)
    

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(lambda u: u.is_staff or u == u.object.author), name='dispatch')
class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("post-list")

    
@method_decorator(login_required, name='dispatch')
class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = post.comments.all()
        context['comments'] = self.get_comments_with_replies(comments)
        context['imageURL'] = post.imageURL
        return context

    def get_comments_with_replies(self, comments):
        comments_with_replies = []
        for comment in comments:
            comment_data = {
                'comment': comment,
                'replies': comment.reply.all()
            }
            comments_with_replies.append(comment_data)
        return comments_with_replies
    
    
    def post(self, request, *args, **kwargs):
        post = self.get_object()
        content = request.POST.get('content')
        
        delete_comment_id = request.POST.get('delete_comment_id')
        delete_reply_id = request.POST.get('delete_reply_id')
        
        parent_comment_id = request.POST.get('parent_comment_id')
        
        if content and parent_comment_id:
            parent_comment = Comment.objects.get(id=parent_comment_id)
            new_reply = Comment.objects.create(
                post=post,
                content=content,
                author=request.user,
                parent_comment=parent_comment
            )
        elif content:
            new_comment = Comment.objects.create(
                post=post,
                content=content,
                author=request.user
            )
        elif delete_comment_id:
            comment_to_delete = Comment.objects.get(id=delete_comment_id)
            comment_to_delete.delete()
        elif delete_reply_id:
            reply_to_delete = Comment.objects.get(id=delete_reply_id)
            reply_to_delete.delete()
            
        return redirect('post-detail', pk=post.id)








    
    