# Generated by Django 5.1.2 on 2024-10-30 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_article_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlecommande',
            old_name='Commande',
            new_name='commande',
        ),
    ]
