# Generated by Django 5.0.2 on 2024-02-16 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Teacher', '0009_alter_quiz_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='answer',
            field=models.CharField(choices=[('option_1', 'Option 1'), ('option_2', 'Option 2'), ('option_3', 'Option 3'), ('option_4', 'Option 4')], max_length=15),
        ),
    ]