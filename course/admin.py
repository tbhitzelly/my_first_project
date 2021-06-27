from django.contrib import admin
from .models import Branch, Course, Group, Student


class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'address')
    list_filter = ('creator', 'manager')
    raw_id_fields = ('creator', )


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'Branch')
    search_fields = ('name', 'Branch')
    list_filter = ('creator', )
    raw_id_fields = ('creator', )


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'gender')
    search_fields = ('name', 'address', 'gender')
    list_filter = ('creator', )
    raw_id_fields = ('creator', )


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )

    


admin.site.register(Branch, BranchAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
