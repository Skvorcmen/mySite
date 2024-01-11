# Generated by Django 4.2.8 on 2024-01-09 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('summary', models.CharField(max_length=255)),
                ('full_text', models.TextField()),
                ('category', models.CharField(max_length=255)),
                ('pubdate', models.DateTimeField()),
                ('slug', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]
