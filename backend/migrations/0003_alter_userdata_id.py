# Generated by Django 4.0.5 on 2022-06-12 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_userdata_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
