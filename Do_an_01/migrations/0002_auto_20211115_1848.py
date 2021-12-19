# Generated by Django 3.2.6 on 2021-11-15 11:48

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Do_an_01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='submit_day',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='story',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Do_an_01.category'),
        ),
        migrations.AlterField(
            model_name='story',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='image',
            field=models.ImageField(default='Do_an_01/img/logo.jpg', upload_to='Do_an_01/img'),
        ),
        migrations.AlterField(
            model_name='story',
            name='public_day',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='story',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]