# Generated by Django 2.1.7 on 2019-03-22 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('launch', '0011_auto_20190322_0655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='ownerprofile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
