from django.shortcuts import render, render_to_response, HttpResponse


# Create your views here.
def index(request):
    context = {
        "page_title": "Главная",
    }
    return render(request, "getapp/index.html", context)


def search(request):
    if request.GET:
        message = request.GET['text']
    else:
        message = ''

    context = {
        "page_title": "Главная",
        'message': message
    }
    return render(request, "getapp/index.html", context)


def btn_click(request, pk):
    if request.is_ajax() and request.GET:
        message = request.GET['massage']
        print(f'пришло от {pk} = {message}')
        return HttpResponse("Success!")  # Sending an success response
    else:
        return HttpResponse("Request method is not a GET")