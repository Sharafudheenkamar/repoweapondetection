
from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('',Login.as_view(),name='login'),
    path('manuser/',User.as_view(),name='manuser'),
    path('feedback/',Feedbackview.as_view(),name='feedback'),
    path('complaint/',Complaintview.as_view(),name='complaint'),
    path('adduser/',Adduser.as_view(),name='adduser'),
    path('deleteuser/',Deleteuser.as_view(),name='deleteuser'),
    path('addreply/<int:id>',addreply.as_view(),name='addreply'),

    path('Edituser/<int:id>',Edituser.as_view(),name='Edituser'),
    path('Deleteuser/<int:id>',Deleteuser.as_view(),name='Deleteuser'),
    path('homepage/',Homepage.as_view(),name='homepage'),


    #########################API#########################
    path('login/',LoginPage.as_view(),name='api_login'),
    path('Addfeedbackapi',Addfeedbackapi.as_view(),name='Addfeedbackapi'),
    path('addcomplaintapi',Addcomplaintapi.as_view(),name='Addcomplaintapi'),
    path('adduserapi/',Adduser.as_view(),name='adduserapi'),
    path('viewcomplaintapi/<int:id>',Viewcomplaintapi.as_view(),name='Viewcomplaintapi'),
    path("detect-weapon/", WeaponDetectionAPI.as_view(), name="weapon-detection"),
    path('notificationsapi/', NotificationListView.as_view(), name='notification-list'),




]
