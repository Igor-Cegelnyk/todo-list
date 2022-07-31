# Generated by Django 4.0.6 on 2022-07-29 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('deadline', models.DateTimeField(blank=True, help_text='Please use the following format: <em>YYYY-MM-DD hh:mm:ss</em>.', null=True)),
                ('status', models.BooleanField(default=False)),
                ('tags', models.ManyToManyField(related_name='tasks', to='catalog.tag')),
            ],
            options={
                'ordering': ['status', '-datetime'],
            },
        ),
    ]