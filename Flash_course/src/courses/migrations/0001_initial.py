# Generated by Django 2.0.3 on 2018-04-03 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_number', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('course_id', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipeds', models.CharField(max_length=64)),
                ('institution_name', models.CharField(max_length=64)),
                ('location', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='parent_institution',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='courses.Institution'),
        ),
    ]