from django.contrib import admin

from models import *

admin.site.register(User)

class ClubAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Name', {
            'fields': ('name', 'region', 'location', 'website')
        }),
        ('Contact', {
            # 'classes': ('collapse',),
            'fields': ('contact_name', 'contact_email', 'contact_phone')
        }),
    )
    list_display = ('name', 'location', 'region', 'contact_name')
    list_filter = ('region',)


class RaceAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Name', {
            'fields': ('name', 'race_series', 'date', 'start_time', 'location', 'fee', 'description', 'website')
        }),
        ('Contact', {
            # 'classes': ('collapse',),
            'fields': ('contact_name', 'contact_email', 'contact_phone')
        }),
        ('Files', {
            # 'classes': ('collapse',),
            'fields': ('info_document', 'result_document')
        }),

    )
    list_display = ('name', 'date', 'race_series', 'start_time', 'location', 'fee', 'contact_name')
    list_filter = ('date', 'start_time', 'location', 'fee', 'contact_name', 'race_series')


class RacerAdmin(admin.ModelAdmin):
    # def age(self, obj):
    #     return self.age(obj)
    #
    # age.short_description = 'age age'
    # age.admin_order_field = 'ageage'

    fieldsets = (
        ('Name', {
            'fields': ('name', 'birthdate', 'gender', 'hometown', 'club')
        }),
        ('User Link', {
            'fields': ('user',)
        }),
    )
    list_display = ('name', 'user', 'birthdate', 'gender', 'hometown', 'club')
    list_filter = ('birthdate', 'club', 'gender')



class ResultAdmin(admin.ModelAdmin):
    # def finish_time_format(self, obj):
    #     return obj.finish_time.strptime("%H:%M:%S")

    # finish_time_format.short_description = 'Finish Time'
    # finish_time_format.admin_order_field = 'finish_time'

    def racer_gender(self, obj):
        return obj.racer.gender

    racer_gender.short_description = 'Gender'
    racer_gender.admin_order_field = 'gender'

    fieldsets = (
        ('Name', {
            'fields': ('race', 'place', 'racer', 'finish_time')
        }),
        ('Shooting', {
            'fields': ('first_shoot', 'second_shoot', 'third_shoot', 'fourth_shoot')
        }),
    )
    list_display = ('place', 'racer', 'racer_gender', 'finish_time', 'race')
    list_filter = ('race', 'place', 'racer')
    ordering = ('place', 'finish_time')


admin.site.register(RaceSeries)
admin.site.register(Club, ClubAdmin)
admin.site.register(Race, RaceAdmin)
admin.site.register(Racer, RacerAdmin)
admin.site.register(Result, ResultAdmin)

#
#
# class ClubAdmin(admin.ModelAdmin):
#     fieldsets = (
#         ('Name', {
#             'fields': ('name','overall_winner')
#         }),
#         ('Advanced options', {
#             'classes': ('collapse',),
#             'fields': ('date', 'location')
#         }),
#     )
#     list_display = ('name', 'overall_winner', 'date', 'location')
#     list_filter = ('name', 'overall_winner', 'date')
#
# admin.site.register(FIFATournament, TournamentAdmin)
