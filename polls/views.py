from django.shortcuts import render,get_object_or_404
from .models import Poll
from django.http import JsonResponse


def poll_list(request):
   max_objects=50
   polls=Poll.objects.all()[:max_objects]
#    fetches upto 50 poll objects
   data = {"results": list(polls.values("question", "created_by__username", "pub_date"))}
   return JsonResponse(data)

def poll_list_item(request,pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {"results": {
    "question": poll.question,
    "created_by": poll.created_by.username,
    "pub_date": poll.pub_date
}}
    return JsonResponse(data)