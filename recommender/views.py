from django.http import HttpResponse

def index(request):
    return HttpResponse("Future site of the world famous GPR Recommender!")