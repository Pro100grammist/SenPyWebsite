import re
from django import template

register = template.Library()


@register.filter(name='generate_stars')
def generate_stars(rating_string):
    rating = int(rating_string.split()[0])
    stars = '★' * rating
    return stars


@register.filter(name='show_score')
def generate_stars(rating_string):
    score = rating_string.split()[1]
    return score
