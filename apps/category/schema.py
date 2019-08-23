# __author__ = 'ly'
# __date__ = '2019/08/15'

import graphene

from utils.uploadaliyun import Xfer
from .models import TestDetails as TestDetailsModel
from .models import TestName as TestNameModel
from .models import Banner as BannerModel
from datetime import datetime

x = Xfer()
x.initAliyun()


class LeaderTestInfo(graphene.ObjectType):
    url = graphene.String()
    title = graphene.String()
    image = graphene.String()


class LeaderTestType(graphene.ObjectType):
    group = graphene.List(LeaderTestInfo)


class Query(graphene.ObjectType):
    leader_test = graphene.Field(LeaderTestType)
    courses = graphene.Field(LeaderTestType)
    indexbanners = graphene.Field(LeaderTestType)

    def resolve_leader_test(self, info):
        leader_test_obj = TestDetailsModel.objects.filter(is_index_show=True, push_time__lt=datetime.now())
        banner_info = leader_test_obj.values_list('title', 'url', 'image')
        group = []

        for i in banner_info:
            title = i[0]
            url = i[1]
            image = x.sign_url(i[2])
            group.append(LeaderTestInfo(title=title, url=url, image=image))
        x.clearAliyun()
        return LeaderTestType(group=group)

    def resolve_courses(self, info):
        # 首页---课程分类
        banner_obj = BannerModel.objects.filter(is_show=True, push_time__lt=datetime.now())
        banner_info = banner_obj.values_list('title', 'url', 'image')
        group = []
        for i in banner_info:
            title = i[0]
            url = i[1]
            image = x.sign_url(i[2])
            group.append(LeaderTestInfo(title=title, url=url, image=image))
        x.clearAliyun()
        return LeaderTestType(group=group)

    def resolve_indexbanners(self, info):
        # 首页 第一部分 轮播图
        name_list = TestNameModel.objects.filter(is_index_show=True).values_list('name')
        leader_test_obj = TestDetailsModel.objects.filter(is_index_show=True, push_time__lt=datetime.now(),
                                                          child_test_name__name__in=name_list)
        banner_info = leader_test_obj.values_list('title', 'url', 'image')
        group = []
        for i in banner_info:
            title = i[0]
            url = i[1]
            image = x.sign_url(i[2])
            group.append(LeaderTestInfo(title=title, url=url, image=image))
        x.clearAliyun()
        return LeaderTestType(group=group)
