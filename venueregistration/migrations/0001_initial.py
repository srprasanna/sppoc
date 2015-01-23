# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingTimeType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=255, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CapacityRange',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('minimum', models.IntegerField(default=0)),
                ('maximum', models.IntegerField(null=True, blank=True)),
                ('display_string', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Capacity Ranges',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Cities',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('mobile', models.BigIntegerField(max_length=10, null=True, blank=True)),
                ('company', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Countries & States',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CustomOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventSubType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('city', models.ForeignKey(to='venueregistration.City')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MealCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('how_to', models.TextField(default=b'', null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Meal Categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MealCategoryItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meal_category', models.ForeignKey(to='venueregistration.MealCategory')),
            ],
            options={
                'verbose_name_plural': 'Items in a Meal Category',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MealCategoryItemOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meal_category_item', models.ForeignKey(to='venueregistration.MealCategoryItem')),
            ],
            options={
                'verbose_name_plural': 'Meal Category Item Option Mapping',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MealItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=255, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Items in a Meal',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MealOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=255, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Options for a Meal Item',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MealType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=255, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Meal Types',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=255)),
                ('expiry_date', models.DateTimeField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=None, max_length=255, null=True, verbose_name=b'name of the package', blank=True)),
                ('custom', models.BooleanField(default=True, verbose_name=b'Is it a custom package')),
                ('meal_type', models.ForeignKey(to='venueregistration.MealType')),
            ],
            options={
                'verbose_name_plural': 'Packages',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PackageContents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contents', models.ForeignKey(to='venueregistration.MealCategoryItemOption')),
                ('package', models.ForeignKey(to='venueregistration.Package', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PackageDescription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(default=b'No Description', verbose_name=b'Package Description')),
                ('display_order', models.IntegerField(default=1)),
                ('package', models.ForeignKey(to='venueregistration.Package')),
            ],
            options={
                'verbose_name_plural': 'Package Descriptions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quote_key', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('date_of_booking', models.DateTimeField()),
                ('status', models.CharField(default=b'0', max_length=255, choices=[(b'0', b'Quote In Progress'), (b'1', b'Quote Requested'), (b'2', b'Responded'), (b'3', b'Accepted')])),
                ('guests', models.ForeignKey(default=1, blank=True, to='venueregistration.CapacityRange', null=True)),
                ('occasion', models.ForeignKey(default=1, blank=True, to='venueregistration.EventType', null=True)),
                ('package', models.ForeignKey(to='venueregistration.Package', null=True)),
                ('time', models.ForeignKey(to='venueregistration.BookingTimeType')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuoteVenue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quote', models.ForeignKey(to='venueregistration.Quote')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecentlyViewed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RelatedVenues',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SeatingOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Seating Options',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('country', models.ForeignKey(to='venueregistration.Country')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SuggestVenue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('venue', models.CharField(max_length=255, null=True, blank=True)),
                ('location', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(max_length=128, null=True, blank=True)),
                ('mobile_number', models.BigIntegerField()),
                ('is_verified', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(default=None, max_length=128, null=True, blank=True)),
                ('capacity', models.IntegerField()),
                ('minimum_occupancy', models.IntegerField(default=0)),
                ('created_at', models.DateField()),
                ('last_modified_at', models.DateField()),
                ('rating', models.DecimalField(default=3.0, max_digits=2, decimal_places=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('is_pure_veg', models.BooleanField()),
                ('serves_liquor', models.BooleanField()),
                ('base_package_rate', models.DecimalField(default=10000.0, verbose_name=django.core.validators.MinValueValidator(0), max_digits=10, decimal_places=2)),
                ('address1', models.CharField(default=None, max_length=255, null=True, blank=True)),
                ('address2', models.CharField(default=None, max_length=255, null=True, blank=True)),
                ('address3', models.CharField(default=None, max_length=255, null=True, blank=True)),
                ('lead_text', models.TextField(default=b'LOREM IPSUM DOLOR SIT AMET, CONSECTETUER ADIPISCING ELIT. NAM CURSUS. MORBI UT MI. NULLAM ENIM LEO, EGESTAS ID, CONDIMENTUM AT, LAOREET MATTIS, MASSA. SED ELEIFEND NONUMMY DIAM. PRAESENT MAURIS ANTE,')),
                ('extra_content', models.TextField(default=b'<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur ipsum velit, porta a orci gravida, tempor placerat leo. Vestibulum eu mauris in erat pulvinar fermentum. Donec quis lacus eu risus congue fermentum. Curabitur scelerisque odio ac pretium placerat. Donec convallis dapibus nunc id sagittis. Donec ut scelerisque urna. Nullam egestas semper est, sed lacinia elit ullamcorper sit amet.</p><p>Suspendisse nec sagittis tortor, ac ullamcorper lorem. Aenean vitae augue et quam pretium accumsan. Donec elementum molestie nunc, sit amet molestie magna sagittis ut. Aenean odio risus, faucibus quis gravida laoreet, scelerisque eu arcu. Donec nisi dui, facilisis id dictum et, faucibus sit amet nisi. Fusce nec erat leo. Nulla facilisi.</p>')),
                ('lighting', models.TextField(default=b'LED Lights')),
                ('music', models.TextField(default=b'Western Classical')),
                ('service', models.TextField(default=b'Bar, Buffet')),
                ('cost_per_head', models.DecimalField(default=2500.0, verbose_name=django.core.validators.MinValueValidator(0), max_digits=10, decimal_places=2)),
                ('review_count', models.IntegerField(default=0)),
                ('lattitude', models.DecimalField(default=17.46994, max_digits=10, decimal_places=5)),
                ('longitude', models.DecimalField(default=78.50757, max_digits=10, decimal_places=5)),
                ('event_type', models.ManyToManyField(to='venueregistration.EventType')),
                ('location', models.ForeignKey(to='venueregistration.Location')),
                ('manager', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VenueBookingHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('booking_time', models.ForeignKey(to='venueregistration.BookingTimeType')),
                ('venue', models.ForeignKey(to='venueregistration.Venue')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VenuePicture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'venue_images')),
                ('displayable', models.BooleanField()),
                ('is_display_pic', models.BooleanField()),
                ('venue', models.ForeignKey(to='venueregistration.Venue')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VenueRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('review', models.TextField(null=True, blank=True)),
                ('rating', models.DecimalField(default=3.0, max_digits=2, decimal_places=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('venue', models.ForeignKey(to='venueregistration.Venue')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VenueSupportsEventType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('evnet_subtype_id', models.IntegerField(default=None, null=True, blank=True)),
                ('event_type', models.ForeignKey(to='venueregistration.EventType')),
                ('venue', models.ForeignKey(to='venueregistration.Venue')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VenueType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Venue Types',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='venue',
            name='venue_type',
            field=models.ForeignKey(to='venueregistration.VenueType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='relatedvenues',
            name='related_venue',
            field=models.ForeignKey(related_name='related_venue', to='venueregistration.Venue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='relatedvenues',
            name='venue',
            field=models.ForeignKey(to='venueregistration.Venue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recentlyviewed',
            name='venue',
            field=models.ForeignKey(to='venueregistration.Venue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='quotevenue',
            name='venue',
            field=models.ForeignKey(to='venueregistration.Venue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='quote',
            name='venuetype',
            field=models.ForeignKey(default=1, blank=True, to='venueregistration.VenueType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mealcategoryitemoption',
            name='meal_option',
            field=models.ForeignKey(to='venueregistration.MealOption'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mealcategoryitem',
            name='meal_item',
            field=models.ForeignKey(to='venueregistration.MealItem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='favourite',
            name='venue',
            field=models.ForeignKey(to='venueregistration.Venue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventsubtype',
            name='event_type',
            field=models.ForeignKey(to='venueregistration.EventType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='customoption',
            name='venue',
            field=models.ForeignKey(to='venueregistration.Venue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(to='venueregistration.State'),
            preserve_default=True,
        ),
    ]
