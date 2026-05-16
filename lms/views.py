from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Course
from .models import Enrollment
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')



def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/dashboard/")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect("/login/")

def courses(request):
    all_courses = Course.objects.all()
    return render(request,'courses.html', {'courses': all_courses})

@login_required
def enroll(request, course_id):
    course = Course.objects.get(id=course_id)

    # check if already enrolled
    if not Enrollment.objects.filter(user=request.user, course=course).exists():
        Enrollment.objects.create(user=request.user, course=course)

    return redirect('/dashboard/')

@login_required
def dashboard(request):
    enrolled = Enrollment.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'enrolled': enrolled})

def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'course_detail.html', {'course': course})



def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)

    is_enrolled = False
    if request.user.is_authenticated:
        is_enrolled = Enrollment.objects.filter(
            user=request.user,
            course=course
        ).exists()

    return render(request, 'course_detail.html', {
        'course': course,
        'is_enrolled': is_enrolled
    })
    
def courses(request):
    query = request.GET.get('q')

    if query:
        all_courses = Course.objects.filter(title__icontains=query)
    else:
        all_courses = Course.objects.all()

    return render(request, 'courses.html', {'courses': all_courses})

@login_required
def my_courses(request):
    enrolled = Enrollment.objects.filter(user=request.user)
    return render(request, 'my_courses.html', {'enrolled': enrolled})