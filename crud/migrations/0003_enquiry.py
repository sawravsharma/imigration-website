# Generated by Django 3.1.4 on 2021-02-25 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_subscriber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=40)),
                ('contact', models.CharField(max_length=40)),
                ('visa_type', models.CharField(max_length=40)),
            ],
        ),
    ]
