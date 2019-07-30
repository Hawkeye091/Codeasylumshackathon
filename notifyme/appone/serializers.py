from rest_framework import serializers
from .models import Clgsdb
from .models import Clgtagsdb
from .models import Detailsdb
from .models import Eventsdb
from .models import Tagsdb

class ClgsSerializer(serializers.ModelSerializer):  # create class to serializer model
    class Meta:
        model = Clgsdb
        fields = ('clg_name',)

class ClgtagsSerializer(serializers.ModelSerializer):  # create class to serializer model
    class Meta:
        model = Clgtagsdb
        fields = ('clg_id','tag_id')

class DetailsSerializer(serializers.ModelSerializer):  # create class to serializer model
    class Meta:
        model = Detailsdb
        fields = ('clg_id','student_type','student_name','student_email','student_password')

class EventsSerializer(serializers.ModelSerializer):  # create class to serializer model
    class Meta:
        model = Eventsdb
        fields = ('clg_id','tag_id','event_name','event_desc','event_date','event_time','event_photourl','event_attenders')

class TagsSerializer(serializers.ModelSerializer):  # create class to serializer model
    class Meta:
        model = Tagsdb
        fields = ('tag_name',)

