# Generated by Django 3.2.5 on 2024-03-17 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=5)),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_email', models.EmailField(max_length=254)),
                ('emp_contact', models.CharField(max_length=15)),
                ('emp_desg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.designation')),
            ],
        ),
    ]
