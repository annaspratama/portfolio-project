# Generated by Django 3.2.8 on 2021-10-25 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0006_alter_portfolio_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='url',
            field=models.TextField(default='Private', max_length=1000, unique=True),
        ),
    ]