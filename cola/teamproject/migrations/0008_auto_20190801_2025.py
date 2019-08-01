# Generated by Django 2.2.3 on 2019-08-01 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teamproject', '0007_teamboard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamboard',
            name='img',
        ),
        migrations.AddField(
            model_name='teamboard',
            name='File',
            field=models.FileField(null=True, upload_to='teamboard/'),
        ),
        migrations.AddField(
            model_name='teamboard',
            name='board_type',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='teamboard',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teamproject.Team'),
        ),
        migrations.CreateModel(
            name='Team_todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.IntegerField()),
                ('content', models.CharField(max_length=50)),
                ('is_finished', models.BooleanField(default=False)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teamproject.Team')),
            ],
        ),
    ]
