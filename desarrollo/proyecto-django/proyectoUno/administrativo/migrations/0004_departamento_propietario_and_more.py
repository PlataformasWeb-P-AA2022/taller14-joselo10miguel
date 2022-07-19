# Generated by Django 4.0.5 on 2022-07-19 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0003_auto_20210624_0048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costo_depa', models.DecimalField(decimal_places=2, max_digits=100)),
                ('num_cuartos', models.IntegerField()),
                ('num_banios', models.IntegerField()),
                ('valor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('nacionalidad', models.CharField(choices=[('ecuatoriana', 'ecuatoriana'), ('peruana', 'peruana'), ('colombiana', 'colombiana')], max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='numerotelefonico',
            name='estudiante',
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
        migrations.DeleteModel(
            name='NumeroTelefonico',
        ),
        migrations.AddField(
            model_name='departamento',
            name='propietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propietario_depa', to='administrativo.propietario'),
        ),
    ]
