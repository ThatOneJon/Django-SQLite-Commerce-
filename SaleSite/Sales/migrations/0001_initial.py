# Generated by Django 4.0.5 on 2022-07-26 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('price', models.IntegerField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='watchlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nameOfListing', to='Sales.sales')),
                ('price2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sales.sales')),
            ],
        ),
    ]