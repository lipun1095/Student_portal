from django.db import models

# Create your models here.

class StudentInfo(models.Model):
	roll_no = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200,blank=True,null=True)
	class_name = models.CharField(max_length=200,blank=True,null=True)
	school_name = models.CharField(max_length=200,blank=True,null=True)
	mobile_number = models.CharField(max_length=200,blank=True,null=True)
	address = models.TextField(blank=True,null=True)
	is_deleted=models.BooleanField(default=False)
	status=models.BooleanField(default=True)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)


	def __str__(self):
		return str(self.name)
	class Meta:
		db_table='student_info'


class StudentAcademics(models.Model):
	student=models.ForeignKey(StudentInfo,on_delete=models.CASCADE,blank=True,null=True,related_name='student_academic_s_i')
	maths = models.IntegerField(blank=True,null=True)
	physics = models.IntegerField(blank=True,null=True)
	chemistry = models.IntegerField(blank=True,null=True)
	biology = models.IntegerField(blank=True,null=True)
	english = models.IntegerField(blank=True,null=True)
	is_deleted=models.BooleanField(default=False)
	status=models.BooleanField(default=True)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)



	def __str__(self):
		return str(self.id)
	class Meta:
		db_table='student_academic'
