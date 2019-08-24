from django.contrib import admin
from .models import Banner, TestDetails, TestIn, TestName
from utils.uploadaliyun import UploadImageAdmin


# Register your models here.
class BannerAdmin(UploadImageAdmin):
    """课程分类"""
    list_display = ['title', 'image', 'is_show', 'push_time']


class TestDetailsAdmin(UploadImageAdmin):
    """测试详情"""

    list_display = ['title', 'parent_test_name', 'child_test_name', 'image', 'test_number',
                    'is_index_show', 'is_class_show', 'push_time', ]


class TestNameAdmin(admin.ModelAdmin):
    """测试分类名"""
    list_display = ['name', 'parent', 'is_index_show']


class TestInAdmin(admin.ModelAdmin):
    """分类页测试介绍"""
    list_display = ['introduce', 'theory', 'notice']


admin.site.register(Banner, BannerAdmin)
admin.site.register(TestDetails, TestDetailsAdmin)
admin.site.register(TestName, TestNameAdmin)
admin.site.register(TestIn, TestInAdmin)

admin.site.site_header = '管理后台'
admin.site.site_title = '大学生领导力潜质研究院'
