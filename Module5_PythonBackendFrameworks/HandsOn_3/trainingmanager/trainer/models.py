from django.db import models

# Create your models here.
class Department(models.Model):
    dept_name = models.CharField(max_length=100, unique=True, null=False)
    hod_name = models.CharField(max_length=100, blank=True, null=True)
    budget = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.dept_name


class Employee(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    date_of_birth = models.DateField(blank=True, null=True)
    hiring_year = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
   
    department = models.ForeignKey(
        Department, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='employees'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Instructor(models.Model):
    instructor_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, unique=True, blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    department = models.ForeignKey(
        Department, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='instructors'
    )

    def __str__(self):
        return self.instructor_name


class SkillModule(models.Model):
    module_name = models.CharField(max_length=150, null=False)
    module_code = models.CharField(max_length=20, unique=True, null=False)
    credits = models.IntegerField(blank=True, null=True)
    department = models.ForeignKey(
        Department, 
        on_delete=models.CASCADE,  # Deleting department removes associated skill modules
        related_name='skill_modules'
    )

    def __str__(self):
        return f"{self.module_code} - {self.module_name}"


class Certification(models.Model):
    completion_date = models.DateField(blank=True, null=True)
    grade = models.CharField(max_length=2, blank=True, null=True)
    
    employee = models.ForeignKey(
        Employee, 
        on_delete=models.CASCADE, 
        related_name='certifications'
    )
    skill_module = models.ForeignKey(
        SkillModule, 
        on_delete=models.CASCADE, 
        related_name='certifications'
    )

    def __str__(self):
        return f"{self.employee} -> {self.skill_module}"

    class Meta:
        unique_together = [['employee', 'skill_module']]


class ModuleSchedule(models.Model):
    module = models.ForeignKey(
        SkillModule, 
        on_delete=models.CASCADE, 
        related_name='schedules'
    )
    day_of_week = models.CharField(max_length=20, null=False)
    start_time = models.CharField(max_length=20, blank=True, null=True)
    end_time = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.module.module_name} schedule on {self.day_of_week}"