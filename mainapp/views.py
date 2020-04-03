from django.shortcuts import render, render_to_response, HttpResponse


# Create your views here.
def index(request):
    context = {
        "page_title": "Главная",
    }
    return render(request, "mainapp/index.html", context)


