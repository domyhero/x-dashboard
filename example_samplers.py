# -*- coding: utf-8 -*-

from dashie_sampler import DashieSampler

import random
import collections

import requests
import os

"""
sampler:
1 from screencapture
2 from api
3 from fix data
"""

class WebsiteUpSampler(DashieSampler):
    def __init__(self, *args, **kwargs):
        DashieSampler.__init__(self, *args, **kwargs)
        self._last = 0
        self.page = 'http://bbs.wandoujia.com'

    def name(self):
        return 'website_up'

    def sample(self):
        try:
            r = requests.get(self.page)
            assert r.status_code == 200
            up='服务正常'
        except:
            up='宕机'
        s = {'text':up}
        return s

class SynergySampler(DashieSampler):
    def __init__(self, *args, **kwargs):
        DashieSampler.__init__(self, *args, **kwargs)
        self._last = 0

    def name(self):
        return 'synergy'

    def sample(self):
        s = {'value': random.randint(0, 100),
             'current': random.randint(0, 100),
             'last': self._last}
        self._last = s['current']
        return s

class BuzzwordsSampler(DashieSampler):
    def name(self):
        return 'buzzwords'

    def sample(self):
        my_little_pony_names = ['OPS',
                                '豌豆荚',
                                '香蕉',
                                '论坛，帮助中心',
                                '工单',
                                '百度贴吧',
                                '沧海教主']
        items = [{'label': pony_name, 'value': random.randint(0, 20)} for pony_name in my_little_pony_names]
        random.shuffle(items)
        return {'items':items}

class ConvergenceSampler(DashieSampler):
    def name(self):
        return 'convergence'

    def __init__(self, *args, **kwargs):
        self.seedX = 0
        self.items = collections.deque()
        DashieSampler.__init__(self, *args, **kwargs)

    def sample(self):
        self.items.append({'x': self.seedX,
                           'y': random.randint(0,20)})
        self.seedX += 1
        if len(self.items) > 10:
            self.items.popleft()
        return {'points': list(self.items)}

class CommentsSampler(DashieSampler):
    """docstring for CommentsSampler"""
    # def __init__(self, arg):
    #     super(CommentsSampler, self).__init__()
    #     self.arg = arg
    def name(self):
        return 'comments'

    def sample(self):
        quote = '我最喜欢豌豆荚的不是别的，仅仅是因为它中立。比如说吧，360手机助手上面首页排行榜上竟然没有手机QQ只有微信，我不知道360是如何想的，浏览器分类上也没有QQ浏览器。只有自己打名字才可以找到，并且不是360系的产品几乎分数和评论都奇差。腾讯的应用宝也是如此。反观豌豆荚，我很喜欢中立加上中肯的评论！'
        avatar = 'http://bbs.wandoujia.com/uc_server/avatar.php?uid=6471290&size=middle'
        name = '论坛用户-Siva'
        return {'current_comment': {'name': name, 'avatar': avatar, 'quote': quote}}

class WdjDollSampler(DashieSampler):
    def __init__(self, *args, **kwargs):
        self.files = os.listdir('assets/images/wdjdoll')
        DashieSampler.__init__(self, *args, **kwargs)
        self.files = [i for i in self.files if i.index('.png')]

    def name(self):
        return 'wdjdoll'

    def sample(self):
        file = '/assets/images/wdjdoll/'+random.sample(self.files,1)[0]
        # file = '/image/wdjdoll/傲娇.png'
        return {'image': file}

class RandomCat(DashieSampler):
    def name(self):
        return 'randomcat'
    def sample(self):

        return {'image': "http://thecatapi.com/api/images/get?format=src&type=gif&timestamp=%s" % (random.random())}

class ZhihuTopicSampler(DashieSampler):
    """docstring for ZhihuTopicSampler"""
    # def __init__(self, arg):
    #     super(ZhihuTopicSampler, self).__init__()
    #     self.arg = arg
    def name(self):
        return 'zhihu_topic'

    def sample(self):
        sampletitles_raw = ["果合张宁为什么去了豌豆荚？", "在与豌豆荚、360 等视频聚合平台合作时，视频网站能获得的利益是什么、如何把控对方截流用户流量的风险？", "云安全吗？", "豌豆荚相比 360 在 LINE 推广上有哪些优势？", "安卓手机应用管理软件中为什么经常出现比某应用官方版本更高的版本号？", "怎样可以让豌豆荚跨网络wifi连接？", "请问豌豆荚团队和V电影团队有什么关系？私交很好么？", "如何删除豌豆荚帐号?", "豌豆荚是怎样实现手机连接数据线就实现宽带上网的?", "360，豌豆荚，百度 (91) 都在做手机助手，传腾讯也将推手机助手，哪家更被看好，为什么？", "豌豆荚更看重求职者的哪些素质？", "安卓有哪款类似倒数日的应用值得推荐？", "国内安卓应用市场互相抓应用的源头在哪？", "豌豆荚，手机管家等应用不能实现google play 那样的在线web安装应用吗？", "豌豆荚手机应用音乐下载的功能存在搜不到最新的和比较偏的民谣歌曲这一缺陷，请问贵荚如何看待这个问题?", "为什么豌豆荚，360 手机助手会把一个软件反复的更新？", "使用手机通过数据线和电脑连接, 然后让手机通过电脑的网络上网, 有实现的可能吗?", "豌豆荚好吗？", "像豌豆荚这样频繁升级你烦不烦?为什么？", "豌豆荚的空气净化器还有戏么？"]
        myRange =  range(0,len(sampletitles_raw))
        random.shuffle(myRange)
        # sorted([random.randint(0, 20) for i])
        sampletitles = [ sampletitles_raw[i] for i in myRange[:4] ]
        items = [{'label': title, 'value': str(random.randint(0, 20))+'小时前'} for title in sampletitles]
        return {'items': items}

# import ga helper
class GAbbsSampler(DashieSampler):
    def __init__(self, *args, **kwargs):
        DashieSampler.__init__(self, *args, **kwargs)
        self._last = 0

    def name(self):
        return 'ga_bbs'

    def sample(self):
        s = {'value': random.randint(0, 100),
             'current': random.randint(0, 100),
             'last': self._last}
        self._last = s['current']
        return s

