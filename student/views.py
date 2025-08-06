from django.shortcuts import render , get_object_or_404 
from django.utils.text import slugify
from django.contrib import messages
from django.shortcuts import redirect
from .models import Student , Parent
from .forms import AddStudentForm , AddParentForm
from django.contrib.auth.decorators import login_required


@login_required
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
            return redirect('student_list')
        else:
            messages.error(request, 'There was an error in the form. Please correct it below.')
    else:
        student_form = AddStudentForm()
        parent_form = AddParentForm()

    return render(request, 'student/add-student.html', {
        'student_form': student_form,
        'parent_form': parent_form,
    })


@login_required
def student_list(request):
    student_list = Student.objects.all()
    return render(request , 'student/students.html', {'student_list' : student_list})

@login_required
def student_detail(request, slug):
    student_detail = get_object_or_404(Student, slug=slug)
    return render(request, 'student/student-details.html', {'student_detail': student_detail})

@login_required
def delete_student(request , slug):
    if request.method == 'POST':
        student = get_object_or_404(Student , slug = slug)
        parent = student.parent
        student.delete()
        # If this parent has no more students, delete them too
        if parent and not Student.objects.filter(parent=parent).exists():
            parent.delete()
        messages.success(request, "Student and parent deleted successfully.")
        return redirect('student_list')
    messages.error(request , 'record not deleted')
    return redirect('student_list')



# def edit_student(request , slug):
#     student = get_object_or_404(Student, slug = slug)
#     if request.method == 'POST':
#         student_form = AddStudentForm(request.POST , request.FILES , instance=student )
#         parent_form = AddParentForm(request.POST , instance=student.parent)

#         if student_form.is_valid() and parent_form.is_valid():
#             parent = parent_form.save()
#             student = student_form.save(commit=False)
#             student.parent = parent
#             student.save()
#             messages.success(request, 'Student and parent updated successfully.')
#             return redirect('student_detail', slug=student.slug)
#         else:
#             messages.error(request, 'There was an error in the form. Please correct it below.')

#     else:
#         student_form = AddStudentForm(instance=student)
#         parent_form = AddParentForm(instance=student.parent)

#     return render(request, 'student/edit-student.html', {
#             'student_form': student_form,
#             'parent_form': parent_form,
#             'student': student,
#         })

@login_required
def edit_student(request, slug):
    student = get_object_or_404(Student, slug=slug)

    if request.method == 'POST':
        student_form = AddStudentForm(request.POST, request.FILES, instance=student)
        parent_form = AddParentForm(request.POST, instance=student.parent)

        if student_form.is_valid() and parent_form.is_valid():
            # Do not update slug or admission_number
            parent = parent_form.save()
            updated_student = student_form.save(commit=False)
            updated_student.parent = parent
            updated_student.slug = student.slug  # Keep the original slug
            updated_student.admission_number = student.admission_number  # Keep original admission number
            updated_student.save()

            messages.success(request, 'Student and parent updated successfully.')
            return redirect('student_detail', slug=student.slug)
        else:
            messages.error(request, 'There was an error in the form. Please correct it.')
    else:
        student_form = AddStudentForm(instance=student)
        parent_form = AddParentForm(instance=student.parent)

    return render(request, 'student/edit-student.html', {
        'student_form': student_form,
        'parent_form': parent_form,
        'student': student,
    })

