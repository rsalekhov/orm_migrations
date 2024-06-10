from django.shortcuts import render
from .models import Student


def students_list(request):
    template = 'school/students_list.html'

    # используйте этот параметр для упорядочивания результатов
    ordering = 'group'

    # Получаем список студентов и упорядочиваем его
    students = Student.objects.all().order_by(ordering)

    # Передаем список студентов в контекст
    context = {'students': students}

    return render(request, template, context)

