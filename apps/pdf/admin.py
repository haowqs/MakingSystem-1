from django.contrib import admin
from .models import PDFupload, PDF


# Register your models here.
class PDFAdmin(admin.ModelAdmin):
    """课程分类"""
    list_display = ['name']


class PDFuploadAdmin(admin.ModelAdmin):
    """PDF上传"""
    def save_model(self, request, obj, form, change):
        obj.save()
        print('-----开始解压文件并上传pdf到阿里云------')

    list_display = ['file', 'name']


admin.site.register(PDFupload, PDFuploadAdmin)
