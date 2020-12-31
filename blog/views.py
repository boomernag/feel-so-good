from django.shortcuts import render


def blog(request):
    """
    A view to return about page
    """
    return render(request, 'blog/blog.html')
