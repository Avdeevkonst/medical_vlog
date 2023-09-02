# Generated by Django 4.2.4 on 2023-08-31 14:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0005_commentmodel_photo"),
    ]

    operations = [
        migrations.AddField(
            model_name="postmodel",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                verbose_name="Время создания",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="commentmodel",
            name="created_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Время создания"),
        ),
    ]
