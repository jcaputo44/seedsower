# Generated by Django 4.0.3 on 2022-05-10 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('water', models.CharField(choices=[('Y', 'YES'), ('N', 'NO')], default='Y', max_length=1)),
                ('seed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.seed')),
            ],
        ),
    ]
