# Generated by Django 2.2.5 on 2019-10-17 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='sample.jpg', upload_to='picz'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='descr',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='head',
            field=models.CharField(max_length=100),
        ),
    ]
