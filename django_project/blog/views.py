from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Member, CenterAdmin


def home(request):

    context = {
        'members': Member.objects.all(),
        'admins': CenterAdmin.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Member
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'members'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Member
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'members'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Member.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Member


class PostCreateView(CreateView):
    model = Member
    fields = ['first_name', 'last_name', 'email', 'center']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Member
    fields = ['first_name', 'last_name', 'image', 'email', 'center']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Member
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
