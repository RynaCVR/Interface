# coding: utf-8
"""记加班"""

from ifautotest.ifmain.common import common_lib


class UserMobileIsExists:
    """判断手机号是否已经注册"""
    route = "user/mobile_is_exists"
    params = {
        "mobile": "18134413794"
    }


class MobileRegister:
    """手机号注册"""
    route = "user/mobile_reg"
    params = {
        "uid": "106089408",     # 来自临时账号接口
        "mobile": None,        # 来自用户输入
        "password": "e10adc3949ba59abbe56e057f20f883e",     # MD5(123456) 来自用户输入
        "smscode": "1234",      # 来自短信验证接口
        "channel": "0",     # 渠道名字
    }


class QQRegister:
    """QQ注册"""
    route = "user/qq_reg"
    params = {
        "uid": "106089408",     # 来自临时账号接口
        "qq_openid": "360570F12B582E902EEDE945D0AD3EFF",        # 来自用户输入
        "password": "e10adc3949ba59abbe56e057f20f883e",     # MD5(123456) 来自用户输入
        "smscode": "1234",      # 来自短信验证接口
        "channel": "0",     # 渠道名字
    }


class Guest:
    """临时账号"""
    route = "user/guest"
    params = {}


class SendSms:
    """发送短信验证码"""
    route = "user_sms_verify_log/sendsms"
    params = {
        "mobile": None,
        "type": None,       # 1: 注册 2：找回密码 3：其他
        "count": "1",
    }


class VerifySmsCode:
    """核对验证码是否正确"""
    route = "user_sms_verify_log/verify_smscode"
    params = {}


class MobileLogin:
    """登录接口"""
    route = "user/mobile_login"
    params = {
        "mobile": "18134413794",
        "password": "e10adc3949ba59abbe56e057f20f883e"
    }


class QQLogin:
    route = "user/qq_login"
    params = {
        "qq_openid": "360570F12B582E902EEDE945D0AD3EFF"
    }


class OpenDays:
    route = "user/open_days"
    params = {
        "current_ver": "5.4.94",
        "lat": "31.289700",
        "lng": "121.314558"
    }


class BackupDatas:
    """日历数据修改上传"""
    route = "user/backup_data_v3"
    params = {
        "jjb": """{"ot_detail":[{"backup":0,"base_salary":1745,"hour_salary":0,"id":2704,}],"workday_setting":[],"month_salary_summary":[],"month_salary_custom":[],"month_salary_user_item":[],"salary_setting_list":[]}"""
    }


class PullDatas:
    """日历数据下拉"""
    route = "user/pull_data_v3"
    params = {
        "current_jid": common_lib.get_default_user()["jjb_uid"]
    }


class SalarySettingAdd:
    """基本工资备份"""
    route = "salary_setting/salary_setting_add"
    params = {
        "salary_setting_list": """[{"active_date":"2016-12-02","backup":0,"base_salary":0.0,"create_date":"2016-12-02","guid":"c9f9c8d8d8da40c2a63ec2f2024104a5","holiday":3.0,"holidaySalary":0.0,"hour_salary":0.0,"m_start_day":0,"weekday":1.5,"weekdaySalary":0.0,"weekend":2.0,"weekendSalary":0.0,"mId":1},{"active_date":"2016-12-02","backup":0,"base_salary":9000.0,"create_date":"2016-12-02","guid":"1ddbf6158b26437b8c2a34ae33ebf988","holiday":3.0,"holidaySalary":0.0,"hour_salary":51.72,"m_start_day":0,"weekday":1.5,"weekdaySalary":0.0,"weekend":2.0,"weekendSalary":0.0,"mId":17}]"""
    }


class SalarySettingList:
    """基本工资列表"""
    route = "salary_setting/salary_setting_list"
    params = {
        "page": "1",
        "size": "10"
    }


class WorkdaySettingAdd:
    """工作日设定添加"""
    route = "workday_setting/add"
    params = {
        "json_data": """[{"guid":"c4ca4238a0b923820dcc509a6f75849b","mon":0,"tue":"1","wed":1,"thu":1,"fri":1,"sat":0,"sun":0,"start_day":"2017-01-01"},{"guid":"c81e728d9d4c2f636f067f89cc14862c","mon":1,"tue":"0","wed":1,"thu":1,"fri":1,"sat":0,"sun":0,"start_day":"2017-01-01"},{"guid":"eccbc87e4b5ce2fe28308fd9f2a7baf3","mon":1,"tue":"1","wed":0,"thu":1,"fri":1,"sat":0,"sun":0,"start_day":"2017-01-01"},{"guid":"a87ff679a2f3e71d9181a67b7542122c","mon":1,"tue":"1","wed":1,"thu":0,"fri":1,"sat":0,"sun":0,"start_day":"2017-01-01"}]"""
    }


class WorkdaySettingDownload:
    """工作日设定下载"""
    route = "workday_setting/download"
    params = {}


class SplashScreen:
    """闪屏"""
    route = "splash_screen/jjb_splash_screen"
    params = {
        "uid": common_lib.get_default_user()["jjb_id"],
        "version": "5.0.14",
        "used_day": "11",
        "is_login": "1"
    }
