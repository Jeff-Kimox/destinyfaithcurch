# Generated by Django 4.1 on 2022-11-01 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chuch', '0003_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='sermon',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='chuch.sermon'),
            preserve_default=False,
        ),
    ]