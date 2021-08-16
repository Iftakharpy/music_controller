from api.models import Room

def is_room_code_unique(code):
  return Room.objects.filter(code=code).count()==0