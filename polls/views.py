
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import PollSerializer
from rest_framework.response import Response
from .models import Poll


class PollList(APIView):
   def get(self,request):
      max_objects=100
      polls=Poll.objects.all()[:max_objects]
      data=PollSerializer(polls,many=True).data
      return Response(data)


class PollDetail(APIView):
   def get(self,request,pk):
      poll = get_object_or_404(Poll, pk=pk)
      data=PollSerializer(poll).data
      return Response(data)