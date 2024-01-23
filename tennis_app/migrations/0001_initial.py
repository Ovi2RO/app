# Generated by Django 4.2.7 on 2024-01-23 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.IntegerField()),
                ('recipient', models.IntegerField()),
                ('content', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_gender', models.CharField(choices=[('A', 'Any'), ('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=10, null=True)),
                ('birth_date', models.DateField(default=django.utils.timezone.now)),
                ('phone', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('current_date', models.DateField(default=django.utils.timezone.now)),
                ('play_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(default='tennis_app/static/image/default.jpg', upload_to='tennis_app/static/image')),
                ('level', models.CharField(choices=[('A', 'Any'), ('1', 'Novice'), ('2', 'Intermediate'), ('3', 'Advanced'), ('4', 'Expert'), ('5', 'Master')], max_length=1)),
                ('language', models.CharField(choices=[('A', 'Any'), ('1', 'english'), ('2', 'deutsch'), ('3', 'spanish'), ('4', 'french'), ('5', 'persia')], max_length=1)),
                ('type', models.CharField(blank=True, max_length=100)),
                ('club_name', models.CharField(blank=True, max_length=50, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500)),
                ('rank', models.CharField(blank=True, choices=[('1', 'Very Bad'), ('2', 'Bad'), ('3', 'Good'), ('4', 'Very Good'), ('5', 'Perfect')], max_length=1)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='tennis_app.posts')),
            ],
        ),
    ]
