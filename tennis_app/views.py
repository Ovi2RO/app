from typing import Any
from django.http import HttpResponse

from django.shortcuts import get_object_or_404,render,redirect
from django.views.generic import (TemplateView,
                                  ListView,
                                  CreateView,
                                  DeleteView,
                                  UpdateView,
                                  DetailView,
                                  View)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Posts
from django.urls import path, reverse_lazy
from django.contrib import messages
from tennis_app import forms
from datetime import datetime, timedelta


class PostListView(LoginRequiredMixin,ListView):
    model = Posts
    template_name = 'tennis/post_search.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['form']= forms.SearchForm()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = forms.SearchForm(self.request.GET)
        if form.is_valid():
            
            start_age = form.cleaned_data.get('start_age')
            end_age = form.cleaned_data.get('end_age')
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            location = form.cleaned_data.get('location')
            level = form.cleaned_data.get('level')
            language = form.cleaned_data.get('language')
            gender = form.cleaned_data.get('gender')

            # Customize the queryset based on your search criteria
            # This is just a simple example, adjust it based on your model fields
            if start_age and end_age:
                end_year = datetime.now().year - start_age
                start_year = datetime.now().year - end_age-1 
                start_date_str = f"{start_year}-01-01T00:00:00Z"
                end_date_str = f"{end_year}-12-31T23:59:59Z"
                queryset = queryset.filter(birth_date__range=(start_date_str, end_date_str))

            if start_date and end_date:
                queryset = queryset.filter(play_date__range=(start_date,end_date))
         
            if location:
                queryset = queryset.filter(club_name__icontains=location)
                
            if level!= 'A':
                queryset = queryset.filter(level=level)

            if language != 'A':
                 queryset = queryset.filter(language=language)
           
            if gender != 'A':
                queryset = queryset.filter(user_gender=gender)             
                
            if not ( start_date or end_date or location or level or language or gender):
              queryset = self.model.objects.all()

            return queryset

"""
- `model`: This attribute specifies the model class that the view will be working with, it is a model `Posts`.
- `template_name`: This attribute specifies the template to be used for rendering the view, in this case, it is 
set to `'tennis/post_search.html'`.
- `context_object_name`: This attribute specifies the name of the variable that will be used in the template to 
access the list of objects, it is set to `'posts'`.
- `get_context_data(self, **kwargs: Any)`: This method is overridden to add extra context data to be used in the 
template. It calls the parent class method to get the initial context data and then adds a `'form'` key with an 
instance of `forms.SearchForm()` as its value.
- `get_queryset(self)`: This method is overridden to customize the queryset based on the search criteria provided 
in the `forms.SearchForm`. It retrieves the form data from the request, performs filtering on the `queryset` based 
on the form data, and returns the modified queryset.
"""


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Posts
    form_class = forms.CreatePostForm
    template_name = 'tennis/post_create.html'
    success_url = reverse_lazy('tennis-post-list')

    def form_valid(self, form):
        print('It is a message')
        messages.success(self.request, 'Created successfully')
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)

"""
- `model = Posts`: This specifies the model that the view is associated with, in this case, the `Posts` model.
- `form_class = forms.CreatePostForm`: This specifies the form class to be used for creating the post. It is 
a custom form defined in the `forms` module.
- `template_name = 'tennis/post_create.html'`: This specifies the template to be rendered when the view is accessed.
- `success_url = reverse_lazy('tennis-post-list')`: This sets the URL to redirect to after a successful form 
submission. It uses the `reverse_lazy` function to provide a URL pattern name.
- `def form_valid(self, form)`: This is a method that is called when the form is valid. It overrides the default 
behavior of the `CreateView` class.
- `print('It is a message')`: This line prints the message "It is a message" to the console.
- `messages.success(self.request, 'Created successfully')`: This line adds a success message to be displayed to 
the user. It uses the `messages` framework to handle user notifications.
- `form.instance.user = self.request.user`: This line sets the `user` attribute of the form instance to the 
currently logged-in user.
- `return super(PostCreateView, self).form_valid(form)`: This line calls the `form_valid` method of the parent 
class to handle the form validation and saving process.
"""
    

class PostDetailView(LoginRequiredMixin,DetailView):
    template_name = 'tennis/post_detail.html'

    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Posts, pk=self.kwargs['pk'])
        comments = post.comments.all()
        comment_form = forms.CommentForm()

        context = {
            'post': post,
            'comments': comments,
            'comment_form': comment_form,
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Posts, pk=self.kwargs['pk'])
        form = forms.CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()

        return redirect('tennis-post-detail', pk=post.pk)

"""
The "PostDetailView" class inherits from two other classes, namely "LoginRequiredMixin" and "DetailView". The view 
requires the user to be logged in and that it is based on Django's built-in "DetailView" class, which provides 
functionality for displaying a single object.

The "template_name" attribute specifies the path to the template file that will be used to render the view, in 
this case, 'tennis/post_detail.html'.

The class has two methods, "get" and "post", which handle HTTP GET and POST requests, respectively.

In the "get" method, the code retrieves the post object based on the provided primary key (pk) using the 
"get_object_or_404" function. It also retrieves all comments associated with the post and initializes a comment 
form. The retrieved objects are then passed to the template context, which will be used to render the template 
with the necessary data.

The "post" method is responsible for handling the submission of comment forms. It retrieves the post object and 
creates an instance of the comment form, populated with the data from the request. If the form is valid, it saves 
the comment object with the associated post and author information. Finally, it redirects the user to the 
'tennis-post-detail' view for the specific post.
"""

   
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posts
    form_class = forms.UpdatePostForm
    template_name = 'tennis/post_update.html'

    def get_success_url(self):
        return reverse_lazy('tennis-post-detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        # Handle the form submission, including the file upload
        messages.success(self.request, 'Updated successfully')
        return super(PostUpdateView, self).form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author or self.request.user.is_staff:
            return True
        return False

"""
The "PostUpdateView" class is a Django view that handles the updating of a specific post. It is designed to be 
used in conjunction with a form to allow users to edit and update the content of a post. This class inherits from 
multiple Django mixins, including "LoginRequiredMixin" and "UserPassesTestMixin", to enforce authentication and 
permission checks.

Key attributes and methods of the "PostUpdateView" class include:

- "model": Specifies the model that the view operates on, in this case, the "Posts" model.
- "form_class": Specifies the form class to be used for updating the post, the "UpdatePostForm" form.
- "template_name": Specifies the template used to render the update view, which is set to 'tennis/post_update.html'.
- "get_success_url()": Overrides the default behavior of determining the URL to redirect to after a successful 
update. It uses the reverse_lazy() function to generate the URL for the "tennis-post-detail" view, passing the 
primary key (pk) of the updated object.
- "form_valid(form)": Overrides the default behavior when the form is valid and submitted. It handles the form 
submission, including any additional processing or actions. It displays a success message using the messages 
framework and then calls the parent class's form_valid() method.
- "test_func()": Overrides the default behavior of the "UserPassesTestMixin" to determine whether the current 
user has permission to update the post. It checks if the user is the author of the post or if the user is a staff 
member.
"""


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Posts
    template_name = 'tennis/post_delete.html'
    context_object_name = 'posts'
    success_url = reverse_lazy('tennis-post-list')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

"""
The `PostDeleteView` class is a view in a web application that handles the deletion of a specific post. It is 
designed to be used in conjunction with other Django mixins, namely `LoginRequiredMixin` and `UserPassesTestMixin`, 
to enforce certain conditions and permissions.

- `LoginRequiredMixin` ensures that only authenticated users can access this view. If a user is not logged in, 
they will be redirected to the login page.
- `UserPassesTestMixin` provides a mechanism to test whether a user passes a specific condition before allowing 
access to the view. It checks if the logged-in user is the author of the post being deleted.

The view inherits from Django's `DeleteView`, which is a generic view that handles the deletion of a model 
instance. The specific model being operated on is `Posts`.

The `template_name` attribute specifies the template used to render the confirmation page for deleting the post. 
It is set to `'tennis/post_delete.html'`.

The `context_object_name` attribute defines the name of the variable that will be used in the template to 
represent the post being deleted. It is set to `'posts'`.

The `success_url` attribute determines the URL to which the user will be redirected after successfully deleting 
the post. It uses Django's `reverse_lazy` function to provide a URL pattern name, `'tennis-post-list'`, which 
will be resolved to the corresponding URL.

Finally, the `test_func` method is implemented to check if the logged-in user is the author of the post. It 
retrieves the post object using `self.get_object()` and compares the author with the current user. If they match, 
the method returns `True`, indicating that the user passes the test and has permission to delete the post. 
Otherwise, it returns `False`.
"""        
  


