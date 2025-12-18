from django.db import models

# Create your models here.

class ClassStatus(models.TextChoices):
    ACTIVE = 'active', 'Active'
    INACTIVE = 'inactive', 'Inactive'
    ARCHIVED = 'archived', 'Archived'
    NOSTATUS = 'nostatus', 'No Status'
    


class Class(models.Model):
    name = models.CharField(max_length=50)
    status = models.CharField(choices=ClassStatus.choices, default=ClassStatus.NOSTATUS, max_length=50  )
    description = models.TextField()
    students = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    


class School(models.Model):
    name = models.CharField(max_length=50)
    status = models.CharField(choices=ClassStatus.choices, default=ClassStatus.NOSTATUS, max_length=50  )
    address = models.CharField(max_length=50)
    classes = models.ManyToManyField(Class,related_name='classes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    


class Student(models.Model):
    fullname = models.CharField(max_length=100)
    status = models.CharField(choices=ClassStatus,default=ClassStatus.NOSTATUS,max_length=50)
    class_data = models.ForeignKey(Class,on_delete=models.CASCADE,max_length=50)
    school = models.ForeignKey(School,on_delete=models.CASCADE,related_name='student_school')
    phone = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname
    
