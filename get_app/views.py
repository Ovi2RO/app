from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    context_object_name = "posts"
    
    """
    A Django class-based view that displays a list of blog posts.

    Attributes:
        model (Post): The model class associated with this view, representing the Post model.
        template_name (str): The name of the template used to render the HTML content.
        context_object_name (str): The name used to identify the list of objects in the template context.

    Methods:
        get_queryset(): Retrieves the list of posts to be displayed.
    """

    def get_queryset(self):
        
        """
        Retrieves the filtered list of posts based on search criteria.

        Returns:
            QuerySet: The filtered list of posts.
        """
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
The get_queryset method is overridden to provide custom logic for filtering the queryset of posts based on search criteria.

The super().get_queryset() call retrieves the initial queryset defined by the parent ListView class.

The method then extracts the search parameters (search_words, search_field, search_date) from the request's GET parameters.

It applies filters to the queryset based on the search parameters. If search_words is provided, it filters by title or description. If search_date is provided, it filters by the creation date.

If no search criteria is provided, it returns the entire queryset of posts.
"""


class PostCreateView(CreateView):
    """
    A Django class-based view for creating a new blog post.

    Attributes:
        model (Post): The model class associated with this view, representing the Post model.
        fields (list): The list of fields from the model that should be included in the form.
        template_name (str): The name of the template used to render the HTML content.
        success_url (str): The URL to redirect to after successfully creating a post.

    Methods:
        form_valid(form): Overrides the default behavior to set the post author before saving.
        post(request, *args, **kwargs): Overrides the default behavior to handle file uploads and form validation.
    """

    model = Post
    fields = ["title", "description", "image"]
    template_name = "post_create.html"
    success_url = reverse_lazy("post-list")
    
    def form_valid(self, form):
        
        """
        Overrides the default behavior to set the post author before saving.

        Parameters:
            form (ModelForm): The form instance representing the blog post.

        Returns:
            HttpResponse: A response indicating the successful form submission.
        """
        
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def post(self, request, *args, **kwargs):
        
        """
        Overrides the default behavior to handle file uploads and form validation.

        Parameters:
            request (HttpRequest): The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            HttpResponse: A response indicating the success or failure of the form submission.
        """
        form = self.get_form()
        if "add_image" in request.FILES:
            form.files["image"] = request.FILES["add_image"]
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        

class PostUpdateView(UpdateView):
    
    """
    A Django class-based view for updating an existing blog post.

    Attributes:
        model (Post): The model class associated with this view, representing the Post model.
        fields (list): The list of fields from the model that should be included in the form.
        template_name (str): The name of the template used to render the HTML content.

    Methods:
        get_success_url(): Returns the URL to redirect to after successfully updating a post.
        form_valid(form): Overrides the default behavior to handle image updates and removal.
    """
    model = Post
    fields = ["title", "description", "image"]
    template_name = "post_update.html"
    
    def get_success_url(self):
        
        """
        Returns the URL to redirect to after successfully updating a post.

        Returns:
            str: The URL to redirect to.
        """
        
        return reverse_lazy("post-detail", kwargs={'pk':self.object.pk})
    
    def form_valid(self, form):
        
        """
        Overrides the default behavior to handle image updates and removal.

        Parameters:
            form (ModelForm): The form instance representing the updated blog post.

        Returns:
            HttpResponse: A response indicating the success of the form submission.
        """
        
        if form.cleaned_data.get("remove_image", False):
            if form.instance.image:
                form.instance.image.delete()
            form.instance.image = None
        elif "replace_image" in self.request.FILES:
            form.instance.image = self.request.FILES["replace_image"]
        return super().form_valid(form)
    
class PostDeleteView(DeleteView):
    
    """
    A Django class-based view for deleting an existing blog post.

    Attributes:
        model (Post): The model class associated with this view, representing the Post model.
        template_name (str): The name of the template used to render the HTML content.
        success_url (str): The URL to redirect to after successfully deleting a post.

    Methods:
        get_success_url(): Returns the URL to redirect to after successfully deleting a post.
    """
    
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("post-list")
    
    
   
    
    
class PostDetailView(DetailView):
    
    """
    A Django class-based view for displaying the details of a blog post.

    Attributes:
        model (Post): The model class associated with this view, representing the Post model.
        template_name (str): The name of the template used to render the HTML content.
        context_object_name (str): The name used to identify the object in the template context.

    Methods:
        get_context_data(**kwargs): Overrides the default behavior to include additional context data.
        get_comments_with_replies(comments): Helper method to organize comments with their replies.
        post(request, *args, **kwargs): Handles POST requests for adding, deleting comments, and replies.
    """
    
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"
    
    def get_context_data(self, **kwargs):
        
        """
        Overrides the default behavior to include additional context data.

        Returns:
            dict: A dictionary containing additional context data.
        """
        
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = post.comments.all()
        context['comments'] = self.get_comments_with_replies(comments)
        context['imageURL'] = post.imageURL
        return context

    def get_comments_with_replies(self, comments):
        
        """
        Helper method to organize comments with their replies.

        Parameters:
            comments (QuerySet): The queryset containing comments related to the post.

        Returns:
            list: A list of dictionaries containing comments and their replies.
        """
        
        comments_with_replies = []
        for comment in comments:
            comment_data = {
                'comment': comment,
                'replies': comment.reply.all()
            }
            comments_with_replies.append(comment_data)
        return comments_with_replies
    
    
    def post(self, request, *args, **kwargs):
        
        """
        Handles POST requests for adding, deleting comments, and replies.

        Parameters:
            request (HttpRequest): The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            HttpResponse: A redirect response after processing the POST request.
        """
        
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








    
    