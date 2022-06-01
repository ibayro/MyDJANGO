from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('<center><h2>Greetings</h2></center>')
