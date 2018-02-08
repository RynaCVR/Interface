# coding=utf-8
"""打工贷"""

from ifautotest.ifmain.common import common_lib


class VersionLimit:
    """手机号注册"""
    route = "param/get_min_version_limit"
    params = {}


class Login:
    """打工贷登录"""
    route = "user/login"
    params = {
        "jjb_uid": common_lib.get_default_user()["jjb_uid"],
        "dgq_uid": common_lib.get_default_user()["dgq_uid"],
        "cid": common_lib.get_default_user()["cid"]
    }


class HoldTicketsLog:
    """加载免息券"""
    route = "handed_out_intereset_log/hold_tickets"
    params = {
        "uid": common_lib.get_default_user()["jjb_id"]
    }


class CheckUserIsReject:
    """检查用户是否被拒"""
    route = "loan_order/check_user_is_reject"
    params = {}


class GetOpenorder:
    """是否有未完成订单"""
    route = "loan_order/get_openorder"
    params = {}


class GetParams:
    """得到参数"""
    route = "params/get_params"
    params = {}


class LoanType:
    """借贷类型列表"""
    route = "loan_type/list"
    params = {
        "page": "1",
        "size": "10"
    }


class CustomPop:
    """获取自定义弹窗"""
    route = "param/custom_popup"
    params = {}


class IsCreate:
    """判断是否可以创建"""
    route = "loan_order/cancreate"
    params = {}


class MyInfo:
    """获取个人信息"""
    route = "loan_order/myinfo"
    params = {}


class CompanyInfo:
    """获取公司数据"""
    route = "user_attribute/get_update_company_info"
    params = {}


class UserInfo:
    """获取用户数据"""
    pass


class UpdateCompanyInfo:
    """提交公司信息"""
    route = "loan_order/update_company_info"
    params = {
        "id": "815739",
        "industry_id": "24",
        "company": "Hx",
        "province": "上海",
        "city": "上海",
        "company_address": "徐汇区",
        "work_status": "1"
    }
