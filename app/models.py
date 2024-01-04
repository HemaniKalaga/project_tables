from django.db import models

# Create your models here.
class Dept(models.Model):
    DeptNo=models.IntegerField(primary_key=True)
    DeptName=models.CharField(max_length=100,unique=True)
    Loc=models.CharField(max_length=100)

    def __str__(self):
        return self.DeptName+'('+str(self.DeptNo)+')'

class Employee(models.Model):
    EmpNo=models.IntegerField(primary_key=True)
    EName=models.CharField(max_length=100,null=False)
    Job=models.CharField(max_length=100)
    MGR=models.IntegerField()
    Hiredate=models.DateField(auto_now=False,auto_now_add=False)
    Sal=models.IntegerField()
    Comm=models.IntegerField()
    DeptNo=models.ForeignKey(Dept,on_delete=models.CASCADE)


    def __str__(self):
        return str(self.EmpNo)+' '+self.EName 
    

class SalGrade(models.Model):
    Grade=models.IntegerField()
    Losal=models.IntegerField()
    Hisal=models.IntegerField()

    def __str__(self):
        return self.Grade

class Bonus(models.Model):
    Job=models.CharField(max_length=100)
    Sal=models.IntegerField()
    Comm=models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return self.Sal+self.Comm

   


    
