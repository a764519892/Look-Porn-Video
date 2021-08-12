# -*- coding: utf-8 -*-
import random
import requests
from lxml import etree
from fake_useragent import UserAgent
import re
import urllib
import threading
import os
import time

class jiujiu_ai():
    def __init__(self):
        guo_chan = ['https://www.33b50.xyz/Html/60/index-{}.html'.format(i) for i in range(185)]
        guo_chan_one = random.sample(guo_chan, 1)
        zhong_wen = ['https://www.33b50.xyz/Html/94/index-{}.html'.format(i) for i in range(29)]
        zhong_wen_one = random.sample(zhong_wen, 3)
        nv_you = ['https://www.33b50.xyz/Html/100/index-{}.html'.format(i) for i in range(29)]
        nv_you_one = random.sample(nv_you, 3)
        self.jiujiu_heji =guo_chan_one +zhong_wen_one +nv_you_one



    def huoqu(self):

        for i in self.jiujiu_heji:
            ua = UserAgent(verify_ssl=False, path='fake_useragent.json').random
            headers = {"User-Agent": ua}
            data = requests.get(url=i, headers=headers)
            data.encoding='utf-8'
            data = data.text
            #print(data.encode('gbk','ignore').decode(encoding="gbk", errors="strict"))
            s = etree.HTML(data.encode('gbk','ignore').decode(encoding="gbk", errors="strict"))
            meinv_liebiao = s.xpath('//li/a/@href')
            #print(meinv_liebiao)
            if len(meinv_liebiao) > 1:
                # #meinv = random.choice(meinv_liebiao)
                # for t in meinv_liebiao:
                #     s = 'https://www.33b50.xyz/'
                #     url = s + t
                #     self.xiazai(url)
                meinv = random.choice(meinv_liebiao)

                s = 'https://www.33b50.xyz/'
                url = s + meinv
                self.xiazai(url)
            else:
                pass

    def xiazai(self,url):
        ua = UserAgent(path='fake_useragent.json').random
        headers = {"User-Agent": ua}
        data = requests.get(url=url, headers=headers)
        data.encoding = "utf-8"
        data = data.text
        #print(data.encode('gbk','ignore').decode(encoding="gbk", errors="strict"))
        s = etree.HTML(data.encode('gbk','ignore').decode(encoding="gbk", errors="strict"))
        meinv_mingzi = (''.join(s.xpath('//title/text()')).replace('0-1','1-1'))
        meinv_dizhi = 'https://www.33b51.xyz/'+''.join(s.xpath('//*[@id="playurl1"]/@href'))
        if meinv_dizhi == 'https://www.33b50.xyz/':
            pass
        else:
            print('请复制到浏览器打开：')
            print(meinv_mingzi+'\n'+meinv_dizhi)
if __name__== '__main__':
    jiujiu_ai().huoqu()
