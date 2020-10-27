# Generated by Django 3.1.2 on 2020-10-27 04:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('buildingID', models.AutoField(primary_key=True, serialize=False)),
                ('buildingName', models.CharField(max_length=20)),
                ('streetAddress', models.CharField(max_length=30)),
                ('supportFactor', models.FloatField(validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(20)])),
            ],
        ),
        migrations.CreateModel(
            name='Desk',
            fields=[
                ('deskID', models.AutoField(primary_key=True, serialize=False)),
                ('place', models.CharField(max_length=500)),
                ('Status', models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed')], max_length=6)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.building')),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('divisionID', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentType',
            fields=[
                ('equipmentTypeID', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=90)),
                ('leaserate', models.FloatField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(15)])),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('locationID', models.AutoField(primary_key=True, serialize=False)),
                ('suburb', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceLevel',
            fields=[
                ('servicelevelID', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=90)),
                ('serviceDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('equipmentID', models.AutoField(primary_key=True, serialize=False)),
                ('Status', models.CharField(choices=[('Available', 'Available'), ('Unavailable', 'Unavailable')], max_length=11)),
                ('desk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.desk')),
                ('equipmentType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.equipmenttype')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employeeID', models.AutoField(primary_key=True, serialize=False)),
                ('divisionDescription', models.CharField(max_length=90)),
                ('lastname', models.CharField(max_length=30)),
                ('firstname', models.CharField(max_length=30)),
                ('emailAddress', models.CharField(max_length=20)),
                ('phoneNumber', models.CharField(max_length=15)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.division')),
            ],
        ),
        migrations.CreateModel(
            name='EmpAndDesk',
            fields=[
                ('empAndDeskID', models.AutoField(primary_key=True, serialize=False)),
                ('desk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.desk')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.employee')),
            ],
        ),
        migrations.AddField(
            model_name='division',
            name='serviceLevel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.servicelevel'),
        ),
        migrations.CreateModel(
            name='DIVAndLOC',
            fields=[
                ('divAndLocID', models.AutoField(primary_key=True, serialize=False)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.division')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.location')),
            ],
        ),
        migrations.AddField(
            model_name='building',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.location'),
        ),
    ]