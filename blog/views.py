from django.shortcuts import render


def blog(request):
    """
    A view to return blog page
    """
    return render(request, 'blog/blog.html')
