from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import ListCreateAPIView

from .serializers import EventsSerializer
from .serializers import TagsSerializer

from .models import Eventsdb
from .models import Tagsdb


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
		newrequest=[]
		for i in range(0,len(events)):
			clgid=events[i].clg_id
			eventname=events[i].event_name
			eventdesc=events[i].event_desc
			eventdate=events[i].event_date
			eventtime=events[i].event_time
			eventphotourl=events[i].event_photourl
			eventattenders=events[i].event_attenders
			tagname=Tagsdb.objects.get(tag_id=events[i].tag_id).tag_name
			j={"clg_id":clgid,
			"tag_name":tagname,
			"event_name":eventname,
			"event_desc":eventdesc,
			"event_date":eventdate,
			"event_time":eventtime,
			"event_photourl":eventphotourl,
			"event_attenders":eventattenders
			}
			newrequest.append(j)			
		return Response(newrequest)
		#serializer = EventsSerializer(events, many=True)
		#return Response(serializer.data)
	def post(self,request):
		mytagname=request.data['tag_name']
		mytagid=Tagsdb.objects.get(tag_name=mytagname)
		newrequest={"clg_id":request.data['clg_id'],"tag_id":mytagid.tag_id,"event_name":request.data['event_name'],"event_desc":request.data['event_desc'],"event_date":request.data['event_date'],"event_time":request.data['event_time'],"event_photourl":request.data['event_photourl']}
		newrequest['event_attenders']=0
		serializer = EventsSerializer(data=newrequest)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
