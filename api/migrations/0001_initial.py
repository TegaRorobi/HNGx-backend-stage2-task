# Generated by Django 4.2.5 on 2023-09-10 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('bio', models.TextField(blank=True, null=True)),
            ],
        ),
    ]