from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from users.forms import *
from django.db.models import Q,F
from django.contrib.auth.decorators import login_required

# Create your views here.

# Add Student
@login_required
def add_student(request):
	if request.method == "GET":
		student_form = StudentInfoFormNew()
		return render(request, 'student/add_student.html',{'fromtype':'add','student_form':student_form})
	elif request.method == "POST":
		student_form = StudentInfoFormNew(request.POST)
		if student_form.is_valid():
			name = request.POST['name']
			class_name = request.POST['class_name']
			school_name = request.POST['school_name']
			mobile_number = request.POST['mobile_number']
			address = request.POST['address']
			maths = request.POST['maths']
			physics = request.POST['physics']
			chemistry = request.POST['chemistry']
			biology = request.POST['biology']
			english = request.POST['english']
			if name and class_name and school_name and mobile_number and address:
				student_info = StudentInfo.objects.create(name=name,class_name=class_name,school_name=school_name,mobile_number=mobile_number,address=address)
			if student_info.roll_no and maths and physics and chemistry and biology and english:
				student_ins = StudentAcademics.objects.create(student_id=student_info.roll_no,maths=maths,physics=physics,chemistry=chemistry,biology=biology,english=english)
			return HttpResponseRedirect('/student_list/')
		else:
			return render(request, 'student/add_student.html', {'fromtype':'add','student_form':student_form})


# Edit Student
@login_required
def edit_student(request,roll_no):
	student=StudentInfo.objects.filter(roll_no=roll_no,is_deleted=False,status=True).exists()
	if student:
		student=StudentInfo.objects.filter(roll_no=roll_no,is_deleted=False,status=True).values().annotate(
						maths=F('student_academic_s_i__maths'),
						physics=F('student_academic_s_i__physics'),
						chemistry=F('student_academic_s_i__chemistry'),
						biology=F('student_academic_s_i__biology'),
						english=F('student_academic_s_i__english'),
						).last()
		if request.method == 'GET':
			student_form = StudentInfoFormNew()
			return render(request, 'student/edit_student.html', {'student':student})
		elif request.method == 'POST':
			student_form = StudentInfoFormNew(request.POST)
			if student_form.is_valid():
				student = StudentInfo.objects.get(roll_no=roll_no)
				name = request.POST['name']
				class_name = request.POST['class_name']
				school_name = request.POST['school_name']
				mobile_number = request.POST['mobile_number']
				address = request.POST['address']
				maths = request.POST['maths']
				physics = request.POST['physics']
				chemistry = request.POST['chemistry']
				biology = request.POST['biology']
				english = request.POST['english']
				if name and class_name and school_name and mobile_number and address:
					student.name=name
					student.class_name=class_name
					student.school_name=school_name
					student.mobile_number=mobile_number
					student.address=address
					student.save()
				if student.roll_no and maths and physics and chemistry and biology and english:
					student_ins = StudentAcademics.objects.get(student_id=student.roll_no)
					student_ins.student_id=student.roll_no
					student_ins.maths=maths,physics=physics
					student_ins.chemistry=chemistry
					student_ins.biology=biology
					student_ins.english=english
					student_ins.save()
		return HttpResponseRedirect('/student_list/')
	else:
		return render(request, 'student/edit_student.html', {'student':student,'student_form':student_form})

# Student List
def show_student_list(request):
	search = request.GET.get('search',None)
	filterquery = Q(status=True,is_deleted=False)
	if search:
		search = search.strip()
		filterquery.add(Q(name__icontains=search),Q.AND)
	all_student = StudentInfo.objects.filter(filterquery)
	return render(request, 'student/all_student.html',{'all_student': all_student})

# Delete Student
@login_required
def delete_student(request,roll_no):
	student=StudentInfo.objects.filter(roll_no=roll_no,is_deleted=False,status=True).exists()
	if student:
		student = StudentInfo.objects.get(roll_no=roll_no)
		student.delete()
	return HttpResponseRedirect('/student_list/')


# Add Student Mark
# This Function is Not Used.
def add_student_mark(request):
	if request.method == "GET":
		student = StudentInfo.objects.filter(is_deleted=False,status=True)
		student_form = StudentAcademicsForm()
		return render(request, 'student/add_student_mark.html',{'fromtype':'add','student_form':student_form,'student':student})
	elif request.method == "POST":
		student_id = request.POST['category']
		maths = request.POST['maths']
		physics = request.POST['physics']
		chemistry = request.POST['chemistry']
		biology = request.POST['biology']
		english = request.POST['english']
		if StudentInfo.objects.filter(roll_no=student_id,is_deleted=False,status=True).exists() and maths and physics and chemistry and biology and english:
			student_ins = StudentAcademics.objects.create(student_id=student_id,maths=maths,physics=physics,chemistry=chemistry,biology=biology,english=english)
		return HttpResponseRedirect('/student_list/')
	else:
		return render(request, 'student/add_student_mark.html', {'fromtype':'add','student_form':student_form,'student':student})

# For showing Mark
@login_required
def show_student_mark(request,roll_no):
	student=StudentAcademics.objects.filter(student_id=roll_no,is_deleted=False,status=True).exists()
	student_mark = []
	if student:
		student_mark = StudentAcademics.objects.filter(student_id=roll_no,  status=True,is_deleted=False).values().annotate(student_name=F('student__name'))
	return render(request, 'student/student_mark.html',{'student_mark': student_mark,'student_name':student_mark[0]['student_name'] if student_mark else None})

def welcome_view(request):
	return render(request, 'student/welcome.html')


def logout_view(request):
	return render(request, 'registration/logout.html')



def signup_view(request):
	form = SignupForm()
	if request.method == 'POST':
		form = SignupForm(request.POST)
		user = form.save()
		user.set_password(user.password)
		user.save()
		return HttpResponseRedirect('/accounts/login')
	return render(request, 'registration/signup.html', {'form': form})
