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
 

@route_post(BASE_URL + 'new', args={'hex1':int,'hex2':int,'hex3':int,'hex4':int})
def new_palette(args):
    new_palette = Palette(
        hex1 = args['hex1'],
        hex2 = args['hex2'],
        hex3 = args['hex3'],
        hex4 = args['hex4'],
        #is_happy = args['is_happy'],
        #likes = 0,
        #archive = False
    )

    new_palette.save()

    return {'palette': new_palette.json_response()}