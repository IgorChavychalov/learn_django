from django.shortcuts import render, render_to_response, HttpResponse


# Create your views here.
def index(request):
    context = {
        "page_title": "Главная",
    }
    return render(request, "postapp/index.html", context)


def search(request):
    if request.POST:
        message = request.POST['text']
    else:
        message = ''

    context = {
        "page_title": "Главная",
        'message': message
    }
    return render(request, "postapp/index.html", context)

