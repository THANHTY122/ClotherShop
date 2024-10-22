# Generated by Django 5.0.4 on 2024-05-21 05:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LoaiSanPham',
            fields=[
                ('MaLoai', models.AutoField(primary_key=True, serialize=False)),
                ('TenLoai', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HoaDon',
            fields=[
                ('MaHD', models.AutoField(primary_key=True, serialize=False)),
                ('NgayDat', models.DateField()),
                ('TrangThai', models.CharField(max_length=100)),
                ('NgayGiao', models.DateField(null=True)),
                ('MaNV', models.IntegerField(null=True)),
                ('Tong', models.BigIntegerField()),
                ('MaKH', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NguoiDung',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DiaChi', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SanPham',
            fields=[
                ('MaSP', models.AutoField(primary_key=True, serialize=False)),
                ('TenSP', models.CharField(max_length=100)),
                ('DonGia', models.PositiveIntegerField()),
                ('HinhAnh', models.ImageField(upload_to='static/img/')),
                ('MoTa', models.TextField(max_length=255)),
                ('NCC', models.CharField(max_length=100)),
                ('SoLuong', models.IntegerField()),
                ('LoaiSP', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.loaisanpham')),
            ],
        ),
        migrations.CreateModel(
            name='CTHoaDon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TenSP', models.CharField(max_length=100)),
                ('SoLuong', models.IntegerField()),
                ('DonGia', models.PositiveIntegerField()),
                ('MaHD', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.hoadon')),
                ('MaSP', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.sanpham')),
            ],
        ),
    ]