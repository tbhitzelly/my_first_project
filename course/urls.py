from django.urls import path
from .views import branches_list, group_list, my_main_page, student_list

urlpatterns = [
    path('', my_main_page, name='my_main_page'),
    path('branches/', branches_list, name='branches_list'),
    path('student/', student_list, name='student_list'),
    path('groups/', group_list, name='group_list')
]