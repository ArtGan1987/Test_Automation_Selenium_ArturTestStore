import random
import string
import logging as logger



def generate_random_email_and_password(domain=None, email_prefix=None):

    if not domain:
        domain = 'artur.pl'

    if not email_prefix:
        email_prefix = 'testuser'

    random_email_string_lenght = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_lenght))

    email = email_prefix + '_' + random_string + '@' + domain

    logger.info(f"Generated random email: {email}")

    rand_password_lenght = 20
    rand_password = ''.join(random.choices(string.ascii_letters, k=random_email_string_lenght))

    random_info = {'email': email, 'password': rand_password}

    return random_info
