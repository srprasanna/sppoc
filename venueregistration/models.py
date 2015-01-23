from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from PIL import Image
    
class NamedBase(models.Model):
    name = models.CharField(max_length=128)
    class Meta:
        abstract = True
    
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    company = models.CharField(null=True, blank=True, max_length=128)
    mobile_number = models.BigIntegerField()
    is_verified = models.BooleanField(default=False)
    
class OTP(models.Model):
    password = models.CharField(null=False,blank=False,max_length=255)
    expiry_date = models.DateTimeField()
    user = models.ForeignKey(User)

class EventType(NamedBase):
    def __unicode__(self):
        return self.name
    
class EventSubType(NamedBase):
    event_type = models.ForeignKey(EventType)
    
class Country(NamedBase):
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Countries & States"
    
class State(NamedBase):
    country = models.ForeignKey(Country)
    def __unicode__(self):
        return self.name
    
class City(NamedBase):
    state = models.ForeignKey(State)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Cities"
        
class Location(NamedBase):
    city = models.ForeignKey(City)
    def __unicode__(self):
        return u'%s, %s' % (self.name,self.city.name)
    
class SeatingOption(NamedBase):
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Seating Options" 

class VenueType(NamedBase):
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Venue Types" 
        
class CapacityRange(models.Model):
    minimum = models.IntegerField(default=0)
    maximum = models.IntegerField(null=True, blank=True)
    display_string = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.display_string
    class Meta:
        verbose_name_plural = "Capacity Ranges" 

# Lunch, Dinner etc

class Venue(NamedBase):
    manager = models.ForeignKey(User)
    location = models.ForeignKey(Location)
    description = models.CharField(default=None, max_length=128, blank=True,
                                    null=True)
    venue_type = models.ForeignKey(VenueType)
    capacity = models.IntegerField()
    minimum_occupancy = models.IntegerField(default=0)
    created_at = models.DateField()
    last_modified_at = models.DateField()
    rating = models.DecimalField(validators=[MinValueValidator(0),
                                       MaxValueValidator(5)], decimal_places=1, max_digits=2, default=3.0)
    is_pure_veg = models.BooleanField()
    serves_liquor = models.BooleanField()
    event_type = models.ManyToManyField(EventType)
    base_package_rate = models.DecimalField(MinValueValidator(0), decimal_places=2, max_digits=10, default=10000.00)
    address1 = models.CharField(default=None, max_length=255, blank=True, null=True)
    address2 = models.CharField(default=None, max_length=255, blank=True, null=True)
    address3 = models.CharField(default=None, max_length=255, blank=True, null=True)
    lead_text = models.TextField(default="LOREM IPSUM DOLOR SIT AMET, CONSECTETUER ADIPISCING ELIT. NAM CURSUS. MORBI UT MI. NULLAM ENIM LEO, EGESTAS ID, CONDIMENTUM AT, LAOREET MATTIS, MASSA. SED ELEIFEND NONUMMY DIAM. PRAESENT MAURIS ANTE,",null=False,blank=False)
    extra_content = models.TextField(default="<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur ipsum velit, porta a orci gravida, tempor placerat leo. Vestibulum eu mauris in erat pulvinar fermentum. Donec quis lacus eu risus congue fermentum. Curabitur scelerisque odio ac pretium placerat. Donec convallis dapibus nunc id sagittis. Donec ut scelerisque urna. Nullam egestas semper est, sed lacinia elit ullamcorper sit amet.</p><p>Suspendisse nec sagittis tortor, ac ullamcorper lorem. Aenean vitae augue et quam pretium accumsan. Donec elementum molestie nunc, sit amet molestie magna sagittis ut. Aenean odio risus, faucibus quis gravida laoreet, scelerisque eu arcu. Donec nisi dui, facilisis id dictum et, faucibus sit amet nisi. Fusce nec erat leo. Nulla facilisi.</p>",null=False,blank=False)
    lighting = models.TextField(null=False,blank=False,default="LED Lights")
    music = models.TextField(null=False,blank=False,default="Western Classical")
    service = models.TextField(null=False,blank=False,default="Bar, Buffet")
    cost_per_head = models.DecimalField(MinValueValidator(0), decimal_places=2, max_digits=10, default=2500.00)
    review_count = models.IntegerField(default=0)
    lattitude = models.DecimalField(max_digits=10,decimal_places=5,default=17.46994)
    longitude = models.DecimalField(max_digits=10,decimal_places=5,default=78.50757)
    def __unicode__(self):
        return self.name
    
class VenueRating(models.Model):
    venue = models.ForeignKey(Venue)
    user = models.ForeignKey(User)
    review = models.TextField(null=True,blank=True)
    rating = models.DecimalField(validators=[MinValueValidator(0),
                                       MaxValueValidator(5)], decimal_places=1, max_digits=2, default=3.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        ratings_count = self.venue.review_count
        ratings_count=ratings_count+1
        self.venue.review_count = ratings_count
        super(VenueRating,self).save()
        self.venue.save()


    def __unicode__(self):
        return u'%s' % (self.venue.name)
    
class CustomOption(NamedBase):
    venue = models.ForeignKey(Venue)

class VenueSupportsEventType(models.Model):
    venue = models.ForeignKey(Venue)
    event_type = models.ForeignKey(EventType)
    evnet_subtype_id = models.IntegerField(default=None, blank=True, null=True)
    
class VenuePicture(models.Model):
    venue = models.ForeignKey(Venue)
    image = models.ImageField(upload_to='venue_images')
    displayable = models.BooleanField()
    is_display_pic = models.BooleanField()
    def __unicode__(self):
        return u'%s' % (self.venue.name)
    
    def getPictureForVenue(self, venue):
        return self.objects.get(venue=venue)

    def save(self, size=(500, 500)):
        if not self.id and not self.image:
            return

        super(VenuePicture, self).save()

        pw = self.image.width
        ph = self.image.height
        nw = size[0]
        nh = size[1]

        # only do this if the image needs resizing
        if pw != ph and ((pw, ph) != (nw, nh)):
            filename = str(self.image.path)
            image = Image.open(filename)
            pr = float(pw) / float(ph)
            nr = float(nw) / float(nh)

            if pr > nr:
                # photo aspect is wider than destination ratio
                tw = int(round(nh * pr))
                image = image.resize((tw, nh), Image.ANTIALIAS)
                l = int(round(( tw - nw ) / 2.0))
                image = image.crop((l, 0, l + nw, nh))
            elif pr < nr:
                # photo aspect is taller than destination ratio
                th = int(round(nw / pr))
                image = image.resize((nw, th), Image.ANTIALIAS)
                t = int(round(( th - nh ) / 2.0))
                print((0, t, nw, t + nh))
                image = image.crop((0, t, nw, t + nh))
            else:
                # photo aspect matches the destination ratio
                image = image.resize(size, Image.ANTIALIAS)

            image.save(filename)


class BookingTimeType(models.Model):
    name = models.CharField(null=True, blank=True,default="", max_length=255)
    def __unicode__(self):
        return u'%s'%(self.name)

class VenueBookingHistory(models.Model):
    venue = models.ForeignKey(Venue)
    date = models.DateField()
    booking_time = models.ForeignKey(BookingTimeType)
    def __unicode__(self):
        return u'%s' % (self.venue.name)


class MealType(models.Model):
    name = models.CharField(null=True,blank=True,default="",max_length=255)

    def __unicode__(self):
        return u'%s' % (self.name)
    class Meta:
        verbose_name_plural = "Meal Types"

class MealCategory(models.Model):
    name = models.CharField(null=True,blank=True,default="",max_length=255)
    how_to = models.TextField(null=True,blank=True, default="")

    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        verbose_name_plural = "Meal Categories"

class MealItem(models.Model):
    name = models.CharField(null=True,blank=True,default="",max_length=255)

    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        verbose_name_plural = "Items in a Meal"

class MealCategoryItem(models.Model):
    meal_category = models.ForeignKey(MealCategory)
    meal_item = models.ForeignKey(MealItem)
    def __unicode__(self):
        return u'%s : %s' % (self.meal_category.name,self.meal_item.name)
    class Meta:
        verbose_name_plural = "Items in a Meal Category"

class MealOption(models.Model):
    name = models.CharField(null=True,blank=True,default="",max_length=255)
    def __unicode__(self):
        return u'%s' %(self.name)
    class Meta:
        verbose_name_plural = "Options for a Meal Item"

class MealCategoryItemOption(models.Model):
    meal_category_item = models.ForeignKey(MealCategoryItem)
    meal_option = models.ForeignKey(MealOption)
    def __unicode__(self):
        return u'%s : %s : %s' %(self.meal_category_item.meal_category.name,self.meal_category_item.meal_item.name,self.meal_option.name)
    class Meta:
        verbose_name_plural = "Meal Category Item Option Mapping"

class Package(models.Model):
    name=models.CharField("name of the package",blank=True,null=True,max_length=255,default=None)
    custom = models.BooleanField("Is it a custom package",blank=False,null=False,default=True)
    meal_type = models.ForeignKey(MealType)
    def __unicode__(self):
        return u'%s' % self.name
    class Meta:
        verbose_name_plural = "Packages"

class PackageDescription(models.Model):
    package = models.ForeignKey(Package)
    description = models.TextField(verbose_name="Package Description",blank=False,null=False,default="No Description")
    display_order = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = "Package Descriptions"

class Quote(models.Model):
    CHOICES_FOR_STATUS = (
        ("0","Quote In Progress"),
        ("1","Quote Requested"),
        ("2","Responded"),
        ("3","Accepted"),
    )
    user=models.ForeignKey(User)
    package = models.ForeignKey(Package,null=True)
    quote_key = models.CharField(max_length=255,default="",null=True,blank=True)
    guests = models.ForeignKey(CapacityRange,default=1,null=True,blank=True)
    venuetype = models.ForeignKey(VenueType,default=1,null=True,blank=True)
    occasion = models.ForeignKey(EventType,default=1,null=True,blank=True)
    time = models.ForeignKey(BookingTimeType)
    date_of_booking = models.DateTimeField()
    status = models.CharField(max_length=255,choices=CHOICES_FOR_STATUS,default="0")
    def __unicode__(self):
        return u'%s' % (self.user)
    

class QuoteVenue(models.Model):
    quote = models.ForeignKey(Quote)
    venue = models.ForeignKey(Venue)
    def __unicode__(self):
        return u'%s' % (self.venue.name)

class PackageContents(models.Model):
    package = models.ForeignKey(Package,null=True)
    contents = models.ForeignKey(MealCategoryItemOption)
     

class Contact(models.Model):
    name=models.CharField(null=False,blank=False,max_length=255)
    email=models.EmailField(null=False,blank=False,max_length=255)
    mobile=models.BigIntegerField(null=True,blank=True,max_length=10)
    company=models.CharField(null=True,blank=True,max_length=255)


class SuggestVenue(models.Model):
    name=models.CharField(null=False,blank=False,max_length=255)
    email=models.EmailField(null=False,blank=False,max_length=255)
    venue=models.CharField(null=True,blank=True,max_length=255)
    location=models.CharField(null=True,blank=True,max_length=255)



class Favourite(models.Model):
    user = models.ForeignKey(User)
    venue=models.ForeignKey(Venue)


class RelatedVenues(models.Model):
    venue = models.ForeignKey(Venue)
    related_venue = models.ForeignKey(Venue,related_name='related_venue')
    def __unicode__(self):
        return u'%s:%s' % (self.venue.name,self.related_venue.name)
    
class RecentlyViewed(models.Model):
    user=models.ForeignKey(User)
    venue=models.ForeignKey(Venue)