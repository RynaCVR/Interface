
"""厂点评"""


class CompanyIndex:
    """厂点评首页"""
    route = "company/index"
    params = {}


class SalaryAdd:
    """添加工资条"""
    route = "jcbd/salary_add"
    params = {
        "secret_id": "ae20954c4aae2917304f4554508d03db",
        "job_id": "1",
        "month": "东莞",
        "base_salary": "1500",
        "month_salary": "2000",
        "is_full_hours": "1",
        "image": "abcdefg"
    }


class CompanySearch:
    """工厂搜索"""
    route = "jcbd/company_search"
    params = {
        "keyword": "达丰"
    }


class CommentsAdd:
    """厂点评添加"""
    route = "jcbd/comments_add"
    params = {
        "secret_id": "ae20954c4aae2917304f4554508d03db",
        "working_years": "1个月以下",
        "working_years_id": "1",
        "is_leave": "0",
        "satisfactory": "很满意",
        "unsatisfactory": "不满意",
        "welfare": "5",
        "welfare_text": "测试内容xxx",
        "food": "5",
        "food_text": "测试内容xxx",
        "accommodation": "2",
        "accommodation_text": "测试内容xxx",
        "environment": "1",
        "environment_text": "测试内容XXX",
        "management": "3",
        "management_text": "测试内容XXX",
        "images": "xxxxx",
    }


class CompanyAdd:
    """创建工厂"""
    route = "jcbd/company_add"
    params = {
        "name": "达丰",
        "short_name": "达丰",
        "address": "上海徐家汇",
        "province": "广东",
        "province_id": "28",
        "city": "东莞",
        "city_id": "2816"
    }


class CompanyHotKeywords:
    """热门搜索词"""
    route = "jcbd/company_hot_keywords"
    params = {}


class JobList:
    """岗位列表"""
    route = "jcbd/company_job_list"
    params = {
        "secret_id": "ae20954c4aae2917304f4554508d03db"
    }


class CompanyHots:
    """热门工厂列表"""
    route = "company/hots"
    params = {}


# 达丰 （上海）电脑有限公司 secret_id
# userinfo 13010000001
class CompanyCommentList:
    """工厂点评列表"""
    route = "company/comment_list"
    params = {
        "id": "12744ee7a533c513b5cfac51a054dec2",
        "userinfo": "e3545d9e9bdaba367ae3f1208663f302f5b20e5b097c5754b4eb12554fbf0a6df2a172a9348b3babee2875fac7d8f3c5c6e4b632882106a39d2b21563607a9ae"
    }


class CompanyShareDetail:
    """工厂详情页分享落地页"""
    route = "company/share_detail"
    params = {
        "id": "12744ee7a533c513b5cfac51a054dec2"        # 达丰 （上海）电脑有限公司 secret_id
    }


class CompanyCommentDetail:
    """
    点评详情
    id: 评论id
    """
    route = "company/comment_detail"
    params = {
        "id": "faed783a0048ace9fb715d25b2dd4e97",
        "userinfo": "e3545d9e9bdaba367ae3f1208663f302f5b20e5b097c5754b4eb12554fbf0a6df2a172a9348b3babee2875fac7d8f3c5c6e4b632882106a39d2b21563607a9ae"
    }


class CompanyCommentShareSuccess:
    """点评分享成功"""
    route = "company/comment_share_success"
    params = {
        "userinfo": "e3545d9e9bdaba367ae3f1208663f302f5b20e5b097c5754b4eb12554fbf0a6df2a172a9348b3babee2875fac7d8f3c5c6e4b632882106a39d2b21563607a9ae"
    }


class CompanySalaryShareSuccess:
    """工资条分享成功"""
    route = "company/salary_share_success"
    params = {
        "userinfo": "e3545d9e9bdaba367ae3f1208663f302f5b20e5b097c5754b4eb12554fbf0a6df2a172a9348b3babee2875fac7d8f3c5c6e4b632882106a39d2b21563607a9ae"
    }


# 混淆加密前： 343
# 混淆加密后： 1facbe50b0385e315557ef25a132bf97
#   0 ✓ 15:51:36 root@10.31.234.8:/var/www/sites/jcbdh5.dev.julanling.com = # php artisan script:confusion encrypt 344
# 混淆加密前： 344
# 混淆加密后： 48514ff4fa16c3eff274c91f4aec106a
#   0 ✓ 15:51:36 root@10.31.234.8:/var/www/sites/jcbdh5.dev.julanling.com = # php artisan script:confusion encrypt 345
# 混淆加密前： 345
# 混淆加密后： 2ecab64e7e69a04e41fb333b135680fa


class CompanySalary:
    """岗位工资条列表"""
    route = "company/salary"
    params = {
        "cp_job_id": "1facbe50b0385e315557ef25a132bf97",
        "userinfo": "e3545d9e9bdaba367ae3f1208663f302f5b20e5b097c5754b4eb12554fbf0a6df2a172a9348b3babee2875fac7d8f3c5c6e4b632882106a39d2b21563607a9ae"
    }


class CompanyRedPacket:
    """上传工资条领红包活动，用户活动状态"""
    route = "company/red_packet"
    params = {
        "userinfo": "e3545d9e9bdaba367ae3f1208663f302f5b20e5b097c5754b4eb12554fbf0a6df2a172a9348b3babee2875fac7d8f3c5c6e4b632882106a39d2b21563607a9ae"
    }
