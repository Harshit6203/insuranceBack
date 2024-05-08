from django.urls import path
from .views import *


urlpatterns = [
path('add_feedback/',AddFeedback.as_view()),
path('add_contact/',AddContact.as_view()),
]