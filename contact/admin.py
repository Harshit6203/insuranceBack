from django.contrib import admin
from contact . models import *

class FeedbackAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "phno",
        "eamil",
        "feed_back",

    ]
admin.site.register(Feedback,FeedbackAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "phno",
        "msg",

    ]
admin.site.register(Contact,ContactAdmin)
