from typing import Any
from django.shortcuts import redirect
from .models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from dj_proj.mixins import AuthorOrStaffRequiredMixin


@method_decorator(login_required, name='dispatch')      
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
    
"""
- `@method_decorator(login_required, name='dispatch')` is a method decorator that applies the 
`login_required` decorator to the `dispatch` method of the `PostListView` class. This decorator 
ensures that only authenticated users can access the view.

- `PostListView` is a class-based view that inherits from `ListView`. It represents a view that 
lists all the posts.

- `model = Post` specifies the model associated with the view, in this case, the `Post` model.

- `template_name = "post_list.html"` specifies the template to use for rendering the view.

- `context_object_name = "posts"` specifies the name of the variable to use in the template for the 
list of posts.

- `get_queryset()` is a method that returns the queryset of posts to be displayed in the view. It 
first calls the `get_queryset()` method of the parent class to get the default queryset. It then 
filters the queryset based on the `search_words`, `search_field`, and `search_date` parameters obtained 
from the request. If no search parameters are provided, it returns all the posts.
"""
    

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

"""
- `@method_decorator(login_required, name='dispatch')` is a method decorator that applies the 
`login_required` decorator to the `dispatch` method of the `PostCreateView` class. This decorator 
ensures that only authenticated users can access the view.

- `PostCreateView` is a class-based view that inherits from `CreateView`. It represents a view for 
creating a new post.

- `model = Post` specifies the model associated with the view, in this case, the `Post` model.

- `fields = ["title", "description", "image"]` specifies the fields of the model that will be included 
in the form for creating a new post.

- `template_name = "post_create.html"` specifies the template to use for rendering the view.

- `success_url = reverse_lazy("post-list")` specifies the URL to redirect to after a successful form 
submission. It redirects to the "post-list" URL.

- `form_valid(form)` is a method that is called when the form is submitted and valid. It sets the author 
of the post to the currently authenticated user and then calls the `form_valid()` method of the parent class.

- `post(self, request, *args, **kwargs)` is a method that is called when a POST request is made to the view. 
It first gets the form using `self.get_form()`. If there is an uploaded file with the key "add_image" in the 
request, it sets that file as the value of the "image" field in the form. It then checks if the form is valid. 
If it is valid, it calls the `form_valid()` method. If it is not valid, it calls the `form_invalid()` method.
"""
  

@method_decorator(login_required, name='dispatch')
class PostUpdateView(AuthorOrStaffRequiredMixin, UpdateView):
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
    
"""
- `@method_decorator(login_required, name='dispatch')` is a method decorator that applies the 
`login_required` decorator to the `dispatch` method of the `PostUpdateView` class. This decorator 
ensures that only authenticated users can access the view.

- `PostUpdateView` is a class-based view that inherits from `UpdateView`. It represents a view for 
updating an existing post.

- `AuthorOrStaffRequiredMixin` is a custom mixin that provides authorization checks to ensure that only 
the author of the post or staff members can access the view.

- `model = Post` specifies the model associated with the view, in this case, the `Post` model.

- `fields = ["title", "description", "image"]` specifies the fields of the model that will be included 
in the form for updating a post.

- `template_name = "post_update.html"` specifies the template to use for rendering the view.

- `get_success_url()` is a method that returns the URL to redirect to after a successful form submission. 
In this example, it uses the `reverse_lazy()` function to generate the URL for the "post-detail" view and 
passes the primary key (`pk`) of the updated post as a keyword argument.

- `form_valid(form)` is a method that is called when the form is submitted and valid. It checks if the 
"remove_image" field in the form's cleaned data is `True`. If it is, it deletes the existing image associated 
with the post (if any) and sets the "image" field to `None`. If the "replace_image" key is present in the 
uploaded files, it sets the "image" field to the uploaded file. Finally, it calls the `form_valid()` method 
of the parent class.
"""
    

@method_decorator(login_required, name='dispatch')
class PostDeleteView(AuthorOrStaffRequiredMixin, DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("post-list")

"""
- `PostDeleteView` is a class-based view that inherits from `DeleteView`. It represents a view for deleting 
an existing post.

- `AuthorOrStaffRequiredMixin` is a custom mixin that provides authorization checks to ensure that only the 
author of the post or staff members can access the view.

- `model = Post` specifies the model associated with the view, in this case, the `Post` model.

- `template_name = "post_delete.html"` specifies the template to use for rendering the view.

- `success_url = reverse_lazy("post-list")` specifies the URL to redirect to after a successful deletion. It 
redirects to the "post-list" URL.
"""

    
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
        for comment in comments.order_by('-created_at'):
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

"""
- `@method_decorator(login_required, name='dispatch')` is a method decorator that applies the 
`login_required` decorator to the `dispatch` method of the `PostDetailView` class. This decorator 
ensures that only authenticated users can access the view.

- `PostDetailView` is a class-based view that inherits from `DetailView`. It represents a view for 
displaying the details of a post.

- `model = Post` specifies the model associated with the view, in this case, the `Post` model.

- `template_name = "post_detail.html"` specifies the template to use for rendering the view.

- `context_object_name = "post"` specifies the name of the variable that will be used to access the 
post object in the template.

- `get_context_data(self, **kwargs)` is a method that adds additional context data to be used in the 
template. It retrieves the comments associated with the post and organizes them into a list of dictionaries 
containing the comment and its replies. It also adds the `imageURL` attribute of the post to the context.

- `get_comments_with_replies(self, comments)` is a helper method that takes a queryset of comments and returns 
a list of dictionaries, each containing a comment and its replies.

- `post(self, request, *args, **kwargs)` is a method that is called when the view receives a POST request. 
It handles the creation of new comments and replies, as well as the deletion of comments and replies. It 
retrieves the necessary data from the request's POST data and performs the appropriate actions based on the 
data. Finally, it redirects the user back to the post detail page.
"""






    
    