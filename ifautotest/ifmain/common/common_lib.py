# coding: utf-8

import enum
import time
import hashlib
import re
import copy
from ifautotest.ifmain.common import config


def get_current_time():
    """取小数点前10位"""
    current_time = str(time.time()).split(".")[0]
    return current_time  # 当前时间


def md5(string):
    """对字符串MD5加密"""
    md5 = hashlib.md5()
    md5.update(string.encode())
    return md5.hexdigest()


def get_secret_header(url, common_header, params):
    """得到加密后的信息头"""

    if isinstance(common_header.get("Signature", False), str):
        common_header.pop("Signature")
    array = []
    common_keys = common_header.keys()
    param_keys = params.keys()
    device_type = common_header["Devicetype"]
    pattern = "^http.*?://(.*?)(/*[?#].*$|[?#].*$|/*$)"
    link = re.match(pattern, url).group(1)

    link_type = link[0:3]

    if link_type == "jjb":
        SecretCode = JJBSecretCode
    else:
        SecretCode = DGQSecretCode

    secret = None
    if device_type is DeviceType.ANDROID.value:
        secret = SecretCode.ANDROID.value
    elif device_type is DeviceType.IOS.value:
        secret = SecretCode.IOS.value

    for _key in common_keys:
        array.append("{0}={1}".format(_key, common_header[_key]))       # 把头拼接到列表

    for _key in param_keys:
        array.append("{0}={1}".format(_key, params[_key]))      # 把用户参数拼接到列表

    array.append("link={0}".format(link))      # 把URL拼接到列表
    array.append("secret={0}".format(secret))       # 把密钥拼接到列表

    array.sort()        # 排序
    secret_string = "".join(array)      # 列表中字符串拼接

    sig = md5(secret_string)        # MD5加密
    common_header["Signature"] = sig        # 把加密字符串添加到头部

    return common_header


class JJBSecretCode(enum.Enum):
    """记加班秘钥"""
    IOS = "apitesdkfowpqfujro"
    ANDROID = "apitesfopq0fiejdkf"
    BROWSER = "apitesfkoelposyufg"
    PC = "apitesfiow9dioeksm"
    WINDOWS_PHONE = "apitesaospdlekfuhr"
    USER_RANDCODE = "z5895465fkioiwtofgtyjcikmt"
    PASSWORD_RANDCODE = "z289fidjifkoiq5oidftoiujm"


class DGQSecretCode(enum.Enum):
    """记加班秘钥"""
    IOS = "apitesgkyjeiirpjlp"
    ANDROID = "apitesol3k9fyoditc"
    BROWSER = "apitesxjakkswjsknf"
    PC = "apitesj3j9o9pksfrd"
    WINDOWS_PHONE = "apiteslxelpo2ij9wi"
    USER_RANDCODE = "f9091987oeoiwkdsalfajfkks"
    PASSWORD_RANDCODE = "f9987078ioeoideawdfdmkasv"


class DeviceType(enum.Enum):
    """设备类型 1：浏览器设备 2：pc设备 3：Android设备 4：ios设备 5：windows phone设备"""
    BROWSER = "1"
    PC = "2"
    ANDROID = "3"
    IOS = "4"
    WINDOWS_PHONE = "5"


def test_re():
    pattern = "^http.*?://(.*?)(/*[?#].*$|[?#].*$|/*$)"
    link = "http://jjbapi.dev.julanling.com/user/mobile_reg?"
    result = re.match(pattern, link)
    print(result.group(1))


def get_common_header(type="jjb"):
    """获取头信息"""
    common_header_dev = {
        "Clientinfo": "julanling_dgq",
        "Clientversion": "1.2",
        "Isdebug": "0",
        "Devicetype": DeviceType.ANDROID.value,  # 设备类型 1：浏览器设备 2：pc设备 3：Android设备 4：ios设备 5：windows phone设备
        "Devicetoken": "aaa",  # 来自客户端
        "Requesttime": get_current_time(),
    }
    common_header_pre = {
        "Clientinfo": "julanling_dgq",
        "Clientversion": "1.2",
        "Isdebug": "0",
        "Devicetype": DeviceType.ANDROID.value,  # 设备类型 1：浏览器设备 2：pc设备 3：Android设备 4：ios设备 5：windows phone设备
        "Devicetoken": "aaa",  # 来自客户端
        "Requesttime": get_current_time(),
    }
    common_header_res = common_header_pre

    _jjb_dev = {
        "Userid": "106088551",
        "Logintime": "1514954608",
        "Checkcode": "3011457d405c1d2a9bd076d4ccd4e12d"
    }
    _dgd_dev = {
        "Userid": "100640302",
        "Logintime": "1514955185",
        "Checkcode": "4c359373b7cf72d8016e93ec1720cd4b"
    }
    _dgq_dev = {
        "Userid": "500001411",
        "Logintime": "1517192567",
        "Checkcode": "89284a215b011d5fb00d3d4f84d08424"
    }

    _jjb_pre = {
        "Userid": "112997230",
        "Logintime": "1514955797",
        "Checkcode": "02740062e47e3d004fc29ae2840cce12"
    }
    _dgd_pre = {
        "Userid": "103950903",
        "Logintime": "1514957439",
        "Checkcode": "7d8252b7e1539880bf9484975711e669"
    }
    _dgq_pre = {
        "Userid": "603045441",
        "Logintime": "1517192660",
        "Checkcode": "907b340ef0cb9d069208d4891129406c"
    }

    _jjb_res = _jjb_pre
    _dgd_res = _dgd_pre
    _dgq_res = _dgq_pre

    if config.Environment == "PRE":
        common_header = common_header_pre
        _jjb = _jjb_pre
        _dgd = _dgd_pre
        _dgq = _dgq_pre
    elif config.Environment == "RES":
        common_header = common_header_res
        _jjb = _jjb_res
        _dgd = _dgd_res
        _dgq = _dgq_res
    else:
        common_header = common_header_dev
        _jjb = _jjb_dev
        _dgd = _dgd_dev
        _dgq = _dgq_dev

    if type == "jjb":
        common_header.update(_jjb)
    elif type == "dgd":
        common_header.update(_dgd)
    else:
        common_header.update(_dgq)

    return common_header


def get_default_user():
    """用户默认数据"""
    user_dev = {
        "jjb_id": "106088551",
        "jjb_uid": "466K48",
        "dgq_uid": "500001411",
        "dgd_uid": "100640302",
        "cid": "074d8f44274818d84263206364ca5e8d"
    }
    user_pre = {
        "jjb_id": "112997230",
        "jjb_uid": "4CRDUF",
        "dgq_uid": "603045441",
        "dgd_uid": "103950903",
        "cid": "1cc98fa9f77759770b08d456e00ec6c7"
    }
    user_res = user_pre

    if config.Environment == "PRE":
        result = user_pre
    elif config.Environment == "RES":
        result = user_res
    else:
        result = user_dev
    return result


def is_afternoon():
    """判断是否为下午"""
    result = False
    now = time.strftime("%H%M%S", time.localtime(time.time()))
    if 180000 <= int(now) <= 183000:
        result = True
    return result


def is_morning():
    """判断是否为上午"""
    result = False
    now = time.strftime("%H%M%S", time.localtime(time.time()))
    if 90000 <= int(now) <= 93000:
        result = True
    return result


def get_random_device_token():
    """得到随机设备号"""
    return "14e1b600b1fd579f47433b" + get_current_time()


if __name__ == "__main__":
    print(md5("1060885511514954608"))
