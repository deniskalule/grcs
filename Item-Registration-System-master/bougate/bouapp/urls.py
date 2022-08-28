from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('update_bank_gadget/<int:pk>/', views.update_bank_gadget, name='update_bank_gadget'),
    path('update_personal_gadget/<int:pk>/', views.update_personal_gadget, name='update_personal_gadget'),
    path('update_badge_nonstaff/<int:pk>/', views.update_badge_nonstaff, name='update_badge_nonstaff'),
    path('update_badge_out/<int:pk>/', views.update_badge_out, name='update_badge_out'),
    # Path for Deleting data in database
    path('delete_badge/<int:pk>/', views.delete_badge, name='delete_badge'),
    path('delete_bin_staff_bank/<int:pk>/', views.delete_bin_staff_bank, name='delete_bin_staff_bank'),
    path('delete_bin_staff_personal/<int:pk>/', views.delete_bin_staff_personal, name='delete_bin_staff_personal'),
    path('badgeIn', views.badgeIn, name='badgeIn'),
    path('badgeout_staff', views.badgeout_staff, name='badgeout_staff'),
    path('badgeIn_nonstaff', views.badgeIn_nonstaff, name='badgeIn_nonstaff'),
    path('badgeout_nonstaff', views.badgeout_nonstaff, name='badgeout_nonstaff'),
    path('badgedoutnonstaff', views.badgedoutnonstaff, name='badgedoutnonstaff'),
    path('badgedoutstaff', views.badgedoutstaff, name='badgedoutstaff'),
    path('badgedinnonstaff', views.badgedinnonstaff, name='badgedinnonstaff'),
    path('badgedinstaff', views.badgedinstaff, name='badgedinstaff'),
    path('badgeIn_staff', views.badgeIn_staff, name='badgeIn_staff'),
    path('search', views.search, name='search'),


]
