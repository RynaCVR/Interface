# coding=utf-8


from ..common import common_lib


"""
打工圈接口
"""


class RandNickname:
    """随机用户名"""
    route = "rand_nickname/nickname"
    params = {}


class JllUserSmsLogSendSms:
    """验证码：发送验证短信"""
    route = "jll_users_sms_log/sendsms"
    params = {
        "mobile": "18134413794",
        "template": "EditPassword",   # EditPassword 修改密码, RegisterVerify 注册账号, MobileBindingVerify, 手机号绑定 MobileRebindingVerify 手机解除绑定, VerifyMobile 实名认证
        "appid": "2"
    }


class JllUsersDeviceAdd:
    """新建设备号信息"""
    route = "jll_users_device/add"
    params = {
        "device_token": None,
        "install_number": "1",
        "imsi": "123456789",
        "brand": "AutoTest",
        "resolution": "1080x1800",
        "mac": "38:bc:1a:a5:e5:e1",
        "imei": "123456789012345",
        "device_id": "123456789",
        "os_version": "7.0",
        "model": "1.0",
        "platform": "Android",
        "channel": "julanling"
    }


class JllTopicIndexTopicList:
    """推荐话题列表"""
    route = "jll_topic/index_topic_list"
    params = {}

    
class JllTopicTopicList:
    """全部话题列表"""
    route = "jll_topic/topic_list"
    params = {
        "page": "1",
        "size": "20"
    }


class JllTopicThreadList:
    """某一话题的贴子列表"""
    route = "jll_topic_thread/thread_list"
    params = {
        "page": "1",
        "size": "20",
        "tpid": "202"        # 话题ID
    }


class JllTopicTopicDetail:
    """某一话题详情"""
    route = "jll_topic/topic_detail"
    params = {
        "id": "202"
    }
    

class JllTopDayTopmark:
    """红人榜 日榜"""
    route = "jll_top_day/get_day_topmark"
    params = {
        "page": "1",
        "size": "20",
        "sex": "0"
    }


class JllTopWeekTopmark:
    """红人榜 周榜"""
    route = "jll_top_week/get_week_topmark"
    params = {
        "page": "1",
        "size": "10",
        "sex": "0"
    }


class JllNewSignGoodAdd:
    """签到点赞 点赞"""
    route = "jll_new_sign_good/add"
    params = {
        "uid": common_lib.get_default_user()["dgq_uid"],
        "type": "1"     # 1 今日榜， 2 累计榜， 3 当月榜
    }


class JllNewSignTotalTotal:
    """签到汇总 总览"""
    route = "jll_new_sign_total/total"
    params = {}


class JllNewSignTotalList:
    """签到汇总 排行榜"""
    route = "jll_new_sign_total/list"
    params = {
        "page": "1",
        "size": "20",
        "type": "3"     # 1 今日榜， 2 累计榜， 3 当月榜
    }


class JllNewSignDetailList:
    """签到明细 签到列表"""
    route = "jll_new_sign_detail/list"
    params = {
        "page": "1",
        "size": "10"
    }


class JllNewSignDetailAdd:
    """打工圈签到操作"""
    route = "jll_new_sign_detail/add"
    params = {}
    

class JllUsersDailyVistLogList:
    """用户地理位置 访问日志列表"""
    route = "jll_users_daily_vist_log/list"
    params = {
        "page": "1",
        "size": "10"
    }


class JllUsersDailyVistLogAdd:
    """用户地理位置 新增每日访问日志"""
    route = "jll_users_daily_vist_log/add"
    params = {
        "device": None,     # 在执行用例时赋值
        "uid": common_lib.get_default_user()["dgq_uid"],
        "lat": "31.287996",
        "lng": "121.319827",
        "city_code": "289",
        "city": "上海",
        "district": "嘉定区",
        "address": "上海市嘉定区银翔路",
        "local_mobile": "13010000001"
    }


class JllUsersChangeMobile:
    """更换手机号"""
    route = "jll_users/change_mobile"
    params = {
        "old_mobile": "13010000001",
        "mobile": "13010000001"
    }


class JllUsersblackListInsert:
    """拉黑用户"""
    route = "jll_users_blacklist/insert"
    params = {
        "uid": None,
    }
    

class JllUsersInfoGetHomeTownList:
    """我的老乡列表"""
    route = "jll_users_info/get_hometownlist"
    params = {}
    

class JllUsersGetColleague:
    """我的同事列表"""
    route = "jll_users/get_colleague"
    params = {}


class JllUsersPhotoAdd:
    """个人中心图片上传"""
    route = "jll_users_photo/add"
    params = {
        "photo": "photo/2015/07/07/559b6cdd1a0ae.jpg"
    }


class JllUsersPhotoDelPhoto:
    """个人中心图片删除"""
    route = "jll_users_photo/del_photo"
    params = {
        "id": "513278"
    }


class JllUsersPhotoList:
    """个人中心图片列表"""
    route = "jll_users_photo/list"
    params = {}


class JllUsersQQIsExists:
    """判断QQ是否已经存在"""
    route = "jll_users/qq_is_exists"
    params = {
        "qq_openid": "360570F12B582E902EEDE945D0AD3EFF"
    }
