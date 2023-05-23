from django.db import models


class Departments(models.Model):
    department_code = models.IntegerField()
    department_name = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name


class Sessions(models.Model):
    session_year = models.CharField(max_length=50)

    def __str__(self):
        return self.session_year


class Students(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )

    student_id = models.CharField(max_length=50)
    roll = models.IntegerField()
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    session = models.ForeignKey(Sessions, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    present_address = models.TextField()
    permanent_address = models.TextField()

    def __str__(self):
        return self.name
