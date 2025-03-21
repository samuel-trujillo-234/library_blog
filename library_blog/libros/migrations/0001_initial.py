# Generated by Django 5.1.7 on 2025-03-21 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=50)),
                ('sinopsis', models.TextField()),
                ('portada', models.ImageField(blank=True, null=True, upload_to='portadas/')),
                ('fecha_publicacion', models.DateField()),
            ],
        ),
    ]
