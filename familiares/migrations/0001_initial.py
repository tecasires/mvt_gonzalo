# Generated by Django 4.0.4 on 2022-05-28 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido_01', models.CharField(max_length=50)),
                ('apellido_02', models.CharField(max_length=50)),
                ('dni', models.IntegerField(max_length=8)),
                ('fecha_nacimiento', models.DateTimeField(max_length=10)),
                ('parentesco', models.CharField(blank=True, max_length=25, null=True)),
                ('ahorros', models.FloatField(max_length=10)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
