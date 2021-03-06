# Generated by Django 4.0.4 on 2022-05-11 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_contact_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='roll',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='number',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
