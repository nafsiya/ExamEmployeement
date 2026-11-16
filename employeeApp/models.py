from django.db import models

# Create your models here.
class EmpolyeeModel(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    joining_date=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}"
    
    
class TaskModel(models.Model):
    PRIORITY_CHOICES=(
        ("low","low"),
        ("medium","medium"),
        ("high","high")
    )
    STATUS_CHOICES=(
        ("pending","pending"),
        ("in progress","in progress"),
        ("completed","completed")
    )
    assigned_to=models.ForeignKey(to=EmpolyeeModel,on_delete=models.CASCADE)
    description=models.TextField(max_length=100,null=True,blank=True)
    priority=models.CharField(max_length=50,choices=PRIORITY_CHOICES)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES)
    due_date=models.DateField()
    
    
    