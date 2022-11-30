# Generated by Django 4.1.2 on 2022-11-30 22:48

import ckeditor.fields
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, choices=[('ur', 'Urgent'), ('ac', 'Acceptable'), ('op', 'Optimized')], max_length=200, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
                ('meta_title', models.CharField(blank=True, max_length=200)),
                ('meta_description', models.CharField(max_length=400)),
                ('content', ckeditor.fields.RichTextField()),
                ('old_url', models.CharField(blank=True, max_length=200)),
                ('notes', models.TextField(blank=True, null=True)),
                ('service_tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
    ]
