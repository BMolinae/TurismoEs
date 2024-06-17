# Generated by Django 5.0.6 on 2024-06-17 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('foto', models.ImageField(default='default.jpg', upload_to='servicios')),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Servicios',
            },
        ),
    ]
