# Generated by Django 3.2.3 on 2021-06-02 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20210602_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='href',
            field=models.CharField(blank=True, max_length=64, verbose_name='Адрес'),
        ),
    ]