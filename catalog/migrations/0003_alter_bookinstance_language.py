# Generated by Django 3.2.5 on 2022-01-27 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20220126_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.language'),
        ),
    ]
