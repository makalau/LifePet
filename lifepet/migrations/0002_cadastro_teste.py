# Generated by Django 4.0.4 on 2022-09-18 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifepet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='teste',
            field=models.CharField(choices=[('Grande', 'Grande'), ('Pequeno', 'Pequeno'), ('Medio', 'Medio')], default='exit', max_length=20),
            preserve_default=False,
        ),
    ]
