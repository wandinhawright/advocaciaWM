from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leadconsultoria',
            name='Data_de_Nascimento',
            field=models.DateField(default='2000-01-01'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='leadconsultoria',
            name='motivo',
            field=models.TextField(verbose_name='Descricao da solicitacao'),
        ),
        migrations.RemoveField(
            model_name='leadconsultoria',
            name='idade',
        ),
    ]
