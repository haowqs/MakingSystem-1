# coding=gbk

# coding=utf-8

# -*- coding: UTF-8 -*-

from CCPRestSDK import REST
# import ConfigParser
import logging

LOG = logging.getLogger(__file__)
# ���ʺ�
accountSid = '8a216da862467c3a0162715bd6361388'

# ���ʺ�Token
accountToken = 'a16822a148f745fdb96d92e89b3a5cfe'

# Ӧ��Id
appId = '8a216da862467c3a0162715bd698138f'

# �����ַ����ʽ���£�����Ҫдhttp://
serverIP = 'app.cloopen.com'

# ����˿�
serverPort = '8883'

# REST�汾��
softVersion = '2013-12-26'


# ����ģ�����
# @param to �ֻ�����
# @param datas �������� ��ʽΪ���� ���磺{'12','34'}���粻���滻���� ''
# @param $tempId ģ��Id


class CCP(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            obj = super().__new__(cls)
            obj.rest = REST(serverIP, serverPort, softVersion)
            obj.rest.setAccount(accountSid, accountToken)
            obj.rest.setAppId(appId)

            cls.instance = obj
        return cls.instance

    def sendTemplateSMS(self, to, datas, tempId):
        status_Code = None
        try:
            result = self.rest.sendTemplateSMS(to, datas, tempId)
        except Exception as e:
            LOG.error(e)
            # raise e
        # else:
        #    for k,v in result.items():
        #
        #         if k=='templateSMS':
        #             for k,s in v.items():
        #                 print('%s:%s' % (k, s))
        #         else:
        #             print('%s:%s' % (k, v))
        else:
            status_Code = result.get('statusCode')

        return 0 if status_Code == '000000' else -1


ccp = CCP()

# sendTemplateSMS(�ֻ�����,��������,ģ��Id)

if __name__ == '__main__':
    ccp = CCP()
    ccp.sendTemplateSMS('13205827585', ["123456", 5], 1)
