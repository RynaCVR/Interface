# coding: utf-8

import enum
import time
import hashlib
import re


def get_current_time():
    """取小数点前位"""
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

    if type == "jjb":
        common_header_dev.update(_jjb_dev)
    elif type == "dgd":
        common_header_dev.update(_dgd_dev)

    return common_header_dev

