from django.urls import path
from .views import PollList,PollDetail,ChoiceList,CreateVote

app_name = "polls"

urlpatterns=[
    path("",PollList.as_view(),name="all-polls"),
    path("<int:pk>/",PollDetail.as_view(),name="poll-detail"),
    path("choices/", ChoiceList.as_view(), name="choice_list"),
    path("vote/", CreateVote.as_view(), name="create_vote"),
]