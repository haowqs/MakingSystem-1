import os
import re

import oss2
import zipfile

from pdf.models import PDF
from users.models import Users
from makingsystem.settings import config, MEDIA_ROOT
# 用户登录名称 object-oss@1463266644828335.onaliyun.com
# AccessKey ID LTAIeFNriSXX6ySq
# AccessKeySecret QHdxPWx7JU9q6Y55D3feQxlwcfZb66
from django.db import connection
import logging
from utils.log import log
from category.models import TestDetails, Banner
from django.contrib import admin

log.initLogConf()

LOG = logging.getLogger(__file__)


# cursor = connection.cursor()


class Xfer(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            obj = super().__new__(cls)
            # obj.rest = REST(serverIP, serverPort, softVersion)
            # obj.rest.setAccount(accountSid, accountToken)
            # obj.rest.setAppId(appId)

            cls.instance = obj
        return cls.instance

    def __init__(self):

        self.auth = None
        self.bucket = None
        self.AccessKeyId = config.AccessKeyId
        self.ACCessKeySecret = config.AccessKeySecret
        self.Endpoint = config.Endpoint
        self.bucketName = config.bucketName

    def initAliyun(self):
        if self.auth is None:
            self.auth = oss2.Auth(self.AccessKeyId, self.ACCessKeySecret)
            self.bucket = oss2.Bucket(self.auth, self.Endpoint, self.bucketName)

    def clearAliyun(self):
        self.auth = None
        self.bucket = None

    def upload(self, localpath):
        if not os.path.isfile(localpath):
            return
        LOG.info(f'{"+" * 10}uploading {"+" * 10}')
        zfile = zipfile.ZipFile(localpath, 'r')
        for fileN in zfile.namelist():
            if fileN.endswith('/'):
                continue
            # name = fileN.encode('cp437').decode('gbk')
            title_name = fileN.split('+')[0]
            test_obj = TestDetails.objects.filter(title=title_name)
            if test_obj:
                test_obj.test_number = int(test_obj.test_number) + 1
            else:
                banner_obj = Banner.objects.filter(title=title_name)
                if banner_obj:
                    banner_obj.test_number = int(banner_obj.test_number) + 1
            name = fileN
            print('###name:', name)
            mobile = re.compile('1[345678]\d{9}')
            mobileNum = mobile.search(name).group()
            # user = Users.objects.filter(mobile=mobileNum)
            PDFInfo = PDF.objects.filter(user__mobile=mobileNum)
            if not PDFInfo.exists():
                print("用户未保存")
                continue
            PDFInfo.name = name.split('/')[-1]
            PDFInfo.aliosspath = name
            print('### mobileNum:', mobileNum)
            # if not user:
            #     LOG.error(f"用户不存在")
            #     user = Users()
            #     user.mobile = mobileNum
            #     user.username = mobileNum
            #     user.save()
            PDFInfo.save()
            data = zfile.read(fileN)
            self.bucket.put_object(name, data)
        try:
            os.remove(localpath)
        except OSError as e:
            pass

    def sign_url(self, name):
        url = self.bucket.sign_url('GET', name, 60 * 30)
        return url


# class UploadImageAdmin(admin.ModelAdmin):
#     """
#     自动上传新建对象的图片至阿里云
#     """
#
#     def save_model(self, request, obj, form, change):
#         obj.save()
#         # LOG.info('----- 开始上传 下载 至本地: %s' % obj.image)
#         # zip_path = os.path.join(MEDIA_ROOT, str(obj.image))
#         # xfer = Xfer()
#         # xfer.initAliyun()
#         # xfer.upload(str(obj.image), )
#         # xfer.clearAliyun()
#         print(obj.__dir__())


if __name__ == '__main__':
    x = Xfer()
    x.initAliyun()
    url = x.sign_url("testPDF/123456.pdf")
    print(url)
