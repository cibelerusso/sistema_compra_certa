# Generated by Django 3.2.9 on 2021-11-17 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0004_produto_consumo_medio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='peso_caixa',
        ),
    ]
