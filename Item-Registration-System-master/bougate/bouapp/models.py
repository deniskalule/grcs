from django.db import models
from datetime import timezone, datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User





# creating the modal for employees and gadgets assigned to them
class Employee_Data(models.Model):
    employee_ID = models.CharField(max_length=50)
    employee_name = models.CharField(max_length=100)
    employee_dept = models.CharField(max_length=50)
    gadget_ID = models.CharField(max_length=50)
    gadget_type = models.CharField(max_length=50)

    def __str__(self):
        return self.employee_ID




# declaring the gates of BOU in form of tuples
gate_select = (
    ('shimoni', 'Shimoni'),
    ('kampala road gate', 'KAMPALA ROAD GATE'),
    ('plot 45', 'Plot 45')
)


# modal for badge staff
class Badge_staff(models.Model):
    employee_ID = models.CharField(max_length=20)
    bank_gadget = models.CharField(max_length=20,default='none')
    bank_gadget_SN = models.CharField(max_length=20,default='none')
    personal_gadget = models.CharField(max_length=50,default='none')
    serial_number = models.CharField(max_length=100,default='none')
    date_time = models.DateTimeField(default=datetime.now, blank=False)
    date_time_out = models.DateTimeField(default=datetime.now, blank=False)
    gate = models.CharField(max_length=20, choices=gate_select, default='none')
    badge_status = models.CharField(max_length=20,default="in")
    
    def __str__(self):
        return self.employee_ID


# modal for badge nonstaff
class Badge_nonstaff(models.Model):
    visitor_ID = models.CharField(max_length=255,default="000")
    fullname = models.CharField(max_length=100)
    dest_dept = models.CharField(max_length=50)
    contact = models.CharField(max_length=20)
    gadget_name = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=100,default='none')
    date_time = models.DateTimeField(default=datetime.now, blank=False)
    date_time_out = models.DateTimeField(default=datetime.now, blank=False)
    gate = models.CharField(max_length=20, choices=gate_select, default='none') 
    badge_status = models.CharField(max_length=20,default="in")
    # badgeout_status = models.CharField(max_length=20, choices=badgeout_status, default="none")

    def __str__(self):
        return self.fullname

class Personal_gadgets(models.Model):
    employee_ID = models.CharField(max_length=20)
    personal_gadget = models.CharField(max_length=50,default='none')
    serial_number = models.CharField(max_length=100,default='none')
    date_time = models.DateTimeField(default=datetime.now, blank=False)
    date_time_out = models.DateTimeField(default=datetime.now, blank=False)
    gate = models.CharField(max_length=20, choices=gate_select, default='none')
    badge_status = models.CharField(max_length=20,default="in")

    def __str__(self):
        return self.employee_ID

class Bank_gadgets(models.Model):
    employee_ID = models.CharField(max_length=20)
    bank_gadget = models.CharField(max_length=20,default='none')
    bank_gadget_SN = models.CharField(max_length=20,default='none')
    date_time = models.DateTimeField(default=datetime.now, blank=False)
    date_time_out = models.DateTimeField(default=datetime.now, blank=False)
    gate = models.CharField(max_length=20, choices=gate_select, default='none')
    badge_status = models.CharField(max_length=20,default="in")
    
    def __str__(self):
        return self.employee_ID