# Generated by Django 4.2.5 on 2023-10-22 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_cart_cartorder'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name_plural': '8. Orders'},
        ),
        migrations.AlterModelOptions(
            name='cartorder',
            options={'verbose_name_plural': '9. Order iteams'},
        ),
    ]
