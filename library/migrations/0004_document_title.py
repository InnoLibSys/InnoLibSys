# Generated by Django 2.0.3 on 2018-04-02 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='title',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
