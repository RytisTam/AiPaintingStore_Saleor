# Generated by Django 3.2.15 on 2022-08-23 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0067_merge_20220715_1400"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="uuid",
            field=models.UUIDField(default=None, null=True),
        ),
        migrations.RunSQL(
            """
            ALTER TABLE account_user ALTER COLUMN uuid SET DEFAULT gen_random_uuid();
            """,
            migrations.RunSQL.noop,
        ),
    ]
