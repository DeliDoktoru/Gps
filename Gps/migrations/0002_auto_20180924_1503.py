# Generated by Django 2.0.7 on 2018-09-24 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('date', models.DateTimeField()),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gps.Employee')),
            ],
            options={
                'verbose_name': 'Coordination',
                'verbose_name_plural': 'Coordinations',
            },
        ),
        migrations.RemoveField(
            model_name='employer',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='employer',
            name='lon',
        ),
    ]
