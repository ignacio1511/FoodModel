# Generated by Django 4.0.5 on 2022-07-04 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_remove_foodimageurl_url_foodimageurl_images_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foodimageurl',
            old_name='images_url',
            new_name='image_url',
        ),
    ]
