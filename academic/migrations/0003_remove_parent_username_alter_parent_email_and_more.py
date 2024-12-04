# Generated by Django 4.0 on 2023-10-01 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='username',
        ),
        migrations.AlterField(
            model_name='parent',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='parent',
            name='last_name',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='middle_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='parent',
            name='monthly_income',
            field=models.FloatField(blank=True, help_text='parents average monthly income', null=True),
        ),
        migrations.AlterField(
            model_name='parent',
            name='occupation',
            field=models.CharField(blank=True, help_text='current occupation', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='parent_guardian',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='academic.parent'),
        ),
    ]