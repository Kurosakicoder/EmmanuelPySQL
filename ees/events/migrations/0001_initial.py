# Generated by Django 3.0.2 on 2020-01-16 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolAssembly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('class_students', models.CharField(default='', max_length=50)),
                ('assembly_notice', models.TextField(default='')),
            ],
            options={
                'verbose_name': 'SchoolAssembly',
                'verbose_name_plural': 'SchoolAssembly',
            },
        ),
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='events/')),
                ('date', models.DateField()),
                ('headerline', models.CharField(default='', max_length=150)),
                ('first_para', models.TextField(default='')),
                ('second_para', models.TextField(default='')),
            ],
            options={
                'verbose_name': 'Trip',
                'verbose_name_plural': 'Trips',
            },
        ),
        migrations.CreateModel(
            name='UpcomingEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('headerline', models.CharField(default='', max_length=50)),
                ('program_notice', models.TextField(default='')),
            ],
            options={
                'verbose_name': 'UpcomingEvent',
                'verbose_name_plural': 'UpcomingEvents',
            },
        ),
    ]