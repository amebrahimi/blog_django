# Generated by Django 4.1.1 on 2022-09-18 12:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_article_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publish',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
