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

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html lang="zh-cn">
 <head> 
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"> 
  <meta content="text/html; charset=utf-8" http-equiv="Content-Type" /> 
  <title>从 优 质 教 育 基 金 中 拨 出 2 亿 元 来 资 助 公 营 中 学 购 置 手 提 式 电 脑 事 宜</title> 
  <meta name="keywords" content="从 优 质 教 育 基 金 中 拨 出 2 亿 元 来 资 助 公 营 中 学 购 置 手 提 式 电 脑 事 宜"> 
  <meta name="description" content="从 优 质 教 育 基 金 中 拨 出 2 亿 元 来 资 助 公 营 中 学 购 置 手 提 式 电 脑 事 宜"> 
  <link type="image/x-icon" href="/sc/favicon.ico" rel="icon"> 
  <link type="image/x-icon" href="/sc/favicon.ico" rel="shortcut icon"> 
  <link media="print" type="text/css" rel="stylesheet" href="/sc/css/print.css"> 
  <link type="text/css" rel="stylesheet" href="/sc/css/plugin.css"> 
  <link media="all" type="text/css" rel="stylesheet" href="/sc/css/style.css"> 
  <link media="all" type="text/css" rel="stylesheet" href="/sc/css/content_final_style.css"> 
  <script src="/sc/js/jquery.js" type="text/javascript"></script>
  <script src="/sc/js/jquery.bxSlider.js" type="text/javascript"></script>
  <script src="/sc/js/jquery.marquee.js" type="text/javascript"></script>
  <script src="/sc/js/common.js" type="text/javascript"></script>
  <script type="text/javascript" src="/sc/js/init.js"></script> 
 </head> 
 <body class=""> 
  <div id="allTop"></div> 
  <div id="wrapper"> 
   <a id="skiptocontent" name="skiptocontent" href="#archorcontent" class="access">跳到主要内容</a>
<a id="skiptosearch" name="skiptosearch" href="#anchorsearch" class="access">跳至搜寻</a>
<div id="header" class="c">
	<a id="btn-logo" href='/index.html'><img alt="教育局" title="教育局" src='/sc/images/edb_logo.gif' width="429" height="65"></a>
	<a id="btn-brand" href='http://www.brandhk.gov.hk/' rel="external"><img alt='香港品牌形象 - 亚洲国际都会' title='香港品牌形象 - 亚洲国际都会' src='/sc/images/brandhk.gif'></a>
	<span class="access">search</span><a id="anchorsearch" name="anchorsearch"></a>
	<div id="feature-bar">
		<div id="languages-panel" class="l">
			<a class='language-chooser' style="width: 171px;" href='http://www.gov.hk/sc/residents/' onmouseout='MM_swapImgRestore()' onblur='MM_swapImgRestore()' onmouseover='MM_swapImage("mainbar1e","","/sc/images/govhk_rollover.gif",1)' onfocus='MM_swapImage("mainbar1e","","/sc/images/govhk_rollover.gif",1)'><img id='mainbar1e' alt='GovHK香港政府一站通' title='GovHK香港政府一站通' src='/sc/images/govhk.gif'></a>
			<a class='language-chooser' style="width: 51px;" href='javascript:switchLanguage("tc");' onmouseout='MM_swapImgRestore()' onblur='MM_swapImgRestore()' onmouseover='MM_swapImage("mainbar3","","/sc/images/tc_rollover.gif",1)' onfocus='MM_swapImage("mainbar3","","/sc/images/tc_rollover.gif",1)'><img id='mainbar3' alt='繁體版' title='繁體版' src='/sc/images/tc.gif'></a>
			<a class='language-chooser' style="width: 56px;" href='javascript:switchLanguage("en");' onmouseout='MM_swapImgRestore()' onblur='MM_swapImgRestore()' onmouseover='MM_swapImage("mainbar4","","/sc/images/en_rollover.gif",1)' onfocus='MM_swapImage("mainbar4","","/sc/images/en_rollover.gif",1)'><img id='mainbar4' alt='英文版' title='英文版' src='/sc/images/en.gif'></a>
			<div class='language-chooser' style="width: 21px;">
				<img alt="" src='/sc/images/mainbar6.gif'>
			</div>
		</div>
		<a id="btn-mobile-version" class="l" href="#">流动／无障碍浏览版本</a>
		<div id="my-color-container" class="l">	
			<a id="btn-my-color" class="l" href='#'>我的自订色彩</a>
			<div id="my-color">
				<ul>
					<li><a class="btn_theme_none" href="javascript:;" onclick="changeTheme('none')">No theme</a></li>
					<li><a class="btn_theme_color1" href="javascript:;" onclick="changeTheme('color1')">Color1 theme</a></li>
					<li><a class="btn_theme_color2" href="javascript:;" onclick="changeTheme('color2')">Color2 theme</a></li>
					<li><a class="btn_theme_color3" href="javascript:;" onclick="changeTheme('color3')">Color3 theme</a></li>
				</ul>
			</div>
		</div>
		<div id='font-size-chooser' class="l">
			<a class='l btn-change-font-size' href='javascript:changeFontSize(0)' title="字型大小：原设定" id="btn-fs-0" style="font-size: 12px; padding-top: 7px;">A</a>
			<a class='l btn-change-font-size' href='javascript:changeFontSize(1)' title="字型大小：较大" id="btn-fs-1" style="font-size: 16px; padding-top: 4px;">A</a>
			<a class='l btn-change-font-size' href='javascript:changeFontSize(2)' title="字型大小：最大" id="btn-fs-2" style="font-size: 20px;">A</a>
		</div>
		
		<form name="search_form" id="frm-search" method="get" action="http://search.gov.hk/search.html" class="l" onsubmit="SimpleSearch()">
			<div>
			<input type=hidden name=ui_lang value="zh-cn">
			<input type=hidden name=ui_charset value="utf-8">
			<input type=hidden name=gp0 value="edb_r2_home">
			<input type=hidden name=gp1 value="edb_r2_home">
			<input type=hidden name=tpl_id value="edb_r2">
			<input type=hidden name=web value="this">
			<input id="txt-search" class="txt-search l" name='query' value='输入查询字串' size='22' type='text' title="搜寻">
			<a class="btn-search l" href='#' onclick="SimpleSearch()" onmouseout='MM_swapImgRestore()' onblur='MM_swapImgRestore()' onmouseover='MM_swapImage("mainbar8","","/sc/images/search_icon_rollover.gif",1)' onfocus='MM_swapImage("mainbar8","","/sc/images/search_icon_rollover.gif",1)'><img id='mainbar8' alt='提交搜寻内容' title='提交搜寻内容' src='/sc/images/search_icon.gif'></a>
			</div>
		</form>
		
		<a id="btn-site-map" class="l" href='/sc/site_map.html' onmouseout='MM_swapImgRestore()' onblur='MM_swapImgRestore()' onmouseover='MM_swapImage("mainbar9e","","/sc/images/sitemap_rollover.gif",1)' onfocus='MM_swapImage("mainbar9e","","/sc/images/sitemap_rollover.gif",1)'><img id='mainbar9e' alt='网页指南' title='网页指南' src='/sc/images/sitemap.gif'></a>
		<a id="btn-contact-us" class="l" href='http://www.edb.gov.hk/sc/contact-us/index.html' onmouseout='MM_swapImgRestore()' onblur='MM_swapImgRestore()' onmouseover='MM_swapImage("mainbar10","","/sc/images/email_rollover.gif",1)' onfocus='MM_swapImage("mainbar10","","/sc/images/email_rollover.gif",1)'><img id='mainbar10' alt='联络我们' title='联络我们' src='/sc/images/email.gif'></a>
	</div>
</div><!--/header--> 
   <div id="content_wrapper"> 
    <div id="content_left_container">
	<h2 class="access">次要选单</h2>
	<div id="nav_container">
<ul>
<li class="nav_first">
<a href="/sc/index.html" title="主页">主页</a>
</li>
<li>
<a href="/sc/news/all.html" title="最新消息">最新消息</a>
</li>
<li>
<a href="/sc/about-edb/list-page.html" title="有关教育局">有关教育局</a>
</li>
<li>
<a href="/sc/edu-system/list-page.html" title="教育制度及政策">教育制度及政策</a>
</li>
<li>
<a href="/sc/curriculum-development/list-page.html" title="课程发展">课程发展</a>
</li>
<li>
<a href="/sc/student-parents/list-page.html" title="学生及家长相关">学生及家长相关</a>
</li>
<li>
<a href="/sc/teacher/list-page.html" title="教师相关">教师相关</a>
</li>
<li>
<a href="/sc/sch-admin/list-page.html" title="学校行政及管理">学校行政及管理</a>
</li>
<li>
<a href="/sc/public-admin/list-page.html" title="公共及行政相关">公共及行政相关</a>
</li>
<li>
<a href="/sc/access-to-info/list-page.html" title="公开资料">公开资料</a>
</li>
<li class="nav_last">
<a href="/sc/contact-us/list-page.html" title="联络我们">联络我们</a>
</li>
</ul>
</div>

	<div id="navBanner">
<h2 class="access">推荐选单</h2>
<div id="bannerTop"></div>
<div id="bannerContent">
<ul id="slider2">
<li>
<a onclick="target='_blank'" href="http://www.edb.gov.hk/sc/about-edb/press/insiderperspective/index.html"><img height="45" width="180" alt="局中人语" title="局中人语" src="/sc/images/ledbicon07.jpg"></a><a onclick="target='_blank'" href="http://www.edb.gov.hk/sc/student-parents/sch-info/about-sch-info/index.html"><img height="45" width="180" alt="学校资料" title="学校资料" src="/sc/images/ledbicon01.gif"></a><a onclick="target='_blank'" href="http://www.ceo.gov.hk/report-yearfour/sim/index.html" class="alpha"><img height="45" width="80" alt="本届政府上任第四年施政汇报" title="本届政府上任第四年施政汇报" src="/sc/images/sedbicon106.gif"></a><a onclick="target='_blank'" href="http://www.edb.gov.hk/sc/about-edb/press/legco/index.html"><img height="45" width="80" alt="2016年施政报告教育局的政策措施" title="2016年施政报告教育局的政策措施" src="/sc/images/sedbicon58.jpg"></a><a onclick="target='_blank'" href="http://334.edb.hkedcity.net/index.php" class="alpha"><img height="45" width="80" alt="新学制网上简报" title="新学制网上简报" src="/sc/images/sedbicon11.gif"></a><a onclick="target='_blank'" href="http://www.policyaddress.gov.hk/2015/sim/index.html"><img height="45" width="80" alt="2016 施政报告" title="2016 施政报告" src="/sc/images/sedbicon101.gif"></a><a onclick="target='_blank'" href="http://www.edb.gov.hk/sc/curriculum-development/resource-support/textbook-info/index.html" class="alpha"><img height="45" width="80" alt="教科书资讯" title="教科书资讯" src="/sc/images/sedbicon04.jpg"></a><a onclick="target='_blank'" href="http://www.edb.gov.hk/sc/curriculum-development/resource-support/textbook-info/emads/index.html"><img height="45" width="80" alt="电子教科书市场开拓计画" title="电子教科书市场开拓计画" src="/sc/images/sedbicon05.jpg"></a><a onclick="target='_blank'" href="https://data.gov.hk/sc" class="alpha"><img height="45" width="80" alt="资料一线通" title="资料一线通" src="/sc/images/sedbicon79.jpg"></a><a onclick="target='_blank'" href="http://www.edb.gov.hk/sc/contact-us/hotline.html"><img height="45" width="80" alt="教育局热线:2891 0088 及其他查询电话" title="教育局热线:2891 0088 及其他查询电话" src="/sc/images/sedbicon02.jpg"></a>
</li>
<li>
<a onclick="target='_blank'" href="http://www.edb.gov.hk/sc/about-edb/press/insiderperspective/index.html"><img height="45" width="180" alt="局中人语" title="局中人语" src="/sc/images/ledbicon07.jpg"></a><a onclick="target='_blank'" href="http://www.edb.gov.hk/sc/student-parents/sch-info/about-sch-info/index.html"><img height="45" width="180" alt="学校资料" title="学校资料" src="/sc/images/ledbicon01.gif"></a><a onclick="target='_blank'" href="http://www.ipass.gov.hk/edb/index.php/ch/" class="alpha"><img height="45" width="80" alt="经评审专上课程资料网" title="经评审专上课程资料网" src="/sc/images/sedbicon31.jpg"></a><a onclick="target='_blank'" href="http://www.edb.gov.hk/sc/edu-system/preprimary-kindergarten/preprimary-voucher/index.html"><img height="45" width="80" alt="幼稚园教育新里程" title="幼稚园教育新里程" src="/sc/images/sedbicon09.jpg"></a><a onclick="target='_blank'" href="http://www.edb.gov.hk/sc/edu-system/preprimary-kindergarten/kindergarten-k1-admission-arrangements/front.html" class="alpha"><img height="45" width="80" alt="幼稚园幼儿班(K1)收生安排" title="幼稚园幼儿班(K1)收生安排" src="/sc/images/sedbicon63.jpg"></a><a onclick="target='_blank'" href="http://www.hkqf.gov.hk/guig/home.asp"><img height="45" width="80" alt="资历架构" title="资历架构" src="/sc/images/sedbicon32.jpg"></a><a onclick="target='_blank'" href="http://www.edb.gov.hk/sc/student-parents/support-subsidies/community-care-fund-assistance-programme/index.html" class="alpha"><img height="45" width="80" alt="关爱基金" title="关爱基金" src="/sc/images/sedbicon07.jpg"></a><a onclick="target='_blank'" href="http://www.edb.gov.hk/sc/curriculum-development/tsa/index.html"><img height="45" width="80" alt="促进学习的评估" title="促进学习的评估" src="/sc/images/sedbicon102.jpg"></a><a onclick="target='_blank'" href="http://www.edb.gov.hk/sc/teacher/student-guidance-discipline-services/gd-resources/index.html" class="alpha"><img height="45" width="80" alt="提升生命成长韧力小锦囊" title="提升生命成长韧力小锦囊" src="/sc/images/sedbicon103.jpg"></a><a onclick="target='_blank'" href="http://www.edb.gov.hk/sc/student-parents/parents-related/ebulletin-for-parents/index.html"><img height="45" width="80" alt="家长电子专递" title="家长电子专递" src="/sc/images/sedbicon06.jpg"></a>
</li>
<li>
<a onclick="target='_blank'" href="http://www.edb.gov.hk/sc/about-edb/press/insiderperspective/index.html"><img height="45" width="180" alt="局中人语" title="局中人语" src="/sc/images/ledbicon07.jpg"></a><a onclick="target='_blank'" href="http://www.edb.gov.hk/tc/student-parents/sch-info/about-sch-info/index.html"><img height="45" width="180" alt="学校资料" title="学校资料" src="/sc/images/ledbicon01.gif"></a><a onclick="target='_blank'" href="http://www.ate.gov.hk/schinese/index.html" class="alpha"><img height="45" width="80" alt="行政长官卓越教学奖（2016/2017）" title="行政长官卓越教学奖（2016/2017）" src="/sc/images/sedbicon24.gif"></a><a onclick="target='_blank'" href="http://www.edb.gov.hk/sc/teacher/teacher-helpline/about-teacher-helpline/index.html"><img height="45" width="80" alt="教师阳光专线" title="教师阳光专线" src="/sc/images/sedbicon13.png"></a><a onclick="target='_blank'" href="http://www.hkedcity.net/edbosp/" class="alpha"><img height="45" width="80" alt="教育局一站式学与教资源平台" title="教育局一站式学与教资源平台" src="/sc/images/sedbicon35.jpg"></a><a onclick="target='_blank'" href="http://www.edb.gov.hk/sc/teacher/qualification-training-development/training/scholarship-for-eng-teacher/index.html"><img height="45" width="80" alt="准英语教师奖学金" title="准英语教师奖学金" src="/sc/images/sedbicon14.jpg"></a><a onclick="target='_blank'" href="http://cotap.hk/index.php/cn/cpd-programmes/pdip-sc" class="alpha"><img height="45" width="80" alt="教师专业发展资讯平台" title="教师专业发展资讯平台" src="/sc/images/sedbicon81.gif"></a><a onclick="target='_blank'" href="http://sc.devb.gov.hk/TuniS/www.greening.gov.hk/tc/home/index.html"><img height="45" width="80" alt="树木园境地图" title="树木园境地图" src="/sc/images/sedbicon40.jpg"></a><a onclick="target='_blank'" href="http://www.edb.gov.hk/sc/edu-system/postsecondary/policy-doc/hkses/index.html" class="alpha"><img height="45" width="80" alt="香港卓越奖学金计划	" title="香港卓越奖学金计划	" src="/sc/images/sedbicon91.jpg"></a><a onclick="target='_blank'" href="http://www.hkedcity.net/"><img height="45" width="80" alt="香港教育城" title="香港教育城" src="/sc/images/sedbicon36.jpg"></a>
</li>
<li>
<a onclick="target='_blank'" href="http://www.edb.gov.hk/sc/about-edb/press/insiderperspective/index.html"><img height="45" width="180" alt="局中人语" title="局中人语" src="/sc/images/ledbicon07.jpg"></a><a onclick="target='_blank'" href="http://www.edb.gov.hk/tc/student-parents/sch-info/about-sch-info/index.html"><img height="45" width="180" alt="学校资料" title="学校资料" src="/sc/images/ledbicon01.gif"></a><a onclick="target='_blank'" href="http://www.edb.gov.hk/sc/sch-admin/sbm/about-sbm/index.html" class="alpha"><img height="45" width="80" alt="校本管理" title="校本管理" src="/sc/images/sedbicon17.jpg"></a><a onclick="target='_blank'" href="http://www.edb.gov.hk/sc/student-parents/ncs-students/about-ncs-students/index.html"><img height="45" width="80" alt="非华语学童教育服务" title="非华语学童教育服务" src="/sc/images/sedbicon59.jpg"></a><a onclick="target='_blank'" href="https://e-link.wfsfaa.gov.hk/EBILLPRD/jsp_public/ens/ens0101.jsp?language=zh_TW" class="alpha"><img height="45" width="80" alt="学资处电子通" title="学资处电子通" src="/sc/images/sedbicon68.jpg"></a><a onclick="target='_blank'" href="http://www.lwb.gov.hk/charter_scheme/index_s.html"><img height="45" width="80" alt="有能者‧聘之约章" title="有能者‧聘之约章" src="/sc/images/sedbicon85.jpg"></a><a onclick="target='_blank'" href="http://twdc.police.gov.hk/ppp_sc/11_useful_info/scrc.html" class="alpha"><img height="45" width="80" alt="性罪行定罪紀錄查核" title="性罪行定罪紀錄查核" src="/sc/images/sedbicon26.gif"></a><a onclick="target='_blank'" href="http://edb.hkedcity.net/internationalschools/index.php?lang=sc"><img height="45" width="80" alt="香港的国际学校 / 搜寻国际学校" title="香港的国际学校 / 搜寻国际学校" src="/sc/images/sedbicon84.gif"></a><a onclick="target='_blank'" href="http://sc.youth.gov.hk/TuniS/www.youth.gov.hk/tc/index.htm" class="alpha"><img height="45" width="80" alt="Youth.gov.hk" title="Youth.gov.hk" src="/sc/images/sedbicon23.jpg"></a><a onclick="target='_blank'" href="http://www.edb.gov.hk/sc/about-edb/info/about-info/accessibility-premises-edb.html"><img height="45" width="80" alt="教育局处所的无障碍事宜" title="教育局处所的无障碍事宜" src="/sc/images/sedbicon18.jpg"></a>
</li>
<li>
<a onclick="target='_blank'" href="http://www.edb.gov.hk/sc/about-edb/press/insiderperspective/index.html"><img height="45" width="180" alt="局中人语" title="局中人语" src="/sc/images/ledbicon07.jpg"></a><a onclick="target='_blank'" href="http://www.edb.gov.hk/tc/student-parents/sch-info/about-sch-info/index.html"><img height="45" width="180" alt="学校资料" title="学校资料" src="/sc/images/ledbicon01.gif"></a><a onclick="target='_blank'" href="http://www.edb.gov.hk/sc/edu-system/primary-secondary/healthy-sch-policy/index.html" class="alpha"><img height="45" width="80" alt="健康校园政策" title="健康校园政策" src="/sc/images/sedbicon12.jpg"></a><a onclick="target='_blank'" href="http://www.edb.gov.hk/sc/about-edb/press/cleartheair/index.html"><img height="45" width="80" alt="政策正面睇" title="政策正面睇" src="/sc/images/sedbicon21.jpg"></a><a onclick="target='_blank'" href="http://www.edb.gov.hk/sc/sch-admin/admin/about-sch/diseases-prevention/index.html" class="alpha"><img height="45" width="80" alt="预防传染病在学校传播" title="预防传染病在学校传播" src="/sc/images/sedbicon08.jpg"></a><a onclick="target='_blank'" href="http://www.edb.gov.hk/sc/curriculum-development/major-level-of-edu/life-wide-learning/jc-fund/index.html"><img height="45" width="80" alt="香港赛马会全方位学习基金" title="香港赛马会全方位学习基金" src="/sc/images/sedbicon15.jpg"></a><a onclick="target='_blank'" href="http://www.edb.gov.hk/sc/sch-admin/admin/about-sch-staff/statutory-minimum-wage/index.html" class="alpha"><img height="45" width="80" alt="法定最低工资" title="法定最低工资" src="/sc/images/sedbicon39.jpg"></a><a onclick="target='_blank'" href="http://sc.1823.gov.hk/TuniS/www.1823.gov.hk/big5/cp-home.aspx"><img height="45" width="80" alt="1823 Online" title="1823 Online" src="/sc/images/sedbicon28.jpg"></a><a onclick="target='_blank'" href="http://sc.news.gov.hk/TuniS/" class="alpha"><img height="45" width="80" alt="香港政府新闻网" title="香港政府新闻网" src="/sc/images/sedbicon27.jpg"></a><a onclick="target='_blank'" href="http://www.edb.gov.hk/sc/contact-us/opening-hour.html"><img height="45" width="80" alt="5天工作周" title="5天工作周" src="/sc/images/sedbicon19.jpg"></a>
</li>
<li>
<a onclick="target='_blank'" href="http://www.edb.gov.hk/sc/about-edb/press/insiderperspective/index.html"><img height="45" width="180" alt="局中人语" title="局中人语" src="/sc/images/ledbicon07.jpg"></a><a onclick="target='_blank'" href="http://www.edb.gov.hk/sc/student-parents/sch-info/about-sch-info/index.html"><img height="45" width="180" alt="学校资料" title="学校资料" src="/sc/images/ledbicon01.gif"></a><a onclick="target='_blank'" href="http://www.hkourhome.gov.hk/sim/index.shtml" class="alpha"><img height="45" width="80" alt="全城清洁2015@家是香港 " title="全城清洁2015@家是香港 " src="/sc/images/sedbicon87.jpg"></a><a onclick="target='_blank'" href="http://www.isd.gov.hk/drinkingwater/sim/index.html"><img height="45" width="80" alt="食水含铅事件" title="食水含铅事件" src="/sc/images/sedbicon86.jpg"></a><a onclick="target='_blank'" href="http://www.elections.gov.hk/legco2016/sim/index.html# " class="alpha"><img height="45" width="80" alt="2016立法会选举" title="2016立法会选举" src="/sc/images/sedbicon105.gif"></a><a onclick="target='_blank'" href="http://www.hongkonggames.hk"><img height="45" width="80" alt="第六届全港运动会" title="第六届全港运动会" src="/sc/images/sedbicon104.gif"></a><a onclick="target='_blank'" href="http://www.mcor.swd.gov.hk/sc/activities/whatsnew.htm" class="alpha"><img height="45" width="80" alt="创业轩" title="创业轩" src="/sc/images/sedbicon43.gif"></a><a onclick="target='_blank'" href="http://www.edb.gov.hk/sc/edu-system/special/overview/newsletter/index.html"><img height="45" width="80" alt="融情 - 融合教育通讯" title="融情 - 融合教育通讯" src="/sc/images/sedbicon95.png"></a><a onclick="target='_blank'" href="http://www.gov.hk/sc/theme/mygovhk/" class="alpha"><img height="45" width="80" alt="欢迎使用我的政府一站通" title="欢迎使用我的政府一站通" src="/sc/images/sedbicon22.gif"></a><a onclick="target='_blank'" href="http://sc.icac.org.hk/TuniS/www.icac.org.hk/icac/elect/2016lc/tc/index.html"><img height="45" width="80" alt="维护廉洁立法会选举" title="维护廉洁立法会选举" src="/sc/images/sedbicon83.gif"></a>
</li>
</ul>
</div>
<div id="bannerBottom"></div>
</div><div id="nav2"><div><a href="http://www.youtube.com/user/edbgovhk"><img src="/sc/images/EDB_youtube_channel.jpg" alt="EDB YouTube Channel" title="EDB YouTube Channel" height="42" width="200" /></a></div></div>

</div> 
    <div id="content_right_container"> 
     <div class="cb mt" id="banner-content-top"> 
      <img src="/sc/images/seasonal_theme.jpg" alt="" />
     </div> 
     <div class="clear"></div> 
     <div class="clear"></div> 
     <div id="breadcrumb" class="l"><a href="/sc/index.html">主页</a> > <a href="/sc/about-edb/list-page.html">有关教育局</a> > <a href="/sc/about-edb/list-page.html">新闻公报</a> > <a href="/sc/about-edb/press/legco/index.html">立法会事项</a> > <a href="/sc/about-edb/press/legco/replies-written/index.html">答覆书面问题</a> > <a href="/sc/about-edb/press/legco/replies-written/index.html">答覆书面问题</a></div> 
     <a class="r" href="javascript:window.print()" id="btn-print"><img src="/sc/images/btn_print.jpg" title="列印本文" alt="列印本文" /></a> 
     <div class="clear"></div> 
     <div id="content"> 
      <a name="archorcontent" id="archorcontent"></a> 
      <div id="intro-header"> 
       <div id="header_left"> 
        <h1>从 优 质 教 育 基 金 中 拨 出 2 亿 元 来 资 助 公 营 中 学 购 置 手 提 式 电 脑 事 宜</h1> 
       </div> 
      </div> 
      <div class="clear"></div>
      <center>
       <b>立 法 会 问 题 第 4 题（ 书 面 答 复 ）</b>
      </center>
      <br /> 
      <br />
      <br /> 
      <div align="right">
        会 议 日 期 ： 二 零 零 零 年 十 一 月 一 日 
      </div> 
      <p><br /> <br /> <b> 提 问 者 </b> : 杨 耀 忠 议 员 <br /> <br /> <b> 作 答 者 </b> : 教 育 统 筹 局 局 长 <br /> <br /> <b> 问 题 </b> : <br /> <br /> 行 政 长 官 于 《 二 零 零 零 年 施 政 报 告 》 中 表 示 ， 会 从 优 质 教 育 基 金 中 拨 出 2 亿 元 来 资 助 公 营 中 学 购 置 手 提 式 电 脑 ， 借 予 家 境 清 贫 的 学 生 使 用 。 就 此 ， 政 府 可 否 告 知 本 会 ∶ </p> 
      <table border="0" cellpadding="2" cellspacing="0"> 
       <tbody>
        <tr> 
         <td align="left" valign="top" width="43">( 一 )</td> 
         <td align="left" valign="top" width="549"> 当 局 以 何 准 则 制 订 该 拨 款 金 额 ； </td> 
        </tr> 
        <tr> 
         <td colspan="2"><br /> </td> 
        </tr> 
        <tr> 
         <td align="left" valign="top" width="43">( 二 )</td> 
         <td align="left" valign="top" width="549"> 当 局 将 如 何 分 配 该 项 拨 款 予 各 公 营 中 学 ； </td> 
        </tr> 
        <tr> 
         <td colspan="2"><br /> </td> 
        </tr> 
        <tr> 
         <td align="left" valign="top" width="43">( 三 )</td> 
         <td align="left" valign="top" width="549"> 估 计 受 惠 于 该 计 划 的 学 生 人 数 为 何 ； </td> 
        </tr> 
        <tr> 
         <td colspan="2"><br /> </td> 
        </tr> 
        <tr> 
         <td align="left" valign="top" width="43">( 四 )</td> 
         <td align="left" valign="top" width="549"> 当 局 是 否 已 制 定 该 批 手 提 电 脑 的 规 格 ； 若 然 ， 详 情 为 何 ； 及 </td> 
        </tr> 
        <tr> 
         <td colspan="2"><br /> </td> 
        </tr> 
        <tr> 
         <td align="left" valign="top" width="43">( 五 )</td> 
         <td align="left" valign="top" width="549"> 哪 一 方 负 责 维 修 这 些 电 脑 ， 以 及 支 付 维 修 费 用 ？ </td> 
        </tr> 
        <tr> 
         <td colspan="2"><br /> </td> 
        </tr> 
       </tbody>
      </table> 
      <p> </p>
      <p> 答 复 ： <br /><br /> 主 席 女 士 : </p> 
      <table border="0" cellspacing="0" cellpadding="2"> 
       <tbody>
        <tr> 
         <td width="100" align="left" valign="top">( 一 ) 、 ( 三 ) 及 ( 五 )</td> 
         <td width="492"> <p> 计 划 的 主 要 受 惠 者 是 那 些 来 自 低 收 入 家 庭 ， 而 又 没 有 能 力 购 置 电 脑 于 家 中 使 用 的 学 生 。 我 们 估 计 ， 约 有 4 万 名 目 前 正 在 接 受 学 生 资 助 办 事 处 辖 下 各 资 助 计 划 全 额 资 助 ， 又 或 是 来 自 领 取 综 合 社 会 保 障 援 助 ( 以 下 简 称 &quot; 综 援 &quot;) 家 庭 的 中 学 生 可 以 受 惠 。 <br /><br /> 假 设 每 两 名 学 生 共 用 一 部 手 提 电 脑 ， 所 需 的 手 提 电 脑 约 为 两 万 部 。 我 们 估 计 ， 购 置 手 提 电 脑 、 日 后 的 电 脑 维 修 ， 以 及 为 存 放 电 脑 而 安 排 的 保 安 设 施 ， 所 需 费 用 约 为 2 亿 元 。 电 脑 供 应 商 会 负 责 维 修 这 些 电 脑 。 优 质 教 育 基 金 已 原 则 上 同 意 资 助 这 项 计 划 。 若 计 划 受 欢 迎 及 需 求 超 出 我 们 预 计 ， 我 们 可 能 考 虑 向 优 质 教 育 基 金 要 求 增 加 拨 款 。 </p> </td> 
        </tr> 
        <tr> 
         <td width="100" align="left" valign="top">&nbsp;</td> 
         <td width="492">&nbsp;</td> 
        </tr> 
        <tr> 
         <td width="100" align="left" valign="top">( 二 ) </td> 
         <td width="492"> <p> 优 质 教 育 基 金 会 应 申 请 向 学 校 拨 款 。 为 方 便 处 理 拨 款 申 请 ， 学 校 议 会 会 负 责 统 筹 并 向 优 质 教 育 基 金 递 交 一 份 综 合 申 请 。 个 别 学 校 可 得 的 资 助 额 ， 将 按 该 校 有 多 少 名 学 生 领 取 学 生 资 助 办 事 处 辖 下 各 资 助 计 划 的 全 额 资 助 ， 或 是 来 自 领 取 综 援 的 家 庭 而 定 。 </p> </td> 
        </tr> 
        <tr> 
         <td width="43" align="left" valign="top">&nbsp;</td> 
         <td width="549">&nbsp;</td> 
        </tr> 
        <tr> 
         <td width="100" align="left" valign="top">( 四 ) </td> 
         <td width="492"> <p> 学 校 议 会 及 教 育 署 会 制 定 该 批 手 提 电 脑 的 详 细 规 格 ， 当 中 会 包 括 下 列 适 合 教 育 用 途 的 一 般 规 格 - </p>
          <ul> 
           <li>500MHz 中 央 处 理 器 ； </li>
           <li>64MB 随 机 存 取 存 贮 器 ； </li>
           <li>4GB 硬 碟 ； </li>
           <li>24 倍 速 唯 读 光 碟 机 ； </li>
           <li> 中 文 视 窗 操 作 系 统 （ 亦 可 选 用 英 文 视 窗 ） ； </li>
           <li> 抗 电 脑 病 毒 实 用 程 序 ； </li>
           <li> 系 统 实 用 程 序 ； </li>
           <li> 网 页 排 版 工 具 ； 及 </li>
           <li> 内 置 式 调 制 解 调 器 。 </li>
          </ul> <p></p> </td> 
        </tr> 
       </tbody>
      </table> 
      <p></p>
     </div> 
     <div class="clear"></div> 
    </div> 
    <div class="clear"></div> 
    <div class="t-right r" id="revision-date"> 
     <span> 修订日期: 2000年11月01日</span> 
    </div> 
    <div class="l" id="site-certification-block"> 
     <a class="l" rel="external" href="http://www.ipv6forum.com"><img src="/sc/images/ipv6.png" title="IPv6 电脑器材可浏览本网站" alt="IPv6 电脑器材可浏览本网站" /></a>
     <a class="l" id="btn-wcag" rel="external" href="http://www.w3.org/WAI/WCAG2AA-Conformance"><img src="/sc/images/web_accessibility_conformance.png" title="我们承诺会尽力确保本网页符合万维网联盟（W3C）《无障碍网页内容指引》（WCAG）2.0 AA级别标准，但本网页载有大量多媒体内容，要规定这类内容全部符合所有AA级别标准并不可能。尽管如此，这类多媒体内容会尽量摆放在特定位置，以免阻碍用户接触本网页所载的重要内容。" alt="我们承诺会尽力确保本网页符合万维网联盟（W3C）《无障碍网页内容指引》（WCAG）2.0 AA级别标准，但本网页载有大量多媒体内容，要规定这类内容全部符合所有AA级别标准并不可能。尽管如此，这类多媒体内容会尽量摆放在特定位置，以免阻碍用户接触本网页所载的重要内容。" /></a>
     <a class="l" id="btn-w3c" rel="external" href="http://validator.w3.org/check?uri=referer"><img src="/sc/images/w3c_html4.01.gif" title="符合超文本标示语言(HTML)4.01严格版" alt="符合超文本标示语言(HTML)4.01严格版" /></a> 
    </div> 
   </div> 
   <div class="clear"></div> 
   <!--footer-->
<div id="footer_wrapper">
<div id="footer_container">
    <div id="footer_left">&copy; 2013 版权所有 | <a href="/sc/important-notices.html">重要告示</a> | <a href="/sc/privacy-policy.html">私隐政策</a></div>
    <div id="social-features" class="r cr">
        <a id="btn-rss" class="l" href="/sc/rss.html"><img alt="RSS" title="RSS" src="/sc/images/footer_rss.jpg" width="24" height="24"></a>
			<div class='popbox'>
				<a class='open' href="#"><img src="/sc/images/footer_share.jpg" width="24" height="24" alt="分享" title="分享"></a>
				<div class='collapse'>
					<div class='box'>
						<a class="shareItem" href="javascript:shareFacebook();"><img src="/sc/images/ico_facebook.png" name="facebook" id="facebook" alt="分享至Facebook" title="分享至Facebook"><span>Facebook</span></a>
						<a class="shareItem" href="javascript:shareTwitter();"><img src="/sc/images/ico_twitter.png" name="twitter" id="twitter" alt="分享至Twitter" title="分享至Twitter"><span>Twitter</span></a>	
						<a class="shareItem" href="javascript:shareWeibo();"><img src="/sc/images/ico_weibo.png" name="weibo" id="weibo" alt="分享至新浪微博" title="分享至新浪微博"><span>新浪微博</span></a>	
						<a class="shareItem" href="javascript:shareEmail();"><img src="/sc/images/ico_email.png" name="email" id="email" alt="分享至电邮" title="分享至电邮"><span>电邮</span></a>	
					</div>
				</div>
			</div>
    </div>
</div><!--footer_container-->
</div><!--footer_wrapper--> 
  </div>   
 </body>
</html>
"""
soup = BeautifulSoup(html_doc, "lxml")
print '---------------------------------'
all_p = soup.find_all('div', id = 'content')[0].get_text().strip()
all_p = re.sub(r'\n', "", all_p)
all_p = re.sub(r'\t', "", all_p)
all_p = all_p.encode('GBK', 'ignore')
print all_p
print '---------------------------------'  


# url = 'http://www.sb.gov.hk/sc/pub/fcc/FCC_Report_32.pdf'
# url1 = 'http://www.sb.gov.hk/sc/pub/fcc/FCC_Report_33.pdf'
# m = md5.new()
# m.update(url)
# md_str = m.hexdigest()
# print md_str

# m = md5.new()
# m.update(url1)
# md_str = m.hexdigest()
# print md_str
