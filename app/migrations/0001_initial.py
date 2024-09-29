# Generated by Django 4.1.13 on 2024-09-18 18:31

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
            name='Binding',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='bindings/')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('author', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=10000)),
                ('genre', models.CharField(max_length=50)),
                ('views', models.IntegerField(default=0)),
                ('star', models.IntegerField(default=0)),
                ('publication_date', models.DateField()),
                ('frontal_page', models.ImageField(blank=True, null=True, upload_to='frontal_pages')),
                ('book_file', models.FileField(blank=True, null=True, upload_to='books')),
                ('audiobook_file', models.FileField(blank=True, null=True, upload_to='audiobooks/')),
                ('audiobook_duration', models.DurationField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExtractedBook',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='extracted_books', serialize=False, to='app.book')),
                ('book_file', models.FileField(blank=True, null=True, upload_to='extracted_books')),
            ],
        ),
        migrations.CreateModel(
            name='VisitedActivity',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('visited_at', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-visited_at'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100)),
                ('personal_info', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('reviewer_name', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='app.book')),
            ],
        ),
        migrations.CreateModel(
            name='BookmarkID',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'book')},
            },
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(default=None, max_length=100)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('page', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('bookmarkId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.bookmarkid')),
            ],
        ),
        migrations.CreateModel(
            name='BindingItem',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('item_position', models.PositiveIntegerField()),
                ('resource_link', models.URLField(max_length=500)),
                ('binding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='app.binding')),
            ],
        ),
        migrations.AddField(
            model_name='binding',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.book'),
        ),
        migrations.AddField(
            model_name='binding',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
