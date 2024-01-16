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



# class HomeView(TemplateView):
# template_name = 'home.html'


# class PostListView(ListView):
# model = Posts
# template_name = 'post_list.html'
# context_object_name = 'posts'
# ordering = ['-play_date']  
# paginate_by = 10 

class PostListView(LoginRequiredMixin,ListView):
    model = Posts
    template_name = 'tennis/post_search.html' #post_list.html 
    context_object_name = 'posts'
   # ordering = ['-play_date']  
   # paginate_by = 10 
    #form_class=forms.SearchForm

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
              queryset = self.model.objects.none()

            return queryset



class PostCreateView(LoginRequiredMixin,CreateView):
    model = Posts
    form_class = forms.CreatePostForm
    template_name = 'tennis/post_create.html'
    success_url = reverse_lazy('tennis-post-list')

    def form_valid(self, form):
        print('It is a message')
        messages.success(self.request, 'Created successfully')
        form.instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)
    

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

   
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
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

        
  


