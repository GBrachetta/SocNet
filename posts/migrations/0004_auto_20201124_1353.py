# Generated by Django 3.1.3 on 2020-11-24 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20201124_1345'),
        ('posts', '0003_comment_like_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='liked',
            field=models.ManyToManyField(blank=True, related_name='likes', to='profiles.Profile'),
        ),
    ]