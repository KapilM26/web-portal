# Generated by Django 2.1.7 on 2019-04-02 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cil', '0007_auto_20190220_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
