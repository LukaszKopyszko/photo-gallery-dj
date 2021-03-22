# Generated by Django 2.2.12 on 2021-03-21 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0002_auto_20210321_2300'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='photo',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='photo',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gallery_app.Category'),
        ),
    ]
