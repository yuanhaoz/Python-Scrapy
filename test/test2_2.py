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
<meta name="description" content="Security Bureau, Narcotics Division Website">
<meta name="author" content="Security Bureau, Narcotics Division">
<script language="JavaScript" src="/js/jquery-1.11.0.min.js" type="text/javascript"></script>
<link href="/css/print.css" rel="stylesheet" type="text/css" media="print"> 
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<script language="JavaScript" src="../js/genLayer.js" type="text/javascript"></script>
<script language="JavaScript" src="../js/common.js" type="text/javascript"></script>	
<script language="JavaScript" src="../js/data.js" type="text/javascript"></script>
<script language="JavaScript" src="../js/swf.js" type="text/javascript"></script>
<title>Narcotics Division, Security Bureau 保安局禁毒處</title>

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
<!--
.search {  font-family: "Arial", "Helvetica", "sans-serif"; font-size: 12px; text-decoration: none}
.sidebar a:visited { font-family: "Arial", "Helvetica", "sans-serif"; font-size: 12px; text-decoration: none ; color: #000099}
.footer { font-size: 10pt; color: #000000; font-family: "Arial", "Helvetica", "sans-serif"}
.header { font-size: 10pt; color: #3333FF ; font-family: "Arial", "Helvetica", "sans-serif"}
-->
</style>
<link href="/css/format.css" rel="stylesheet" type="text/css" >
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
      <td align="left" valign="top" width="153" height="22" >
        <script language="JavaScript" type="text/javascript">getLeftMenu();</script>
      </td>
      <td align="left" valign="top" bgcolor="#FFFFFF"> 
        <table width="100%" border="0" cellpadding="5" cellspacing="5" >
          <tr> 
            <td valign="top" align="left"><img src="images/1_pixel.gif" alt="" width="8" height="15"><a name="top"></a></td>
          </tr>
          <tr> 
            <td valign="top"><img src="images/chi/c_press_handing.jpg" alt="新聞公報" width="125" height="35"></td>
          </tr>
          <tr> 
            <td valign="top"> 
              <table width="100%" border="0" cellpadding="0" cellspacing="0">
                <tr> 
                  <td height="17"> 
                    <div align="center"> 
                      <p>二 零 零 四 年 三 月 四 日 新 聞 稿</p>
                      </div>
                  </td>
                </tr>
                <tr> 
                  <td> 
                    <div align="center"><strong>香港首個永久藥物教育展覽館局部啟用</strong></div>
                  </td>
                </tr>
              </table>
              <p align="left">

　　香港首個以藥物教育為主題的永久展覽館──香港賽馬會藥物資訊天地（簡稱藥物資訊天地）由今日（三月四日）起非正式開放給部份團體預約參觀，為稍後正式啟用作好籌備工作。<p>

<p>

　　保安局局長李少光今日在主持藥物資訊天地局部啟用儀式時表示，藥物資訊天地提供一個以社區為本的禁毒教育場地，是禁毒教育工作的新里程碑。<p>

<p>

　　李少光說：「香港多年來努力不懈，致力建立一個健康、免除毒害的社會。在禁毒常務委員會的督導下，政府採用多管齊下的方針，打擊及遏止濫用藥物問題。」<p>

<p>

　　李少光補充：「香港禁毒策略中重要的一環是推廣以社會大眾為對象的禁毒預防教育。打擊濫用藥物運動能否成功推行，社會大眾的支持是不可或缺的。」<p>

<p>

　　保安局局長代表香港特別行政區政府向香港賽馬會慈善信託基金（信託基金）致謝。信託基金慷慨捐助5 058萬元，不僅使藥物資訊天地的計劃能得以落實，並為香港的禁毒工作倍添原動力。<p>

<p>

　　他亦感謝所有曾為藥物資訊天地的展品及設施提供專業知識及意見的人士。<p>

<p>

　　除禁毒常務委員會及其轄下小組委員會和藥物資訊天地督導委員會的主席及委員外，撲滅罪行委員會委員和超過五十名各國駐港領事或其代表均有出席今日的儀式。<p>

<p>

　　保安局局長說：「今日各位撥冗光臨，標誌著香港與國際間多年來建立的緊密伙伴關係。我相信，這關係將會更形密切。」<p>

<p>

　　他補充說：「濫用藥物是一個全球性的問題。打擊毒禍並無界限之分，我們應放眼世界。各國共同合作、分享資料才是打擊毒禍的最有效對策。」<p>

<p>

　　佔地九百平方米的藥物資訊天地位於金鐘道政府合署低座平台，透過多媒體展品、互動遊戲及角色扮演，傳遞禁毒信息。<p>

<p>

　　特別為吸引年青人而設計的藥物資訊天地共分兩層，由三個主要展覽場地、互動影院、課室、資訊站及圖書館組成。<p>

<p>

　　保安局局長期望老師、家長及青少年工作者均能參與打擊毒禍的教育工作，而藥物資訊天地正好成為推行禁毒教育活動的新焦點。<p>

<p>

　　藥物資訊天地將於本年六月全面投入服務。在三月至六月期間，藥物資訊天地將開放予學校、青少年團體、地區領袖、禁毒工作者及有關的非政府機構預約參觀。<p>

<p>

　　今日出席儀式的嘉賓包括：香港賽馬會慈善及公司事務執行總監饒恩培、禁毒常務委員會主席蔡元雲醫生、藥物資訊天地督導委員會主席李紹鴻教授、保安局常任秘書長應耀康、建築署署長余熾鏗及禁毒專員余呂杏茜。<p>

<p>

完
<!--<p>

<p>

二○○四年三月四日（星期四）-->

<p>
     <p> <IMG SRC="http://www.info.gov.hk/graphics7-00/tvicon.gif" WIDTH="20" HEIGHT="18" ALIGN="BOTTOM" BORDER="0" alt=""> 
        <A HREF="http://webcast.info.gov.hk/2004/0403.ram">短片</A> 
      <p>


              <p></p>
            </td>
          </tr>
          <tr> 
            <td valign="top"> 
              <div align="center"><br>
                <a href="#top"><img src="images/c_top_bullnet.gif" alt="主頁" width="40" height="14" border="0"><br>
                </a> <img src="images/chi/botdot.jpg" alt="" width="602" height="3" style="width:603px;" ><br>
              </div>
            </td>
          </tr>
          <tr> 
            <td valign="top" align="center"><br>
              <br>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
  <p>&nbsp;</p>

<!-- Use genLayer.js to create the following code -->

<!--

<div id="Layer1" style="position:absolute; left:2px; top:550px; width:150px; height:74px; z-index:1"> 
  <div align="center"><a href="javascript:MM_openBrWindow('c_flash.htm','','width=760,height=420');"><img src="images/chi_drug.gif" alt="啪丸--有何結局? 啪丸=玩完" border="0"></a></div>
</div>
<br>
<br>
<div id="Layer2" style="position:absolute; left:4px; top:633px; width:146px; height:61px; z-index:2"> 
  <div align="center"><a href="javascript:MM_openBrWindow('NDgame_c/c_game.htm','','width=640,height=480');"><img src="images/chi_beautiful.gif" alt="角色扮演禁毒遊戲 -- 美麗人生" border="0"></a></div>
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


soup = BeautifulSoup(html_doc, "lxml")
print '---------------------------------'
# print len(soup.find_all('table'))
all_p = soup.find_all('table')[0].get_text().strip()
content = all_p
content = re.sub(r'\w+_\w+\(\w+\)', "", content)
content = re.sub(r'\w+\s\w+=\w+>', "", content)
content = re.sub(r'\d+\s\w+=\"\d+\"\s\w+=\"\d+\">', "", content)
content = re.sub(r'top>', "", content)
content = re.sub(r'footer\(\)', "", content)
content = re.sub(r'\n', "", content)
content = re.sub(r'\t', "", content)

print content
print '---------------------------------'  


