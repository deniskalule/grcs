# Generated by Django 4.1 on 2022-08-24 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bouapp', '0002_alter_badge_nonstaff_date_time_out_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='badge_staff',
            name='bank_gadget_SN',
            field=models.CharField(default='none', max_length=20),
        ),
    ]
