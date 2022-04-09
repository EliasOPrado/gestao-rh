# Generated by Django 2.0 on 2022-04-06 12:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("empresas", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("departamentos", "0001_initial"),
        ("funcionarios", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="funcionario",
            name="departamento",
            field=models.ManyToManyField(to="departamentos.Departamento"),
        ),
        migrations.AddField(
            model_name="funcionario",
            name="empresa",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="empresas.Empresa",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="funcionario",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]