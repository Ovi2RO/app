from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .models import Post, LaikaProfileUser, Pet
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from dj_proj.mixins import AuthorOrStaffRequiredMixin
from .custom_form import ProfileForm, PetForm


@method_decorator(login_required, name = 'dispatch')
class PostListView(ListView):
    model = Post
    template_name = 'laika/post_list.html'
    context_object_name = 'posts'
    
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
- `@method_decorator(login_required, name='dispatch')` is a decorator that applies the `login_required` decorator 
to the `dispatch` method of the `PostListView` class. This decorator ensures that only authenticated users can 
access the view.

- `class PostListView(ListView):` defines a class-based view that inherits from the `ListView` class provided by 
Django. This view is responsible for displaying a list of posts.

- `model = Post` specifies the model that the view should use for querying the database. It is the `Post` model.

- `template_name = 'laika/post_list.html'` specifies the template that should be used to render the view. It is 
the `post_list.html` template located in the `laika` directory.

- `context_object_name = 'posts'` specifies the name of the context variable that will be passed to the template. 
It is `posts`, which means that the list of posts retrieved from the database will be available in the template as 
`posts`.

- `def get_queryset(self):` is a method that is called to retrieve the queryset of posts that should be displayed 
in the view. It overrides the default implementation provided by the `ListView` class.

- `queryset = super().get_queryset()` retrieves the default queryset from the parent class.

- `search_words = self.request.GET.get("search_words")` retrieves the value of the `search_words` parameter from 
the GET request.

- `search_field = self.request.GET.get("search_field")` retrieves the value of the `search_field` parameter from 
the GET request.

- `search_date = self.request.GET.get("search_date")` retrieves the value of the `search_date` parameter from the 
GET request.

- The following `if` statements check if the `search_words` and `search_date` parameters have values and apply 
corresponding filters to the queryset. If no search parameters are provided, the default queryset is returned.

- Finally, the modified queryset is returned.

By using this view, you can display a list of posts with optional search functionality based on the provided 
parameters in the GET request.
"""

        
@method_decorator(login_required, name = 'dispatch')
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'description', 'image'] 
    template_name = 'post_create.html'
    success_url = reverse_lazy('laika-post-list')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        
        return super().form_valid(form) 
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        
        if "add_image" in request.FILES:
            form.files['image'] = request.FILES["add_image"]
        
        if form.is_valid():
            return self.form_valid(form)
        else: 
            return self.form_invalid(form)

"""
- `@method_decorator(login_required, name='dispatch')` is a decorator that applies the `login_required` decorator 
to the `dispatch` method of the `PostCreateView` class. This decorator ensures that only authenticated users can 
access the view.

- `class PostCreateView(CreateView):` defines a class-based view that inherits from the `CreateView` class 
provided by Django. This view is responsible for creating a new `Post` object.

- `model = Post` specifies the model that the view should use for creating new objects. It is the `Post` model.

- `fields = ['title', 'description', 'image']` specifies the fields that should be displayed in the form for 
creating a new `Post` object.

- `template_name = 'post_create.html'` specifies the template that should be used to render the view. It is the 
`post_create.html` template.

- `success_url = reverse_lazy('laika-post-list')` specifies the URL to redirect to after a successful form 
submission. In this case, it is the URL named `laika-post-list`.

- `def form_valid(self, form):` is a method that is called when the form is valid. It is responsible for 
performing any additional processing before saving the form. It sets the `author` field of the `Post` object to 
the currently logged-in user.

- `return super().form_valid(form)` calls the `form_valid` method of the parent class to save the form and return 
a response indicating success.

- `def post(self, request, *args, **kwargs):` is a method that is called when a POST request is made to the view. 
It is responsible for handling the form submission.

- `form = self.get_form()` retrieves the form instance for the view.

- `if "add_image" in request.FILES:` checks if an image file was uploaded in the request.

- `form.files['image'] = request.FILES["add_image"]` assigns the uploaded image file to the `image` field of the 
form.

- `if form.is_valid():` checks if the form is valid.

- `return self.form_valid(form)` calls the `form_valid` method to save the form and return a response indicating 
success.

- `return self.form_invalid(form)` returns a response indicating that the form is invalid.

By using this view, you can display a form for creating a new `Post` object, handle form submissions, and perform 
additional processing before saving the form.
"""


@method_decorator(login_required, name = 'dispatch')
class PostDetailView(DetailView):
    model = Post
    template_name = "laika/post_detail.html"
    context_object_name = "post"
    
"""
- `@method_decorator(login_required, name='dispatch')` is a decorator that applies the `login_required` decorator 
to the `dispatch` method of the `PostDetailView` class. This decorator ensures that only authenticated users can 
access the view.

- `class PostDetailView(DetailView):` defines a class-based view that inherits from the `DetailView` class 
provided by Django. This view is responsible for displaying the details of a `Post` object.

- `model = Post` specifies the model that the view should use for retrieving the object. It is the `Post` model.

- `template_name = "laika/post_detail.html"` specifies the template that should be used to render the view. It is 
the `post_detail.html` template located in the `laika` directory.

- `context_object_name = "post"` specifies the name of the variable that will be used to access the `Post` object 
in the template. It will be available as `post`.

By using this view, you can display the details of a specific `Post` object, such as its title, description, and 
other fields.
"""

    
@method_decorator(login_required, name = 'dispatch')
class PostUpdateView(AuthorOrStaffRequiredMixin ,UpdateView):
    model = Post
    fields = ['title', 'description', 'image'] 
    template_name = "laika/post_update.html"
    
    def get_success_url(self):
        return reverse_lazy('laika-post-detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        if form.cleaned_data.get("remove_image", False):
            if form.instance.image:
                form.instance.image.delete()
            form.instance.image = None
        elif "replace_image" in self.request.FILES:
            form.instance.image = self.request.FILES["replace_image"]
        return super().form_valid(form)
    
"""
- `@method_decorator(login_required, name='dispatch')` is a decorator that applies the `login_required` decorator 
to the `dispatch` method of the `PostUpdateView` class. This decorator ensures that only authenticated users can 
access the view.

- `class PostUpdateView(AuthorOrStaffRequiredMixin, UpdateView):` defines a class-based view that inherits from 
the `UpdateView` class provided by Django. This view is responsible for updating an existing `Post` object.

- `model = Post` specifies the model that the view should use for retrieving and updating the object. It is the 
`Post` model.

- `fields = ['title', 'description', 'image']` specifies the fields that should be displayed in the form for 
updating the `Post` object.

- `template_name = "laika/post_update.html"` specifies the template that should be used to render the view. It is 
the `post_update.html` template located in the `laika` directory.

- `def get_success_url(self):` is a method that returns the URL to redirect to after a successful form submission.

- `return reverse_lazy('laika-post-detail', kwargs={'pk': self.object.pk})` generates the URL for the `Post` 
detail view (`laika-post-detail`) using the primary key (`pk`) of the updated `Post` object.

- `def form_valid(self, form):` is a method that is called when the form is valid. It is responsible for 
performing any additional processing before saving the form. It handles the logic for removing or replacing the 
image associated with the `Post` object.

- `if form.cleaned_data.get("remove_image", False):` checks if the "remove_image" field in the form's cleaned 
data is set to `True`. This field can be added to the form to allow the user to indicate whether they want to 
remove the image.

- `if form.instance.image:` checks if the `Post` object has an image associated with it.

- `form.instance.image.delete()` deletes the image file associated with the `Post` object.

- `form.instance.image = None` sets the `image` field of the `Post` object to `None`.

- `elif "replace_image" in self.request.FILES:` checks if a new image file was uploaded in the request.

- `form.instance.image = self.request.FILES["replace_image"]` assigns the uploaded image file to the `image` 
field of the `Post` object.

- `return super().form_valid(form)` calls the `form_valid` method of the parent class to save the form and return 
a response indicating success.

By using this view, you can display a form for updating an existing `Post` object, handle form submissions, and 
perform additional processing before saving the form.
"""
    

@method_decorator(login_required, name = 'dispatch')
class PostDeleteView(AuthorOrStaffRequiredMixin ,DeleteView):
    model = Post
    template_name = "laika/post_delete.html"
    success_url = reverse_lazy('laika-post-list') 

"""
- `@method_decorator(login_required, name='dispatch')` is a decorator that applies the `login_required` decorator 
to the `dispatch` method of the `PostDeleteView` class. This decorator ensures that only authenticated users can 
access the view.

- `class PostDeleteView(AuthorOrStaffRequiredMixin, DeleteView):` defines a class-based view that inherits from 
the `DeleteView` class provided by Django. This view is responsible for deleting an existing `Post` object.

- `model = Post` specifies the model that the view should use for retrieving and deleting the object. It is the 
`Post` model.

- `template_name = "laika/post_delete.html"` specifies the template that should be used to render the view. It is 
the `post_delete.html` template located in the `laika` directory.

- `success_url = reverse_lazy('laika-post-list')` specifies the URL to redirect to after a successful deletion. 
It is the URL pattern named `laika-post-list`, which is typically associated with a view that lists all `Post` 
objects.

By using this view, you can display a confirmation page for deleting an existing `Post` object and handle the 
deletion upon user confirmation.
"""
    

@method_decorator(login_required, name = 'dispatch')
class LaikaProfileView(View):
    template_name = "laika/profile.html"
            
    def get(self, request):
        try:
            profile = LaikaProfileUser.objects.get(laika_user=request.user)
            pet = Pet.objects.get(owner=request.user)
            
            profile_form = ProfileForm(instance=profile)
            pet_form = PetForm(instance=pet)
        except (LaikaProfileUser.DoesNotExist, Pet.DoesNotExist):
            profile_form = ProfileForm()
            pet_form = PetForm()    
        
        return render(request, self.template_name, {"profile_form": profile_form, "pet_form": pet_form})
    
    def post(self, request):
        profile, create = LaikaProfileUser.objects.get_or_create(laika_user=request.user)
        pet, create = Pet.objects.get_or_create(owner=request.user)
        
        profile_form = ProfileForm(request.POST, request.FILES, instance = profile)
        pet_form = PetForm(request.POST, instance = pet)
        
        if profile_form.is_valid() and pet_form.is_valid():
            profile_form.save()
            pet_form.save()
            
            return redirect("laika-profile")  
        
        return render(request, self.template_name, {"profile_form": profile_form, "pet_form": pet_form})            

"""
- `@method_decorator(login_required, name='dispatch')` is a decorator that applies the `login_required` decorator 
to the `dispatch` method of the `LaikaProfileView` class. This decorator ensures that only authenticated users can 
access the view.

- `class LaikaProfileView(View):` defines a class-based view that inherits from the `View` class provided by 
Django. This view is responsible for handling the profile page for a user.

- `template_name = "laika/profile.html"` specifies the template that should be used to render the view. It is the 
`profile.html` template located in the `laika` directory.

- `def get(self, request):` is a method that handles HTTP GET requests to the view. It retrieves the user's 
profile and pet information, if available, and populates the corresponding forms (`ProfileForm` and `PetForm`) 
with the retrieved data.

- `profile = LaikaProfileUser.objects.get(laika_user=request.user)` retrieves the `LaikaProfileUser` object 
associated with the currently logged-in user.

- `pet = Pet.objects.get(owner=request.user)` retrieves the `Pet` object associated with the currently logged-in 
user.

- `profile_form = ProfileForm(instance=profile)` creates an instance of the `ProfileForm` form and populates it 
with the retrieved `LaikaProfileUser` object.

- `pet_form = PetForm(instance=pet)` creates an instance of the `PetForm` form and populates it with the 
retrieved `Pet` object.

- `except (LaikaProfileUser.DoesNotExist, Pet.DoesNotExist):` handles the case when the `LaikaProfileUser` or 
`Pet` objects do not exist for the currently logged-in user. In this case, it creates empty instances of the forms.

- `return render(request, self.template_name, {"profile_form": profile_form, "pet_form": pet_form})` renders the 
`profile.html` template with the populated forms as context variables.

- `def post(self, request):` is a method that handles HTTP POST requests to the view. It processes the submitted 
forms and saves the data.

- `profile, create = LaikaProfileUser.objects.get_or_create(laika_user=request.user)` retrieves the 
`LaikaProfileUser` object associated with the currently logged-in user or creates a new one if it doesn't exist.

- `pet, create = Pet.objects.get_or_create(owner=request.user)` retrieves the `Pet` object associated with the 
currently logged-in user or creates a new one if it doesn't exist.

- `profile_form = ProfileForm(request.POST, request.FILES, instance=profile)` creates an instance of the 
`ProfileForm` form and populates it with the submitted data, including files, and associates it with the retrieved 
or created `LaikaProfileUser` object.

- `pet_form = PetForm(request.POST, instance=pet)` creates an instance of the `PetForm` form and populates it with 
the submitted data and associates it with the retrieved or created `Pet` object.

- `if profile_form.is_valid() and pet_form.is_valid():` checks if both forms are valid.

- `profile_form.save()` saves the data from the `ProfileForm` form to the associated `LaikaProfileUser` object.

- `pet_form.save()` saves the data from the `PetForm` form to the associated `Pet` object.

- `return redirect("laika-profile")` redirects the user to the "laika-profile" URL after successful form submission.

- `return render(request, self.template_name, {"profile_form": profile_form, "pet_form": pet_form})` renders the 
`profile.html` template with the forms as context variables if the forms are not valid.

By using this view, you can display and handle the user profile page, allowing the user to view and update their 
profile and pet information.
"""


          