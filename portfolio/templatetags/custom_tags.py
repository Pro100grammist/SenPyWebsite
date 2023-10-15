from django import template

register = template.Library()


@register.filter(name='generate_stars')
def generate_stars(rating):
    stars = '*' * int(rating)
    return stars
