# Generated by Django 3.2.9 on 2021-11-10 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_payment', models.CharField(choices=[('PD', 'paid'), ('AW', 'awaiting'), ('FL', 'failed')], max_length=2)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date of happend')),
            ],
        ),
    ]