# Generated by Django 4.0.4 on 2022-12-20 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_id', models.CharField(choices=[('USD', 'USD'), ('TRPV', 'TRPV'), ('TP', 'TP'), ('TID', 'TID'), ('THI', 'THI'), ('TESU', 'TESU'), ('TEST', 'TEST'), ('TESP', 'TESP'), ('TESOROS', 'TESOROS'), ('TESI', 'TESI')], max_length=20, unique=True)),
                ('title', models.CharField(choices=[('USD', 'USD'), ('TRPV', 'TRPV'), ('TP', 'TP'), ('TID', 'TID'), ('THI', 'THI'), ('TESU', 'TESU'), ('TEST', 'TEST'), ('TESP', 'TESP'), ('TESOROS', 'TESOROS'), ('TESI', 'TESI')], max_length=30)),
                ('clasification', models.CharField(blank=True, max_length=30, null=True)),
                ('value', models.CharField(max_length=30)),
                ('created_date', models.DateField()),
                ('expiration_date', models.DateField()),
                ('fee_paid', models.CharField(choices=[('Y', 'YES'), ('N', 'NO')], max_length=20)),
            ],
        ),
    ]
