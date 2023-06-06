# Generated by Django 4.2.1 on 2023-06-06 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_blogs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=60)),
                ('usn', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=60)),
                ('college_name', models.CharField(max_length=100)),
                ('offer_status', models.CharField(max_length=60)),
                ('start_date', models.CharField(max_length=60)),
                ('end_date', models.CharField(max_length=60)),
                ('proj_report', models.CharField(max_length=60)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
