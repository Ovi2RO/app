# Generated by Django 4.2.7 on 2024-01-10 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laika', '0003_alter_laikaprofileuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laikaprofileuser',
            name='image',
            field=models.ImageField(blank=True, default='laika_logo_400.png', null=True, upload_to='images/'),
        ),
    ]
