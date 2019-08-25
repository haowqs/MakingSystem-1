# __author__ = 'ly'
# __date__ = '2019/08/23'
"""
获取统计信息
"""
from users.models import Users, CollectInfo  # 注册人数
from pdf.models import PDF  # 上传报告数量
from category.models import TestDetails, Banner


def get_info():
    registration = Users.objects.all().count()
    upload_number = PDF.objects.all().count()
    test_num = sum(TestDetails.objects.all().value_list('title'))
    banner_num = sum(Banner.objects.all().value_list('title'))
    info = CollectInfo.objects.first()
    if not info:
        info = CollectInfo()
    info.registration = int(registration)
    info.read_number = test_num + banner_num
    info.upload_number = int(upload_number)
    info.save()



