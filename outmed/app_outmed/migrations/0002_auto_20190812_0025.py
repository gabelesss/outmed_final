# Generated by Django 2.2.3 on 2019-08-12 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_outmed', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.CharField(max_length=20)),
                ('editora', models.CharField(max_length=50)),
                ('edição', models.CharField(max_length=20)),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=50)),
                ('genero', models.CharField(default=None, max_length=80)),
                ('preco_compra', models.DecimalField(decimal_places=2, default=None, max_digits=5)),
                ('preco_venda', models.DecimalField(decimal_places=2, default=None, max_digits=5)),
                ('quantidade', models.IntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Data', models.DateField(verbose_name='Data da venda')),
                ('Valor', models.DecimalField(decimal_places=2, max_digits=5)),
                ('quantidade', models.IntegerField()),
                ('situação', models.CharField(blank=True, max_length=50, null=True)),
                ('Titulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_outmed.Livros')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='bairro',
            field=models.CharField(default=None, max_length=60, verbose_name='Bairro'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='celular',
            field=models.CharField(default=None, max_length=20, verbose_name='Celular'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='cep',
            field=models.CharField(default=None, max_length=10, verbose_name='CEP'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='cidade',
            field=models.CharField(default=None, max_length=60, verbose_name='Cidade'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='fixo',
            field=models.CharField(default=None, max_length=20, verbose_name='Fixo'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='last_name',
            field=models.CharField(default=None, max_length=80, verbose_name='Sobrenome'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='numero',
            field=models.CharField(default=None, max_length=10, verbose_name='Numero'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='rua',
            field=models.CharField(default=None, max_length=50, verbose_name='Rua'),
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='bairro',
            field=models.CharField(default=None, max_length=60, verbose_name='Bairro'),
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='cep',
            field=models.CharField(default=None, max_length=10, verbose_name='CEP'),
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='cidade',
            field=models.CharField(default=None, max_length=60, verbose_name='Cidade'),
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='cnpj',
            field=models.CharField(default=None, max_length=20, verbose_name='CNPJ'),
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='numero',
            field=models.CharField(default=None, max_length=10, verbose_name='Numero'),
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='rua',
            field=models.CharField(default=None, max_length=50, verbose_name='Rua'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='celular',
            field=models.CharField(default=None, max_length=20, verbose_name='Celular'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='cpf',
            field=models.CharField(default=None, max_length=20, verbose_name='CPF'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='fixo',
            field=models.CharField(default=None, max_length=20, verbose_name='Fixo'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='contato_fornecedor',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='contato_fornecedor',
            name='telefone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
        migrations.DeleteModel(
            name='CPF_funcionario',
        ),
        migrations.AddField(
            model_name='pedido',
            name='cod_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_outmed.Cliente'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='cod_funcionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_outmed.Funcionario'),
        ),
    ]
