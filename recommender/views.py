from django.http import HttpResponse
from django.shortcuts import render
from recommender.models import Article
from recommender.forms import ArticleForm
from recommender.article_classifier import naive_bayes

c1=naive_bayes()
article_list=Article.objects.all()
for article in article_list:
    c1.train(article.content,article.category)  # Should eventually be moved to database

def index(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid(): #Add form validation
            form_title = form.cleaned_data['title']
            cat = c1.classify(form.cleaned_data['content'])
            recommended_list = Article.objects.filter(category=cat).order_by('-pub_date')[:3]
            form = ArticleForm()
            context = {'articles':recommended_list,'form':form,'form_title':form_title}
        return render(request, 'recommender/index.html',context)

    else:
        form = ArticleForm()
        return render(request, 'recommender/index.html',{'form':form,})
