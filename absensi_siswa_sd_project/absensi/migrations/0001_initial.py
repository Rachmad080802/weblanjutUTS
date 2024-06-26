# Generated by Django 5.0.3 on 2024-05-11 12:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kelas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('guru_pengajar', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Siswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('nomor_absen', models.PositiveIntegerField()),
                ('kelas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='absensi.kelas')),
            ],
        ),
        migrations.CreateModel(
            name='Absensi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField()),
                ('hadir', models.BooleanField()),
                ('siswa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='absensi.siswa')),
            ],
        ),
    ]
