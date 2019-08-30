# Generated by Django 2.2.3 on 2019-07-27 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='CPF_funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.IntegerField()),
                ('cod_funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_outmed.Funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='contato_fornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=70)),
                ('telefone', models.IntegerField()),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_outmed.Fornecedor')),
            ],
        ),
    ]
