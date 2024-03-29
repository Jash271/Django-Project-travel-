# Generated by Django 2.2.2 on 2019-07-06 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='itenary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('day1', models.TextField()),
                ('day2', models.TextField()),
                ('day3', models.TextField()),
                ('day4', models.TextField()),
                ('day5', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='plac',
            name='code',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
