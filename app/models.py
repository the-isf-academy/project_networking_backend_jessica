# models.py

from banjo.models import Model, StringField, IntegerField, FloatField, BooleanField

class Palette(Model):
    hex1 = IntegerField()
    hex2 = IntegerField()
    hex3 = IntegerField()
    hex4 = IntegerField()
#    tone = StringField()
#    likes = IntegerField()
#    archive = BooleanField()

    def json_response(self):
        
        return {
            'id': self.id,
            'hex1': self.hex1,
            'hex2': self.hex2,
            'hex3': self.hex3,
            'hex4': self.hex4,
            #'likes': self.likes,
            #'tone': self.tone
        }
