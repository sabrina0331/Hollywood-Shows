# Generated by Django 3.2 on 2021-04-14 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('network', models.CharField(max_length=50)),
                ('released_date', models.DateField()),
            ],
        ),
    ]
