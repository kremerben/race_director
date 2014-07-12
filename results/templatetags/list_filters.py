import os
from django import template
from random import shuffle
import datetime
from results.models import Biathlete

register = template.Library()



@register.filter
def ageclass(age, gender):
    if gender == 'M':
        if int(age) < Biathlete.BOY10:
            return Biathlete.age_class['BOY10']
        elif int(age) < Biathlete.BOY12:
            return Biathlete.age_class['BOY12']
        elif int(age) < Biathlete.BOY14:
            return Biathlete.age_class['BOY14']
        elif int(age) < Biathlete.BOY16:
            return Biathlete.age_class['BOY16']
        elif int(age) < Biathlete.YM:
            return Biathlete.age_class['YM']
        elif int(age) < Biathlete.JM:
            return Biathlete.age_class['JM']
        elif int(age) < Biathlete.SM:
            return Biathlete.age_class['SM']
        elif int(age) < Biathlete.MM:
            return Biathlete.age_class['MM']
        elif int(age) < Biathlete.SMM:
            return Biathlete.age_class['SMM']
    elif gender == 'W':
        if int(age) < Biathlete.GIRL10:
            return Biathlete.age_class['GIRL10']
        elif int(age) < Biathlete.GIRL12:
            return Biathlete.age_class['GIRL12']
        elif int(age) < Biathlete.GIRL14:
            return Biathlete.age_class['GIRL14']
        elif int(age) < Biathlete.GIRL16:
            return Biathlete.age_class['GIRL16']
        elif int(age) < Biathlete.YW:
            return Biathlete.age_class['YW']
        elif int(age) < Biathlete.JW:
            return Biathlete.age_class['JW']
        elif int(age) < Biathlete.SW:
            return Biathlete.age_class['SW']
        elif int(age) < Biathlete.MW:
            return Biathlete.age_class['MW']
        elif int(age) < Biathlete.SMW:
            return Biathlete.age_class['SMW']
    else:
        return ""


@register.filter
def filename_only(value):
    return os.path.basename(value.file.name)


@register.filter
def related_images(list, project):
    return [item for item in list if item.project == project]




# @register.filter
# def first(list):
#     if list is not None and len(list):
#         return list[0]
#
#
# @register.filter
# def suit(list, suit_type):
#     return [item for item in list if item.get_suit_display() == suit_type]
#
#
# @register.filter
# def rank(list, rank):
#     return [item for item in list if item.rank == rank]
#
#
# @register.filter
# def random(cards):
#     newlist = list(cards)
#     shuffle(newlist)
#     return newlist
#
# @register.filter
# def random2(list):
#     newlist = list[:]
#     shuffle(newlist)
#     return newlist
#
#
# @register.filter
# def dealsrandom(list, amount):
#     newlist = list[:]
#     shuffle(newlist)
#     return newlist[:amount]
#
# @register.filter
# def deals(list, amount):
#     return list[:amount]
#
