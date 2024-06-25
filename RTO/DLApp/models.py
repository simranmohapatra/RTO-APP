from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class DLmodel(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL,null=True, blank=True)
    
    dlname =models.CharField(max_length = 30)
    
    dlid =models.IntegerField()
    
    dlphno =models.IntegerField()
    
    address =models.TextField()




class Department(models.Model):
    department=models.CharField(max_length=100)
    def __str__(self):
        return self.department
    class Meta:
        ordering=['department']
    
class StudentID(models.Model):
    astudent_id=models.CharField(max_length=100)
    def __str__(self):
        return self.astudent_id
    class meta:
        ordering=('astudent_id',)

class Student(models.Model):
    department=models.ForeignKey(Department,related_name="depart",
    on_delete=models.CASCADE)

    student_id=models.OneToOneField(StudentID,
    related_name="student_id",on_delete=models.CASCADE)

    names=models.CharField(max_length=100)

    email=models.EmailField()

    age=models.IntegerField(default=15)

    address=models.TextField()

    def __str__(self):
        return self.name
    
    class meta:
        ordering=['name']
        verbose_name='student'