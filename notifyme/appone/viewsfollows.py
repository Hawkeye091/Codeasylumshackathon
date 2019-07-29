from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import ListCreateAPIView

from .serializers import FollowsSerializer

from .models import Followsdb

# Create your views here.
class get_delete_update_follows(RetrieveUpdateDestroyAPIView):
	serializer_class=FollowsSerializer

	def get_queryset(self,pk):
		try:
			follows=Followsdb.objects.get(pk=pk)
		except Followsdb.DoesNotExist:
			content={
				'status':'Not Found'
			}	
			return Response(content,status=status.HTTP_404_NOT_FOUND)
		return follows	

	def get(self,request,pk):
		follows=self.get_queryset(pk)
		serializer=FollowsSerializer(follows)
		return Response(serializer.data,status=status.HTTP_200_OK)

	def put(self,request,pk):
		follows=self.get_queryset(pk)
		serializer=FollowsSerializer(follows,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)		

	def delete(self,request,pk):
		follows=self.get_queryset(pk)
		follows.delete()
		content={
		'status':'Item Deleted'
		}
		return Response(content,status=status.HTTP_204_NO_CONTENT)


class get_post_follows(ListCreateAPIView):
	serializer_class = FollowsSerializer
	def get(self,request):
		follows = Followsdb.objects.all()
		serializer = FollowsSerializer(follows, many=True)
		return Response(serializer.data)
	def post(self,request):
		serializer = FollowsSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
