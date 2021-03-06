# Generated by Django 2.0.4 on 2018-11-06 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EstiloMusical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('bandas', models.ManyToManyField(to='music.Banda')),
            ],
        ),
        migrations.CreateModel(
            name='Musico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('sobrenome', models.TextField()),
                ('idade', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='banda',
            name='estilo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.EstiloMusical'),
        ),
        migrations.AddField(
            model_name='banda',
            name='musicos',
            field=models.ManyToManyField(to='music.Musico'),
        ),
    ]
