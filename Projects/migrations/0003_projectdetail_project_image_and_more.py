# Generated by Django 5.1.7 on 2025-03-22 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0002_alter_projectdetail_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectdetail',
            name='project_image',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='projectdetail',
            name='project_github_repo',
            field=models.URLField(blank=True, default='Comming Soon', null=True),
        ),
        migrations.AlterField(
            model_name='projectdetail',
            name='project_url',
            field=models.URLField(blank=True, default='Comming Soon', null=True),
        ),
    ]
