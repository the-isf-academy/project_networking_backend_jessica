# views.py

from banjo.urls import route_get, route_post
from settings import BASE_URL
from .models import Palette

@route_get(BASE_URL + 'all')
def all_palette(args):
    palette_list = []

    for palette in Palette.objects.all():
        palette_list.append(palette.json_response())

    return {'palette':palette_list}

 

@route_post(BASE_URL + 'new', args={'hex1':str,'hex2':str,'hex3':str,'hex4':str})
def new_palette(args):

    new_palette = Palette(
        hex1 = args['hex1'],
        hex2 = args['hex2'],
        hex3 = args['hex3'],
        hex4 = args['hex4'],
    )  

    new_palette.save()

    return {'palette': new_palette.json_response()}

@route_post(BASE_URL + 'likes', args={'id':int})
def palette_likes(args):
    if Palette.objects.filter(id=args['id']).exists():
        palette_likes = Palette.objects.get(id=args['id'])
        palette_likes.increase_likes()

    return {'likes': palette_likes.json_response()}