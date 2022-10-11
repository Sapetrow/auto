# Generated by Django 4.1.1 on 2022-09-28 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("seau", "0003_alter_order_auto"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="datepub",
            field=models.DateTimeField(auto_now=True, verbose_name="Дата открытия"),
        ),
        migrations.AlterField(
            model_name="order",
            name="work",
            field=models.ManyToManyField(
                limit_choices_to={"cod": True}, to="seau.work"
            ),
        ),
    ]