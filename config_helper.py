import os

def get_base_url():

    env = os.environ.get('ENV', 'test')

    if env.lower() == 'test':
        return 'http://arturteststore.local'
    elif env.lower() == 'prod':
        return 'http://arturteststore.prod.local'
    else:
        raise Exception(f"Unknown environment: {env}")

def database_credentials():

    env = os.environ.get('ENV', 'test')

    db_user = os.environ.get("DB_USER")
    db_password = os.environ.get("DB_PASSWORD")
    if not db_user or db_password:
        raise Exception("Environment variables must be set")

    if env == 'test':
        db_host = '127.0.0.1'
        db_port = 10006
    elif env == 'prod':
        db_host = 'ArturTestStore.com'
        db_port = 1111
    else:
        raise Exception('Unknown environment')

    db_info = {"db_host": db_host, "db_port": db_port,
               "db_host": db_host, "db_port": db_port}

    return db_info


