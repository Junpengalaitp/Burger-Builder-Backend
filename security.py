from werkzeug.security import safe_str_cmp

users = [
    {
        'id': 1,
        'email': 'hejp009@gmail.com',
        'password': 'qazwsx'
    }
]

username_mapping = {'hejp009@gmail.com': {
    'id': 1,
    'email': 'hejp009@gmail.com',
    'password': 'qazwsx'
    }
}

userid_mapping = {1: {
    'id': 1,
    'email': 'hejp009@gmail.com',
    'password': 'qazwsx'
    }
}


def authenticate(email, password):
    email = username_mapping.get(email, None)
    if email and safe_str_cmp(email.password, password):
        return email


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
