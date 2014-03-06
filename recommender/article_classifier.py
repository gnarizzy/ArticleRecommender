import re
import math

#Classifies articles into one of 10 categories

#returns a dictionary of unique words in text
def get_words(text):
    splitter=re.compile('\\W*') #non alphabet characters
    words = [word.lower() for word in splitter.split(text)]
    return dict([(word,1) for word in words])

class classifier:
    def __init__(self, get_features, file_name=None):
        self.feature_count={} #feature-category counts
        self.category_count={} #number of documents in each category
        self.get_features=get_features #function used to get features, in this case get_words

    #increments feature-category count
    def inc_feature_count(self, feature, category):
        self.feature_count.setdefault(feature,{})
        self.feature_count[feature].setdefault(category,0)
        self.feature_count[feature][category]+=1

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
        features=self.get_features(text)
        for feature in features:
            self.inc_feature_count(feature, category)
        self.inc_category_count(category)
