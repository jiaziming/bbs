# Generated by Django 2.1.5 on 2019-05-10 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0002_auto_20190509_1122'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name_plural': '文章'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': '类别'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': '评论'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name_plural': '用户信息'},
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=255, verbose_name='标题'),
        ),
    ]
