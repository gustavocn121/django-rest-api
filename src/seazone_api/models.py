from django.db import models


class Guest(models.Model):
    name = models.CharField(("Guest's full name"), max_length=255)
    email= models.EmailField(("Guest's email"), max_length=254)  
    phone_num = models.CharField(("Guest's contact number"), max_length=15)
    


class CalendarDate(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    user_id = models.ForeignKey(Guest, verbose_name=("Guest"),default=None,null=True,  on_delete=models.SET_NULL)


class Assignment(models.Model):
    date = models.ForeignKey(CalendarDate, on_delete=models.CASCADE, related_name="assignment_date", )
    time = models.TimeField(auto_now=False, auto_now_add=False)
    color = models.CharField(max_length=16, default='#FFFFFF')
    title = models.CharField(max_length=20)
    event_id = models.IntegerField()
    booking_id = models.CharField(max_length=6)
    
    
class CheckInOut(models.Model):
    num_childrens = models.IntegerField()
    num_adults = models.IntegerField()
    num_pets = models.IntegerField()

    
class Cleaning(models.Model):

    pass


class AssignmentTag(models.Model):
    name = models.CharField(max_length=10)    
    color = models.CharField(max_length=16, default='#FFFFFF')
    assignment_id = models.ForeignKey(Assignment, models.CASCADE)


    
    

    
