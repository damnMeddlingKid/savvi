from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.core import serializers
from .models import Idea

# Create your views here.

#TODO move this method into a helper class
def jsonEncodedResponse(model_array):
    response = serializers.serialize('json',model_array)
    return HttpResponse(response[0],mimetype="application/json")

def index(request,idea_id):
    try:
        idea = Idea.objects.get(pk = idea_id)
    except Idea.DoesNotExist:
        raise Http404("IDEA DOES NOT EXIST") #TODO need better error handling design for the API
    return jsonEncodedResponse([idea,])

def top_ideas(request):
    ideas = Idea.objects.order_by("-pub_date")[:100]
    return jsonEncodedResponse(ideas)