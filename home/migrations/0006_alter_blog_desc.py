# Generated by Django 3.2.5 on 2021-10-04 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_blog_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='desc',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
