# Generated by Django 5.0.6 on 2024-06-28 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('duedate', models.DateField()),
                ('priority', models.CharField(choices=[('Low', 'LOW'), ('Medium', 'MEDIUM'), ('High', 'HIGH')], default='Low', max_length=10)),
                ('status', models.CharField(choices=[('pending', 'PENDING'), ('completed', 'COMPLETED')], default='pending', max_length=10)),
            ],
        ),
    ]
