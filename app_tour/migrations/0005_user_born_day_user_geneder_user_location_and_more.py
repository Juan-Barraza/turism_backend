# Generated by Django 5.1.1 on 2024-10-06 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tour', '0004_alter_user_preferred_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='born_day',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='geneder',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='picture',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
