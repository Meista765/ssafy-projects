# Generated by Django 4.2.16 on 2024-11-19 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DepositOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.TextField()),
                ('fin_co_no', models.TextField()),
                ('fin_prdt_cd', models.TextField()),
                ('intr_rate_type', models.TextField()),
                ('intr_rate_type_nm', models.TextField()),
                ('save_trm', models.IntegerField()),
                ('intr_rate', models.DecimalField(decimal_places=2, max_digits=4)),
                ('intr_rate2', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='DepositProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.TextField()),
                ('fin_co_no', models.TextField()),
                ('fin_prdt_cd', models.TextField(unique=True)),
                ('kor_co_nm', models.TextField()),
                ('fin_prdt_nm', models.TextField()),
                ('join_way', models.TextField()),
                ('mtrt_int', models.TextField()),
                ('spcl_cnd', models.TextField()),
                ('join_deny', models.IntegerField()),
                ('join_member', models.TextField()),
                ('etc_note', models.TextField()),
                ('max_limit', models.IntegerField()),
                ('dcls_strt_day', models.TextField()),
                ('dcls_end_day', models.TextField(null=True)),
                ('fin_co_subm_day', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='InstallmentOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.TextField()),
                ('fin_co_no', models.TextField()),
                ('fin_prdt_cd', models.TextField()),
                ('intr_rate_type', models.TextField()),
                ('intr_rate_type_nm', models.TextField()),
                ('rsrv_type', models.TextField()),
                ('rsrv_type_nm', models.TextField()),
                ('save_trm', models.IntegerField()),
                ('intr_rate', models.DecimalField(decimal_places=2, max_digits=4)),
                ('intr_rate2', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='InstallmentProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.TextField()),
                ('fin_co_no', models.TextField()),
                ('fin_prdt_cd', models.TextField(unique=True)),
                ('kor_co_nm', models.TextField()),
                ('fin_prdt_nm', models.TextField()),
                ('join_way', models.TextField()),
                ('mtrt_int', models.TextField()),
                ('spcl_cnd', models.TextField()),
                ('join_deny', models.IntegerField()),
                ('join_member', models.TextField()),
                ('etc_note', models.TextField()),
                ('max_limit', models.IntegerField()),
                ('dcls_strt_day', models.TextField()),
                ('dcls_end_day', models.TextField(null=True)),
                ('fin_co_subm_day', models.TextField()),
            ],
        ),
        migrations.AddConstraint(
            model_name='installmentproducts',
            constraint=models.UniqueConstraint(fields=('dcls_month', 'fin_co_no', 'fin_prdt_cd'), name='saving_product_primary_key'),
        ),
        migrations.AddConstraint(
            model_name='installmentproducts',
            constraint=models.CheckConstraint(check=models.Q(('join_deny__gte', 1), ('join_deny__lte', 3)), name='saving_join_deny_range_1_to_3'),
        ),
        migrations.AddField(
            model_name='installmentoptions',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='finances.installmentproducts'),
        ),
        migrations.AddConstraint(
            model_name='depositproducts',
            constraint=models.UniqueConstraint(fields=('dcls_month', 'fin_co_no', 'fin_prdt_cd'), name='deposit_product_primary_key'),
        ),
        migrations.AddConstraint(
            model_name='depositproducts',
            constraint=models.CheckConstraint(check=models.Q(('join_deny__gte', 1), ('join_deny__lte', 3)), name='product_join_deny_range_1_to_3'),
        ),
        migrations.AddField(
            model_name='depositoptions',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='finances.depositproducts'),
        ),
    ]
