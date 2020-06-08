import secrets
import random
import os
from ihu import app
from flask_login import current_user

def unique_id():
    token = secrets.token_hex(16)[:7]
    new_token = ' '.join(token).split(' ')
    main_id = ''.join(random.sample(new_token, len(new_token)-1))
    return (main_id)



from ihu.models import User
