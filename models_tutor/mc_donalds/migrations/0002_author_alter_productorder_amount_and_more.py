# Generated by Django 4.2.10 on 2024-03-03 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mc_donalds', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=64, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='productorder',
            name='amount',
            field=models.IntegerField(db_column='amount', default=1),
        ),
        migrations.RenameField(
            model_name='productorder',
            old_name='amount',
            new_name='_amount',
        ),
    ]
