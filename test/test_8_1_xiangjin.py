# -*- coding: utf-8 -*-
########################################################################
#
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
#
########################################################################

import md5
import time
import urllib
import re
import sys

import scrapy
from scrapy.http import Request
from bs4 import BeautifulSoup
from scrapy import signals

html_doc = """

<!DOCTYPE  html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="zh">
<title>香港警察年报 2012</title>
<head>

<link href="../css/chi.css" rel="stylesheet" type="text/css" />
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
<link rel="shortcut icon" type="image/x-icon" href="favicon.ico">
</head>
<body>
<p align="center"><a name="top" id="top"></a>[ <a href="../en/HKPF_Eng10.html">English</a> ] [ <a href="../tc/HKPF_TChi10.html">繁體</a> ]</p><br />
<h1 align="center">2012 香港警察年报</h1>
<h2 align="center">服务为本 精益求精</h2>
<p align="center">[ <a href="HKPF_SChi01.html">序言</a> ]   [ <a href="HKPF_SChi02.html">大事回顾</a> ]   [ <a href="HKPF_SChi03.html">精英荟萃 携手灭罪</a> ]   [ <a href="HKPF_SChi04.html">行动</a> ]   [ <a href="HKPF_SChi05.html">总区指挥官汇报</a> ]   [ <a href="HKPF_SChi06.html">人事及训练</a> ]   [ <a href="HKPF_SChi07.html">监管处</a> ]</p>
<p align="center">[ <a href="HKPF_SChi08.html">配备精良 技术先进</a> ]   [ <a href="HKPF_SChi09.html">财务、政务及策划</a> ]   [ <a href="HKPF_SChi10.html">环保报告</a> ]   [ <a href="HKPF_SChi11.html">警务处架构</a> ]   [ <a href="HKPF_SChi12.html">附件及附录</a> ]   [ <a href="HKPF_SChi13.html">查询或意见</a> ]</p>
<p align="center"> </p>
<table width="100%" border="0" cellspacing="0" cellpadding="10">
  <tr>
    <td align="left" valign="top"><h3>环保报告</h3></td>
  </tr>
  <tr>
    <td align="left" valign="top"><h4>环保措施　绿化未来 </h4>
      <p>警队的目标是透过教育及宣传提高员工的环保意识，并鼓励他们参与保护环境的工作。警队与有关机构合作，推广环保管理措施，包括遵 行《清新空气约章 》、有关的环保法例及实务守则。 </p>
      <p><img src="../images/111.jpg" alt="大埔分区警署的天台花园。" width="300" height="160" /></p>
    <p>大埔分区警署的天台花园。</p></td>
  </tr>
  <tr>
    <td align="left" valign="top"><h4>环保管理</h4>
      <p>警队致力通过适当的方法保护环境。由财务、政务及策划处处长担任主席的环保管理督导委员会负责监督和处理节约能源及环保管理事宜，监察範围包括纸张、信封、电力、食水、燃气和燃油的耗用量及废纸收集情况。在各员工同心协力下，信封、燃气、警察车辆燃油和水警船队燃油的耗用量於二零一二年均告减少。</p></td>
  </tr>
  <tr>
    <td align="left" valign="top"><h4>减少消耗</h4>
      <p>年内，警队持续努力减少用纸。各级人员已实行减少用纸的措施，包括以电子邮件通讯、以电子方式代替打印文本发布和储存大量文件及参考资料，以及双面列印等。警队也鼓励总部及总区的单位采取无纸张会议的模式。</p>
    <p>采购物品时，警队在情况许可时尽量考虑相关的环保因素，例如能源效益及循环再造能力。警队采购环保物品包括可再充电电池，不含水银和镉的乾电池，以及再造墨╱碳粉盒。不含木材的纸张及再造纸占总用纸量很高比率。此外，警队鼓励员工，如价格合理，应尽量购买环保产品。</p></td>
  </tr>
  <tr>
    <td align="left" valign="top"><h4>珍惜食水</h4>
    <p>警队遵行政府的全面水资源管理策略，鼓励员工在警察楼宇用地使用节约用水的装置，包括低流量花灑╱设有时间掣的花灑、低流量感应式水龙头、双掣式冲厕水箱及感应式尿厕。警队已在电子环保角发出《节约用水指引》，以加强员工善用食水的意识。</p></td>
  </tr>
  <tr>
    <td align="left" valign="top"><h4>节约能源</h4>
      <p>警队已广泛使用节能灯泡及光管，包括将T8光管及安装在「出口」标誌内的20瓦特光管分别改为更节能的T5光管及5瓦特发光二极管（LED）灯泡。在楼梯、公用走廊及升降机大堂安装附有感应器的低瓦数光管，以提高照明装置的能源效益。</p>
    <p>警政大楼停车场已装设一氧化碳探测仪器，以便调校通风系统的运作。警队会提醒用电量急增的单位采取措施，控制用电量。</p></td>
  </tr>
  <tr>
    <td align="left" valign="top"><h4>提高员工环保意识</h4>
      <p>警队在警察楼宇用地内共设有19 个「环保角」，提供地方让员工分享环保管理的经验和良好做法。此外，警队在内联网设立六个「电子环保角」，提供一个平台，发放环保管理信息，例如实用环保提示。</p>
      <p>绿化对营造环保和优质工作环境是十分重要的。九个警察建築物已设有天台花园，而警政大楼东翼天台、警察总部夏悫花园员工入口处和黄大仙警署报案室则设置绿化隔音墙。</p>
    <p>环保管理概念已纳入各项警队训练课程及活动内。警队定期在训练日向员工简介环保管理事宜，以加强他们的环保意识。</p></td>
  </tr>
  <tr>
    <td align="left" valign="top"><h4>回收物资循环再用</h4>
    <p>警队辖下27个警察楼宇用地已参加由环境保护署举办 的「工商业废物源头分类计划 」。警队已实行废纸、铝罐及胶樽、玻璃樽、光碟╱录像光碟╱数码录像光碟、炭粉盒和食油废物回收计划。</p></td>
  </tr>
  <tr>
    <td align="left" valign="top"><h4>新警察建築物的环保措施</h4>
      <p>新警察楼宇用地注重节约能源及环保，南丫岛新警岗和黄大仙警署新一代报案室均引入绿化元素，提供清新怡人的环境。</p>
    <p>警队争取机会为新建築工程引入环保元素，例如在新油麻地分区警署工程中，建築物的设计善用可再生能源、采用创新建築方法，以及使用具有高循环再用成份的环保建築物料。</p></td>
  </tr>
  <tr>
    <td align="left" valign="top"><h4>参与持份者的活动</h4>
      <p>警队与机电工程署、香港城市大学、应用科技研究院和中华电力有限公司合作，为警队研究及制订节能措施。</p>
    <p>为配合警队的策略行动计划，警队鼓励员工履行社会责任和贡献社会，警队继续推广与救世军合办 的「旧衣回收运动 」，并参加世界自然基金会於叁月叁十一日举办的「地球一小时2012」熄灯活动。</p></td>
  </tr>
  <tr>
    <td align="left" valign="top"><h4>室内空气质素</h4>
      <p>警队参与室内空气质素检定计划，委託机电工程署为警队楼宇用地，定期进行室内空气质素检查。二零一二年，警队辖下十个楼宇用地曾进行室内空气质素检查。</p>
      <p>中区警区总部及分区警署获颁室内空气质素检定證书（卓越级），而七个警队楼宇用地则获颁室内空气质素检定證书（良好级）。</p>
    <p>未来数年，警队会继续选出辖下楼宇用地，以量度室内空气质素及进行相关改善工程。</p></td>
  </tr>
  <tr>
    <td align="left" valign="top"><h4>气候转变带来的挑战</h4>
      <p>为支持政府应付气候转变所带来的挑战，警队已参 加「建築物碳审核计划 」，量度警察楼宇用地的温室气体排放量，并制订节能措施，以减低警队的碳足迹。</p>
      <p>警队继续致力减低燃料耗用量和温室气体排放量。所有警察驾驶训练课程均采用环保驾驶原则，更多警队车辆使用循环再造机油，警队以较洁净的柴油引擎车辆取替汽油引擎车辆，执行巡逻任务。儘管警车使用量有所增加，但警队车辆的燃料总消耗量在二零一二年持续减少。</p>
    <p>水警船队继续致力减少燃料耗用量、温室气体及海洋污染物的排放量。自水警整支船队采用欧盟五期无铅汽油及柴油後，在废气及污染物排放量方面的表现已显著改善。由於新款中型巡逻警轮采用功率与重量比例较高的柴油轮机，所以取得更佳的燃料效益。</p>
    <p><img src="../images/112.jpg" alt="中区警区总部及分区警署" width="300" height="199" /></p>
    <p><img src="../images/113.jpg" alt="中区警区总部及分区警署获颁室内空气质素检定證书（卓越级）。" width="300" height="207" /></p>
    <p>中区警区总部及分区警署获颁室内空气质素检定證书（卓越级）。</p>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top">[ <a href="#top">回页首</a> ]</td>
  </tr>
</table>

<p class="s88"> </p>


</body>
</html>

"""
soup = BeautifulSoup(html_doc, "lxml")
print '---------------------------------'

try:
    con1 = soup.find('div', class_ = 'span9')
    con2 = soup.find('div', id = 'main_content_area')
    if con1:
        all_p = con1.get_text().strip()
    elif con2:
        all_p = con2.get_text().strip()
    else:
        all_p = soup.get_text().strip()
    all_p = all_p.encode('GBK', 'ignore')
    all_p = re.sub(r'\w+\s\w+\s\=\s\w+\s\w+\.\w+\.\w+\(\"\w+\"\)\;', "", all_p)
    all_p = re.sub(r'\w+\.\w+\(\"\w+\"\,\s\"\w+\"\,\s\w+\,\s\w+\)\;', "", all_p)
    all_p = re.sub(r'\w+\s\w+\=\"\w+\-\w+\-\w+\"\s\w+\=\"\W+\"\>', "", all_p)
    all_p = re.sub(r'\n', "", all_p)
    all_p = re.sub(r'\t', "", all_p)
    content = all_p
    print all_p
except:
    print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'

print '---------------------------------'  

# # 打开一个文件
# fo = open("D:\\Workspace\\Python\\Scrapy\\test\\1.txt", "wb+")
# fo.write( all_p);
# fo.close()