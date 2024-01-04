from typing import Any
from django.shortcuts import redirect
from .models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator


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
By applying the `@login_required` decorator to the `dispatch` method of the `PostListView`, the view 
will only be accessible to authenticated users. If an unauthenticated user tries to access the view, 
they will be redirected to the login page.


The `model` attribute specifies the model class that the `ListView` should use to fetch the list 
of objects. It is set to `Post`, which means the `ListView` will fetch all the `Post` 
objects from the database.

The `template_name` attribute specifies the HTML template file that should be used to render the 
list of objects. It is set to `"post_list.html"`, which means the `ListView` will use the `post_list.html` 
template.

The `context_object_name` attribute specifies the name of the context variable that will be used in the 
template to access the list of objects. It is set to `"posts"`, which means the list of `Post` objects 
will be available as `posts` in the template.

The `get_queryset()` method is overridden to provide custom filtering and sorting of the list of objects. 
It first calls the parent class's `get_queryset()` method to get the default queryset. Then, it retrieves 
the search parameters (`search_words`, `search_field`, and `search_date`) from the request's GET parameters.

If `search_words` is provided, it filters the queryset based on the `search_field` (either "title" or 
"description"). If `search_date` is provided, it filters the queryset based on the `created_at` field. If 
neither `search_words` nor `search_date` is provided, it sets the queryset to fetch all `Post` objects.

Finally, it returns the filtered queryset.
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
By applying the `@login_required` decorator to the `dispatch` method of the `PostListView`, the view 
will only be accessible to authenticated users. If an unauthenticated user tries to access the view, 
they will be redirected to the login page.

The `CreateView` class is a generic class-based view provided by Django. It is used for creating new 
objects of a model.

`PostCreateView` class inherits from `CreateView` and provides some additional functionality.

The `model` attribute specifies the model class that the `CreateView` should use to create a new object. 
It is set to `Post`, which means the `CreateView` will create a new `Post` object.

The `fields` attribute specifies the form fields that should be displayed in the template for creating a new 
object. It is set to `["title", "description", "image"]`, which means the form will have fields for `title`, 
`description`, and `image`.

The `template_name` attribute specifies the HTML template file that should be used to render the form for 
creating a new object. It is set to `"post_create.html"`, which means the `CreateView` will use the 
`post_create.html` template.

The `success_url` attribute specifies the URL to which the user should be redirected after successfully 
creating a new object. It is set to `reverse_lazy("post-list")`, which means the user will be redirected to 
the URL named `"post-list"`.

The `form_valid()` method is overridden to provide additional logic when the form is valid. It sets the 
`author` field of the `Post` object to the currently logged-in user (`self.request.user`) before saving the form.

The `post()` method is overridden to handle the POST request for creating a new object. It first gets the 
form using `self.get_form()`. Then, it checks if the `add_image` key is present in the `request.FILES` 
dictionary. If it is, it assigns the uploaded image file to the `image` field of the form.

Next, it checks if the form is valid. If the form is valid, it calls `self.form_valid(form)` to save the 
form and perform any additional logic. If the form is not valid, it calls `self.form_invalid(form)` to handle 
the invalid form.

This code allows the user to create a new `Post` object by displaying a form with specified fields, 
handling file uploads, and redirecting the user to a specified URL after successful creation.
"""
  

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
    
"""
By applying the `@login_required` decorator to the `dispatch` method of the `PostListView`, the view 
will only be accessible to authenticated users. If an unauthenticated user tries to access the view, 
they will be redirected to the login page.

The `user_passes_test` decorator is a built-in Django decorator that allows you to define a custom test 
function to determine if a user is allowed to access a view. The test function should take a user object 
as input and return `True` if the user passes the test, or `False` otherwise. 

The `UpdateView` class is a generic class-based view provided by Django. It is used for updating existing 
objects of a model.

The `model` attribute specifies the model class that the `UpdateView` should use to update an existing object. 
It is set to `Post`, which means the `UpdateView` will update an existing `Post` object.

The `fields` attribute specifies the form fields that should be displayed in the template for updating an 
existing object. It is set to `["title", "description", "image"]`, which means the form will have fields for 
`title`, `description`, and `image`.

The `template_name` attribute specifies the HTML template file that should be used to render the form for 
updating an existing object. It is set to `post_update.html`, which means the `UpdateView` will use the 
`post_update.html` template.

The `get_success_url()` method is overridden to provide the URL to which the user should be redirected after 
successfully updating an object. It uses `reverse_lazy("post-detail", kwargs={'pk':self.object.pk})` to 
reverse the URL named `post-detail` and pass the primary key (`pk`) of the updated object as a keyword argument.

The `form_valid()` method is overridden to provide additional logic when the form is valid. It checks if the 
`remove_image` key is present in the `form.cleaned_data` dictionary. If it is, it deletes the existing image 
file associated with the `Post` object (if any) and sets the `image` field to `None`. This allows the user 
to remove the current image.

If the `replace_image` key is present in the `request.FILES` dictionary, it assigns the uploaded image file 
to the `image` field of the form. This allows the user to replace the current image with a new one.

Finally, it calls `super().form_valid(form)` to save the form and perform any additional logic.
"""
    

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(lambda u: u.is_staff or u == u.object.author), name='dispatch')
class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("post-list")

"""
By applying the `@login_required` decorator to the `dispatch` method of the `PostListView`, the view 
will only be accessible to authenticated users. If an unauthenticated user tries to access the view, 
they will be redirected to the login page.

The `user_passes_test` decorator is a built-in Django decorator that allows you to define a custom test 
function to determine if a user is allowed to access a view. The test function should take a user object 
as input and return `True` if the user passes the test, or `False` otherwise. 

`PostDeleteView` class inherits from `DeleteView` and provides some additional functionality.

The `model` attribute specifies the model class that the `DeleteView` should use to delete an object. It is 
set to `Post`, which means the `DeleteView` will delete a `Post` object.

The `template_name` attribute specifies the HTML template file that should be used to render the confirmation 
page for deleting an object. It is set to `post_delete.html`, which means the `DeleteView` will use the 
`post_delete.html` template.

The `success_url` attribute specifies the URL to which the user should be redirected after successfully 
deleting an object. It is set to `reverse_lazy("post-list")`, which means the user will be redirected to the 
URL named `"post-list"`.

This code allows the user to delete an existing `Post` object by displaying a confirmation page and handling 
the deletion process.
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

"""
By applying the `@login_required` decorator to the `dispatch` method of the `PostListView`, the view 
will only be accessible to authenticated users. If an unauthenticated user tries to access the view, 
they will be redirected to the login page.

The `model` attribute specifies the model class that the `DetailView` should use to retrieve the object 
to display. It is set to `Post`, which means the `DetailView` will retrieve a `Post` object.

The `template_name` attribute specifies the HTML template file that should be used to render the details 
of the object. It is set to `post_detail.html`, which means the `DetailView` will use the `post_detail.html` 
template.

The `context_object_name` attribute specifies the name of the variable that will be used in the template 
to access the object being displayed. It is set to `post`, which means the object will be accessible in 
the template using the variable name `post`.

The `get_context_data()` method is overridden to provide additional context data to the template. It retrieves 
the `comments` associated with the `Post` object and organizes them along with their replies into a list of 
dictionaries. It also includes the `imageURL` of the `Post` object in the context.

The `post()` method is overridden to handle HTTP POST requests sent to the view. It retrieves the `Post` object, 
the `content` of the comment or reply from the request, and the IDs of the comment or reply to delete from the 
request.

If the `content` and `parent_comment_id` are present in the request, it creates a new reply to a comment by 
retrieving the parent comment and creating a new `Comment` object with the provided content, author, and parent 
comment.

If only the `content` is present in the request, it creates a new comment on the post with the provided content 
and author.

If only the `delete_comment_id` is present in the request, it retrieves the comment to delete and deletes it 
from the database.

If only the `delete_reply_id` is present in the request, it retrieves the reply to delete and deletes it from 
the database.

Finally, it redirects the user to the `post-detail` URL for the current post.
"""






    
    