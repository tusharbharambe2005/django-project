# Generated by Django 5.0.2 on 2024-07-14 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='title',
            field=models.CharField(default=1, max_length=210),
            preserve_default=False,
        ),
    ]
