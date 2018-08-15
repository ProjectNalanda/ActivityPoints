# Generated by Django 2.0.3 on 2018-08-02 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0019_auto_20180704_1842'),
    ]

    operations = [
        migrations.CreateModel(
            name='GamePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OneYear', models.IntegerField(choices=[(1, 'Yes'), (2, 'No')], default=0)),
                ('Category', models.IntegerField(choices=[(0, 'Select:'), (1, 'Sports'), (2, 'Games')], default=0)),
                ('Level', models.IntegerField(choices=[(0, 'Select:'), (1, 'College Events'), (2, 'Zonal Events'), (3, 'State/ University Events'), (4, 'National Events'), (5, 'International Events')], default=0)),
                ('Position', models.IntegerField(choices=[(0, 'Select:'), (1, 'First'), (2, 'Second'), (3, 'Third')], default=0)),
                ('DocType', models.IntegerField(choices=[(0, 'Select:'), (1, '(a) Certificate'), (2, '(b) Letter from Authorities'), (3, '(c) Appreciation recognition letter'), (4, '(d)Documentary evidence'), (5, '(e) Legal Proof'), (6, 'Others')], default=0)),
                ('File', models.FileField(blank=True, null=True, upload_to='')),
                ('user6', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
