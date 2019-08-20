# __author__ = 'ly'
# __date__ = '2019/08/15'
from datetime import datetime
import graphene
from .models import Banner as BannerModel
from .models import TestDetails as TestDetailsModel
from .models import TestName as TestNameModel
from .models import Banner as BannerModel
from datetime import datetime
from makingsystem.settings.base import MEDIA_ROOT


class LeaderTestInfo(graphene.ObjectType):
    url = graphene.String()
    title = graphene.String()
    image = graphene.String()


class LeaderTestType(graphene.ObjectType):
    group = graphene.List(LeaderTestInfo)


class BannerType(LeaderTestType):
    pass


class IndexBannerType(LeaderTestType):
    pass


class Query:
    leader_test = graphene.Field(LeaderTestType)
    courses = graphene.Field(BannerType)
    indexbanners = graphene.Field(IndexBannerType)

    def resolve_leader_test(self, info):
        leader_test_obj = TestDetailsModel.objects.filter(is_index_show=True, push_time__lt=datetime.now())
        banner_info = leader_test_obj.values_list('title', 'url', 'image')
        return LeaderTestType(group=[LeaderTestInfo(title=i[0], url=i[1], image=i[2]) for i in banner_info])

    def resolve_courses(self, info):
        # 首页---课程分类
        banner_obj = BannerModel.objects.filter(is_show=True, push_time__lt=datetime.now())
        banner_info = banner_obj.values_list('title', 'url', 'image')
        return LeaderTestType(group=[LeaderTestInfo(title=i[0], url=i[1], image=i[2]) for i in banner_info])

    def resolve_indexbanners(self, info):
        # 首页 第一部分 轮播图
        banner_show_class = TestNameModel.objects.filter(is_index_show=True)  # 能在首页轮播的类对象
        name_list = [obj.name for obj in banner_show_class]
        leader_test_obj = TestDetailsModel.objects.filter(is_index_show=True, push_time__lt=datetime.now(),
                                                          child_test_name__in=name_list)
        banner_info = leader_test_obj.values_list('title', 'url', 'image')
        return IndexBannerType(group=[LeaderTestInfo(title=i[0], url=i[1], image=i[2]) for i in banner_info])
