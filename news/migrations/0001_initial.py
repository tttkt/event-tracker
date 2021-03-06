# Generated by Django 2.0.5 on 2018-06-05 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_name', models.CharField(max_length=200)),
                ('source_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Source'),
        ),
    ]
