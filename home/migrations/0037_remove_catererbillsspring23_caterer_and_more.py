# Generated by Django 4.1.7 on 2023-05-26 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_alter_rebate_allocation_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catererbillsspring23',
            name='Caterer',
        ),
        migrations.AddField(
            model_name='catererbillsspring23',
            name='caterer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.caterer'),
        ),
    ]
