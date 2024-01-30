from django.http import HttpResponse

#All view functions must accept a request because they are routes

def index(request):
    return HttpResponse("Hello World!")

def files(request):
    return render(request,"files/files.html",)