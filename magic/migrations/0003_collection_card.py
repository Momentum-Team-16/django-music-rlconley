# Generated by Django 4.1.5 on 2023-01-03 20:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magic', '0002_alter_user_bio_alter_user_birth_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('edition', models.CharField(max_length=3)),
                ('condition', models.CharField(choices=[('NM', 'Near Mint'), ('PR', 'Poor'), ('MT', 'Mint'), ('GD', 'Good')], max_length=2)),
                ('language', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
