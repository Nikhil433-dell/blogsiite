# Generated by Django 3.2.5 on 2021-10-13 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_remove_profile_forget_password_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_img',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
