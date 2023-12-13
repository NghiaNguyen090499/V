# Generated by Django 4.2.7 on 2023-12-08 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_remove_imagereview_choice_choice_image_review_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='image_review',
        ),
        migrations.AddField(
            model_name='imagereview',
            name='choice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chat.choice'),
        ),
    ]
