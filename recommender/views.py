from django.http import HttpResponse
from django.shortcuts import render
from recommender.forms import ArticleForm

def index(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
    else:
        form = ArticleForm()
    return render(request, 'recommender/index.html',{'form':form,})
