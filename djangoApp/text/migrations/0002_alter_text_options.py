# Generated by Django 4.2.5 on 2023-09-20 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='text',
            options={'ordering': ['-created_at']},
        ),
    ]
