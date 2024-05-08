from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=20)
    phno = models.CharField(max_length=12)  
    eamil = models.EmailField()
    feed_back = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=20) 
    phno = models.CharField(max_length=12)  
    msg = models.TextField()  

    def __str__(self):
        return self.name