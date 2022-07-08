# Generated by Django 4.0.3 on 2022-07-01 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.TextField(default='')),
                ('firstname', models.TextField(default='')),
                ('middlename', models.TextField(default='')),
                ('gender', models.TextField(default='')),
                ('dob', models.DateField(default='')),
                ('vcat', models.TextField(default='')),
                ('email', models.TextField(default='')),
                ('phone', models.TextField(default='')),
            ],
        ),
    ]
