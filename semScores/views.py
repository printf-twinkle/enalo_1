from semScores.models import CustomUser
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser
from django.forms.models import model_to_dict
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class CreateUserView(APIView):
    def post(self, request):
        data = request.data
        the_email = data.get("email")
        first_name = data.get("firstName")
        last_name = data.get("lastName")
        password = make_password(data.get("password"))
        dob = data.get("dob")
        course_name = data.get("courseName")
        department = data.get("department")
        year_of_admission = data.get("yearOfAdmission")
        year_of_passing = data.get("yearOfPassing")
        student_id = data.get("studentId")
        sub1_score = data.get("sub1Score")
        sub2_score = data.get("sub2Score")
        try:
            print("yes")
            if not CustomUser.objects.filter(username=the_email).exists():
                user = CustomUser(
                    first_name=first_name,
                    last_name=last_name,
                    username=the_email,
                    email=the_email,
                    dob=dob,
                    password=password,
                    course_name=course_name,
                    department=department,
                    student_id=student_id,
                    year_of_admission=year_of_admission,
                    year_of_passing=year_of_passing,
                    sub1_score = sub1_score,
                    sub2_score = sub2_score
                )
                user.save()
                print(user)
                user = model_to_dict(user)
                del user["password"]
        except:
            return Response({"ok":False, "message": "email(user) already exists!!"}, status=403)
        return Response({"ok": True, "message": "User created and membershipID sent successfully!", "user": user})


class ProfileView(APIView):
    authentication_class = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = model_to_dict(request.user)
        del user['password']
        return Response({"ok": True, "userData": user})

class ProfileUpdate(APIView):
    # authentication_class = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data
        email = data.get("email")
        first_name = data.get("firstName")
        last_name = data.get("lastName")
        password = make_password(data.get("password"))
        dob = data.get("dob")
        course_name = data.get("courseName")
        department = data.get("department")
        year_of_admission = data.get("yearOfAdmission")
        year_of_passing = data.get("yearOfPassing")
        student_id = data.get("studentId")
        sub1_score = data.get("sub1Score")
        sub2_score = data.get("sub2Score")

        try:
            user_exists_or_not = CustomUser.objects.get(username = email)
            user_exists_or_not.first_name = first_name,
            user_exists_or_not.last_name = last_name,
            user_exists_or_not.password = password,
            user_exists_or_not.dob = dob,
            user_exists_or_not.course_name = course_name,
            user_exists_or_not.department = department,
            user_exists_or_not.year_of_admission = year_of_admission,
            user_exists_or_not.year_of_passing = year_of_passing,
            user_exists_or_not.student_id = student_id,
            user_exists_or_not.sub1_score = sub1_score,
            user_exists_or_not.sub2_score = sub2_score
            user_exists_or_not = model_to_dict(user_exists_or_not)
            del user_exists_or_not["password"]
        except:
            return Response({"ok": False, "message": "Profile could not be updated"})
        return Response({"ok": True, "message": "Profile updated"})

class ProfileDelete(APIView):
    # authentication_class = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data
        email = data.get('email')
        try:
            email_existing_or_not = CustomUser.objects.get(username = email)
            user = model_to_dict(email_existing_or_not)
            email_existing_or_not.delete()
            del user["password"]
        except:
            return Response({"ok": False, "message": "Profile could not be deleted"})
        return Response({"ok": True, "message": "Profile could be deleted"})
