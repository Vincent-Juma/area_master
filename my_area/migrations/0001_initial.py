# Generated by Django 3.2 on 2021-05-02 00:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Myloc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_area_name', models.CharField(max_length=60, null=True)),
                ('location', models.CharField(max_length=60)),
                ('my_area_image', models.ImageField(default='', upload_to='images/')),
                ('description', models.TextField(default='')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(null=True, upload_to='profile_pic/')),
                ('bio', models.CharField(max_length=200)),
                ('mylocs', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='my_area.myloc')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=200, null=True)),
                ('myloc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_area.myloc')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=60, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('myloc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_area.myloc')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
