# Generated by Django 2.2.3 on 2019-09-24 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jaya', '0003_auto_20190902_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='sample.jpg', upload_to='pics'),
            preserve_default=False,
        ),
    ]
