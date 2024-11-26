# views.py

from banjo.urls import route_get, route_post
from settings import BASE_URL
from .models import Palette

@route_get(BASE_URL + 'all')
def all_palette(args):
    palette_list = []

    if len(Palette.objects.all())  > 0:

        for palette in Palette.objects.all():
            palette_list.append(palette.json_response())

        return {'palette':palette_list}
    
    else:
        return {'error': 'no palette exist'}


 

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

    else:
        return {'error': 'no palette exist'}

@route_post(BASE_URL + 'edit', args={'id':int,'hex1':str,'hex2':str,'hex3':str,'hex4':str})
def change_palette(args):
    if Palette.objects.filter(id=args['id']).exists():
        palette_change = Palette.objects.get(id=args['id'])
        palette_change.change_palette(args['hex1'], args['hex2'], args['hex3'], args['hex4'])

        return {'edit': palette_change.json_response()}

    else:
        return {'error': 'no palette exist'}


@route_get(BASE_URL + 'search', args={'keyword':str})
def search_palette(args):
    palette_list = []

    if Palette.objects.filter(keyword=args['keyword']).exists():
        Palette.objects.filter(keyword__contains='keyword')
        return {'Palette': palette_list}
    else:
        return {'error': 'no palette exist'}