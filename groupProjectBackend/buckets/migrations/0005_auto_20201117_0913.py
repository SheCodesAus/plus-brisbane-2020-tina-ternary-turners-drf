# Generated by Django 3.0.8 on 2020-11-17 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buckets', '0004_auto_20201116_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bucket',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_buckets', to=settings.AUTH_USER_MODEL),
        ),
    ]