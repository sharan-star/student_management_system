from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .password import hash_pass,check_pw
from .models import Register,Student_Details,Courses,Drives
# Create your views here.
def home(req):
    courses = Courses.objects.all()
    return render(req,'home.html',{'courses': courses})

def dashboard(req):
    search_name = req.GET.get('q', '').strip()
    matched_students = Student_Details.objects.none()

    # Only search when the user types something in the box.
    if search_name:
        matched_students = Student_Details.objects.filter(Name__icontains=search_name)

    context = {
        'students': matched_students,
        'query': search_name,
        'has_search': bool(search_name),
    }
    return render(req, 'Dashboard.html', context)

def login(req):
    if req.method=='POST':
        username=req.POST.get('Username')
        password=req.POST.get('Password')
        print(password)
        reg_obj=Register.objects.get(UserName=username)
        print(reg_obj)
        if check_pw(password,reg_obj.Password):
            return redirect('dashboard')
    return render(req,'login.html')

def register(req):
    if req.method=='POST':
        fullname=req.POST.get('FullName')
        username=req.POST.get('UserName')
        email=req.POST.get('Email')
        password=req.POST.get('Password')
        confirm_password=req.POST.get('confirm_password')
        if password==confirm_password:
            print(password)
            hashed_pass=hash_pass(password)
        Register.objects.create(
            FullName=fullname,
            UserName=username,
            Email=email,
            Password=hashed_pass
        )
        return redirect('login')
    return render(req,'register.html')

def add_student(req):
    if req.method=='POST':
        name=req.POST.get('Student_name')
        age=req.POST.get('Student_age')
        phone_no=req.POST.get('Student_phoneno')
        course=req.POST.get('Student_course')
        resume=req.FILES.get('Student_resume')
        email=req.POST.get('Student_email')
        address=req.POST.get('Student_address')
        Student_Details.objects.create(
            Name=name,
            Age=age,
            Phone_no=phone_no,
            Course=course,
            Resume=resume,
            Email=email,
            Address=address
        )
        return render(req,'Dashboard.html')
    return render(req,'add_student.html')

def view_students(req):
    all_details=Student_Details.objects.all()
    context={
        'stu_details':all_details
    }
    return render(req,'view_student.html',context)

def update_student(req,input_id):
    student=get_object_or_404(Student_Details, id=input_id)
    if req.method=='POST':
        student.Name=req.POST.get('Student_name')
        student.Age=req.POST.get('Student_age')
        student.Phone_no=req.POST.get('Student_phoneno')
        student.Course=req.POST.get('Student_course')
        resume=req.FILES.get('Student_resume')
        if resume:
            student.Resume=resume
        student.Email=req.POST.get('Student_email')
        student.Address=req.POST.get('Student_address')
        student.save()
        return redirect('view_students')
    return render(req,'update_student.html',{'student':student})

def delete_student(req,input_id):
    student=get_object_or_404(Student_Details,id=input_id)
    student.delete()
    return redirect('view_students')

def drives(req):
    drives=Drives.objects.all()
    return render(req,'Drives.html',{'drives':drives})