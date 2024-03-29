# Generated by Django 3.2.12 on 2023-11-24 17:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Of_code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('delete_timestamp', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, help_text='This is deleted datetime', null=True, verbose_name='Deleted Datetime')),
                ('is_deleted', models.BooleanField(default=False, help_text='This is deleted status', verbose_name='Deleted status')),
                ('is_active', models.BooleanField(default=True, help_text='This is active status', verbose_name='Active status')),
                ('value', models.PositiveIntegerField()),
                ('type', models.CharField(choices=[('price', 'Price'), ('percent', 'Percent')], max_length=10)),
                ('max_price', models.PositiveIntegerField(blank=True, null=True)),
                ('off_code', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'verbose_name': 'Off_code',
                'verbose_name_plural': 'Off_codes',
            },
        ),
        migrations.CreateModel(
            name='Order_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('delete_timestamp', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, help_text='This is deleted datetime', null=True, verbose_name='Deleted Datetime')),
                ('is_deleted', models.BooleanField(default=False, help_text='This is deleted status', verbose_name='Deleted status')),
                ('is_active', models.BooleanField(default=True, help_text='This is active status', verbose_name='Active status')),
                ('Count', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='product.product')),
            ],
            options={
                'verbose_name': 'Order item',
                'verbose_name_plural': 'Order items',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('delete_timestamp', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, help_text='This is deleted datetime', null=True, verbose_name='Deleted Datetime')),
                ('is_deleted', models.BooleanField(default=False, help_text='This is deleted status', verbose_name='Deleted status')),
                ('is_active', models.BooleanField(default=True, help_text='This is active status', verbose_name='Active status')),
                ('status_Order', models.IntegerField(blank=True, choices=[(1, 'Current'), (2, 'Delivered'), (3, 'Canceled')], default=1, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='customer.address')),
                ('off_code', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='order.of_code')),
                ('order_items', models.ManyToManyField(to='order.Order_item')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Order',
            },
        ),
    ]
