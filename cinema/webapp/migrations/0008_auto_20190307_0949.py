# Generated by Django 2.1 on 2019-03-07 09:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import webapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20190305_1207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=webapp.models.generate_code, editable=False, max_length=10, unique_for_date='created_date')),
                ('status', models.CharField(choices=[('created', 'Created'), ('sold', 'Sold'), ('canceled', 'Canceled')], default='created', max_length=255, verbose_name='Status')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('seats', models.ManyToManyField(blank=True, related_name='booking', to='webapp.Seat')),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
                ('start_date', models.DateField(blank=True, null=True)),
                ('finish_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refund', models.BooleanField(default=False)),
                ('discount', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ticket', to='webapp.Discount', verbose_name='Discount')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ticket', to='webapp.Seat', verbose_name='Seat')),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='movie',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='movies', to='webapp.Category'),
        ),
        migrations.AlterField(
            model_name='show',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shows', to='webapp.Movie', verbose_name='Movie'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ticket', to='webapp.Show', verbose_name='Show'),
        ),
        migrations.AddField(
            model_name='booking',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='booking', to='webapp.Show', verbose_name='Show'),
        ),
    ]