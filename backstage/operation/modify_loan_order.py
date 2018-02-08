# coding=utf-8


import time

import pymysql
from sshtunnel import SSHTunnelForwarder


def con_db():
    """连接数据库"""
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
        db="julanling_dgd",
        charset="utf8"
    )
    return server, client


def discon_db(server, client):
    """断开数据库"""
    client.close()
    server.stop()


def modify_status(order_num="", status=""):
    """修改订单状态"""
    if order_num == "" or status == "":
        return
    server, client = con_db()
    try:
        cursor = client.cursor()
        sql_str = """UPDATE loan_order SET STATUS="{0}" WHERE order_num="{1}";""".format(status, order_num)
        cursor.execute(sql_str)
        client.commit()
    except:
        return
    finally:
        discon_db(server, client)


def modify_order_due_day(order_num="", days=""):
    """修改订单为逾期订单"""
    if order_num == "" or days == "":       # 过滤空格和特殊字符
        return
    server, client = con_db()
    try:
        cursor = client.cursor()
        sql_loan_days = """SELECT loan_days FROM loan_order WHERE order_num="{0}";""".format(order_num)
        cursor.execute(sql_loan_days)
        client.commit()
        loan_days = cursor.fetchall()[0][0]     # int

        now = int(str(time.time()).split(".")[0])
        due_date = now - int(days)*24*60*60
        release_time = due_date - loan_days*24*60*60
        due_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(due_date))
        release_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(release_time))
        sql_modify = """
        UPDATE loan_order 
        SET STATUS="145", create_time="{0}", release_time="{1}", due_date="{2}" 
        WHERE order_num="{3}";""".format(
            release_time, release_time, due_date, order_num
        )
        cursor.execute(sql_modify)
        client.commit()
    except:
        return
    finally:
        discon_db(server, client)


if __name__ == "__main__":
    # modify_status("44DQFA201608170936", "151")
    modify_order_due_day(order_num="4AF9NC20171221185224", days="0")

