# Generated by Django 5.0.2 on 2024-04-13 20:45

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_instructor_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='description',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
