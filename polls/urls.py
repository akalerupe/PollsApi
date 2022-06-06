from django.urls import path
from .views import PollList,PollDetail

app_name = "polls"

urlpatterns=[
    path("",PollList.as_view(),name="all-polls"),
    path("<int:pk>/",PollDetail.as_view(),name="poll-detail"),
]