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


@method_decorator(login_required, name = 'dispatch')
class PostDetailView(DetailView):
    model = Post
    template_name = "laika/post_detail.html"
    context_object_name = "post"
    
    
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
    

@method_decorator(login_required, name = 'dispatch')
class PostDeleteView(AuthorOrStaffRequiredMixin ,DeleteView):
    model = Post
    template_name = "laika/post_delete.html"
    success_url = reverse_lazy('laika-post-list') 
    

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
        
        print(request.FILES)
        
        print(request.POST)
        
        
        profile_form = ProfileForm(request.POST, request.FILES, instance = profile)
        pet_form = PetForm(request.POST, instance = pet)
        
        if profile_form.is_valid() and pet_form.is_valid():
            profile_form.save()
            pet_form.save()
            
            # profile, create = LaikaProfileUser.objects.get_or_create(laika_user=request.user)
            # pet, create = Pet.objects.get_or_create(owner=request.user)
            
            return redirect("laika-profile")  
        
        return render(request, self.template_name, {"profile_form": profile_form, "pet_form": pet_form})            

















           
            
            
            
            