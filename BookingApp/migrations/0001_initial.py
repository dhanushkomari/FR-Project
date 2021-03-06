# Generated by Django 3.1.4 on 2021-04-08 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CameraApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('designation', models.CharField(max_length=25)),
                ('contact', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Photo', models.ImageField(upload_to='doctors')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookingApp.department')),
            ],
            options={
                'verbose_name': 'Doctor',
                'verbose_name_plural': 'Doctors',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('Booking_time', models.CharField(choices=[('10:00 to 10:30', '10:00 to 10:30'), ('10:30 to 11:00', '10:30 to 11:00'), ('11:00 to 11:30', '11:00 to 11:30'), ('11:30 to 12:00', '11:30 to 12:00'), ('12:00 to 12:30', '12:00 to 12:30'), ('12:30 to 01:00', '12:30 to 01:00'), ('18:00 to 18:30', '18:00 to 18:30'), ('18:30 to 19:00', '18:30 to 19:00'), ('19:00 to 19:30', '19:00 to 19:30')], default='10:00 to 10:30', max_length=15)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookingApp.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CameraApp.patient')),
            ],
            options={
                'verbose_name': 'Booking',
                'verbose_name_plural': 'Bookings',
                'ordering': ('-id',),
            },
        ),
    ]
