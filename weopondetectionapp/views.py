from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from rest_framework.views import APIView

from weopondetectionapp.serializer import *
from .form import *

from weopondetectionapp.models import LoginTable
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        login_obj = LoginTable.objects.get(username=username, password=password)
        if login_obj.usertype == "admin":
            return HttpResponse('''<script>alert("login successful");window.location="/homepage"</script>''')
class User(View):
    def get(self, request):
        obj=LoginTable.objects.all()

        return render(request, 'manuser.html',{'obj':obj})
    

class Feedbackview(View):
    def get(self, request):
        obj=Feedback.objects.all()
        
        return render(request, 'feedback.html',{'obj':obj})    
class Complaintview(View):
    def get(self, request):
        obj=Complaint.objects.all()
        return render(request, 'complaint.html',{'complaints':obj})
    
class addreply(View):
    def get(self,request,id):
        obj=Complaint.objects.get(id=id)
        return render(request,'replyuser.html',{'obj':obj})
    def post(self, request,id):
        obj=Complaint.objects.get(id=id)
        form=Sentreplyform(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("reply added successfully");window.location="/complaint"</script>''')

class Adduser(View):
    def get(self, request):
        return render(request, 'adduser.html')
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("User Added Successfully");window.location="/manuser"</script>''')
        return HttpResponse('''<script>alert("User not added");window.location="/manuser"</script>''')
        
class Edituser(View):
    def get(self, request,id):
        obj=LoginTable.objects.get(id=id)
        return render(request, 'edituser.html',{'obj':obj})
    def post(self, request,id):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("User Added Successfully");window.location="/manuser"</script>''')
class Deleteuser(View):
        def get(self, request,id):
            obj=LoginTable.objects.get(id=id)
            obj.delete()
            return redirect('manuser')
   
class Homepage(View):
    def get(self, request):
        return render(request, 'homepage.html')  


 #///////////////////////////////////////////////////////////API///////////////////////////////  

class UserReg(APIView):
    def post(self, request):
        print("###################",request.data)
        login_serial = Logintableserializer(data=request.data)
        login_valid = login_serial.is_valid()

        if login_valid:
            print("&&&&&&&&&&&&&&&&&&&&&&&")
            login_profile = login_serial.save()
            return Response(login_profile.data, status=status.HTTP_201_CREATED)
        return Response({'login_error': login_serial.errors if not login_valid else None},status=status.HTTP_400_BAD_REQUEST)
class LoginPage(APIView):
    def post(self, request):
        response_dict = {}

        # Get data from the request
        username = request.data.get("username")
        password = request.data.get("password")

        # Validate input
        if not username or not password:
            response_dict["message"] = "failed"
            return Response(response_dict, status=status.HTTP_400_BAD_REQUEST)

        # Fetch the user from LoginTable
        t_user = LoginTable.objects.filter(username=username,password=password).first()

        if not t_user:
            response_dict["message"] = "failed"
            return Response(response_dict, status=status.HTTP_401_UNAUTHORIZED)

        # # Check password using check_password
        # if not check_password(password, t_user.password):
        #     response_dict["message"] = "failed"
        #     return Response(response_dict, status=status.HTTP_401_UNAUTHORIZED)

        # Successful login response
        response_dict["message"] = "success"
        response_dict["login_id"] = t_user.id

        return Response(response_dict, status=status.HTTP_200_OK)
    
class Addfeedbackapi(APIView):
    def post(self,request):
        serial=Feedbackserializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data,status=status.HTTP_200_OK)
        else:
            return Response({"msg":serial.errors},status=status.HTTP_400_BAD_REQUEST)
class Addcomplaintapi(APIView):
    def post(self, request):
        serializer = Complaintserializeradd(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Viewcomplaintapi(APIView):
    def get(self,request,id):
        response={}
        complaint=Complaint.objects.filter(USER_id=id).all()
        serializer=Complaintserializerview(complaint,many=True)
        response["data"]=serializer.data
        response["status"]="success"

        return Response(response,status=status.HTTP_200_OK)
    
        
# class Viewthreat(APIView):
#     def get(self,request):
#         threat=Threat.objects.all()
#         serializer=Threatserializer(threat,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)

# class Viewcameraapi(APIView)
#     def get(self,request):
#         complaint=Camera.objects.all()
#         serializer=Cameraserializerview(complaint,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
# class ViewUploadimageapi(APIView)
#     def post(self,request):
        
#         serializer=Imageuploadserializer(data=request.data)
        

import os
import cv2
import base64
import numpy as np
from datetime import datetime
from django.core.files.base import ContentFile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from ultralytics import YOLO
from .models import Notification
from django.core.files.storage import default_storage
from django.utils import timezone

# Path to the YOLO model
MODEL_PATH = os.path.join('../weapon_detection', 'runs', 'detect', 'train', 'weights', 'last.pt')

# Load YOLO model


class WeaponDetectionAPI(APIView):
    def get(self, request):
        # Initialize webcam capture
        cap = cv2.VideoCapture(0)

        # Load the YOLO model
        # model_path = os.path.join('path_to_your_model', 'last.pt')
        model = YOLO("//home//sharafu//Desktop//djangoprojects//weapondetection//weopon-detection//last.pt")

        # Detection threshold
        threshold = 0.5

        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            if not ret:
                break

            # Perform detection
            results = model(frame)[0]

            for result in results.boxes.data.tolist():
                x1, y1, x2, y2, score, class_id = result

                if score > threshold:
                    # Draw bounding box and label
                    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                    label = results.names[int(class_id)].upper()
                    cv2.putText(frame, label, (int(x1), int(y1) - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

                    # Save the detected frame as an image
                    _, img_encoded = cv2.imencode('.jpg', frame)
                    img_bytes = img_encoded.tobytes()
                    image_name = f"detection_{timezone.now().strftime('%Y%m%d_%H%M%S')}.jpg"

                    # Create Notification instance
                    notification = Notification(
                        message=f"{label} detected",
                        detected_at=timezone.now()
                    )
                    notification.image.save(image_name, ContentFile(img_bytes), save=True)

            # Display the resulting frame
            cv2.imshow('Live Detection', frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the capture and close windows
        cap.release()
        cv2.destroyAllWindows()

        # Retrieve all notifications
        notifications = Notification.objects.all()
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Notification
from .serializer import NotificationSerializer

class NotificationListView(APIView):
    def get(self, request):
        notifications = Notification.objects.all()
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
