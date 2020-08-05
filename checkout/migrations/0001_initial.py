# Generated by Django 3.0.8 on 2020-08-05 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_ref', models.CharField(editable=False, max_length=32)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=256)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('order_total', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('product', models.ForeignKey(db_column='product', on_delete=django.db.models.deletion.CASCADE, to='services.Training_Type')),
                ('userprofile', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to='profiles.UserProfile')),
            ],
        ),
    ]
