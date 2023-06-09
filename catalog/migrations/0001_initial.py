# Generated by Django 4.2 on 2023-05-02 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('biography', models.TextField()),
                ('photo', models.ImageField(upload_to='author_headshots')),
            ],
            options={
                'ordering': ['-last_name'],
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mail', models.EmailField(max_length=254)),
                ('website', models.URLField()),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pub_date', models.DateField()),
                ('synopsis', models.TextField()),
                ('genre', models.CharField(choices=[('FA', 'Fantasy'), ('SF', 'Science Fiction'), ('DY', 'Dystopian'), ('AA', 'Action & Adventure'), ('MY', 'Mystery'), ('HO', 'Horror'), ('TH', 'Thriller & Suspense'), ('HF', 'Historical Fiction'), ('RO', 'Romance'), ('ME', 'Memoir & Autobiography'), ('BI', 'Biography'), ('FD', 'Food & Drinks'), ('AP', 'Art & Photography'), ('SH', 'Self Help'), ('HI', 'History'), ('TR', 'Travel'), ('TC', 'True Crime'), ('HU', 'Humor'), ('ES', 'Essay'), ('GU', 'Guide'), ('RS', 'Religion & Spirituality'), ('HS', 'Humanities & Social sciences'), ('PA', 'Parenting & Families'), ('ST', 'Science & Technology'), ('CH', "Children's"), ('UN', 'Unknown')], default='UN', max_length=2)),
                ('cover_photo', models.ImageField(upload_to='book_covers')),
                ('rating', models.FloatField()),
                ('num_rating', models.PositiveIntegerField()),
                ('num_comments', models.PositiveIntegerField()),
                ('weekly_cover', models.BooleanField(default=False)),
                ('sell_price', models.FloatField()),
                ('init_price', models.FloatField()),
                ('stocks', models.PositiveIntegerField()),
                ('booked', models.PositiveIntegerField()),
                ('author', models.ManyToManyField(to='catalog.author')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.publisher')),
            ],
            options={
                'ordering': ['-title'],
            },
        ),
    ]
