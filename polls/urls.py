from django.urls import path
from .views import poll_list, poll_list_item

urlpatterns=[
    path("polls/",poll_list,name="poll_list"),
    path("polls/<int:pk>/",poll_list_item,name="poll_list"),
]