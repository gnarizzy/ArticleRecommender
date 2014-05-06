#Create the classifier, the test set, and the training set
#Train the classifier, test it against the test set and keep track of the results
#Output the results

from recommender.models import Article
from recommender.article_classifier import naive_bayes

#create the classifier, training set, and test set
classifier = naive_bayes()
articles = Article.objects.all()
training_set = articles[:200]
test_set = articles[200:]

#Train the classifier
for article in training_set:
    classifier.train(article.content, article.category)

#classify the test set and record the results
correct = 0.0
incorrect = 0.0
for article in test_set:
    if classifier.classify(article.content) == article.category: #correct
        correct+=1
    else: #incorrect
        incorrect+=1

print "Correct: " + str(correct) + " Incorrect: "+ str(incorrect)+ " Accuracy: " + str(correct/(incorrect+ correct))
