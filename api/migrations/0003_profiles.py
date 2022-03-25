# Generated by Django 4.0.3 on 2022-03-25 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_note_delete_todo'),
    ]

    operations = [
        migrations.CreateModel(
            name='profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('name', models.CharField(default='name', max_length=80)),
                ('phone', models.CharField(default='813-xxx-xxxx', max_length=80)),
                ('address', models.CharField(default='abc street', max_length=80)),
                ('picUrl', models.CharField(default='xyz.jpeg', max_length=200)),
                ('workingHours', models.CharField(default='6-12am', max_length=30)),
                ('city', models.CharField(default='tampa', max_length=80)),
            ],
        ),
    ]