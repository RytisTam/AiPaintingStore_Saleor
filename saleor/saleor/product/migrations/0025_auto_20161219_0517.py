# Generated by Django 1.10.3 on 2016-12-19 11:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("product", "0024_migrate_json_data")]

    operations = [
        migrations.RemoveField(model_name="attributechoicevalue", name="image")
    ]
