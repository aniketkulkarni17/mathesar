# Generated by Django 3.1.14 on 2022-07-04 20:28

from django.db import migrations, models
import django.db.models.constraints


class Migration(migrations.Migration):

    dependencies = [
        ('mathesar', '0029_auto_20220629_1450'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='column',
            constraint=models.UniqueConstraint(deferrable=django.db.models.constraints.Deferrable['DEFERRED'], fields=('attnum', 'table'), name='unique_column'),
        ),
    ]
