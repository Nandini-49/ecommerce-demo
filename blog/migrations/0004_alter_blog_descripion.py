# Generated by Django 4.0.4 on 2022-05-20 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_brief_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='descripion',
            field=models.TextField(max_length=1000),
        ),
    ]
