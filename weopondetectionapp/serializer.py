from rest_framework.serializers import ModelSerializer


from .models import *

class Logintableserializer(ModelSerializer):
    class Meta:
        model=LoginTable
        fields='__all__'
class Feedbackserializer(ModelSerializer):
    class Meta:
        model=Feedback
        fields=['USER','feedback']
class Complaintserializeradd(ModelSerializer):
    class Meta:
        model=Complaint
        fields=['USER','complaint']
class Complaintserializerview(ModelSerializer):
    class Meta:
        model=Complaint
        fields=['USER','complaint','reply']
# class imageserializer(ModelSerializer):
#     class Meta:
#         model=image
#         fields='__all__'                
# serializers.py
from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'message', 'detected_at', 'image']
