# Generated by Django 4.0.3 on 2022-03-17 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traversetnapi', '0005_alter_member_about'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='memberId',
            new_name='member',
        ),
    ]
