# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-25 12:56
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("lava_results_app", "0006_auto_20160111_1318")]

    operations = [
        migrations.CreateModel(
            name="QueryOmitResult",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("object_id", models.PositiveIntegerField()),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.ContentType",
                    ),
                ),
                (
                    "query",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lava_results_app.Query",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="querycondition",
            name="operator",
            field=models.CharField(
                choices=[
                    ("exact", "Exact match"),
                    ("iexact", "Case-insensitive match"),
                    ("ne", "Not equal to"),
                    ("icontains", "Contains"),
                    ("gt", "Greater than"),
                    ("lt", "Less than"),
                ],
                default="exact",
                max_length=20,
                verbose_name="Operator",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="queryomitresult",
            unique_together=set([("object_id", "query", "content_type")]),
        ),
    ]
