from rest_framework import serializers
from .models import Choice, Vote,Poll

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vote
        fields="__all__"

class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False)
    class Meta:
        model=Choice
        fields="__all__"


class PollSerializer(serializers.ModelSerializer):
    choices=ChoiceSerializer(many=True,read_only=True) 
    class Meta:
        model=Poll
        fields="__all__"

