from django.shortcuts import render
from .serializers import FeedbackSerializer,ContactSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class AddFeedback(APIView):
    def post(self, request):
        print(request.data)
        serializer = FeedbackSerializer(data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        

class AddContact(APIView):
    def post(self, request):
        print(request.data)
        serializer = ContactSerializer(data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
