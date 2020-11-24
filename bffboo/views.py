from django.shortcuts import render


def home_view(request):
    """Home"""
    user = request.user
    hello = "Hello World"

    context = {"user": user, "hello": hello}
    return render(request, "main/home.html", context)
