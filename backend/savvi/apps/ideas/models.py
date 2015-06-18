from enum import Enum
from django.db import models
from django.contrib.auth.models import User

VoteType = Enum('VoteType','UP_VOTE DOWN_VOTE')

class Idea(models.Model):
    author = models.ForeignKey(User)
    content = models.CharField(max_length=300)
    upvote_count = models.IntegerField()
    downvote_count = models.IntegerField()

    #this will be ok for the MVP, but it wont scale.
    #should do it async
    def Vote(self,vote_type):
        if(vote_type == VoteType.UP_VOTE):
            self.upvote_count += 1
        elif(vote_type == VoteType.DOWN_VOTE):
            self.downvote_count += 1
        else:
            raise Exception('INVALID VOTE %d' % vote_type)
    
class Comment(models.Model):
    author = models.ForeignKey(User)
    idea = models.ForeignKey(Idea)
    content = models.TextField()    
    parent = models.ForeignKey('self',null=True,blank=True)

