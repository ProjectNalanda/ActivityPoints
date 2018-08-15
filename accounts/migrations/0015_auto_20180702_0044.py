# Generated by Django 2.0.3 on 2018-07-01 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20180702_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leadpage',
            name='Category',
            field=models.IntegerField(choices=[(0, 'Select:'), (1, 'Student Professional Societies (IEEE,IET, ASME, SAE,NASA etc.)'), (2, 'College Association Chapters (Mechanical, Civil,Electrical etc.)'), (3, 'Festival & Technical Events(College approved)'), (4, 'Hobby Clubs'), (5, 'Special Initiatives(Approval from College and University is mandatory)')], default=0),
        ),
        migrations.AlterField(
            model_name='leadpage',
            name='DocType',
            field=models.IntegerField(choices=[(0, 'Select:'), (1, '(a) Certificate'), (2, '(b) Letter from Authorities'), (3, '(c) Appreciation recognition letter'), (4, '(d)Documentary evidence'), (5, '(e) Legal Proof'), (6, 'Others')], default=0),
        ),
        migrations.AlterField(
            model_name='leadpage',
            name='SubCategory',
            field=models.IntegerField(choices=[(0, 'Select:'), (1, 'Core coordinator'), (2, 'Sub coordinator'), (3, 'Volunteer')], default=0),
        ),
    ]
