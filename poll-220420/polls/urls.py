from django.urls import path

from polls.views import IndexPageView, DetailPageView, ResultPageView, vote

app_name = 'polls'

urlpatterns = [
    path("", IndexPageView.as_view(), name="index"),  # /polls/
    path("<int:pk>/", DetailPageView.as_view(), name="detail"),  # /polls/5/
    path("<int:pk>/result/", ResultPageView.as_view(), name="result"),  # /polls/5/result/
    path("<int:pk>/vote/", vote, name="vote")  # /polls/5/vote
]
