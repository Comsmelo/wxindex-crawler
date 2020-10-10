# ============================================
# date: 2020.10 
# name: wxindex crawler
# author: zyq
# reference: https://www.cnblogs.com/zzh--blog/p/10599708.html; https://blog.csdn.net/weixin_45463877/article/details/106490773
# ============================================

import requests
import urllib
import time

# 头部信息根据charles抓包结果来写
headers = {
    'Host': 'search.weixin.qq.com',
    'Content-Type': 'application/json',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E217 MicroMessenger/6.8.0(0x16080000) NetType/WIFI Language/en Branch/Br_trunk MiniProgramEnv/Mac',
    'Referer': 'https://servicewechat.com/wxc026e7662ec26a3a/10/page-frame.html' 
  }


def wxindex_crawler(keyword):
    keyword = urllib.parse.quote(keyword)
    # 以下两个参数的每隔几分钟就要人工获取一次, 自动化获取工具还未探索
    openid = 'ov4ns0Pms-ZP55JgkG__RiRW5Y54'
    search_key = '1602323727015999_1886479408'
    url = 'https://search.weixin.qq.com/cgi-bin/searchweb/wxindex/querywxindexgroup?query_sug_list=&group_query_sug_list=&group_query_list={}&wxindex_query_list={}&gid=&openid={}&search_key={}'.format(keyword, keyword, openid, search_key)
    print(url)
    res = requests.get(url, headers = headers, verify = False)
    data = res.json()['data']['group_wxindex'][0]
    wxindex = eval('[' + data['wxindex_str'] + ']')[:]
    return wxindex


def main():
    # 扔关键词的地方
    #keywords = ['期货', '人工智能', '迪丽热巴', '黑人']
    keywords = ['奥特曼']
    for key in keywords:
        result = wxindex_crawler(key)
        print(key,'的近',len(result),'天微信指数：', result)
        # 延迟用于反爬虫机制
        time.sleep(10)

if __name__ == '__main__':
    main()
