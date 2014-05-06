import re
import math

#Classifies articles into one of 10 categories

class classifier:
    def __init__(self, file_name=None):
        self.feature_count={} #feature-category counts
        self.category_count={} #number of documents in each category

    #returns total number of features in classifier
    def num_features(self):
        return len(self.feature_count)

    #increments feature-category count, i.e. {'Putin': {'International':5, 'Domestic':3},'UN':...}
    def inc_feature_count(self, feature, category):
        self.feature_count.setdefault(feature,{})
        self.feature_count[feature].setdefault(category,0)
        self.feature_count[feature][category]+=1

    #returns a dictionary of unique words in text
    def get_words(self,text):
        splitter=re.compile('\\W*') #split on non alphabet characters
        words = [word.lower() for word in splitter.split(text)]
        return dict([(word,1) for word in words])

    #increase category count
    def inc_category_count(self, category):
        self.category_count.setdefault(category,0)
        self.category_count[category]+=1

    #returns number of times feature appears in a category
    def feat_count(self,feature,category):
        if feature in self.feature_count and category in self.feature_count[feature]:
            return float(self.feature_count[feature][category])
        return 0.0

    #number of documents in a particular category
    def cat_count(self, category):
        if category in self.category_count:
            return float(self.category_count[category])
        return 0

    #Total number of documents
    def total_count(self):
        return sum(self.category_count.values())

    #All categories
    def categories(self):
        return self.category_count.keys()

    #breaks down document features, then increments counts appropriately
    def train(self,text,category):
        features=self.get_words(text)
        for feature in features:
            self.inc_feature_count(feature, category)
        self.inc_category_count(category)

    #calculates feature probabilities
    def feature_probability(self,feature,category):
        if self.cat_count(category)==0:
            return 0
        return self.feat_count(feature,category)/self.cat_count(category)

    #Begins with starting weight of .5 for reach feature
    def weighted_probability(self, feature, category, feature_probability, weight=1.0, assumed_prob=0.5):
        current_probability=feature_probability(feature, category)
        total= sum([self.feat_count(feature,cat) for cat in self.categories()])
        weighted= ((weight*assumed_prob)+(total*current_probability))/(weight+total)
        return weighted

class naive_bayes(classifier):
    #overall probability of being a specific article, given the category
    def article_probability(self, text, category):
        features = self.get_words(text)
        probability=1
        for feature in features:
            probability*=self.weighted_probability(feature,category,self.feature_probability)
        return probability

    #uses Bayes Theorem to give the probability of being in a category, given an article
    def probability(self, text, category):
        cat_prob=self.cat_count(category)/self.total_count()
        art_prob=self.article_probability(text,category)
        return art_prob*cat_prob

    #Classifies text into category with the highest probability
    def classify(self,text):
        best=''
        probabilities={}
        max= 0.0
        for category in self.categories():
            probabilities[category]=self.probability(text,category)
            if probabilities[category]>=max:
                max=probabilities[category]
                best=category
        return best


#len(self.feature_count) for number of features

    #def accuracy(self, size):
