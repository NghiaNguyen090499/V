# Generated by Django 4.2.7 on 2023-11-28 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_alter_authenticationmethod_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authenticationmethod',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
