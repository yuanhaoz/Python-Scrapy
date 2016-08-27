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

import scrapy
from scrapy.http import Request
from bs4 import BeautifulSoup
from scrapy import signals

html_doc = """

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-HK" lang="zh-cn">

<head>
<meta name="Keywords" content="保安局禁毒處, 香港戒毒治療和康復服務三年計劃, 2015至2017年">
<meta name="description" content="保安局禁毒處 - 香港戒毒治療和康復服務三年計劃（2015至2017年）">
<meta name="description-2" content="Security Bureau, Narcotics Division Website">
<meta name="author" content="Security Bureau, Narcotics Division">
	<script language="JavaScript" src="/js/jquery-1.11.0.min.js" type="text/javascript"></script>
	<link href="/css/print.css" rel="stylesheet" type="text/css" media="print">
	<meta http-equiv="Content-Type" content="text/html;CHARSET=UTF-8">
	<title>保安局禁毒處 - 香港戒毒治療和康復服務三年計劃（2015至2017年）</title>
</head>

<body>
	<h1 style="display:none">Title</h1>
	<table border="0" cellspacing="2" cellpadding="2" width="600" align=center>
		<tr valign=top>
			<td>
				<strong>相 關 文 件</strong>
				<br>
				<br>
			</td>
		</tr>
		<tr valign=top>
			<td>
				<!--------------- Start of Content ----------------->
				<a name="top"></a>
				<table border="0" cellpadding="6" cellspacing="2" width="550">
					<tr>
						<td align="LEFT" colspan="3" valign="TOP">
							<table cellspacing="2" cellpadding="6" width="590" border="0">
								<tr>
									<td colspan="2"><p><strong><span>香 港 戒 毒 治 療 和 康 復 服 務 三 年 計 劃 （ 2015 至 2017 年 ）</span></strong></td>
								</tr>
								<tr>
									<td colspan="2"><p><strong><br><u>目 錄</u></strong></td>
								</tr>
								<tr valign="top">
									<td nowrap>第 一 章</td>
									<td><a href="/pdf/typdtrs_ch1_c.pdf" target="_blank">引 言</a></td>
								</tr>                            
								<tr valign="top">                
									<td>第 二 章</td>            
									<td><a href="/pdf/typdtrs_ch2_c.pdf" target="_blank">戒 毒 治 療 和 康 復 服 務 及 禁 毒 措 施</a></td>
								</tr>                            
								<tr valign="top">                
									<td>第 三 章</td>            
									<td><a href="/pdf/typdtrs_ch3_c.pdf" target="_blank">吸 毒 情 況</a></td>
								</tr>                             
								<tr valign="top">                 
									<td>第 四 章</td>             
									<td><a href="/pdf/typdtrs_ch4_c.pdf" target="_blank">策 略</a></td>
								</tr>
								<tr><td colspan="2">&nbsp;</td></tr>
								<tr valign="top">
									<td colspan="2"><strong><u>附 件</u></strong></td>
								</tr>
								<tr valign="top">
									<td>附 件 一</td>
									<td><a href="/pdf/typdtrs_15_17_annex1_c.pdf" target="_blank">香 港 戒 毒 治 療 和 康 復 服 務 三 年 計 劃 （ 2015 至 2017 年 ） 工 作 小 組 成 員 名 單</a></td>
								</tr>
								<tr valign="top">
									<td>附 件 二</td>
									<td><a href="/pdf/typdtrs_15_17_annex2_c.pdf" target="_blank">工 作 小 組 職 權 範 圍</a></td>
								</tr>
								<tr valign="top">
									<td>附 件 三</td>
									<td><a href="/pdf/typdtrs_15_17_annex3_c.pdf" target="_blank">禁 毒 基 金 核 准 計 劃（ 2012 - 2014 ）</a></td>
								</tr>
							</table>
							<table> 
								<tr valign="top">
									<td>&nbsp;</td>
								</tr>
								<tr valign="top">
									<td nowrap>( 請 按 <a href="/pdf/typdtrs_full_c.pdf" target="_blank">此 處</a> 下 載 整 份 報 告 )</td>
								</tr>
								<tr valign="top">
									<td>( 備 註 ： 請 用 Acrobat Reader 7.0 或 以 上 來 檢 視 文 件 )
									</td>
								</tr>
							</table>  

						</td>
					</tr>
				</table>
				<!---------------- End of Content ------------------>
				<tr valign=top>
					<td align=center nowrap>
						<!-- <p><br><br>
		~ <a style="color:#000000;" href="../new/index.htm">最新消息</a> ~ 
		<a style="color:#000000;" href="../aboutus/index.htm">保安局禁毒處</a> ~ 
		<a style="color:#000000;" href="../agenda/index.htm">禁毒常務委員會及轄下小組委員會</a> ~ 
		<a style="color:#000000;" href="../dlc/index.htm">毒品問題聯絡委員會</a> ~ <br> ~ 
		<a style="color:#000000;" href="../research/rag.htm">研究諮詢小組</a> ~ 
		<a style="color:#000000;" href="../report/index.htm">香港禁毒及反洗黑錢報告書</a> ~
		<a style="color:#000000;" href="../press/index.htm">新聞公報</a> ~ 
		<a style="color:#000000;" href="../strategy/index.htm">禁毒策略</a> ~  <br>~ 
		<a style="color:#000000;" href="../prevent/index.htm">禁毒教育和宣傳</a> ~ 
		<a style="color:#000000;" href="../law/index.htm">禁毒法例和執法工作</a> ~ 
		<a style="color:#000000;" href="../treat/index.htm">戒毒治療和康復服務</a> ~ 
		<a style="color:#000000;" href="../external/index.htm">對外合作</a> ~ 
		<a style="color:#000000;" href="../research/index.htm">研究工作</a> ~ <br>~ 
		<a style="color:#000000;" href="../treat/services_psa.htm">為吸食危害精神毒品人士提供的服務</a> ~ 
		<a style="color:#000000;" href="../treat/services_ha.htm">為吸食海洛英人士提供的服務</a> ~ 
		<a style="color:#000000;" href="../treat/services_sp.htm">為被判刑人士提供的服務</a> ~ <br>~ 
		<a style="color:#000000;" href="../treat/relevant_docs.htm">相關文件</a> ~ 
		<a style="color:#000000;" href="../treat/list_tr_services.htm">提供戒毒治療及康復服務機構一覽表</a> ~
		<a style="color:#000000;" href="../info/index.htm">毒品資料</a> ~ 
		<a style="color:#000000;" href="../public/index.htm">禁毒刊物</a> ~ <br>~ 
		<a style="color:#000000;" href="../resources/videos_radio_clips.htm">禁毒影音短片</a> ~ 
		<a style="color:#000000;" href="../resources/resources_parents.htm">給家長的禁毒資源</a> ~ 
		<a style="color:#000000;" href="../resources/resources_teachers.htm">給教師和社工的禁毒資源</a> ~ 
		<a style="color:#000000;" href="../resources/resources_youths.htm">給青年人的禁毒資源</a> ~ <br>~ 
		<a style="color:#000000;" href="../druginfocentre/index.htm">香港賽馬會藥物資訊天地</a> ~ 
		<a style="color:#000000;" href="../stat/index.htm">藥物濫用資料中央檔案室及毒品統計數字</a> ~ 
		<a style="color:#000000;" href="../beat/index.htm">禁毒基金</a> ~ 
		<a style="color:#000000;" href="../prevent/antidrug_volunteer.htm">禁毒義工團</a> ~ <br>~ 
		<a style="color:#000000;" href="../moneylaundering/index.htm">打擊洗清黑錢及恐怖分子融資活動</a> ~ 
		<a style="color:#000000;" href="../useful/index.htm">相關網址</a> ~ 
						</p> -->
						<p><a style="color:#000000;" href="../index.htm">主 頁</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a style="color:#000000;" href="../../en/treat/three_year_plan_2015_2017.htm">English</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a style="color:#000000;" href="../../sc/treat/three_year_plan_2015_2017.htm">簡 體</a>
					</td>
				</tr>
	</table>
</body>

</html>


"""


soup = BeautifulSoup(html_doc, "lxml-xml")

# print '---------------------------------'
# all_p = soup.find_all('table')[1].find_all('td')[1].find_all('tr')[1].get_text().strip()
# all_p = all_p.replace('0 cellpadding=0 cellspacing=0>', '')
# all_p = all_p.replace('footer();', '')
# all_p = all_p.replace('left valign=top width="50">', '')
# all_p = all_p.replace('left valign=top>', '')
# all_p = all_p.replace('border="0">', '')
# all_p = all_p.replace('250>', '')
# all_p = all_p.replace('\n', '')
# all_p = all_p.replace('\t', '')
# print all_p
# print '---------------------------------'

# all_p = soup.find_all('table')[1].find_all('td')[1].find_all('p')
# titles = soup.find_all('h1')
# title = ''
# content = ''
# for i in range(1, len(titles)):
    # title += titles[i].get_text().strip()
# for i in range(0, len(all_p)-1):
    # content += all_p[i].get_text().strip()
    # content = content.replace('\n', '')
    # content = content.replace('\t', '')
# content = title + '\n' + content
# print content
# print '---------------------------------'

# all_p = soup.find_all('table')[1].find_all('td')[1].find_all('p')
# all_p = soup.find_all('table')[0].find_all('td')[1]
# titles = soup.find_all('h1')
# title = ''
# content = ''
# for i in range(1, len(titles)):
    # title += titles[i].get_text().strip()

# if all_p:
    # ex1 = all_p.find_all(['p','h2','h3','h4','strong','a'])
    # for i in range(0, len(ex1)-1):
        # content += ex1[i].get_text().strip()
        # content = content.replace('\n', '')
        # content = content.replace('\t', '')


# content = title + '\n' + content
# print content
print '---------------------------------'

# all_p = soup.find_all('td', colspan = re.compile("[1-9]"))
all_p = soup.find_all('table')
content = ''
for p in all_p:
    t = p.get_text().strip()
    content += t

print content
print '---------------------------------'  
# all_p = soup.find_all('td', colspan = '4')[1].get_text().strip()
# print all_p

