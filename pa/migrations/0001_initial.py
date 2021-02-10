# Generated by Django 2.2.17 on 2020-12-28 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Última atualização')),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pa.Base')),
                ('task', models.CharField(max_length=1500, verbose_name='Qual a tarefa a ser adicionada?')),
            ],
            options={
                'verbose_name': 'Tarefa',
                'verbose_name_plural': 'Tarefas',
            },
            bases=('pa.base',),
        ),
    ]