# Generated by Django 4.0.3 on 2022-03-12 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traversetnapi', '0004_remove_member_name_alter_member_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='about',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
