# Generated by Django 3.2.3 on 2021-06-02 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_productcategory_href'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='href',
            field=models.URLField(blank=True, max_length=64, verbose_name='Адрес'),
        ),
    ]
