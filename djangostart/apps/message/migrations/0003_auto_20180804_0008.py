# Generated by Django 2.0.7 on 2018-08-03 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_auto_20180801_2254'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermessage',
            options={'verbose_name': '用户留言信息', 'verbose_name_plural': '用户留言信息'},
        ),
        migrations.AlterModelTable(
            name='usermessage',
            table='user_message',
        ),
    ]
