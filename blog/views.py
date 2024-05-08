from django.shortcuts import render
from .serializers import BlogPostSerializer,PosterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BlogPost,Poster

class Getblog(APIView):
    def get(self, request):
        print(request.data ,"---------------")
        b_log = BlogPost.objects.all()
        serializer = BlogPostSerializer(b_log, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


class GetPoster(APIView):
    def get(self, request):
        print(request.data ,"---------------")
        poster = Poster.objects.all()
        serializer = PosterSerializer(poster, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)