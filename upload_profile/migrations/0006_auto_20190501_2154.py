# Generated by Django 2.2 on 2019-05-01 13:54

from django.db import migrations, models
import upload_profile.storage


class Migration(migrations.Migration):

    dependencies = [
        ('upload_profile', '0005_auto_20190501_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_image',
            field=models.ImageField(storage=upload_profile.storage.ImageStorage(), upload_to='image/'),
        ),
    ]
