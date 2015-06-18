from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Idea

# Create your views here.

#TODO move this method into a helper class
#This may not work due to lazy evaluation of the ORM stuff,
#Need to do some research
def render_to_json(model_array):
    response = serializers.serialize('json',model_array)
    return HttpResponse(response[0],mimetype="application/json")

def index(request,idea_id):
    try:
        idea = Idea.objects.get(pk = idea_id)
    except Idea.DoesNotExist:
        raise Http404("IDEA DOES NOT EXIST") #TODO need better error handling design for the API
    return render_to_json([idea,])

#returns the newest 100 ideas
def top_ideas(request):
    ideas = Idea.objects.order_by("-pub_date")[:100]
    return render_to_json(ideas)

#Grab all ideas with id greater than the last read idea
def ideas_from(request,id,page_limit):

    idea_list = Idea.objects.filter(pk__gt=id)
    pages = Paginator(idea_list,page_limit)
    page_number = request.GET.get('page')

    try:
        contacts = pages.page(page_number)
    except PageNotAnInteger:
        #deliver first page
        ideas = pages.page(1)
    except EmptyPage:
        #There are no more new ideas, return the last one
        ideas = pages.page(pages.num_pages)

    return render_to_json(ideas)



