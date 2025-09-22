from django.contrib import admin
from .models import Department, Program, Teacher, MainPage

@admin.register(MainPage)
class MainPageAdmin(admin.ModelAdmin):
    list_display = ('title',)
    # Забороняємо додавати нові записи, якщо один вже є
    def has_add_permission(self, request):
        return MainPage.objects.count() == 0


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'head_of_department')
    search_fields = ('name', 'head_of_department')


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'coordinator_name', 'graduating_department')
    list_filter = ('graduating_department',)
    search_fields = ('name', 'code', 'coordinator_name')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'degree', 'department')
    list_filter = ('department', 'degree', 'position')
    search_fields = ('name', 'department__name')
