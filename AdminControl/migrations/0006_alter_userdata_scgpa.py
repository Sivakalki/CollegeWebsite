# Generated by Django 4.2.2 on 2023-08-15 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminControl', '0005_alter_minorsmodel_selecteddept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='scgpa',
            field=models.DecimalField(decimal_places=6, max_digits=8),
        ),
    ]
