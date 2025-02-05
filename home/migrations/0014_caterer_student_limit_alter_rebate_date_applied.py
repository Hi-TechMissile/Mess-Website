# Generated by Django 4.1.7 on 2023-04-18 16:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_rebate_email_student_email_alter_rebate_date_applied'),
    ]

    operations = [
        migrations.AddField(
            model_name='caterer',
            name='student_limit',
            field=models.IntegerField(default=0, help_text='The limit on number of students it can have', verbose_name='Caterers Student Limit'),
        ),
        migrations.AlterField(
            model_name='rebate',
            name='date_applied',
            field=models.DateField(default=datetime.date(2023, 4, 18), help_text='Date on which the rebate was applied'),
        ),
    ]
