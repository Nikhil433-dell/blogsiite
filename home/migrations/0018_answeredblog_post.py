# Generated by Django 3.2.5 on 2021-10-07 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_answeredblog'),
    ]

    operations = [
        migrations.AddField(
            model_name='answeredblog',
            name='post',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='home.blog'),
            preserve_default=False,
        ),
    ]
