# Generated by Django 3.2.3 on 2021-06-14 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geek', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
