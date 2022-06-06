
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import PollSerializer,ChoiceSerializer,VoteSerializer
from rest_framework.response import Response
from .models import Poll,Choice
from rest_framework import generics


class PollList(generics.ListCreateAPIView):
   queryset=Poll.objects.all()
   serailizer_class=PollSerializer


class PollDetail(generics.RetrieveDestroyAPIView):
   queryset = Poll.objects.all()
   serializer_class = PollSerializer


class ChoiceList(generics.ListCreateAPIView):
   queryset = Choice.objects.all()
   serializer_class = ChoiceSerializer
class CreateVote(generics.CreateAPIView):
   serializer_class = VoteSerializer