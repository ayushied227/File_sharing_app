from django.shortcuts import render
from itsdangerous import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response

from home.serializers import FileListSerializer
# Create your views here.

class HandleFileUpload(APIView):
    def post(self, request):
        try:
            data=request.data
            serializer=FileListSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status' : 200,
                    'message' : 'files uploaded successfully',
                    'data' : serializer.data
                    })
            
            return Response({
                'status' : 400,
                'message' : 'somethign went wrong',
                'data'  : serializer.errors
            })
        except Exception as e:
            print(e)