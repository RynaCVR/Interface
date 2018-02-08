# coding=utf-8


import time

import pymysql
from sshtunnel import SSHTunnelForwarder


def con_db(db_name=None):
    """连接数据库"""
    if db_name is None:
        return None, None

    if db_name != 'jjb' and db_name != 'dgd':
        return None, None

    server = SSHTunnelForwarder(
        ("115.28.80.76", 22),
        ssh_username="root",
        ssh_password="34SIzAy$Spg@Ea45",
        remote_bind_address=('localhost', 3306)
    )
    server.start()

    client = pymysql.connect(
        host="localhost",
        port=server.local_bind_port,
        user="root",
        passwd="julanling",
        # db=(lambda db_name: 'julanling_jjb' if db_name == 'jjb' else 'julanling_dgd')(db_name),
        db='julanling_jjb' if db_name == 'jjb' else 'julanling_dgd',
        charset="utf8"
    )
    return server, client


def discon_db(server, client):
    """断开数据库"""
    if client is not None:
        client.close()

    if server is not None:
        server.stop()


def select_sms(db_name):
    """查询验证码"""

    if db_name == 'jjb':
        sql = """SELECT mobile, code, create_time FROM user_sms_verify_log ORDER BY id DESC LIMIT 10;"""
    elif db_name == 'dgd':
        sql = """SELECT mobile, code, create_time, order_id FROM user_sms_verify_log ORDER BY id DESC LIMIT 10;"""
    else:
        return
    try:
        server, client = con_db(db_name)
    except:
        return
    try:
        cursor = client.cursor()
        cursor.execute(sql)
        client.commit()
        result = list(cursor.fetchall())

        for i in range(len(result)):
            result[i] = list(result[i])
            result[i][2] = str(result[i][2])

            if db_name == 'dgd':
                result[i][3] = str(result[i][3])
        return result
    except:
        return
    finally:
        discon_db(server, client)


if __name__ == '__main__':
    select_sms('dgd')
