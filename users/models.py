from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.validators import validate_comma_separated_integer_list
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

ROOM_TYPES = (
    ('Living Room','LIVING ROOM'),
    ('Kitchen', 'KITCHEN'),
    ('Bed Room','BEDROOM'),
    ('Bath Room','BATHROOM'),
    ('Other','OTHER'),
)

class Room(models.Model):
    title = models.CharField(max_length=100)
    room_type = models.CharField(max_length=50, choices=ROOM_TYPES)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

default_reading =  "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"


# user_rooms = []
# for room in Room.objects.get(owner=User):
#     user_rooms.append((room.title,room))
#
# user_rooms = tuple(user_rooms)



class Device(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    device_room = models.ForeignKey(Room, on_delete=models.CASCADE)
    device_status = models.BooleanField(default=False)
    device_reading = models.CharField(max_length=1000, default=default_reading, validators=[validate_comma_separated_integer_list])



    def __str__(self):
        return self.title
