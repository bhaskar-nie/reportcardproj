from django.db import models

# Create your models here.
class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department
    
    class Meta:
        ordering = ['department']

class StudentID(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.subject_name

class Student(models.Model):
    student_department = models.ForeignKey(Department, related_name="depart", on_delete=models.CASCADE, null=True, blank=True)
    student_id = models.OneToOneField(StudentID, related_name='studentid', on_delete=models.CASCADE, null=True, blank=True)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True, null=True, blank=True) #should be unique
    student_age = models.IntegerField(default=18)
    student_address = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.student_name
    
    class Meta:
        ordering = ['student_department']
        verbose_name = "student"

class SubjectMarks(models.Model):
    # ForeignKey to Student model; if a student is deleted, their marks are also deleted
    student = models.ForeignKey(Student, related_name="student", on_delete=models.CASCADE)
    
    # ForeignKey to Subject model; if a subject is deleted, related marks are also deleted
    subject = models.ForeignKey(Subject, related_name="subject", on_delete=models.CASCADE)
    
    # IntegerField to store the marks, default value is 0
    marks = models.IntegerField(default=0)

    # Ensure each student has only one marks entry per subject
    class Meta:
        # unique_together enforces that each combination of student and subject is unique
        unique_together = ['student', 'subject']

    # String representation of the SubjectMarks object
    def __str__(self) -> str:
        # Returns a string combining the student's name and the subject name
        return f'{self.student.student_name} {self.subject.subject_name}'

class Rank(models.Model):
    student=models.ForeignKey(Student, related_name="studentrank", on_delete=models.CASCADE)
    student_rank=models.IntegerField(default=0)
    date_of_report_generation=models.DateField(auto_now_add=True)

    class Meta:
        unique_together=['student_rank', 'date_of_report_generation'] 
        #Rank of a student cannot be different on the same day of report generation