# Generated by Django 4.0.5 on 2022-06-24 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_alter_book_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='img_url',
            field=models.URLField(max_length=1000, null=True),
        ),
    ]
