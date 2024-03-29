# Generated by Django 4.1.2 on 2022-10-19 11:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('jedzonko', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='updated',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='votes',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
