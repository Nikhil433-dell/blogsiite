# Generated by Django 3.2.5 on 2021-10-03 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_blog_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pro_img',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
