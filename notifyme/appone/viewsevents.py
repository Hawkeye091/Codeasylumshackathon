from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import ListCreateAPIView

from .serializers import EventsSerializer

from .models import Eventsdb

# Create your views here.
class get_delete_update_events(RetrieveUpdateDestroyAPIView):
	serializer_class=EventsSerializer

	def get_queryset(self,pk):
		try:
			events=Eventsdb.objects.get(pk=pk)
		except Eventsdb.DoesNotExist:
			content={
				'status':'Not Found'
			}	
			return Response(content,status=status.HTTP_404_NOT_FOUND)
		return events	

	def get(self,request,pk):
		events=self.get_queryset(pk)
		serializer=EventsSerializer(events)
		return Response(serializer.data,status=status.HTTP_200_OK)

	def put(self,request,pk):
		events=self.get_queryset(pk)
		serializer=EventsSerializer(events,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)		

	def delete(self,request,pk):
		events=self.get_queryset(pk)
		events.delete()
		content={
		'status':'Item Deleted'
		}
		return Response(content,status=status.HTTP_204_NO_CONTENT)


class get_post_events(ListCreateAPIView):
	serializer_class = EventsSerializer
	def get(self,request):
		events = Eventsdb.objects.all()
		serializer = EventsSerializer(events, many=True)
		return Response(serializer.data)
	def post(self,request):
		serializer = EventsSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
