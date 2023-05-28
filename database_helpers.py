import pymysql
from ArturTestStore.src.helpers.config_helper import database_credentials


def read_from_db(sql):
    # db_creds = database_credentials()
    # connect to database
    connection = pymysql.connect(host='127.0.0.1', port=10006,
                                 user='root', password='root')
    # connection = pymysql.connect(host=db_creds["db_host"], port=db_creds["db_port"],
    #                              user=db_creds["db_user"], password=db_creds["db_password"])
    try:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        db_data = cursor.fetchall()
        cursor.close()
    finally:
        connection.close()

    # return the result
    return db_data


def get_order_from_db_by_order_no(order_no):
    sql = f"SELECT * FROM local.wp_posts WHERE ID = {order_no} AND post_type = 'shop_order'"

    db_order = read_from_db(sql)
    return db_order
