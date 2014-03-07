from django.http import HttpResponse
from django.shortcuts import render
from recommender.models import Article
from recommender.forms import ArticleForm
from recommender.article_classifier import naive_bayes

def index(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        #if form.is_valid(): Add form validation
        c1=naive_bayes()
        article_list=Article.objects.all()
        for article in article_list:
            c1.train(article.content,article.category) #Should eventually be moved to database



    else:
        form = ArticleForm()
        return render(request, 'recommender/index.html',{'form':form,})
