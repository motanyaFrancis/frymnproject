# Generated by Django 3.1.1 on 2020-11-15 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('useradmin', '0001_initial'),
        ('authentication', '0001_initial'),
        ('usershop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('approval', models.BooleanField(null=True)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to='authentication.profile')),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useradmin.medicine')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to='authentication.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('trans_date', models.DateField(auto_now_add=True)),
                ('total_price', models.PositiveIntegerField(default=0)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user_trans', to='authentication.profile')),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useradmin.medicine')),
                ('order_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='activities.order')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user_trans', to='authentication.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('notification_type', models.CharField(choices=[('D', 'Declined'), ('A', 'Accepted'), ('L', 'Low'), ('E', 'Expired')], max_length=1)),
                ('is_read', models.BooleanField(default=False)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='n_from', to='authentication.profile')),
                ('medicine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='useradmin.medicine')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='activities.order')),
                ('stock', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='usershop.shopstock')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='n_to', to='authentication.profile')),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
                'ordering': ('-date',),
            },
        ),
    ]
