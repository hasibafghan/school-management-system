from django.db import models
from django.utils.text import slugify
from django.utils import timezone


class Parent(models.Model):
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100)
    father_mobile = models.CharField(max_length=100)
    father_email = models.EmailField(max_length=100)
    mother_name = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100)
    mother_email = models.EmailField(max_length=100)
    mother_mobile = models.CharField(max_length=100)
    present_address = models.TextField()
    permanent_address = models.TextField()

    def __str__(self) -> str:
        return f"{self.father_name} & {self.mother_name}"


class Student(models.Model):
    # Custom primary key optional — Django creates 'id' by default
    student_id = models.CharField(max_length=10, unique=True, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=10,
        choices=[
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Others', 'Others')
        ]
    )
    # delete, listview , update , retrive , search
    # must added--------------- slug , add id manualy
    date_of_birth = models.DateTimeField(blank=True, null=True)
    student_class = models.CharField(max_length=100)
    section = models.CharField(max_length=2)
    religion = models.CharField(max_length=20)
    joining_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    mobile_number = models.CharField(max_length=15)
    student_image = models.ImageField(upload_to='student/', blank=True, null=True)
    parent = models.ForeignKey(Parent,on_delete=models.CASCADE, related_name='students', blank=True, null=True)
    admission_number = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.first_name}-{self.last_name}-{self.admission_number}')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.admission_number})'
