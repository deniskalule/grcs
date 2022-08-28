from django.contrib import admin
# from .models import Item, Person, Badge

# Creating a new Admin dashboard / Adding Another Admin Dashboard
from django.contrib.admin import AdminSite


class UserSite(AdminSite):
    site_header = "User"
    site_title = "User Manager"
    index_title = 'Welcome to User Portal'


# Defining Modules User can access
user_site = UserSite(name='user_portal')

