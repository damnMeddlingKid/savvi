from django.db import models
from savvi.apps.users import User

class Idea(models.Model):
    author = models.ForeignKey(User)
    content = models.CharField(max_length=300)
    upvote_count = models.IntegerField()
    downvote_count = models.IntegerField()
    
class Comment(models.Model):
    author = models.ForeignKey(User)
    topic = models.ForeignKey(Idea)
    content = models.TextField()    
    

