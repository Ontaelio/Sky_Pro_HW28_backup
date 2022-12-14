# Generated by Django 4.1.3 on 2022-11-15 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='ad',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ads.category'),
        ),
        migrations.AddField(
            model_name='ad',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=15)),
                ('role', models.CharField(choices=[('moderator', 'moderator'), ('admin', 'admin'), ('member', 'member')], default='member', max_length=10)),
                ('age', models.PositiveSmallIntegerField()),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ads.location')),
            ],
        ),
    ]
