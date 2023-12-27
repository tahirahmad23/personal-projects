# Generated by Django 5.0 on 2023-12-26 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accomodation', '0006_alter_house_number_of_rooms_alter_house_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='air_conditioning',
            field=models.CharField(choices=[('Yes', 'Yes'), ('NO', 'No')], max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='backup_gen',
            field=models.CharField(choices=[('Yes', 'Yes'), ('NO', 'No')], max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='runing_water',
            field=models.CharField(choices=[('Yes', 'Yes'), ('NO', 'No')], max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='security_guards',
            field=models.CharField(choices=[('Yes', 'Yes'), ('NO', 'No')], max_length=255),
        ),
    ]