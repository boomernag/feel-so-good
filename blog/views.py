from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.views import generic
from .forms import PostForm
from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


@login_required
def add_post(request):
    """ Add a post to the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Successfully added post!')
            return redirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(request, 'Failed to add post. Please ensure the form is valid.')
    else:
        form = PostForm()

    template = 'blog/add_post.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_post(request, product_id):
    """ Edit a post in the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(post, pk=post_slug)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated form!')
            return redirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(request, 'Failed to update post. Please ensure the form is valid.')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing {post.title}')
    template = 'blog/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }
    return render(request, template, context)


@login_required
def delete_post(request, post_slug):
    """ Delete a post from the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, pk=post_slug)
    post.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('blog'))