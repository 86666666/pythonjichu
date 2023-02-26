# Generated by Django 3.2.5 on 2022-08-05 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BOOK',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50, verbose_name='书名')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='定价')),
            ],
        ),
    ]