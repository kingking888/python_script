# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json


class JSONPipeline(object):

    def __init__(self):
        self.file = open("result_2.json", 'w', encoding='utf-8')
        self.file.write('[')
        self.file.write('\n')

    def process_item(self, item, spider):
        json_line = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.file.write(json_line)

        return item

    def close_spider(self, spider):
        #  let the json file end with a ']'
        self.file.write(']')
        self.file.close()


import os
from scrapy.pipelines.files import FilesPipeline
from scrapy import Request


class MyImagesPipeline(FilesPipeline):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



        self.juan ={
            45268: "封面",
            45269: "扉页",
            45270: "彩图",
            45271: "序一",
            45272: "序二",
            45273: "凡例",
            45274: "概述",
            45275: "大事记",
            45276: "卷一 建置",
            45277: "卷二 自然地理",
            45278: "卷三 农业",
            45279: "卷四 林业",
            45280: "卷五 水利 电力",
            45281: "卷六 畜牧 水产",
            45282: "卷七 粮油",
            45283: "卷八 工业",
            45284: "卷九 交通 邮电",
            45285: "卷十 城乡建设",
            45286: "卷十一 商业",
            45287: "卷十二 财政",
            45288: "卷十三 税务",
            45289: "卷十四 金融",
            45290: "卷十五 供销",
            45291: "卷十六 政党",
            45292: "卷十七 人大 政府 政协",
            45293: "卷十八 民政",
            45294: "卷十九 政法",
            45295: "卷二十 劳动 人事",
            45296: "卷二十一 群团",
            45298: "卷二十三 文化",
            45299: "卷二十四 教育",
            45300: "卷二十五 体育",
            45301: "卷二十六 科技",
            45302: "卷二十七 卫生",
            45303: "卷二十八 文物",
            45304: "卷二十九 艺文",
            45305: "卷三十 方言",
            45306: "卷三十一 宗教",
            45307: "卷三十二 风俗",
            45308: "卷三十三 人口",
            45309: "卷三十四 宗祠 会馆 祠庙",
            45310: "卷三十五 谚语 歇后语 传说",
            45311: "卷三十六 人物",
        }

        self.zhang = {
            45313: "第一章建置沿革",
            45314: "第二章区划治所",
            45315: "第一章 地貌 地质",
            45316: "第二章 山脉 水系",
            45317: "第三章 土壤 植被",
            45318: "第四章 气候 物候",
            45319: "第五章 自然资源与灾害",
            45320: "第一章土地制度与生产组织",
            45321: "第二章生产基本条件",
            45322: "第三章农作物",
            45323: "第四章农技农艺",
            45324: "第五章 经济效益",
            45325: "第一章森林分布与权属",
            45326: "第二章造林育林",
            45327: "第三章森林保护",
            45328: "第四章购销经营",
            45329: "第一章水利设施",
            45330: "第二章水利灌溉    ",
            45331: "第三章水土保持",
            45332: "第四章水电建设",
            45333: "第五章农村初级电气化",
            45334: "第一章畜牧业",
            45335: "第二章水产业",
            45336: "第一章购销",
            45337: "第二章贮运",
            45338: "第一章企业设置",
            45339: "第二章工业门类",
            45340: "第三章生产经营",
            45341: "第一章交通",
            45342: "第二章 邮电",
            45343: "第一章县城建设",
            45344: "第二章镇乡场",
            45345: "第一章经济成分",
            45346: "第二章经营网点",
            45347: "第三章商品流通",
            45348: "第四章物价",
            45349: "第五章名特土产",
            45350: "第一章机构体制",
            45351: "第二章财政收支",
            45352: "第三章审计监察",
            45353: "第一章征收管理",
            45354: "第二章税收",
            45355: "第一章机构",
            45362: "第二章货币流通",
            45363: "第三章信贷",
            45364: "第四章储蓄",
            45365: "第五章会计出纳",
            45366: "第六章保险",
            45367: "第七章有价证券发行",
            45368: "第一章机构演变",
            45372: "第二章民主管理",
            45373: "第三章 业务经营",
            45374: "第四章 扶助生产",
            45375: "第一章中国共产党奉新地方组织",
            45376: "第二章国民党奉新县党部",
            45377: "第三章其它党派",
            45378: "第一章人大",
            45379: "第二章政府",
            45380: "第三章政协",
            45381: "第一章普选",
            45382: "第二章社会救济",
            45383: "第三章拥军优属",
            45384: "第四章殡葬改革",
            45385: "第一章治安工作",
            45386: "第二章检察",
            45389: "第三章审判工作",
            45390: "第四章司法行政",
            45391: "第一章劳动  ",
            45392: "第二章人事",
            45393: "第三章工资待遇",
            45394: "第四章离退休制度",
            45395: "第一章工农妇商组织",
            45396: "第二章文侨社联组织",
            45397: "第三章靑少年组织",
            45403: "第一章群众文艺",
            45404: "第二章戏剧",
            45405: "第三章图书",
            45406: "第四章档案",
            45409: "第五章电影",
            45410: "第六章报刊广播电视",
            45411: "第一章书院、儒学、私塾",
            45412: "第二章普通教育",
            45413: "第三章成人教育",
            45414: "第四章教师队伍",
            45415: "第一章体育管理",
            45416: "第二章传统体育",
            45417: "第三章社会体育",
            45418: "第四章学校体育",
            45419: "第五章竞技体育",
            45420: "第一章科技机构",
            45421: "第二章科技队伍",
            45422: "第三章科普工作",
            45423: "第四章科研成果",
            45424: "第五章其它科技工作",
            45425: "第一章预防",
            45426: "第二章医疗",
        }

    def get_media_requests(self, item, info):
        '''
        :param item: spiders传递过来的 item
        :param info: info其实是一个用来保存保存图片的名字和下载链接的列表
        :return:
        '''
        for i in range(len(item['pdf_url'])):
            # 添加meta是为了下面重命名文件名使用
            yield Request(item['pdf_url'][i], meta={'item': item})

    def file_path(self, request, response=None, info=None):
        # 通过上面的meta传递过来item
        item = request.meta['item']

        father, son = item['father'].split("_")
        father = father.replace("c","")

        father = int(father)

        son = son.replace("c", "")
        son =int(son)
        # 卷
        # if father == "0":
        #     filename = u'奉新县志/卷/{0}/{1}.pdf'.format(self.juan[son], item["title"])
        #     return filename
        #
        # #  (45268, 45311) 是卷的范围
        # if father in range(45268, 45311):
        #     filename = u'奉新县志/章/{0}/{1}/{2}.pdf'.format(self.juan[father], self.zhang[son], item["title"])
        #     return filename
        #
        # if father in range(45313, 45457):
        #     filename = u'奉新县志/节/{0}/{1}.pdf'.format(self.zhang[father], item["title"])
        #     return filename

        return "file/"+str(father) + "-" + str(son) + "-" + item["title"]+".pdf"
