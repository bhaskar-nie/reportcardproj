from faker import Faker
import random
from .models import *
from django.db.models import Sum
fake=Faker()

def seed_db(n=10) -> None:
    #->None means fn returns None
    for _ in range(n):
        department_objects=Department.objects.all()
        if department_objects.exists():  # Check if there are any departments available
            random_idx = random.randint(0, len(department_objects) - 1)
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(15, 30)
            student_address = fake.address()
            student_department = department_objects[random_idx]
            student_id = f'4NI22-{random.randint(100,999)}'

            # Create a StudentID instance
            student_id_object = StudentID.objects.create(student_id=student_id)

            # Create a Student instance
            Student.objects.create(
                #student_id n student_dept me respective objects pass honge
                #see their models.py
                student_id=student_id_object,
                student_department=student_department,
                student_email=student_email,
                student_age=student_age,
                student_address=student_address,
                student_name=student_name
            )


def create_subject_marks():
    try:
        student_objects=Student.objects.all()
        #bring all students
        for student in student_objects:
            #bring all subjects
            subjects=Subject.objects.all()
            for subject in subjects:
                #create 
                SubjectMarks.objects.create(
                    subject=subject,
                    student=student,
                    marks=random.randint(0,100)
                )
    except Exception as e:
        print(e)


def generate_rank():
    #generating ranks
    studentranklist = Student.objects.annotate(total_marks=Sum('student__marks'))
    #see the explanation of the brackets in detail on GPT
    #The name subject comes from the related name specified in a ForeignKey or OneToOneField defined in the Student model.


    # Now 'studentranklist' contains the queryset of Student objects with an additional attribute 'total_marks', which represents the total marks obtained by each student.

    # Order the students by their total marks in descending order
    studentranklist = studentranklist.order_by('-total_marks')
    #print(studentranklist.values_list('student_name', 'total_marks'))

    #mapping the rank of each student in Rank class, which contains student and rank 
    i=1

    #studentranklist is an objectof Students only, since it has been annotated from students only
    for thisstudent in studentranklist:
        #Create object of Rank Class
        Rank.objects.create(
            #first member is student, second is student_rank, see Rank class
            student=thisstudent,
            student_rank=i
        )
        i=i+1
    
  