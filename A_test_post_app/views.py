from django.shortcuts import render
from .models import TestPost
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class TestPostListView(LoginRequiredMixin, ListView):
    model = TestPost
    template_name = 'A_test_post_app/test_post_list.html'
    context_object_name = 'test_posts'


class TestPostDetailView(LoginRequiredMixin, DetailView):
    model = TestPost
    template_name = 'A_test_post_app/test_post_detail.html'
    context_object_name = 'test_post'


class TestPostCreateView(LoginRequiredMixin, CreateView):
    model = TestPost
    fields = ['title', 'description']
    template_name = 'A_test_post_app/test_post_create.html'
    success_url = reverse_lazy('test-post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TestPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = TestPost
    fields = ['title', 'description']
    template_name = 'A_test_post_app/test_post_edit.html'
    
    def get_success_url(self):
        return reverse_lazy('test-post-detail', kwargs={'pk':self.object.pk})
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_staff


class TestPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = TestPost
    template_name = 'A_test_post_app/test_post_delete.html'
    success_url = reverse_lazy('test-post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_staff


