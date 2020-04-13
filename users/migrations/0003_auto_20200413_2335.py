# Generated by Django 2.2.12 on 2020-04-13 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_device_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='room_name',
        ),
        migrations.AddField(
            model_name='device',
            name='device_room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Room'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('Living Room', 'LIVING ROOM'), ('Kitchen', 'KITCHEN'), ('Bed Room', 'BEDROOM'), ('Bath Room', 'BATHROOM'), ('Other', 'OTHER')], max_length=50),
        ),
    ]