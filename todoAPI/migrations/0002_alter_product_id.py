# Generated by Django 5.0 on 2023-12-20 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
