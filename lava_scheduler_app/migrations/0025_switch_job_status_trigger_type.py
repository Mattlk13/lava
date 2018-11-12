# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 09:47
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("lava_scheduler_app", "0024_do_not_cascade_deletions")]

    operations = [
        migrations.AlterField(
            model_name="notification",
            name="job_status_trigger",
            field=models.CharField(
                choices=[
                    (0, "Submitted"),
                    (1, "Running"),
                    (2, "Complete"),
                    (3, "Incomplete"),
                    (4, "Canceled"),
                    (5, "Canceling"),
                ],
                default=2,
                max_length=30,
                verbose_name="Job status trigger",
            ),
        )
    ]
