# Generated by Django 3.2.13 on 2022-07-01 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("enrollments", "0021_auto_20220629_1419"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coursethroughenrollment",
            name="completed_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
