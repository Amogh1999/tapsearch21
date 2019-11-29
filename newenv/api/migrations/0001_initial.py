# Generated by Django 2.2.7 on 2019-11-25 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WordFrequencies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequency', models.IntegerField()),
                ('doc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Document')),
                ('word_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Words')),
            ],
            options={
                'ordering': ['frequency'],
            },
        ),
    ]