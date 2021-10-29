# Generated by Django 3.2.5 on 2021-10-07 12:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0016_delete_followercount'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnsweredBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=15)),
                ('category', models.CharField(max_length=15)),
                ('desc', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
                ('question', models.CharField(blank=True, max_length=300)),
                ('liked', models.ManyToManyField(blank=True, related_name='uslike', to=settings.AUTH_USER_MODEL)),
                ('writer_name', models.ForeignKey(default='none', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]