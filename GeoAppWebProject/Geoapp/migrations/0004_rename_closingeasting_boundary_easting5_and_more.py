# Generated by Django 4.1.2 on 2022-11-20 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Geoapp', '0003_alter_boundary_parcelid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boundary',
            old_name='ClosingEasting',
            new_name='Easting5',
        ),
        migrations.RenameField(
            model_name='boundary',
            old_name='ClosingNorthing',
            new_name='Northing5',
        ),
        migrations.AddField(
            model_name='boundary',
            name='District',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AddField(
            model_name='boundary',
            name='Locality',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AddField(
            model_name='boundary',
            name='OwnerPhoto',
            field=models.ImageField(default=0, upload_to=''),
        ),
        migrations.AddField(
            model_name='boundary',
            name='ParcelSizeInAcres',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='boundary',
            name='Region',
            field=models.CharField(default='none', max_length=100),
        ),
    ]
