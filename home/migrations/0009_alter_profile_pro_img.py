# Generated by Django 3.2.5 on 2021-10-05 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_profile_pro_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pro_img',
            field=models.ImageField(blank=True, default='media/profile.png', null=True, upload_to='media/'),
        ),
    ]
