from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q, Sum
# Create your views here.
def get_students(request):
    queryset=Student.objects.all()

    #check if search request
    if request.GET.get('search_query'): # the varname in brackets is the name of <input> tag
        search_query= request.GET.get('search_query')
        #update queryset 
        queryset=queryset.filter(
            Q(student_name__icontains=search_query)|
            Q(student_department__department__icontains=search_query)| #since stud_dept is an object
            Q(student_id__student_id__icontains=search_query)|
            Q(student_email__icontains=search_query)|
            Q(student_age__icontains=search_query)|
            Q(student_address__icontains=search_query)
        )



    paginator = Paginator(queryset, 25)  # Show 25 querys per page.
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'students.html',{"queryset": page_obj})
    #change context here 

def see_marks(request, student_id):
    #marks n usse related details SubjectMarks class me hain
    queryset=SubjectMarks.objects.filter(student__student_id__student_id=student_id)
    #SubjectMarks contains Student object->Student_IDobject->student_id member, compare with student_id from request
    #returns a StudentMarks objects list
    #each StudentMarks object conains student object, subjects object and marks int
    #print(queryset) VERY IMPORTANT TO UNDERSTAND HOW THE QUERYSET LOOKS LIKE


    #this queryset contains many marks fields, sum them
    total_marks=queryset.aggregate(Sum('marks')) 
    #The main issue here is that total_marks is being passed to the template as a dictionary
    total_marks=total_marks['marks__sum']#retrieve dict value


    #rank generate in seed.py and models
    
    return render(request, 'studentmarks.html', {'queryset':queryset, 'total_marks': total_marks})
