# Generated by Django 3.2.10 on 2021-12-29 08:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='This will be exposed to the outside world.', unique=True, verbose_name='UUID')),
                ('code', models.CharField(help_text='Unique reference given by the author.', max_length=128, unique=True)),
                ('is_available', models.BooleanField(default=False, help_text='If TRUE, then record is available')),
                ('name', models.CharField(help_text='Name of the Product Type.', max_length=128, unique=True)),
                ('description', models.TextField(blank=True, default='', help_text='Description of the Product Type.')),
                ('system_type', models.CharField(choices=[('none', 'User defined'), ('handset', 'Handset'), ('tablet', 'Tablet')], default='none', max_length=20)),
                ('created_by', models.ForeignKey(blank=True, help_text='who created.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='producttype_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, help_text='who updated.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='producttype_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id', 'name', 'system_type'],
            },
        ),
        migrations.CreateModel(
            name='ProductGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='This will be exposed to the outside world.', unique=True, verbose_name='UUID')),
                ('code', models.CharField(help_text='Unique reference given by the author.', max_length=128, unique=True)),
                ('is_available', models.BooleanField(default=False, help_text='If TRUE, then record is available')),
                ('name', models.CharField(help_text='Name of the Option Group', max_length=128, unique=True)),
                ('description', models.TextField(blank=True, default='', help_text='Description of the Group')),
                ('created_by', models.ForeignKey(blank=True, help_text='who created.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productgroup_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, help_text='who updated.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productgroup_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id', 'name'],
            },
        ),
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='This will be exposed to the outside world.', unique=True, verbose_name='UUID')),
                ('code', models.CharField(help_text='Unique reference given by the author.', max_length=128, unique=True)),
                ('is_available', models.BooleanField(default=False, help_text='If TRUE, then record is available')),
                ('name', models.CharField(help_text='Name of the Brand', max_length=128, unique=True)),
                ('description', models.TextField(blank=True, default='', help_text='Small Description of the Brand')),
                ('created_by', models.ForeignKey(blank=True, help_text='who created.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productbrand_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, help_text='who updated.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productbrand_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='This will be exposed to the outside world.', unique=True, verbose_name='UUID')),
                ('code', models.CharField(help_text='Unique reference given by the author.', max_length=128, unique=True)),
                ('is_available', models.BooleanField(default=False, help_text='If TRUE, then record is available')),
                ('name', models.CharField(help_text='Name of product.', max_length=256)),
                ('in_stock', models.PositiveIntegerField(default=0, help_text='Amount of available products.')),
                ('short_description', models.TextField(blank=True, default='', help_text='Short summary, can be used in search results.')),
                ('long_description', models.TextField(blank=True, default='', help_text='Long Description')),
                ('weight', models.DecimalField(blank=True, decimal_places=3, help_text='Default weight of product in grams. ', max_digits=13, null=True)),
                ('release_date', models.DateField(blank=True, help_text='Release date. Product release on date, can be used for taking pre-orders.', null=True)),
                ('pre_order', models.BooleanField(default=False, help_text='Can be pre ordered', verbose_name='Product is a pre-order product')),
                ('is_serviceable', models.BooleanField(default=False, help_text='Is the product serviceable')),
                ('valid_from', models.DateTimeField(blank=True, help_text='Enter the datetime from which the product is valid', null=True, verbose_name='Valid from')),
                ('valid_until', models.DateTimeField(blank=True, help_text="Enter the datetime on which the product's validity expires", null=True, verbose_name='Valid until')),
                ('brand', models.ForeignKey(blank=True, help_text='related product brand', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='product.productbrand')),
                ('created_by', models.ForeignKey(blank=True, help_text='who created.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_created_by', to=settings.AUTH_USER_MODEL)),
                ('product_group', models.ForeignKey(blank=True, help_text='related product group.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='product.productgroup')),
                ('product_type', models.ForeignKey(blank=True, help_text='related product type', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='product.producttype')),
                ('updated_by', models.ForeignKey(blank=True, help_text='who updated.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id', 'name'],
            },
        ),
        migrations.AddIndex(
            model_name='producttype',
            index=models.Index(fields=['name', 'is_available', 'system_type'], name='product_pro_name_777b24_idx'),
        ),
        migrations.AddIndex(
            model_name='productgroup',
            index=models.Index(fields=['name', 'is_available'], name='product_pro_name_6699b1_idx'),
        ),
        migrations.AddIndex(
            model_name='productbrand',
            index=models.Index(fields=['name', 'is_available'], name='product_pro_name_c72138_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['code', 'name', 'product_group', 'product_type', 'brand', 'in_stock'], name='product_pro_code_7efa32_idx'),
        ),
    ]
