# Generated by Django 3.2.13 on 2023-05-26 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0003_alter_users_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
    ]
