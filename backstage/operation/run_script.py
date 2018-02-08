
import requests
from backstage.operation.common import common_lib


def auto_payment():
    """连连自动打款"""
    header = common_lib.get_common_header(type='dgd')
    url = "http://dgdapi.dev.julanling.com/AutoSetting/AutoPayment"
    header = common_lib.get_secret_header(url, header, {})
    respone = requests.get(url, headers=header)
    return respone.json()


def auto_delay_back_loan():
    """逾期催回报表数据刷新"""
    header = common_lib.get_common_header(type='dgd')
    url = 'http://dgdapi.dev.julanling.com/task/DailyDelayBackLoanDay'
    header = common_lib.get_secret_header(url, header, {})
    respone = requests.get(url, headers=header)
    return respone.json()


def sys_push():
    """打工圈消息推送"""
    url = 'http://xserver.dev.julanling.com:8080/msg/send_msg'
    respone = requests.get(url)
    return respone.json()


if __name__ == "__main__":
    auto_payment()


