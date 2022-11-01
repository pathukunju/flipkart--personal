# Generated by Django 4.1.2 on 2022-10-28 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('companybname', models.TextField()),
                ('slideimage', models.ImageField(upload_to='')),
                ('slideimages', models.ImageField(upload_to='')),
                ('pimage1', models.ImageField(upload_to='')),
                ('pimage2', models.ImageField(upload_to='')),
                ('pimage3', models.ImageField(upload_to='')),
                ('pimage4', models.ImageField(upload_to='')),
                ('pimage5', models.ImageField(upload_to='')),
                ('price', models.IntegerField()),
                ('disprice', models.IntegerField()),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
        ),
    ]