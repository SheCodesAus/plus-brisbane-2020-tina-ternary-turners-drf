# Generated by Django 3.0.8 on 2020-11-16 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bucket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_open', models.BooleanField(default=True)),
                ('source_bsb_number', models.IntegerField()),
                ('source_account_number', models.IntegerField()),
                ('source_account_name', models.TextField()),
                ('source_balance', models.IntegerField()),
                ('owner', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pipe_name', models.CharField(max_length=200)),
                ('dest_bsb_number', models.IntegerField()),
                ('dest_account_number', models.IntegerField()),
                ('dest_account_name', models.TextField()),
                ('dest_balance', models.IntegerField()),
                ('amount_dollar', models.IntegerField()),
                ('amount_percent', models.IntegerField()),
                ('bucket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pipes', to='buckets.Bucket')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_pipes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
