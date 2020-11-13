# Generated by Django 3.1.1 on 2020-10-28 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('useradmin', '0002_auto_20170311_1150'),
        ('authentication', '0006_auto_20201028_0815'),
        ('usershop', '0001_initial'),
        ('activities', '0007_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='n_from', to='authentication.profile'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='medicine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='useradmin.medicine'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='activities.order'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='stock',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='usershop.shopstock'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='n_to', to='authentication.profile'),
        ),
    ]