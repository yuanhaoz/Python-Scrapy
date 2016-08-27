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
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-HK" lang="zh-hk">
<head>
<meta name="Keywords" content="保安局禁毒處, 禁毒影音短片">
<meta name="description" content="保安局禁毒處 - 禁毒影音短片">
<meta name="description-2" content="Security Bureau, Narcotics Division Website">
<meta name="author" content="Security Bureau, Narcotics Division">
<script language="JavaScript" src="/js/jquery-1.11.0.min.js" type="text/javascript"></script>
<link href="/css/print.css" rel="stylesheet" type="text/css" media="print"> 
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<script language="JavaScript" src="../js/genLayer.js" type="text/javascript"></script>
<script language="JavaScript" src="../js/common.js" type="text/javascript"></script>	
<script language="JavaScript" src="../js/data.js" type="text/javascript"></script>
<script language="JavaScript" src="../js/swf.js" type="text/javascript"></script>
<script language="JavaScript" src="../js/jquery-1.11.0.min.js" type="text/javascript"></script>
<script language="JavaScript" src="../js/reCon.js" type="text/javascript"></script>
<link href="/css/format.css" rel="stylesheet" type="text/css" >
<title>保安局禁毒處 - 禁毒影音短片</title>

<script language="JavaScript" type="text/javascript">
<!--
var currentSection='7,3';
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

function openWin(theURL,winName,features,opener) { //v2.0

	popUp=window.open(theURL,winName,features);

	popUp.opener=opener;

}
//-->
</script>
<style type="text/css">
<!--
.search {  span-family: "Arial", "Helvetica", "sans-serif"; span-size: 12px; text-decoration: none}
.sidebar a:visited { span-family: "Arial", "Helvetica", "sans-serif"; span-size: 12px; text-decoration: none ; color: #000099}
.footer { span-size: 10pt; color: #000000; span-family: "Arial", "Helvetica", "sans-serif"}
.header { span-size: 10pt; color: #3333FF ; span-family: "Arial", "Helvetica", "sans-serif"}
-->
.reCon3 .batch {
	clear: both;
	padding-top: 5px !important;
}
</style>
</head>
<body><h1 style="display:none">Title</h1>
<table border="0" cellpadding="0" cellspacing="0" width="760">
	<tr valign="top">
		<td>
			<script language="JavaScript" type="text/javascript">targetSwitchPage = ""</script>
			<script language="JavaScript" src="/js/header.js" type="text/javascript"></script>
		</td>
	</tr>
</table>

  <table id="content" width="760" border="0" align="left"  cellpadding="0" cellspacing="0">
    <tr> 
      <td align="left" valign="top" width="153" height="22" >	  <script language="JavaScript" type="text/javascript">getLeftMenu();</script> </td>
      <td align="left" valign="top" bgcolor="#FFFFFF"> 
        <table width="597" border="0" cellpadding="5" cellspacing="5" >
		<!-- <tr>
			  <td>
				<script language="JavaScript" type="text/javascript">generateTopMenu();</script>
				</td>
				</tr> -->
									<tr>
						<td>
							<table border="1">
								<Tr valign="middle">
									<td width="25%"><a href="druginfo.htm" title="This link will open in new window">毒品資料</a></td>
									<td width="25%"><a href="publications.htm" title="This link will open in new window">禁毒刊物</a></td>
									<td width="25%"><a href="videos_radio_clips.htm" title="This link will open in new window">禁毒影音短片</a></td>
									<td width="25%"><a href="resources_parents.htm" title="This link will open in new window">給家長的禁毒資源</a></td>
								</tr>
								<Tr valign="middle">
									<td width="25%"><a href="resources_teachers.htm" title="This link will open in new window">給教師和社工的禁毒資源</a></td>
									<td width="25%"><a href="resources_professionals.htm" title="This link will open in new window">給醫護人員的禁毒資源</a></td>
									<td width="25%"><a href="resources_youths.htm" title="This link will open in new window">給青年人的禁毒資源</a></td>
									<td width="25%"><a href="druginfocentre.htm" title="This link will open in new window">香港賽馬會藥物資訊天地</a></td>
								</tr>
							</table>
						</td>
					</tr>
					<tr>
						<td valign="top" align="left"><img src="images/top_buttons/top_buttons_dot_line.gif" alt=""> </td>
					</tr>
				
          <tr> 
            <td valign="top" align="left"><a name="top"></a></td>
          </tr>
          <tr> 
			<a name="main-content" id="main-content" tabindex="0"></a>
            <td valign="top"><span ><strong>禁毒影音短片</strong></span></td>
          </tr>
		  <tr>
            <td valign="top"> 
				<table border="0" cellspacing="2" cellpadding="8" >
					<Tr valign="top">
						<td><strong>禁毒影像短片：</strong></td>
					</tr>
					
					<tr>
						<td>
							<div style="width:100%;" class="reCon3">
							    <div class="iso">
									<a href="http://www.hkayd.org.hk/YourChoice/finalentries.pdf" target="_blank"><img src="/tc/images/finalentries.jpg" alt="" border="0" >
									<br>禁 毒 基 金 贊 助 「 Your Choice 」 納 米 電 影 創 作 比 賽</a>
								</div>
								<div class="iso">
									<a href="tv_announcements.htm"><img src="/tc/images/banner_03.gif" alt="" border="0" >
									<br>電 視 宣 傳 短 片</a>
								</div>
								<div class="iso">
									<a href="sunproject.htm"><img src="/tc/images/sunlife_icon.gif" alt="" border="0" >
									<br>禁 毒 基 金 贊 助 「 路 訊 通 」 節 目 《Sun 生 命》</a>
								</div>
								<!--div class="iso">
									<div class="isopic"><a href="http://www.metroradio.com.hk/Campaign/997/TeensNoDrugs/" target="_blank" title="此連結會於新視窗開啟"><img src="../en/images/antidrug_event_2012.gif" border="0" width="137" height="103"></a></div>
									<div class="isotext"><a href="http://www.metroradio.com.hk/Campaign/997/TeensNoDrugs/" target="_blank" title="此連結會於新視窗開啟">打 開 TEEN 窗 愛 ＠ 無 毒 SHOW</a></div>
								</div-->
								<!--div class="iso">
									<div class="isopic"><a target="_blank" title="此連結會於新視窗開啟" href="http://www.metroradio.com.hk/Campaign997/KnockDrugsOutWithLove/ "><img src="../en/images/teenteenshow.gif" border="0" width="137" height="103"></a></div>
									<div class="isotext"><a target="_blank" title="此連結會於新視窗開啟"  href="http://www.metroradio.com.hk/Campaign997/KnockDrugsOutWithLove/ ">TEEN TEEN 有 愛 無 毒 Show</a></div>
								</div-->
								<!--div class="iso">
									<div class="isopic"><a href="http://programme.rthk.hk/rthk/tv/programme.php?name=tv/drugbattleforum&p=5923" target="_blank" title="此連結會於新視窗開啟"><img src="../en/images/Drug Battle Forum.png" border="0" width="137" height="103"></a></div>
									<div class="isotext"><a href="http://programme.rthk.hk/rthk/tv/programme.php?name=tv/drugbattleforum&p=5923" target="_blank" title="此連結會於新視窗開啟">香 港 電 台 電 視 節 目 《 毒 海 論 浮 生 》 </a></div>
								</div-->
								<!--div class="iso">
									<div class="isopic"><a href="http://programme.rthk.hk/rthk/tv/programme.php?name=tv/drugbattle2013&p=5689" target="_blank" title="此連結會於新視窗開啟"><img src="../en/images/rthk_progam.gif" border="0" width="137" height="103"></a></div>
									<div class="isotext"><a href="http://programme.rthk.hk/rthk/tv/programme.php?name=tv/drugbattle2013&p=5689" target="_blank" title="此連結會於新視窗開啟">香 港 電 台 電 視 節 目 《 毒 海 浮 生 》</a></div>
								</div-->
								<!--div class="iso">
									<div class="isopic"><a href="http://programme.tvb.com/drama/beautyofthegame" target="_blank" title="此連結會於新視窗開啟"><img src="../en/images/icon_beautyofthegame.gif" border="0" width="137" height="103"></a></div>
									<div class="isotext"><a href="http://programme.tvb.com/drama/beautyofthegame" target="_blank" title="此連結會於新視窗開啟">禁毒電視連續劇《美麗高解像》</a></div>
								</div-->
								<div class="iso">
									<a href="antidrug_themesong_2.htm"><img src="/tc/images/icon_antidrug_song_2.gif" border="0" width="137" height="103" alt="" b>
									<br>「不可一．不可再」<br>全港青少年禁毒運動2009 <br>主題曲「天造之材」MTV</a>
								</div>
								<div class="iso">
									<a href="antidrug_themesong.htm"><img src="/tc/images/icon_antidrug_song.gif" border="0" width="137" height="103" alt="" b>
									<br>「不可一．不可再」禁毒運動主題曲「不不不」MTV</a>
								</div>
							</div>
						</td>
					</tr>
					
					<tr>
						<td>&nbsp;</td>
					</tr>

				</table>
			</td>
		   </tr>

		  <tr>
            <td valign="top"> 
				<table border="0" cellspacing="2" cellpadding="8" >
					<Tr valign="top">
						<td colspan="3"><strong>禁毒聲音短片：</strong></td>
					</tr>
					
					<tr>
						<td>
							<div style="width:100%;" class="reCon3">
								<div class="iso">
									<a href="radio_announcements.htm"><img src="/tc/images/icon_antidrug_radio.gif" border="0" width="137" height="103" alt="" >
									<br>電台宣傳聲帶</a>
								</div>
								<div class="iso">
									<a href="rs_handstogether_2015.htm"><img src="/tc/images/sqsqkd2015.jpg" border="0"  alt="" >
									<br>禁毒電台環節「手牽手　齊抗毒」</a>
								</div>
								<div class="iso">
									<a href="adEduSeg.htm"><img src="/tc/images/jjdp_qxkd_s.jpg" border="0" alt="" >
									<br>禁毒電台環節「堅拒毒品　齊心抗毒」</a>
								</div>
								<div class="iso">
									<a href="http://www.metroradio.com.hk/Campaign/2013/997/Narcotics/" target="_blank" title="此連結會於新視窗開啟"><img src="/tc/images/jbtc.gif" alt="" b width="137" height="103" border="0">
									<br>禁毒廣播劇「戒不太遲」</a>
								</div>
								<div class="iso">
									<a href="antidrug_themesong_2.htm"><img src="/tc/images/icon_antidrug_song_2.gif" border="0" width="137" height="103" alt="" b>
									<br>「不可一．不可再」全港青少年禁毒運動2009 主題曲「天造之材」</a>
								</div>
								<div class="iso">
									<a href="antidrug_themesong.htm"><img src="/tc/images/icon_antidrug_song.gif" border="0" width="137" height="103" alt="" b>
									<br>「不可一．不可再」禁毒運動主題曲「不不不」</a>
								</div>
							</div>
						</td>
					</tr>
					
					<tr>
						<td>&nbsp;</td>
                        <td>&nbsp;</td>
					</tr>
				</table>
			</td>
		   </tr>
		   <tr>
					<td> 
						<div align="center"><img src="images/chi/botdot.jpg" alt="" width="602" height="3" style="width:603px;" ></div>
						<table align="center" border="0" cellpadding="0" cellspacing="0" width="98%">
							<tbody><tr> 
								<td><script language="JavaScript" src="../js/footer.js" type="text/javascript"></script><script language="JavaScript" type="text/javascript"> footer(); </script></td>

								<td>
                    <div align="right"><span class="footer"><script type="text/javascript">var manual_date ="";lastrevision();</script></span></div>
                  </td>
							</tr>
										<!--<script language="JavaScript" type="text/javascript"> footer_wcag(); </script>-->
						</tbody></table>
					</td>
		   </tr>
        </table>
      </td>
  </tr>
</table>
<p>&nbsp;</p>

<!-- Use genLayer.js to create the following code -->
<!-- 

<div id="Layer2" style="position:absolute; left:4px; top:633px; width:146px; height:61px; z-index:2"> 
  <div align="center"><a href="javascript:MM_openBrWindow('NDgame_c/c_game.htm','','width=640,height=480');"><img src="images/chi_beautiful.gif" alt="角色扮演禁毒遊戲 -- 美麗人生" border="0"></a></div>
</div>
<div id="Layer1" style="position:absolute; left:2px; top:550px; width:150px; height:74px; z-index:1"> 
  <div align="center"><a href="javascript:MM_openBrWindow('c_flash.htm','','width=760,height=420');"><img src="images/chi_drug.gif" alt="啪丸--有何結局? 啪丸=玩完" border="0"></a></div>
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

# print '---------------------------------'
# all_p = soup.find_all('table')[1].find_all('td')[1].find_all('tr')[1].get_text().strip()
# all_p = all_p.replace('0 cellpadding=0 cellspacing=0>', '')
# all_p = all_p.replace('footer();', '')
# all_p = all_p.replace('''left valign=top width="50">''', '')
# all_p = all_p.replace('left valign=top>', '')
# all_p = all_p.replace('''border="0">''', '')
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
print '---------------------------------'

# all_p = soup.find_all('table')[1].find_all('td')[1].find_all('p')
all_p = soup.find_all('table')[1].find_all('td')[1]
titles = soup.find_all('h1')
title = ''
content = ''
for i in range(1, len(titles)):
    title += titles[i].get_text().strip()

if all_p:
    ex1 = all_p.find_all(['p','h2','h3','h4','strong','a'])
    for i in range(0, len(ex1)-1):
        content += ex1[i].get_text().strip()
        content = re.sub(r'\w+=\"(\w+)?\"', "", content)
        content = re.sub(r'\w+=\w+', "", content)
        content = re.sub(r'\w+=\"\w+\:#\d+\;\w+\-\w+:\w+;\w+\-\w+:\w+\">', "", content)
        content = re.sub(r':#\d+;\w+-\w+:\w+;\w+-\w+:\w+', "", content)
        content = re.sub(r'>\"', "", content)
        content = re.sub(r'>', "", content)
        content = re.sub(r'\"', "", content)
        content = re.sub(r'top', "", content)
        content = content.replace('\n', '')
        content = content.replace('\t', '')
content = title + '\n' + content
print content
print '---------------------------------'

