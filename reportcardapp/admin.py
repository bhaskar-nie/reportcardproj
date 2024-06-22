from django.contrib import admin
from .models import *
from django.db.models import Sum

# Register your models here.
admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Subject)

class SubjectMarksAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'marks']
    #members inside list are the members inside the class models

admin.site.register(SubjectMarks, SubjectMarksAdmin)


class RankAdmin(admin.ModelAdmin):
    # This attribute specifies the fields to be displayed in the list view of the Rank model in the admin interface.
    list_display = ['student', 'student_rank', 'total_marks', 'date_of_report_generation']

    def total_marks(self, obj):
        # Get all the SubjectMarks objects for the student associated with this Rank instance (obj).
        subject_marks = SubjectMarks.objects.filter(student=obj.student)
        
        # Aggregate the total marks for the student by summing up the marks from all SubjectMarks objects.
        # The aggregate function returns a dictionary where 'total' is the key, and the sum of marks is the value.
        total = subject_marks.aggregate(total=Sum('marks'))['total'] # dictionary to int
        
        # Return the total marks for display in the admin interface.
        return total

    # This sets the column header for the 'total_marks' field in the Django admin list view to 'Total Marks'.
    total_marks.short_description = 'Total Marks'

# Register the Rank model with the RankAdmin class to customize its representation in the admin interface.
admin.site.register(Rank, RankAdmin)
