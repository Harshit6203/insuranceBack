from django.urls import path
from .views import *


urlpatterns = [
path('get_blog/',Getblog.as_view()),
path('get_poster/',GetPoster.as_view()),
]