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
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN" lang="zh-CN">

<head>
<meta name="Keywords" content="保安局禁毒处, 毒品麻醉镇痛剂资料">
<meta name="description" content="保安局禁毒处 - 毒品麻醉镇痛剂资料">
	<meta name="description-2" content="Security Bureau, Narcotics Division Website">
	<meta name="author" content="Security Bureau, Narcotics Division">
	<script language="JavaScript" src="/js/jquery-1.11.0.min.js" type="text/javascript"></script>
	<link href="/css/print.css" rel="stylesheet" type="text/css" media="print">
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<script language="JavaScript" src="/js/genLayer.js" type="text/javascript"></script>
	<script language="JavaScript" src="/js/common.js" type="text/javascript"></script>
	<script language="JavaScript" src="/js/data.js" type="text/javascript"></script>
	<script language="JavaScript" src="/js/swf.js" type="text/javascript"></script>
	<title>保安局禁毒处 - 毒品麻醉镇痛剂资料</title>
	<link href="/css/format.css" rel="stylesheet" type="text/css">
	<script language="JavaScript" type="text/javascript">
		<!--
	function MM_swapImgRestore() { //v3.0
  var i,x,a=document.MM_sr; for(i=0;a&&i<a.length&&(x=a[i])&&x.oSrc;i++) x.src=x.oSrc;
}

function MM_preloadImages() { //v3.0
  var d=document; if(d.images){ if(!d.MM_p) d.MM_p=new Array();
    var i,j=d.MM_p.length,a=MM_preloadImages.arguments; for(i=0; i<a.length; i++)
    if (a[i].indexOf("#")!=0){ d.MM_p[j]=new Image; d.MM_p[j++].src=a[i];}}
}

function MM_findObj(n, d) { //v4.01
  var p,i,x;  if(!d) d=document; if((p=n.indexOf("?"))>0&&parent.frames.length) {
    d=parent.frames[n.substring(p+1)].document; n=n.substring(0,p);}
  if(!(x=d[n])&&d.all) x=d.all[n]; for (i=0;!x&&i<d.forms.length;i++) x=d.forms[i][n];
  for(i=0;!x&&d.layers&&i<d.layers.length;i++) x=MM_findObj(n,d.layers[i].document);
  if(!x && d.getElementById) x=d.getElementById(n); return x;
}

function MM_swapImage() { //v3.0
  var i,j=0,x,a=MM_swapImage.arguments; document.MM_sr=new Array; for(i=0;i<(a.length-2);i+=3)
   if ((x=MM_findObj(a[i]))!=null){document.MM_sr[j++]=x; if(!x.oSrc) x.oSrc=x.src; x.src=a[i+2];}
}

function MM_openBrWindow(theURL,winName,features) { //v2.0
  window.open(theURL,winName,features);
}

		//-->
	</script>
	<style type="text/css">
		<!-- .search {
			font-family: "Arial", "Helvetica", "sans-serif";
			font-size: 12px;
			text-decoration: none
		}
		
		.sidebar a:visited {
			font-family: "Arial", "Helvetica", "sans-serif";
			font-size: 12px;
			text-decoration: none;
			color: #000099
		}
		
		.footer {
			font-size: 10pt;
			color: #000000;
			font-family: "Arial", "Helvetica", "sans-serif"
		}
		
		.header {
			font-size: 10pt;
			color: #3333FF;
			font-family: "Arial", "Helvetica", "sans-serif"
		}
		
		-->
	</style>
</head>

<body>
	
	<table border="0" cellpadding="0" cellspacing="0" width="760">
		<tr valign="top">
			<td>
				<script language="JavaScript" type="text/javascript">
					targetSwitchPage = ""
				</script>
				<script language="JavaScript" src="/js/header.js" type="text/javascript"></script>
			</td>
		</tr>
	</table>
	<table id="content" width="760" border="0" align="left" cellpadding="0" cellspacing="0">
		<tr>
			<td align="left" valign="top" width="153">
				<script language="JavaScript" type="text/javascript">
					getLeftMenu();
				</script>
			</td>
			<td align="left" valign="top" bgcolor="#FFFFFF">
				<table width="100%" border="0" cellpadding="5" cellspacing="5">
					<tr>
						<td valign="top" align="left"><img src="/sc/images/1_pixel.gif" alt="" width="8" height="15">
							<a name="top"></a>
						</td>
					</tr>
					<tr>
						<td valign="top" align="left"><strong>有 用 资 料</strong></td>
					</tr>
				</table>	
							<table width="585" cellspacing="2" cellpadding="2" border="0" align="center">
								
									<tr>
										<td align="center"><span><strong>麻 醉 镇 痛 剂 </strong></span>
											<br>
											<br> </td>
									</tr></table>
									
											<table width="585" border="1" cellspacing="2" cellpadding="8" align=center border="0">
												
													<tr valign=top bgcolor="#7070ce">
														<th width="164" align="center"><span><strong>物 质 </strong></span></th>
														<th width="124" align="center"><span><strong>俗 称 </strong></span></th>
														<th width="129" align="center"><span><strong>医 药 用 途 </strong></span></th>
														<th width="168" align="center"><span><strong>吸 食 祸 害 </strong></span></th>
													</tr>
													<tr>
														<td valign="middle" align="center" width="164" bgcolor="#e5e5ff">
															<br><img src="/sc/images/heroin.jpg" alt="海洛英" border="0" width="103" height="69">
															<br>海 洛 英
															<br>
															<br> </td>
														<td width="164" bgcolor="#e5e5ff">白 粉 、 粉 、 灰 、 四 仔 、 美 金 、 港 纸 </td>
														<td valign="middle" width="109" bgcolor="#e5e5ff">没 有 </td>
														<td valign="middle" width="148" bgcolor="#e5e5ff" rowspan="5" nowrap>
															<br>
															<ol>
																<li>成 瘾</li>
																<li>昏 睡</li>
																<li>压 抑 呼 吸</li>
																<li>恶 心</li>
																<li>断 瘾 症 状 :
																	<br> 流 眼 水 、
																	<br> 流 鼻 涕 、
																	<br> 打 呵 欠 、
																	<br> 食 欲 不 振 、
																	<br> 烦 躁 、 震
																	<br> 颤 、 惊 惶 、
																	<br> 感 到 寒 冷
																	<br> 、 出 汗 、
																	<br> 痉 挛 </li>
															</ol>
														</td>
													</tr>
													<tr>
														<td valign="middle" align="center" width="164" bgcolor="#e5e5ff">
															<br><img src="/sc/images/dipipanone.jpg" alt="地匹哌酮" border="0" width="103" height="43">
															<br>地 匹 <img src="/sc/images/word_1.gif" alt="" align=top border="0" width="16" height="15"> 酮
															<br>
															<br> </td>
														<td valign="middle" width="164" bgcolor="#e5e5ff">红 色 菲 仕 通 </td>
														<td valign="middle" width="109" bgcolor="#e5e5ff"> 镇 痛 、 防 止 因 戒 除 毒 瘾 所 引 起 的 不 适 </td>
													</tr>
													<tr>
														<td valign=top align="center" width="164" bgcolor="#e5e5ff">
															<br> <img src="/sc/images/methadone.jpg" alt="美沙酮" border="0" width="103" height="54">
															<br> 美 沙 酮
															<br>
															<br> <img src="/sc/images/physeptone.jpg" alt="菲仕通" border="0" width="103" height="54">
															<br> 菲 仕 通
															<br>
															<br> </td>
														<td valign="middle" width="164" bgcolor="#e5e5ff">
															<p>蜜 瓜 汁 </p>
															<br>
															<br>
															<p>帆 船 仔 、 白 色 菲 仕 通 </p>
														</td>
														<td valign="middle" width="109" bgcolor="#e5e5ff"> 戒 毒 治 疗 </td>
													</tr>
													<tr>
														<td valign=top align="center" width="164" bgcolor="#e5e5ff">
															<br><img src="/sc/images/morphine.jpg" alt="吗啡针剂" border="0" width="103" height="34">
															<br> 吗 啡 针 剂
															<br>
															<br> </td>
														<td valign="middle" width="164" bgcolor="#e5e5ff">
															<br>吗 啡 针
															<p></p>
														</td>
														<td valign="middle" width="109" bgcolor="#e5e5ff"> 镇 痛 </td>
													</tr>
													<tr>
														<td valign=top align="center" width="164" bgcolor="#e5e5ff">
															<br><img src="/sc/images/opium.jpg" alt="鸦片" border="0" width="103" height="64">
															<br> 鸦 片
															<br>
															<br> </td>
														<td valign="middle" width="164" bgcolor="#e5e5ff">熟 膏 、 福 寿 膏
															<p></p>
														</td>
														<td valign="middle" width="109" bgcolor="#e5e5ff">没 有 </td>
													</tr>
												
											</table>
											<p align="center"><strong><u><a href="#top"><span>回 页 首 </span></a></u></strong></p>
										
								
							 <img src="/sc/images/chi/botdot.jpg" alt="" width="602" style="width:603px;" height="3">
							<br>
							<table width="100%" border="0" cellspacing="0" cellpadding="0">
								<tr>
									<td>
										<script language="JavaScript" src="/js/footer.js" type="text/javascript"></script>
										<script language="JavaScript" type="text/javascript">
											footer();
										</script>
									</td>
									<td width="61%">
										<div align="right"><span class="footer">最 近 修 订 日 期 : <strong>2013 年 4 月 18 日</strong></span></div>
									</td>
									<td>&nbsp;</td>
								</tr>
								<!--<script language="JavaScript" type="text/javascript"> footer_wcag(); </script>-->
							</table>
						
					<tr>
						<td valign="top" align="center">&nbsp;</td>
					</tr>
				</table>
			</td>
		</tr>
	</table>
	<p>&nbsp;</p>
	<!-- Use genLayer.js to create the following code -->
	<!-- 

  <div id="Layer1" style="position:absolute; left:2px; top:550px; width:150px; height:74px; z-index:1"> 
    <div align="center"><a href="javascript:MM_openBrWindow('c_flash.htm','','width=760,height=420');"><img src="images/chi_drug.gif" alt="啪 丸 --有 何 结 局 ? 啪 丸 =玩 完 " border="0"></a></div>
  </div>
  <div id="Layer2" style="position:absolute; left:4px; top:633px; width:146px; height:61px; z-index:2"> 
    <div align="center"><a href="javascript:MM_openBrWindow('NDgame_c/c_game.htm','','width=640,height=480');"><img src="images/chi_beautiful.gif" alt="角 色 扮 演 禁 毒 游 戏 -- 美 丽 人 生 " border="0"></a></div>
  </div>

-->
	<script type="text/javascript">
		<!--
		genfooterLayer();
		//-->
	</script>
</body>

</html>

"""


soup = BeautifulSoup(html_doc, "lxml-xml")

print '---------------------------------'

def predeal(content):
    content = re.sub(r'(LEFT\sVALIGN=TOP)(\sWIDTH=\d+)?\>', "", content)
    content = re.sub(r'\d\s\w+=\d+\s\w+=\d+\s\w+=\w+>', "", content)
    content = re.sub(r'\d\s\w+=\d+\s\w+=\d+\>', "", content)
    content = re.sub(r'\d\s\w+=\w+>', "", content)
    content = re.sub(r'\w+\s\w+=\W\d+\W\W>', "", content)
    content = re.sub(r'\w+>', "", content)
    content = re.sub(r'center', "", content)
    content = re.sub(r'//\s+\w+_\w+_\w+\(\)\;', "", content)
    content = re.sub(r'\w+=\w+\s\w+=\d+\W', "", content)
    content = re.sub(r'\d\s\w+=\W\d+\W\s\w+=\W\d+\W>', "", content)
    content = re.sub(r'\w+\s\w+=', "", content)
    content = re.sub(r'\w+=#', "", content)
    content = re.sub(r'\w+=\d+', "", content)
    content = re.sub(r'\w+=#\w*', "", content)
    content = re.sub(r'\w+\(\d*\)', "", content)
    content = re.sub(r'\s\w+=\"\d+\%\">', "", content)
    content = re.sub(r'"\d+\%\"\s>', "", content)
    content = re.sub(r'\"\d+\"', "", content)
    content = re.sub(r'\w+=', "", content)
    content = re.sub(r'top', "", content)
    content = re.sub(r'left', "", content)
    content = re.sub(r'middle', "", content)
    content = re.sub(r'\//;', "", content)
    content = re.sub(r'>', "", content)
    content = re.sub(r';', "", content)
    
    content = re.sub(r'\n', "", content)
    content = re.sub(r'\t', "", content)
    return content

# url = 'view-source:http://www.nd.gov.hk/text/tc/agenda/c_acan4.htm'
# u = url.split('/')
# print len(u)
# name = u[len(u) - 1]
# if '_' in name:
    # print 'true'
# else:
    # print 'false'

# url = 'http://www.nd.gov.hk/text/tc/treat/three_year_plan_2015_2017.htm'
# if '/text/' in url:
    # print 'true'
# else:
    # print 'false'
    
all_p = soup.find_all('table')
content = ''
for p in all_p:
    # t = p.get_text(" ", strip=True).strip()
    t = p.get_text().strip()
    content += t
    content = predeal(content)

print content

print '---------------------------------'

all_p = soup.find_all('table')[0].get_text().strip()
content = ''
content += all_p
content = predeal(content)

print content
