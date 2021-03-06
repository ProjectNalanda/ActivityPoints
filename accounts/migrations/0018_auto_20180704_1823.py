# Generated by Django 2.0.3 on 2018-07-04 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20180704_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='natpage',
            name='TwoYears',
            field=models.IntegerField(choices=[(1, 'Yes'), (2, 'No')], default=0),
        ),
        migrations.AlterField(
            model_name='natpage',
            name='Category',
            field=models.IntegerField(choices=[(1, 'Yes'), (2, 'No')], default=0),
        ),
        migrations.AlterField(
            model_name='natpage',
            name='DocType',
            field=models.IntegerField(choices=[(0, 'Select:'), (1, 'C certificate(os performance)'), (2, 'Best NSS Volunteer Awardee(University Level)'), (3, 'Participation in National Integration Camp'), (4, 'Participation in Pre-Republic Day Parade Camp'), (5, 'Best NSS Awardee(State Level/National Level)'), (6, 'Participation in Republic Day Parade Camp'), (7, 'International Youth Exchange Programme'), (8, 'Others')], default=0),
        ),
        migrations.AlterField(
            model_name='natpage',
            name='SubCategory',
            field=models.IntegerField(choices=[(0, 'Select:'), (1, 'NCC'), (2, 'NSS')], default=0),
        ),
    ]
