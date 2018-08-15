# Generated by Django 2.0.3 on 2018-07-01 17:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0010_auto_20180624_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='CultPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.IntegerField(choices=[(0, 'Select:'), (1, 'Music'), (2, 'Performing Arts'), (3, 'Literary Arts')], default=0)),
                ('SubCategory', models.IntegerField(choices=[(0, 'Select:'), (1, 'College Events'), (2, 'Zonal Events'), (3, 'State/ University Events'), (4, 'National Events'), (5, 'International Events')], default=0)),
                ('DocType', models.IntegerField(choices=[(0, 'Select:'), (1, 'First'), (2, 'Second'), (3, 'Third')], default=0)),
                ('File', models.FileField(blank=True, null=True, upload_to='')),
                ('user3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='natpage',
            old_name='user',
            new_name='user2',
        ),
    ]
