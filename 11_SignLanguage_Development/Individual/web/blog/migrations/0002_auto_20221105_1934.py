# Generated by Django 3.2 on 2022-11-05 10:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='region',
            field=models.CharField(choices=[('Africa', '아프리카'), ('Europe', '유럽'), ('Oceania', '오세아니아'), ('Asia', '아시아'), ('North America', '북아메리카'), ('South America', '남아메리카')], default='Asia', max_length=20, verbose_name='지역'),
        ),
        migrations.AddField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=250, verbose_name='제목'),
        ),
    ]
