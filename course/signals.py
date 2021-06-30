from django.db.models.signals import post_save
from course.models import Student, Group
from django.dispatch import receiver
from datetime import date



@receiver([post_save], sender=Student)
def my_signal(sender, instance, created, **kwargs):
    if created:
        current_date = date.today()
        current_year = current_date.year
        age = current_year - instance.date_of_birth.year
        instance.age = age
        instance.save()

#@receiver([post_save], sender=Group)
#def signal_group(sender, instance, created, **kwargs):
    #counter = Group.objects.filter(name = instance)
    #res = counter.count
    #print(res)