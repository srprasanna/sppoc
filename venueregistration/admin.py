from django.contrib import admin
from venueregistration.models import (
    EventType, EventSubType, Country, State, City, Location, VenueType,
    SeatingOption, MealType, CapacityRange, MealCategory,MealItem,MealCategoryItem,Venue,VenuePicture,VenueRating,VenueBookingHistory,QuoteVenue,Quote,Package,RelatedVenues,MealOption,MealCategoryItemOption,PackageDescription,BookingTimeType
)

class EventSubTypeInline(admin.StackedInline):    
    model = EventSubType
    extra = 3
    
class EventTypeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']})
    ]
    inlines = [EventSubTypeInline]

admin.site.register(EventType, EventTypeAdmin)

class StateInline(admin.StackedInline):    
    model = State
    extra = 3
    
class CountryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']})
    ]
    inlines = [StateInline]

admin.site.register(Country, CountryAdmin)

class LocationInline(admin.StackedInline):    
    model = Location
    extra = 3
    
class CityAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ('name', 'state')})
    ]
    inlines = [LocationInline]


class PackageDescriptionInline(admin.StackedInline):
    model=PackageDescription


class PackageAdmin(admin.ModelAdmin):
    inlines=[PackageDescriptionInline]
    def queryset(self, request):
        qs = admin.ModelAdmin.queryset(self, request)
        return qs.filter(custom=False)


class VenuePictureInline(admin.StackedInline):
    model=VenuePicture




class VenueAdmin(admin.ModelAdmin):
    inlines=[VenuePictureInline]


class RelatedVenueAdmin(admin.ModelAdmin):
    pass



admin.site.register(Package,PackageAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Venue,VenueAdmin)
admin.site.register(VenueType)
admin.site.register(SeatingOption)
admin.site.register(CapacityRange)
admin.site.register(MealType)
admin.site.register(MealCategory)
admin.site.register(MealItem)
admin.site.register(MealCategoryItem)
admin.site.register(MealOption)
admin.site.register(MealCategoryItemOption)
admin.site.register(RelatedVenues)
admin.site.register(BookingTimeType)