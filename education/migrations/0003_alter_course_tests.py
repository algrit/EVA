# Generated by Django 4.2 on 2023-04-27 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_alter_question_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='tests',
            field=models.ManyToManyField(related_name='courses', to='education.test', verbose_name='tests in course'),
        ),
    ]
