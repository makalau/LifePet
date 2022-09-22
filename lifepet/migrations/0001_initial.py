# Generated by Django 4.0.4 on 2022-09-22 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('nascimento', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('telefone', models.CharField(max_length=25)),
                ('local', models.CharField(blank=True, max_length=255, null=True)),
                ('numero', models.CharField(blank=True, max_length=4, null=True)),
                ('bairro', models.CharField(blank=True, max_length=50, null=True)),
                ('cep', models.CharField(blank=True, max_length=20, null=True)),
                ('obs', models.TextField(blank=True, null=True)),
                ('especie', models.CharField(choices=[('cachorro', 'Cachorro'), ('gato', 'Gato')], max_length=20)),
                ('raca', models.CharField(blank=True, max_length=20, null=True)),
                ('porte', models.CharField(choices=[('grande', 'Grande'), ('medio', 'Medio'), ('pequeno', 'Pequeno')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
