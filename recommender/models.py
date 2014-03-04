from django.db import models

class Article(models.Model):
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=500)
    CATEGORY_CHOICES = (
        ('economy','Economy'),
        ('stem','STEM'),
        ('middle east','Middle East'),
        ('pop culture','Pop Culture'),
        ('elections','Elections'),
        ('domestic political issues','Domestic Political Issues'),
        ('international political issues','International Political Issues'),
        ('georgia','Georgia/UGA'),
        ('totally international','Totes International'),

    )
    category=models.CharField(max_length=200,choices=CATEGORY_CHOICES) #Article category choices
    url=models.URLField()
    content=models.TextField()
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.title