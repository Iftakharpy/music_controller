import string
import random

from .validator_unique_room_code import is_room_code_unique


def get_unique_code(unique_code_validator_fn=is_room_code_unique, length=8):
  chars = string.ascii_letters+string.digits
  
  # keep validating code until a unique code is found
  while True:
    random_code = ''.join(random.choices(chars, k=length))
    if unique_code_validator_fn(random_code)==True:
      return random_code
