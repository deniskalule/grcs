# import cv2
# import datetime
import datetime as dt
from multiprocessing import context
import re
# from pyzbar import pyzbar
from django.db.models import Count
from django.db.models.functions import ExtractMonth
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ItemForm, PersonForm, BadgeForm, BadgeFormOut
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator




import calendar
@login_required(login_url='login')
def home(request):
    username = request.GET['username']
    gate = request.GET['gate']
    bin_staff = Badge_staff.objects.annotate(month=ExtractMonth('date_time')).values('month').annotate(count=Count('id')).values('month','count')
    bout_staff =Badge_staff.objects.filter(badge_status="out").annotate(month=ExtractMonth('date_time')).values('month').annotate(count=Count('id')).values('month','count')
    badgein_nonstaff = Badge_nonstaff.objects.annotate(month=ExtractMonth('date_time')).values('month').annotate(count=Count('id')).values('month','count')
    badgeout_nonstaff =Badge_nonstaff.objects.filter(badge_status="out").annotate(month=ExtractMonth('date_time')).values('month').annotate(count=Count('id')).values('month','count')
    
    #data for badged in staff
    monthNo=[]
    in_staff_count =[]
    for d in bin_staff:
        monthNo.append(calendar.month_name[d['month']])
        in_staff_count.append(d['count'])

    #data for month and count for badged in non staff
    monthNumber=[]
    count = []
    for d in badgein_nonstaff:
        monthNumber.append(calendar.month_name[d['month']])
        count.append(d['count'])
    #data for month and count of badged out non staff
    bo_monthNumber = []
    bo_count = []
    for d in badgeout_nonstaff:
        bo_monthNumber.append(calendar.month_name[d['month']])
        bo_count.append(d['count'])
    out_staff_count=[]
    for d in bout_staff:
            out_staff_count.append(d['count'])
    bin_staff_results = Badge_staff.objects.filter(badge_status="in")
    bout_staff_results = Badge_staff.objects.filter(badge_status="out")
    bin_nonstaff_results = Badge_nonstaff.objects.filter(badge_status="in")
    bout_nonstaff_results = Badge_nonstaff.objects.filter(badge_status="out")
    bin_staff_count = bin_staff_results.count()
    bout_staff_count = bout_staff_results.count()
    bin_nonstaff_count = bin_nonstaff_results.count()
    bout_nonstaff_count = bout_nonstaff_results.count()
    context = {
        'bin_staff_count': bin_staff_count,
        'bin_nonstaff_count': bin_nonstaff_count,
        'bout_staff_count': bout_staff_count,
        'bout_nonstaff_count': bout_nonstaff_count,
        'username': username,
        'gate':gate,
        'monthNumber':monthNumber,
        'in_staff_count':in_staff_count,
        'out_staff_count':out_staff_count,
        'count': count,
        'bo_monthNumber':bo_monthNumber,
        'bo_count': bo_count,
        
    }
    return render(request, "home.html", context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        gate = request.POST['gate']
        user = auth.authenticate(username=username, password=password)
        bin_staff_results = Badge_staff.objects.filter(badge_status="in")
        bin_nonstaff_results = Badge_nonstaff.objects.filter(badge_status="in")
        bout_nonstaff_results = Badge_nonstaff.objects.filter(badge_status="out")
        bout_staff_results = Badge_staff.objects.filter(badge_status="out")
        bin_staff_count = bin_staff_results.count()
        bout_staff_count = bout_staff_results.count()
        bin_nonstaff_count = bin_nonstaff_results.count()
        bout_nonstaff_count = bout_nonstaff_results.count()
        bin_staff = Badge_staff.objects.annotate(month=ExtractMonth('date_time')).values('month').annotate(count=Count('id')).values('month','count')
        bout_staff =Badge_staff.objects.filter(badge_status="out").annotate(month=ExtractMonth('date_time')).values('month').annotate(count=Count('id')).values('month','count')
        badgein_nonstaff = Badge_nonstaff.objects.annotate(month=ExtractMonth('date_time')).values('month').annotate(count=Count('id')).values('month','count')
        badgeout_nonstaff =Badge_nonstaff.objects.filter(badge_status="out").annotate(month=ExtractMonth('date_time')).values('month').annotate(count=Count('id')).values('month','count')
        
        monthNo=[]
        in_staff_count =[]
        out_staff_count =[]
        for d in bin_staff:
            monthNo.append(calendar.month_name[d['month']])
            in_staff_count.append(d['count'])
        monthNumber=[]
        count = []
        for d in badgein_nonstaff:
            monthNumber.append(calendar.month_name[d['month']])
            count.append(d['count'])
        bo_monthNumber = []
        bo_count = []
        for d in badgeout_nonstaff:
            bo_monthNumber.append(calendar.month_name[d['month']])
            bo_count.append(d['count'])
        for d in bout_staff:
            out_staff_count.append(d['count'])
        if user is not None:
            # # auth.login(request, user)
            # # print('Login Successful!')
            if gate:
                request.session['username'] = username
                auth.login(request, user)
                return render(request,'home.html',{'bin_staff_count': bin_staff_count,'bout_staff_count': bout_staff_count,'bin_nonstaff_count': bin_nonstaff_count,'bout_nonstaff_count': bout_nonstaff_count,"username":username,"gate":gate, "monthNumber":monthNumber,"count":count,'in_staff_count':in_staff_count,'out_staff_count':out_staff_count,'bo_monthNumber':bo_monthNumber,'bo_count':bo_count})
            else:
                messages.error(request, 'Gate is not selected,Try again')
                return redirect('login')
            
            # return redirect('home',{"username":username})
        else:
            messages.error(request, 'Username or Password not correct,Try again')
            return redirect('login')
        
    else:
        return render(request, 'login.html')


@login_required(login_url='home')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        print('logged out from App..')
        return redirect('login')


# Creating, Validating and saving forms
@login_required(login_url='home')
def register_item(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('badge')
    else:
        form = ItemForm()
    context = {
        "form_item": form
    }
    return render(request, 'register_item.html', context)


@login_required(login_url='home')
def person(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('badge')
    else:
        form = PersonForm()
    context = {
        "form_person": form
    }
    return render(request, 'person.html', context)


@login_required(login_url='home')
def badge(request):
    form = BadgeForm()
    form_person = PersonForm()
    form_item = ItemForm()
    if request.method == 'POST':
        form = BadgeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BadgeForm()
    context = {
        "form_badge": form,
        "form_person": form_person,
        "form_item": form_item,
        "username": username
    }
    return render(request, 'badge.html', context)


# Creating Functions to Update data by the Users
def update_person(request, pk):
    person = Person.objects.get(id=pk)
    form = PersonForm(instance=person)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'update_person.html', context)


def update_badge_staff(request, pk):
    username = request.GET['username']
    gate = request.GET['gate']
    badge = Badge_staff.objects.get(id=pk)
    if request.method == 'POST':
        badge.employee_ID = request.POST['employee_id']
        badge.bank_gadget = request.POST['bank_gadget']
        badge.personal_gadget = request.POST['personal_gadget']
        badge.serial_number = request.POST['serial_number']
        # post.gate = gate
        badge.save()
    context = {
        'username': username,
        'gate':gate
    }
    return render(request, 'badgedinstaff.html', context)


def update_badge_nonstaff(request, pk):
    username = request.GET['username']
    gate = request.GET['gate']
    badge = Badge_nonstaff.objects.get(id=pk)
    if request.method == 'POST':
        badge.fullname = request.POST['name']
        badge.dest_dept = request.POST['dest_dept']
        badge.visitor_ID = request.POST['visitor_id']
        badge.contact = request.POST['contact']
        badge.gadget_name = request.POST['gadget_name']
        badge.serial_number = request.POST['serial_number']
        # post.gate = gate
        badge.save()
    context = {
        'username': username,
        'gate':gate
    }
    # message = "<script>alert('updated successfully');</script>"
    return render(request, 'badgedinnonstaff.html', context)
    # return HttpResponseRedirect('badgedinnonstaff.html')
    


def update_badge_out(request, pk):
    badge_out = Badge.objects.get(id=pk)
    form = BadgeFormOut(instance=badge_out)
    if request.method == 'POST':

        form = BadgeFormOut(request.POST, instance=badge_out)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'update_badge_out.html', context)


def view_items(request):
    items_results = Item.objects.all()
    items_count = items_results.count()
    context = {
        'items_results': items_results,
        'items_count': items_count
    }
    return render(request, 'view_items.html', context)


def view_badge(request):
    badge_results = Badge.objects.all()
    return render(request, 'view_badge.html', {'badge_results': badge_results})


def view_person(request):
    person_results = Person.objects.all()
    return render(request, 'view_person.html', {'person_results': person_results})


# function for deleting person
def delete_bin_staff(request, pk):
    username = request.GET['username']
    gate = request.GET['gate']
    badge = Badge_staff.objects.get(id=pk)
    badge.badge_status = "out"
    now = dt.datetime.now()
    badge.date_time_out=now.strftime("%Y-%m-%d %H:%M:%S")
    badge.save()
    results = Badge_staff.objects.filter(badge_status='out')
    return render(request, 'badgedoutstaff.html', {"username":username,"gate":gate,"results":results})


    


# function for deleting item
def delete_item(request, pk):
    item_delete = Item.objects.get(id=pk)
    item_delete.delete()
    return redirect('view_item')


# function for deleting badge
def delete_badge(request, pk):
    username = request.GET['username']
    gate = request.GET['gate']
    badge = Badge_nonstaff.objects.get(id=pk)
    badge.badge_status = "out"
    now = dt.datetime.now()
    badge.date_time_out=now.strftime("%Y-%m-%d %H:%M:%S")
    badge.save()
    results = Badge_nonstaff.objects.filter(badge_status='out')
    return render(request, 'badgedoutnonstaff.html', {"username":username,"gate":gate,"results":results})
    


# function to search in the data Person
def person_search_bar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            persons = Person.objects.filter(organisation__icontains=query)
            return render(request, 'person_search.html', {'persons': persons})
        else:
            print("No person to search from")
            return render(request, 'person_search.html', {})


# function to search in the data item
def item_search_bar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            items = Item.objects.filter(item_name__icontains = query)
            context = {
                'items': items
                       }
            return render(request, 'item_search.html', context)
        else:
            print("No Items to search from")
            return render(request, 'item_search.html', {})


# Function to search for badges or badged items
def badge_search_bar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            badges = Badge.objects.filter(location__icontains=query)

            context = {
                'badges': badges,
            }
            return render(request, 'badge_search.html', context)
        else:
            print("No Badge to search from")
            return render(request, 'badge_search.html', {})


# function for badge in staff
def badgeIn_staff(request):
    username = request.GET['username']
    gate = request.GET['gate']
    # results = Badge_staff.objects.only('employee_id')
    if request.method == 'POST' and request.POST['bank_gadget']:
        # row = request.POST['row']
        # print(row)
        # for x in row:
        post = Badge_staff()
        post.employee_ID = request.POST['employee_id']
        post.bank_gadget = request.POST['bank_gadget']
        post.bank_gadget_SN = request.POST['bserial_number']
        post.gate = gate
        post.save()
    context={
        'username': username,
        'gate':gate
    }
    return render(request, 'badgeIn.html', context)



def badgeIn(request):
    username = request.GET['username']
    gate = request.GET['gate']
    if request.method == 'POST' and request.POST['personal_gadget']:
        post = Badge_staff()
        post.employee_ID = request.POST['employee_id']
        # post.bank_gadget = request.POST['bank_gadget']
        # post.bank_gadget_SN = request.POST['bserial_number']
        post.personal_gadget = request.POST['personal_gadget']
        post.serial_number = request.POST['serial_number']
        post.gate = gate
        post.save()
        # messages.error(request, "<script>alert('Badge In successful');</script>")
    context={
        'username': username,
        'gate':gate
    }
    return render(request, 'badgeIn.html', context)
    

    return render(request, 'badgeIn.html', context)

# function for badge out staff
def badgeout_staff(request):
    username = request.GET['username']
    gate = request.GET['gate']
    results = Badge_staff.objects.filter(badge_status="in")
    p = Paginator(Badge_staff.objects.filter(badge_status="in"),5)
    page = request.GET.get('page')

    staff = p.get_page(page)
    return render(request, 'badgeout_staff.html', {"username":username,"gate":gate, 'results':results,"staff":staff})

#function for badge in non staff
def badgeIn_nonstaff(request):
    username = request.GET['username']
    gate = request.GET['gate']
    # results = Badge_nonstaff.objects.only('visitor_ID')
    if request.method == 'POST':
        post = Badge_nonstaff()
        post.fullname = request.POST['name']
        post.dest_dept = request.POST['dest_dept']
        post.visitor_ID = request.POST['visitor_id']
        post.contact = request.POST['contact']
        post.gadget_name = request.POST['gadget_name']
        post.serial_number = request.POST['serial_number']
        post.gate = gate
        post.save()
        # messages.error(request, 'Badge In successful')
        
    return render(request, 'badgeIn.html', {"username":username,"gate":gate})


#function for badge out non staff
def badgeout_nonstaff(request):
    username = request.GET['username']
    gate = request.GET['gate']
    # results = Badge_nonstaff.objects.filter(badge_status="in")
    p = Paginator(Badge_nonstaff.objects.filter(badge_status="in"),10)
    page = request.GET.get('page')
    results = p.get_page(page)
    return render(request, 'badgeout_nonstaff.html', {"username":username,"gate":gate,"results":results})

# function for badged in staff list
def badgedinstaff(request):
    username = request.GET['username']
    gate = request.GET['gate']
    results = Badge_staff.objects.all()

    p = Paginator(Badge_staff.objects.filter(badge_status="in"),5)
    page = request.GET.get('page')

    staff = p.get_page(page)
    # results = Badge_nonstaff.objects.all()
    return render(request, 'badgedinstaff.html', {"username":username,"gate":gate,"results":results, "staff":staff})

# function for badged out staff list
def badgedoutstaff(request):
    username = request.GET['username']
    gate = request.GET['gate']
    p = Paginator(Badge_staff.objects.filter(badge_status="out"),10)
    page = request.GET.get('page')

    staff = p.get_page(page)
    results = Badge_staff.objects.filter(badge_status="out")
    return render(request, 'badgedoutstaff.html', {"username":username,"gate":gate,"results":results,"staff":staff})

# function for badged in nonstaff list
def badgedinnonstaff(request):
    username = request.GET['username']
    gate = request.GET['gate']
    p = Paginator(Badge_nonstaff.objects.filter(badge_status="in"),7)
    
    page = request.GET.get('page')
    results  = p.get_page(page)
    return render(request, 'badgedinnonstaff.html', {"username":username,"gate":gate,"results":results})

# function for badged out non staff list
def badgedoutnonstaff(request):
    username = request.GET['username']
    gate = request.GET['gate']
    p = Paginator(Badge_nonstaff.objects.filter(badge_status="out"),7)

    page = request.GET.get('page')
    results  = p.get_page(page)
    
    return render(request, 'badgedoutnonstaff.html', {"username":username,"gate":gate,"results":results})




# fucntion for the search bar
def search(request):
    username = request.GET['username']
    gate = request.GET['gate']
    if request.method == "POST":
        searched = request.POST['searched']
        results = Badge_nonstaff.objects.filter(Q(fullname__icontains=searched) | Q(visitor_ID__icontains=searched)| Q(dest_dept__icontains=searched) | Q(gate__icontains=searched))
        results2 = Badge_staff.objects.filter(Q(employee_ID__icontains=searched) | Q(bank_gadget__icontains=searched)| Q(personal_gadget__icontains=searched))
        x = {'badge':'badge in','badge2': 'badge in staff'}
        context = {
            'username':username,
            'gate': gate,
            'searched': searched,
            'results':results,
            'results2':results2,
            'x':x
        }
        return render(request, "search.html",context)