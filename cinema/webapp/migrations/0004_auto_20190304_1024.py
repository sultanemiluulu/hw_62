# Generated by Django 2.1 on 2019-03-04 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20190303_0906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='category',
        ),
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.ManyToManyField(null=True, related_name='movies', to='webapp.Category', verbose_name='Category'),
        ),
    ]
