# Generated by Django 4.2 on 2024-04-29 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_admin_u_id_client_u_id_stylist_u_id_stylist_verified_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Otp',
        ),
    ]
