# Generated by Django 3.0.8 on 2020-07-28 20:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_billing_address_line1', models.CharField(blank=True, max_length=80, null=True)),
                ('default_billing_address_line2', models.CharField(blank=True, max_length=80, null=True)),
                ('default_billing_address_postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('default_billing_address_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
