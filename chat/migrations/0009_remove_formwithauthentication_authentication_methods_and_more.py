# Generated by Django 4.2.7 on 2023-11-30 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_formwithauthentication_other_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formwithauthentication',
            name='authentication_methods',
        ),
        migrations.RemoveField(
            model_name='formwithauthentication',
            name='evaluation_methods',
        ),
        migrations.DeleteModel(
            name='EvaluationMethod',
        ),
        migrations.DeleteModel(
            name='FormWithAuthentication',
        ),
    ]
