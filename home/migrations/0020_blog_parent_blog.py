# Generated by Django 3.2.5 on 2021-10-07 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_delete_answeredblog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='parent_blog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.blog'),
        ),
    ]