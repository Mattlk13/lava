# Generated by Django 2.2.16 on 2020-10-07 08:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("lava_scheduler_app", "0053_testjob_and_worker_token"),
    ]

    operations = [
        migrations.CreateModel(
            name="RemoteArtifactsAuth",
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
                ("name", models.CharField(max_length=100, verbose_name="Token name")),
                ("token", models.CharField(max_length=100, verbose_name="Token value")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={"ordering": ["name"], "unique_together": {("name", "user")}},
        )
    ]