# Generated by Django 4.2.3 on 2023-07-04 12:50

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
                ('clienteId', models.AutoField(primary_key=True, serialize=False)),
                ('aziendaFlag', models.BooleanField(default=False)),
                ('clienteName', models.CharField(max_length=20)),
                ('clienteCognome', models.CharField(max_length=20)),
                ('clienteCodF', models.CharField(max_length=16)),
                ('clienteregione', models.CharField(max_length=50)),
                ('clientepiva', models.CharField(max_length=11)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clienti',
            },
        ),
        migrations.CreateModel(
            name='Contratto',
            fields=[
                ('id_contratto', models.AutoField(primary_key=True, serialize=False)),
                ('importo', models.FloatField()),
                ('data', models.DateField()),
                ('scadenzaContratto', models.CharField(max_length=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cliente', to='Anagrafica.cliente')),
            ],
            options={
                'verbose_name': 'Contratto',
                'verbose_name_plural': 'Contratti',
            },
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id_Pagamento', models.AutoField(primary_key=True, serialize=False)),
                ('dataPaga', models.DateField()),
                ('importo', models.FloatField()),
                ('id_Contratto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Anagrafica.contratto')),
            ],
            options={
                'verbose_name': 'Pagamento',
                'verbose_name_plural': 'Pagamenti',
            },
        ),
    ]