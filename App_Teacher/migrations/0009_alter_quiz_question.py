# Generated by Django 5.0.2 on 2024-02-16 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Teacher', '0008_alter_replay_options_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='question',
            field=models.TextField(max_length=500),
        ),
    ]
