from django.db import models

# Create your models here.
class User(models.Model):
    """This database contains all users including administrators and students

    Args:
        models (_type_): _description_
    """

    firstname = models.CharField(verbose_name="Full Name", max_length=100, blank=False)
    lastname = models.CharField(verbose_name="Lastname", max_length=100, blank=False)
    othername = models.CharField(verbose_name="Other Name", max_length=100, blank=True)
    course  = models.CharField(verbose_name="Course", max_length=100)
    matric_number = models.CharField(
        verbose_name="Matriculation Number",
        max_length=50,
        blank=False,
        unique=True
    )
    email = models.EmailField(verbose_name="Email", max_length=254, unique=True)
    role = models.CharField(verbose_name="Role", max_length=50, default="u")
    username = models.CharField(verbose_name="Username", max_length=100, unique=True)
    password = models.CharField(verbose_name="Password", max_length=500)
    suspended = models.BooleanField(verbose_name="Suspended", default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_accessed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.firstname + " " + self.lastname)

class Course(models.Model):
    code=models.CharField(verbose_name="Course Code", max_length=50, unique=True)
    name=models.CharField(verbose_name="Course Name", max_length=100)
    faculty_code=models.CharField(verbose_name="Faculty", max_length=100)

    def __str__(self):
        return str(self.name)

class Faculty(models.Model):
    code=models.CharField(verbose_name="Faculty Code", max_length=50, unique=True)
    name=models.CharField(verbose_name="Faculty Name", max_length=100)

    def __str__(self):
        return str("Faculty of " + self.name)

class Exam(models.Model):
    code=models.CharField(verbose_name="Exam Code", max_length=50, unique=True)
    label=models.CharField(verbose_name="Exam Label", max_length=100)
    course=models.CharField(verbose_name="Course", max_length=50)
    time_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.label + " (" + Course.objects.get(code=self.course).name + ")")
