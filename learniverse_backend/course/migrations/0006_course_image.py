# Generated by Django 4.1.7 on 2023-03-29 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads'),
        ),
    ]