# Generated by Django 4.0.6 on 2022-08-28 21:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Badge_nonstaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_ID', models.CharField(default='000', max_length=255)),
                ('fullname', models.CharField(max_length=100)),
                ('dest_dept', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=20)),
                ('gadget_name', models.CharField(max_length=50)),
                ('serial_number', models.CharField(default='none', max_length=100)),
                ('date_time', models.DateTimeField(default=datetime.datetime.now)),
                ('date_time_out', models.DateTimeField(default=datetime.datetime.now)),
                ('gate', models.CharField(choices=[('shimoni', 'Shimoni'), ('kampala road gate', 'KAMPALA ROAD GATE'), ('plot 45', 'Plot 45')], default='none', max_length=20)),
                ('badge_status', models.CharField(default='in', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Badge_staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_ID', models.CharField(max_length=20)),
                ('bank_gadget', models.CharField(default='none', max_length=20)),
                ('bank_gadget_SN', models.CharField(default='none', max_length=20)),
                ('personal_gadget', models.CharField(default='none', max_length=50)),
                ('serial_number', models.CharField(default='none', max_length=100)),
                ('date_time', models.DateTimeField(default=datetime.datetime.now)),
                ('date_time_out', models.DateTimeField(default=datetime.datetime.now)),
                ('gate', models.CharField(choices=[('shimoni', 'Shimoni'), ('kampala road gate', 'KAMPALA ROAD GATE'), ('plot 45', 'Plot 45')], default='none', max_length=20)),
                ('badge_status', models.CharField(default='in', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Bank_gadgets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_ID', models.CharField(max_length=20)),
                ('bank_gadget', models.CharField(default='none', max_length=20)),
                ('bank_gadget_SN', models.CharField(default='none', max_length=20)),
                ('date_time', models.DateTimeField(default=datetime.datetime.now)),
                ('date_time_out', models.DateTimeField(default=datetime.datetime.now)),
                ('gate', models.CharField(choices=[('shimoni', 'Shimoni'), ('kampala road gate', 'KAMPALA ROAD GATE'), ('plot 45', 'Plot 45')], default='none', max_length=20)),
                ('badge_status', models.CharField(default='in', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_ID', models.CharField(max_length=50)),
                ('employee_name', models.CharField(max_length=100)),
                ('employee_dept', models.CharField(max_length=50)),
                ('gadget_ID', models.CharField(max_length=50)),
                ('gadget_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Personal_gadgets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_ID', models.CharField(max_length=20)),
                ('personal_gadget', models.CharField(default='none', max_length=50)),
                ('serial_number', models.CharField(default='none', max_length=100)),
                ('date_time', models.DateTimeField(default=datetime.datetime.now)),
                ('date_time_out', models.DateTimeField(default=datetime.datetime.now)),
                ('gate', models.CharField(choices=[('shimoni', 'Shimoni'), ('kampala road gate', 'KAMPALA ROAD GATE'), ('plot 45', 'Plot 45')], default='none', max_length=20)),
                ('badge_status', models.CharField(default='in', max_length=20)),
            ],
        ),
    ]
