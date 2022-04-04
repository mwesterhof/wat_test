# Generated by Django 3.2.12 on 2022-04-04 12:33

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField([('page', wagtail.core.blocks.PageChooserBlock())], blank=True, null=True),
        ),
    ]