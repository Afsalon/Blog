# Generated by Django 4.1.1 on 2022-09-12 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0003_article_is_featured'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_date']},
        ),
    ]