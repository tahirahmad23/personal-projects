# Generated by Django 5.1.4 on 2024-12-31 10:51

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(),
        ),
    ]