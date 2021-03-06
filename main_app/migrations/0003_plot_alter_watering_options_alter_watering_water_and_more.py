# Generated by Django 4.0.3 on 2022-05-11 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_watering'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('zone', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='watering',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='watering',
            name='water',
            field=models.CharField(choices=[('Y', 'YES'), ('N', 'NO')], default='Y', max_length=1, verbose_name='Watered?'),
        ),
        migrations.AddField(
            model_name='seed',
            name='plots',
            field=models.ManyToManyField(to='main_app.plot'),
        ),
    ]
