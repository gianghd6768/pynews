# Generated by Django 3.2.6 on 2021-11-16 07:46

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Do_an_01', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('author', models.CharField(max_length=250)),
                ('url', models.URLField(unique=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('public_day', models.DateField(default=datetime.date.today)),
                ('image', models.ImageField(default='Do_an_01/img/logo.jpg', upload_to='Do_an_01/img')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Do_an_01.category')),
            ],
        ),
    ]