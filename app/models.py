# models.py

from banjo.models import Model, StringField, IntegerField, FloatField, BooleanField

class Palette(Model):
    hex1 = StringField()
    hex2 = StringField()
    hex3 = StringField()
    hex4 = StringField()
#    tone = StringField()
    likes = IntegerField()
    keyword = StringField()
#    archive = BooleanField()

    def json_response(self):
        
        return {
            'id': self.id,
            'hex1': self.hex1,
            'hex2': self.hex2,
            'hex3': self.hex3,
            'hex4': self.hex4,
            'likes': self.likes,
            #'tone': self.tone
        }

    def increase_likes(self):
        self.likes =+ 1
        self.save()

    def change_palette(self,hex1,hex2,hex3,hex4):
        self.hex1 = hex1
        self.hex2 = hex2
        self.hex3 = hex3
        self.hex4 = hex4
        self.likes = 0
        self.save
        