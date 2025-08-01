from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .forms import AddStudentForm , AddParentForm



# def add_student_with_parent(request):
#     if request.method == 'POST':
#         form = AddStudentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Record added successfully')
#             return redirect('add_student')
#         else:
#             messages.error(request, 'Error!')
#             return redirect('add_student')
#     else:
#         form = AddStudentForm()
#     return render(request, 'student/add-student.html', {'student_form': form})

def add_student_with_parent(request):
    if request.method == 'POST':
        student_form = AddStudentForm(request.POST, request.FILES)
        parent_form = AddParentForm(request.POST)

        if student_form.is_valid() and parent_form.is_valid():
            parent = parent_form.save()
            student = student_form.save(commit=False)
            student.parent = parent
            student.save()
            messages.success(request, 'Student and parent added successfully.')
            return redirect('add_student')
        else:
            messages.error(request, 'There was an error in the form. Please correct it below.')
    else:
        student_form = AddStudentForm()
        parent_form = AddParentForm()

    return render(request, 'student/add-student.html', {
        'student_form': student_form,
        'parent_form': parent_form,
    })



def student_list(request):
    return render(request , 'student/students.html')