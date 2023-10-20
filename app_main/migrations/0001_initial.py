
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122, null=True)),
                ('phone', models.CharField(max_length=122, null=True)),
                ('message', models.TextField(blank=True, max_length=900, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'User Feedback',
                'verbose_name_plural': 'User Feedbacks',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122, null=True)),
                ('email', models.CharField(max_length=122, null=True)),
                ('phone', models.CharField(max_length=122, null=True)),
                ('gender', models.CharField(blank=True, choices=[('', 'Select Gender'), ('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=122, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=122, null=True)),
                ('country', models.CharField(blank=True, max_length=122, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Custom User',
                'verbose_name_plural': 'Custom Users',
                'ordering': ['-id'],
            },
        ),
    ]