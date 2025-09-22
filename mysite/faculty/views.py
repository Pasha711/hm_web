from django.shortcuts import render, get_object_or_404
from .models import Department, Program, Teacher, MainPage

def index(request):
    """
    Відображає головну сторінку.
    Бере перший й єдиний запис з моделі MainPage.
    """
    main_page_content = MainPage.objects.first()
    context = {
        'content': main_page_content
    }
    return render(request, 'faculty/index.html', context)

def program_list(request):
    """
    Відображає список усіх спеціальностей.
    """
    programs = Program.objects.all().select_related('graduating_department')
    context = {
        'programs': programs
    }
    return render(request, 'faculty/programs_list.html', context)

def program_detail(request, pk):
    """
    Відображає детальну інформацію про конкретну спеціальність.
    """
    program = get_object_or_404(Program, pk=pk)
    # Перетворюємо рядок з дисциплінами у список
    disciplines_list = [d.strip() for d in program.disciplines.split(',')]
    context = {
        'program': program,
        'disciplines_list': disciplines_list
    }
    return render(request, 'faculty/program_detail.html', context)

def department_list(request):
    """
    Відображає список усіх кафедр та їх спеціальності.
    """
    departments = Department.objects.all().prefetch_related('programs')
    context = {
        'departments': departments
    }
    return render(request, 'faculty/departments_list.html', context)

def department_detail(request, pk):
    """
    Відображає детальну інформациі про кафедру та список викладачів.
    """
    department = get_object_or_404(
        Department.objects.prefetch_related('teachers'), 
        pk=pk
    )
    context = {
        'department': department
    }
    return render(request, 'faculty/department_detail.html', context)
