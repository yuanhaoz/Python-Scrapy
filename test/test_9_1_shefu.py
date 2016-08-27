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


<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html lang="zh-cn">
<head><META HTTP-EQUIV="Content-type" CONTENT="text/html; charset=utf-8">
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>社会福利署 - 其他资料</title>
<link rel="meta" href="/labels.rdf" type="application/rdf+xml" title="Content labels" />
<meta name="keywords" content="其它澬料, 家 庭 及 儿 童 福 利 服 务, 青 少 年 服 务, 违 法 者 服 务, 康 复 服 务, 社 会 保 障, 安 老 服 务, 治 疗 中 心发 牌 制 度">
<script type="text/javascript" src="/css_js_sc/function.js"></script>
<script type="text/javascript" src="/css_js_sc/jquery-min.js"></script>
<!--<script type="text/javascript" src="/css_js/jquery-1.6.2.min.js"></script>-->
<!--<script type="text/javascript" src="/css_js/gistfile1.js"></script>-->
<!--<script type="text/javascript" src="/css_js/jquery-1.4.2.min.js"></script>-->
<script type="text/javascript" src="/css_js_sc/jquery.collection-min.js"></script>
<script type="text/javascript" src="/css_js_sc/jquery.fixSelect.js"></script>
<SCRIPT type="text/javascript" SRC="http://www.map.gov.hk/static/gihs_interface.js"></SCRIPT>
<script type="text/javascript">
<!--
MM_reloadPage(true);

function win(target){
	LeftPosition = 0;
	TopPosition = (screen.height-553);
	var newwin1 = window.open(target, "new","scrollbars=0, resizable=0,width=336,height=215,top="+TopPosition+",left="+LeftPosition);

} 

function nowLoadImage(img) { 
    document.images['placeHolder'].src = img; 

} 

var NS = false;
var IE = false;
if (document.layers)
{	NS = true;}
else if(document.all)
{	IE = true;}


function popup(menuName,on){
	if(on)
	{	//if(NS){
		//	document.layers[menuName].visibility="show";
			//document.layers[menuName].location="http://www.swd.gov.hk/cgi-bin/swd/calendar/popup.pl";
		//}
		//else if(IE){
			//document.all[menuName].style.visibility = "hidden";
			//details_frame.location = '/cgi-bin/swd/calendar/popup.pl';
		//}
	}
	else
	{	
		//if(NS)
		//	document.layers[menuName].visibility="hide";
		//else if(IE)
			//document.all[menuName].style.visibility = "hidden";
	}
}

// -->
</script>
<style>
@media print {
	.noprint {
		display: none;
	}
}	
</style>
<style type="text/css">
<!--
BODY{
  background-image : url('/sc/img/main/watermark.gif');
  background-repeat : no-repeat;
  background-attachment : fixed;
  background-position : 140 130;
}
-->
</style>

<link id="css0" rel="stylesheet" href="/css_js_sc/tc_style_medium.css" type="text/css">
<!--<link href="/css_js/coolmenus4/coolmenus4_orange.css" rel="stylesheet" type="text/css">-->
<!--<script type="text/javascript" src="/css_js/scroll.js"></script>-->
<!--<script type="text/javascript" src="/css_js/coolmenus4/coolmenus4.js"></script>-->
<script type="text/javascript" src="/css_js_sc/combine.js"></script>
<script> 
	myLang = "tc";
</script> 
</head>
<body bgproperties="fixed" onLoad="MM_preloadImages('/sc/img/clf/mainbar1_f2.gif','/sc/img/clf/mainbar2_f2.gif','/sc/img/clf/mainbar3_f2.gif','/sc/img/clf/mainbar4_f2.gif','/sc/img/clf/mainbar6_f2.gif','/sc/img/clf/mainbar8_f2.gif','/sc/img/clf/mainbar9_f2.gif','/sc/img/clf/mainbar10_f2.gif')" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<div id="skipwrapper">
<a name="skiptocontent" id="skiptocontent" href="#content" class="access">跳至主要内容</a>
</div>
<table width="760" border="0" cellspacing="0" cellpadding="0">
  <tr valign="top"> 
    <td><table width="760" border="0" cellspacing="0" cellpadding="0">
	<form name="searchform" action="http://search.gov.hk/search.html" method="get" target="_blank">
        <tr valign="top"> 
          <td> 
		  
          <table width="760" border="0" cellspacing="0" cellpadding="0" background="/sc/img/clf/bkgdtexture.gif">
		   <tr><td colspan="2">
			  <table width="760" border="0" cellspacing="0" cellpadding="0">
				  <tr><td><img src="/sc/img/clf/logo.gif" alt="社会福利署"></td><td align="right"><a href="http://www.brandhk.gov.hk/brandhk/index.htm" target="_blank"><img name="BrandHK" src="/sc/img/clf/BrandHK.gif" border="0" alt="香港品牌形像"></a></td></tr>
				  </table>
			  </td>
			  </tr>
                <tr > 
                  <td width="536" valign="bottom"> 
                  <table width="536" border="0" cellspacing="0" cellpadding="0">
                      <tr> 
                        <td > 
							<table width="536" border="0" cellspacing="0" cellpadding="0">
                            <tr > 
                              <td width="170"><script>printgovhkbar();</script><img name="mainbar1" src="/sc/img/clf/mainbar1.gif" border="0" alt="GovHK香港政府一站通"></a></td>
                              <td width="77"><script>printmenuicon();</script><!-- <a href="javascript:ChangeVer('index', 'textonly');" onMouseOut="MM_swapImgRestore()"  onMouseOver="MM_swapImage('mainbar2','','/tc/img/clf/mainbar2_f2.gif',1)" ><img name="mainbar2" src="/tc/img/clf/mainbar2.gif" border="0" alt="繁体纯文字"></a>--></td>
                              <td width="49"><script>printmenuicon2();</script><!-- <a href="javascript:ChiToogle();" onMouseOut="MM_swapImgRestore()"  onMouseOver="MM_swapImage('mainbar3','','/tc/img/clf/mainbar3_f2.gif',1)" ><img name="mainbar3" src="/tc/img/clf/mainbar3.gif" border="0" alt="简体版"></a>//--></td>
                              <td width="56"><a href="javascript:ChangeLang('tc', 'en');" onMouseOut="MM_swapImgRestore()"  onBlur="MM_swapImgRestore()" onMouseOver="MM_swapImage('mainbar4','','/sc/img/clf/mainbar4_f2.gif',1)" onFocus="MM_swapImage('mainbar4','','/sc/img/clf/mainbar4_f2.gif',1)"><img name="mainbar4" src="/sc/img/clf/mainbar4.gif" border="0" alt="ENGLISH"></a></td>
                              <td width="29"><img name="mainbar5" src="/sc/img/clf/mainbar5.gif" border="0" alt=""></td>
							  <td width="80"><a href="javascript:changeFontTitle('Medium');" title="原始大小"><img src="/images/font_size/Medium_on.gif" id="imgMedium" border=0 alt="原始大小"></a>&nbsp;<a href="javascript:changeFontTitle('Large');" title="较大"><img src="/images/font_size/Large_off.gif" id="imgLarge" border=0 alt="较大"></a>&nbsp;<a href="javascript:changeFontTitle('Extra');" title="最大"><img src="/images/font_size/Extra_off.gif" id="imgExtra" border=0 alt="最大"></a></td>
                              <td width="55" ><a href="javascript:document.searchform.submit();" onMouseOut="MM_swapImgRestore()" onBlur="MM_swapImgRestore()" onMouseOver="MM_swapImage('mainbar6','','/sc/img/clf/mainbar6_f2.gif',1)" onFocus="MM_swapImage('mainbar6','','/sc/img/clf/mainbar6_f2.gif',1)" ><img name="mainbar6" src="/sc/img/clf/mainbar6.gif" border="0" alt="搜寻"></a></td>
                            </tr>
                          </table>
						</td>
                      </tr>
                    </table>
                  </td>
                  <td width="224" valign="bottom">       
                    <table width="224" border="0" cellspacing="0" cellpadding="0">
                    <tr valign="bottom" align="right"> 
                          <td colspan="2"><!--<a href="http://www.brandhk.gov.hk/brandhk/index.htm" target="_blank"><img name="BrandHK" src="/tc/img/clf/BrandHK.gif" border="0" alt="香港品牌形像"></a>--></td>
                    </tr>
                    <tr>
                      <td width="99" valign="bottom" align="left">
						<label for="query" class="access">输入查询字串</label> 
                        <input id="query" class="search" type="text" name="query" size="10" value="输入查询字串" onmouseover="this.focus();" onmouseout="if(this.value=='')this.value='';" onblur="if(this.value=='')this.value='';" onfocus="this.select();" onclick="if(this.value=='输入查询字串')this.value=''" onkeypress="if(this.value=='输入查询字串')this.value=''"> 
                        <input type="hidden" name="tpl_id" value="stdsearch"> 
                        <input type="hidden" name="ui_lang" value="zh-cnhk"> 
                        <input type="hidden" name="ui_charset" value="UTF-8"> 
                        <input type="hidden" name="gp0" value="swd_home"> 
                        <input type="hidden" name="gp1" value="swd_home"> 
                        <input type="hidden" name="web" value="this"> 
                      </td>
                      <td width="125" valign="bottom" align="left"> 
                          <table border="0" cellspacing="0" cellpadding="0">
                              <tr> 
                                  <td width="22"><a href="javascript:document.searchform.submit();;" onMouseOut="MM_swapImgRestore()" onBlur="MM_swapImgRestore()" onMouseOver="MM_swapImage('mainbar8','','/sc/img/clf/mainbar8_f2.gif',1)" onFocus="MM_swapImage('mainbar8','','/sc/img/clf/mainbar8_f2.gif',1)"><img name="mainbar8" border="0" src="/sc/img/clf/mainbar8.gif" alt="提交搜寻内容"></a></td>
                                  <td width="67"><a href="/sc/index/site_sitemap/" onMouseOut="MM_swapImgRestore()"  onBlur="MM_swapImgRestore()" onMouseOver="MM_swapImage('mainbar9','','/sc/img/clf/mainbar9_f2.gif',1)" onFocus="MM_swapImage('mainbar9','','/sc/img/clf/mainbar9_f2.gif',1)" ><img name="mainbar9" src="/sc/img/clf/mainbar9.gif" border="0" alt="网页指南"></a></td>
                                  <td width="36"><a href="/sc/index/site_contactus/" onMouseOut="MM_swapImgRestore()"  onBlur="MM_swapImgRestore()" onMouseOver="MM_swapImage('mainbar10','','/sc/img/clf/mainbar10_f2.gif',1)" onFocus="MM_swapImage('mainbar10','','/sc/img/clf/mainbar10_f2.gif',1)" ><img name="mainbar10" src="/sc/img/clf/mainbar10.gif" border="0" alt="联络我们"></a></td>
                            </tr>
                          </table>
                       </td>
                    </tr>
                    </table>
                  </td> 
                </tr>
             
            </table>
			
			</td>
        </tr>
        <tr valign="top" bgcolor="#BB3333"> 
          <td><img src="/sc/img/general/spacer.gif" width="30" height="2" alt=""></td>
        </tr>
		</form>
      </table></td>
  </tr>
  <tr valign="top"> 
    <td><table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
        <td width="155" align="left" style="vertical-align: top;" background="/sc/img/general/menubar_bg.gif">
          <!--  menu bar -->
            <!--<img src="/tc/img/general/spacer.gif" width="1" height="500" alt="">-->
            <script type="text/javascript" src="/css_js_sc/coolmenus4/tc_menu.js"></script>
			<script type="text/javascript" src="/css_js_sc/left_menu.js"></script>
			
			<script type="text/javascript" src="/css_js_sc/wcag_logo_tc.js"></script>
	  <!-- End menu bar -->
          </td>
          <td align="left" valign="top">
              <!-- Content Start here -->
		 <table width="625" border="0" cellspacing="0" cellpadding="0">
  <tr bgcolor="#FFAD6A">
    <td width="14"><img src="/sc/img/general/spacer.gif" width="14" height="29" alt=""></td>
    <td background="/sc/img/general/nav_bg.gif" class="navigation" width="490"><a href="/sc/index/" class="nav">主页</a>
     > <a href="/sc/index/site_download/" class="nav">下载区</a> > 其他资料
    </td>
    <!--<td bgcolor="#FFEFD5" align=right><img src="/tc/img/font_size2.jpg" style="margin-right:2px"><a href="javascript:changeFontTitle('Medium');" title="原始大小"><img src="/images/font_size/Medium_on.gif" id="imgMedium" border=0></a>&nbsp;<a href="javascript:changeFontTitle('Large');" title="较大"><img src="/images/font_size/Large_off.gif" id="imgLarge" border=0></a>&nbsp;<a href="javascript:changeFontTitle('Extra');" title="最大"><img src="/images/font_size/Extra_off.gif" id="imgExtra" border=0></a>&nbsp;</td>-->
<td bgcolor="#FFEFD5" align="right"><!--<table style="width:170px"><tr><td align="right"><span class="fontsize_txt">字型大小:&nbsp;</span><a href="javascript:changeFontTitle('Medium');" title="原始大小"><img src="/images/font_size/Medium_on.gif" id="imgMedium" border=0 alt="原始大小"></a>&nbsp;<a href="javascript:changeFontTitle('Large');" title="较大"><img src="/images/font_size/Large_off.gif" id="imgLarge" border=0 alt="较大"></a>&nbsp;<a href="javascript:changeFontTitle('Extra');" title="最大"><img src="/images/font_size/Extra_off.gif" id="imgExtra" border=0 alt="最大"></a>&nbsp;</td></tr></table>--></td>
	</tr>
  <tr>
    <td valign="top"><table width="14" border="0" cellspacing="0" cellpadding="0">
        <tr>
          <td><img src="/sc/img/general/banner_corner.gif" width="14" height="19" alt=""></td>
        </tr>
        <tr>
          <td><img src="/sc/img/general/spacer.gif" width="14" height="400" alt=""></td>
        </tr>
      </table></td>
    <td align="left" valign="top" colspan=2>
	 <h1 class="access"> - 其他资料</h1><a name="content" id="content"></a>
    <table width="610" border="0" cellspacing="0" cellpadding="3">
    <tr>
    	<td width="530"><img src="/sc/img/general/spacer.gif" width="530" height="18" alt=""></td>
	 <td width="67" align="right" valign="top"><a href="#" onClick="javascript:MM_openBrWindow('/sc/print/page_292/','Printer','scrollbars=yes,resizable=no,width=640,height=500');"><img src="/sc/img/general/tools_printthis.gif" alt="友善列印" width="67" height="26" border="0"></a></td>

    </tr>
    <tr> 
        <td colspan=2 width="98%">
	<!-- Include file here -->	
	<TABLE width="100%" align=center class=event-table border=0 cellSpacing=0 cellPadding=2>
<TBODY class=desc>
<TR>
<TD align=left vAlign=top><IMG width=12 height=12 alt="" src="/sc/img/general/buttondot.gif" border=0></TD>
<TD align=left vAlign=top><A class=link href="/sc/index/site_download/page_listofserv/">服务单位名单</A></TD></TR>
<TR>
<TD align=left vAlign=top><IMG width=12 height=12 alt="" src="/sc/img/general/buttondot.gif" border=0></TD>
<TD align=left vAlign=top><A class=link href="/sc/index/site_download/page_document/">文件</A> </TD></TR>
<TR>
<TD width=20 align=left vAlign=top><IMG width=12 height=12 alt="" src="/sc/img/general/buttondot.gif" border=0></TD>
<TD align=left vAlign=top>其他资料</TD></TR></TBODY></TABLE><BR>
<TABLE width="100%" class=event-table border=0 cellSpacing=0 cellPadding=0>
<TBODY>
<TR>
<TD width=30 align=left vAlign=top></TD>
<TD width="100%" align=left vAlign=top>
<TABLE width="100%" border=0 cellSpacing=0 cellPadding=0>
<TBODY>
<TR>
<TD colSpan=2><A class=link href="http://get.adobe.com/reader" target=_blank></A><IMG width=14 height=13 alt="" src="/en/img/general/spacer.gif" border=0><BR><EM><IMG width=14 height=13 alt="" src="/en/img/general/spacer.gif" border=0><BR></EM><IMG width=14 height=13 alt="" src="/en/img/general/spacer.gif" border=0><IMG width=14 height=13 alt="" src="/en/img/general/spacer.gif" border=0><EM><SPAN><EM class=desc_80>以 下 文 件 内 容 须 以 Adobe(R) acrobat(R) Reader 阅 读 , 阅 读 软 件 可 在 Adobe Systems Incorporated 网 站 下 载</EM><A class=link href="http://get.adobe.com/reader" target=_blank><IMG width=88 height=31 align=right alt="取得 Acrobat Reader" src="/sc/img/general/getacro.gif" border=0></A></SPAN></EM><BR><BR></TD></TR>
<TR>
<TD width="50%"><SPAN class=desc_80><IMG width=20 height=20 alt="PDF 文件" src="/sc/img/general/acrobat.gif" border=0 hspace=2>&nbsp;- Adobe Acrobat 文 件</SPAN> </TD>
<TD width="50%"><IMG width=20 height=20 alt="Excel 文件" src="/sc/img/general/excel.gif" border=0>&nbsp;<SPAN class=desc_80>- Microsoft Excel 文 件 </SPAN></TD></TR>
<TR>
<TD width="50%" class=desc_80><IMG width=20 height=20 alt="Word 文件 (文字版)" src="/sc/img/general/word.gif" border=0 hspace=2>&nbsp;- Microsoft Word 文 件 </TD>
<TD width="50%"><IMG width=20 height=20 alt=ZIP文件 src="/sc/img/general/zip.gif" border=0>&nbsp;<SPAN class=desc_80>- Zip 压 缩 档 案</SPAN> </TD></TR>
<TR>
<TD width="50%"><IMG width=20 height=20 alt="PowerPoint 文件" src="/sc/img/general/powerpoint.gif" border=0>&nbsp; <SPAN class=desc_80>- Microsoft PowerPoint 文 件</SPAN> </TD>
<TD width="50%"><IMG width=20 height=20 alt="JPEG 文件" src="/sc/img/general/images.gif" border=0>&nbsp;<SPAN class=desc_80>-&nbsp;JPEG 图 片 档 案</SPAN> </TD></TR></TBODY></TABLE>
<P>&nbsp;&nbsp; <BR><A name=doc></A><B class=topichd><U>其 他 资 料<BR><BR></U></B><STRONG class=subjecthd><BR>家 庭 及 儿 童 福 利 服 务</STRONG> </P>
<TABLE width="100%" border=0 cellSpacing=2 cellPadding=3>
<TBODY class=desc_80>
<TR>
<TD width="60%" align=center vAlign=top bgColor=#762e6a>&nbsp;<FONT color=#ffffff><STRONG>内 容</STRONG></FONT></TD>
<TD width="15%" align=center vAlign=top bgColor=#762e6a><FONT color=#ffffff><STRONG>&nbsp;语 言</STRONG></FONT></TD>
<TD width="25%" align=center vAlign=top bgColor=#762e6a>&nbsp;<FONT color=#ffffff><STRONG>下 载</STRONG></FONT></TD></TR>
<TR>
<TD vAlign=top>慈善/信托基金资料简介</TD>
<TD align=center vAlign=top>中 文</TD>
<TD align=left vAlign=top><A class=link href="/doc_sc/downsecinfo/Trust%20Funds%20Leaflet%202008%20(C).pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/sc/img/general/acrobat.gif" border=0 hspace=2>PDF 文件<BR></A><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2><A class=link href="/doc_sc/downsecinfo/Trust%20Funds%20Leaflet%202008%20(C).doc">Word 文件 (文字版)</A> </TD></TR>
<TR>
<TD>&nbsp;</TD>
<TD align=center vAlign=top>印度语</TD>
<TD align=left vAlign=top><A class=link href="/doc_sc/downsecinfo/Charitable_Trust%20Funds%20(2010)%20(Hindi).pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A>&nbsp;</TD></TR>
<TR>
<TD>&nbsp;</TD>
<TD align=center vAlign=top>印尼语</TD>
<TD align=left vAlign=top><A class=link href="/doc_sc/downsecinfo/Charitable_Trust%20Funds%20(2010)%20(Indonesian).pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A>&nbsp;</TD></TR>
<TR>
<TD>&nbsp;</TD>
<TD align=center vAlign=top>尼泊尔语</TD>
<TD align=left vAlign=top><A class=link href="/doc_sc/downsecinfo/Charitable_Trust%20Funds%20(2010)%20(Nepali).pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A>&nbsp;</TD></TR>
<TR>
<TD>&nbsp;</TD>
<TD align=center vAlign=top>菲律宾语</TD>
<TD align=left vAlign=top><A class=link href="/doc_sc/downsecinfo/Charitable_Trust%20Funds%20(2010)%20(Tagalog).pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A>&nbsp;</TD></TR>
<TR>
<TD>&nbsp;</TD>
<TD align=center vAlign=top>泰语</TD>
<TD align=left vAlign=top><A class=link href="/doc_sc/downsecinfo/Charitable_Trust%20Funds%20(2010)%20(Thai).pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A>&nbsp;</TD></TR>
<TR>
<TD>&nbsp;</TD>
<TD align=center vAlign=top>巴基斯坦语</TD>
<TD align=left vAlign=top><A class=link href="/doc_sc/downsecinfo/Charitable_Trust%20Funds%20(2010)%20(Urdu).pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A>&nbsp;</TD></TR>
<TR>
<TD vAlign=top bgColor=#ffffff>综合家庭服务中心简介</TD>
<TD align=center vAlign=top bgColor=#ffffff>双语</TD>
<TD align=left vAlign=top bgColor=#ffffff><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2><A class=link href="/doc_sc/family/IFSC/IFSC Leaflet (Traditional Chinese and English)_Jan 2016.PDF">PDF 文件</A>&nbsp;</TD></TR>
<TR bgColor=#ffffff>
<TD>&nbsp;</TD>
<TD align=center vAlign=top bgColor=#ffffff>印度语</TD>
<TD align=left vAlign=top bgColor=#ffffff><A class=link href="/doc_sc/family/IFSC/IFSC leaflet_Hindi_Jan 2016.PDF"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A>&nbsp;</TD></TR>
<TR>
<TD bgColor=#ffffff>&nbsp;</TD>
<TD align=center vAlign=top bgColor=#ffffff>印尼语</TD>
<TD align=left vAlign=top bgColor=#ffffff><A class=link href="/doc_sc/family/IFSC/IFSC leaflet_Bahasa Indonesia_Jan 2016.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A>&nbsp;</TD></TR>
<TR>
<TD bgColor=#ffffff>&nbsp;</TD>
<TD align=center vAlign=top bgColor=#ffffff>尼泊尔语</TD>
<TD align=left vAlign=top bgColor=#ffffff><A class=link href="/doc_sc/family/IFSC/IFSC leaflet_Nepali_Jan 2016.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A>&nbsp;</TD></TR>
<TR>
<TD bgColor=#ffffff>&nbsp;</TD>
<TD align=center vAlign=top bgColor=#ffffff>菲律宾语</TD>
<TD bgColor=#ffffff><A class=link href="/doc_sc/family/IFSC/IFSC leaflet_Tagalog_Jan 2016.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A>&nbsp;</TD></TR>
<TR>
<TD bgColor=#ffffff>&nbsp;</TD>
<TD align=center vAlign=top bgColor=#ffffff>泰语</TD>
<TD bgColor=#ffffff><A class=link href="/doc_sc/family/IFSC/IFSC leaflet_Thai_Jan 2016.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A>&nbsp;</TD></TR>
<TR>
<TD bgColor=#ffffff>&nbsp;</TD>
<TD align=center vAlign=top bgColor=#ffffff>巴基斯坦语</TD>
<TD align=left vAlign=top bgColor=#ffffff><A class=link href="/doc_sc/family/IFSC/IFSC leaflet_Urdu_Jan 2016.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A>&nbsp;</TD></TR>
<TR>
<TD align=left vAlign=top>体恤安置及其他房屋协助单张<FONT size=+0></FONT></TD>
<TD align=center vAlign=top>中 文</TD>
<TD align=left vAlign=top><A class=link href="/doc_sc/family/SWD%20leaflet_A%20Tchi-w3c.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top><FONT class=desc>&nbsp;</FONT></TD>
<TD align=center vAlign=top>印度语</TD>
<TD vAlign=top><A class=link href="/doc_sc/family/SWD leaflet_Hindi_w3c.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD>&nbsp;</TD>
<TD align=center vAlign=top>印尼语</TD>
<TD><A class=link href="/doc_sc/family/SWD leaflet_Indonesian_w3c.pdf"><IMG width=20 height=20 align=top alt="`" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A>&nbsp;</TD></TR>
<TR>
<TD>&nbsp;</TD>
<TD align=center vAlign=top>尼泊尔语</TD>
<TD><A class=link href="/doc_sc/family/SWD leaflet_Nepali_w3c.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A>&nbsp;</TD></TR>
<TR>
<TD>&nbsp;</TD>
<TD align=center vAlign=top>菲律宾语</TD>
<TD><A class=link href="/doc_sc/family/SWD leaflet_Tagalog_w3c.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD>&nbsp;</TD>
<TD align=center vAlign=top>泰语</TD>
<TD align=left vAlign=top><A class=link href="/doc_sc/family/SWD leaflet_Thai_w3c.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD>&nbsp;</TD>
<TD align=center vAlign=top>巴基斯坦语</TD>
<TD><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2><A class=link href="/doc_sc/family/SWD leaflet_Urdu_w3c.pdf">PDF 文件</A></TD></TR>
<TR>
<TD align=left vAlign=top bgColor=#ffffff>露宿者福利服务<FONT size=+0></FONT></TD>
<TD align=center vAlign=top bgColor=#ffffff>中 文</TD>
<TD vAlign=top bgColor=#ffffff><A class=link href="/doc_sc/family/Welfare%20Service%20for%20Street%20Sleepers_Chinese.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A><BR><A class=link href="/doc_sc/family/Brief_Street%20Sleepers%20Chinese%20(042013).doc"><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2>Word 文件 (文字版)</A></TD></TR>
<TR>
<TD vAlign=top>支援虐待配偶 / 同居情侣个案的服务</TD>
<TD align=center vAlign=top>&nbsp;双语</TD>
<TD><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2><A class=link href="http://www.swd.gov.hk/vs/doc_sc/publicity/Support%20Services%20to%20Spouse%20Cohabitant%20Battering%20Cases(Chi-SC).pdf">PDF 文件<BR></A><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2><A class=link href="http://www.swd.gov.hk/vs/doc_sc/publicity/Support%20Services%20to%20Spouse_Cohabitant%20Battering%20Cases(clean%20version)(121211)-chi.doc">Word 文件 (文字版)</A></TD></TR>
<TR>
<TD align=left vAlign=top></TD>
<TD align=center vAlign=top>印度语</TD>
<TD align=left vAlign=top><A class=link href="http://www.swd.gov.hk/vs/doc_sc/publicity/leaflet-Hindi.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD>&nbsp;</TD>
<TD align=center vAlign=top>印尼语</TD>
<TD align=left vAlign=top><A class=link href="http://www.swd.gov.hk/vs/doc_sc/publicity/leaflet-Indoesia.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD>&nbsp;</TD>
<TD align=center vAlign=top>尼泊尔语</TD>
<TD><A class=link href="http://www.swd.gov.hk/vs/doc_sc/publicity/leaflet-Nepali.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD>&nbsp;</TD>
<TD align=center vAlign=top>菲律宾语</TD>
<TD><A class=link href="http://www.swd.gov.hk/vs/doc_sc/publicity/leaflet-Tagalog.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD>&nbsp;</TD>
<TD align=center>泰语</TD>
<TD><A class=link href="http://www.swd.gov.hk/vs/doc_sc/publicity/leaflet-Thai%20final%20version.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A>&nbsp;</TD></TR>
<TR>
<TD>&nbsp;</TD>
<TD align=center>巴基斯坦语</TD>
<TD><A class=link href="http://www.swd.gov.hk/vs/doc_sc/publicity/leaflet-Urdu.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A>&nbsp;</TD></TR>
<TR>
<TD vAlign=top bgColor=#ffffff>及早求助制止配偶 / 同居情侣暴力 - 为受虐男士提供的服务 </TD>
<TD align=center vAlign=top bgColor=#ffffff>&nbsp;双语</TD>
<TD bgColor=#ffffff><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2><A class=link href="http://www.swd.gov.hk/vs/doc_sc/publicity/Services%20for%20Battered%20Men%20(2011).pdf">PDF 文件<BR></A><FONT color=#0066cc><U><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2></U></FONT><FONT color=#000000><A class=link href="http://www.swd.gov.hk/vs/doc_sc/publicity/Seek%20Early%20Assistance%20for%20battered%20men-022011-chi.doc">Word 文件 (文字版)</A></FONT></TD></TR>
<TR>
<TD vAlign=top bgColor=#ffffff></TD>
<TD align=center vAlign=top bgColor=#ffffff>印度语</TD>
<TD vAlign=top bgColor=#ffffff><A class=link href="http://www.swd.gov.hk/vs/doc_sc/publicity/SBM%20Hindi%20Leaflet.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD bgColor=#ffffff>&nbsp;</TD>
<TD align=center vAlign=top bgColor=#ffffff>印尼语</TD>
<TD bgColor=#ffffff><A class=link href="http://www.swd.gov.hk/vs/doc_sc/publicity/SBM-Indonesia.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A>&nbsp;</TD></TR>
<TR>
<TD bgColor=#ffffff>&nbsp;</TD>
<TD align=center vAlign=top bgColor=#ffffff>尼泊尔语</TD>
<TD bgColor=#ffffff><A class=link href="http://www.swd.gov.hk/vs/doc_sc/publicity/SBM%20Nepali%20Leaflet.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A>&nbsp;</TD></TR>
<TR>
<TD bgColor=#ffffff>&nbsp;</TD>
<TD align=center vAlign=top bgColor=#ffffff>菲律宾语</TD>
<TD bgColor=#ffffff><A class=link href="http://www.swd.gov.hk/vs/doc_sc/publicity/SBM-Tagalog.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A>&nbsp;</TD></TR>
<TR>
<TD bgColor=#ffffff>&nbsp;</TD>
<TD align=center vAlign=top bgColor=#ffffff>泰语</TD>
<TD bgColor=#ffffff><A class=link href="http://www.swd.gov.hk/vs/doc_sc/publicity/SBM-Thai.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A>&nbsp;</TD></TR>
<TR>
<TD bgColor=#ffffff></TD>
<TD align=center vAlign=top bgColor=#ffffff>巴基斯坦语</TD>
<TD bgColor=#ffffff><A class=link href="http://www.swd.gov.hk/vs/doc_sc/publicity/SBM%20Urdu%20Leaflet.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A>&nbsp;</TD></TR>
<TR>
<TD vAlign=top>意外怀孕了！怎么办？</TD>
<TD align=center vAlign=top>双语</TD>
<TD><A class=link href="/doc_sc/downsecinfo/Unplanned_Pregnancy_Leaflet.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A><BR><A class=link href="/doc_sc/downsecinfo/Unplanned_Pregnancy.doc"><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2>Word 文件 (文字版)</A></TD></TR>
<TR>
<TD>&nbsp;</TD>
<TD align=center vAlign=top>印度语</TD>
<TD><A class=link href="/doc_sc/downsecinfo/UP-Hindi.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A>&nbsp;</TD></TR>
<TR>
<TD>&nbsp;</TD>
<TD align=center vAlign=top>印尼语</TD>
<TD><A class=link href="/doc_sc/downsecinfo/UP-Indonesia.pdf"><IMG width=20 height=20 align=middle alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A>&nbsp;</TD></TR>
<TR>
<TD>&nbsp;</TD>
<TD align=center vAlign=top>尼泊尔语</TD>
<TD><A class=link href="/doc_sc/downsecinfo/UP-Nepali.pdf"><IMG width=20 height=20 align=top alt="PDF Document" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A>&nbsp;</TD></TR>
<TR>
<TD>&nbsp;</TD>
<TD align=center vAlign=top>菲律宾语 </TD>
<TD><A class=link href="/doc_sc/downsecinfo/UP-Tagalog.pdf"><IMG width=20 height=20 align=top alt="PDF Document" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A>&nbsp;</TD></TR>
<TR>
<TD>&nbsp;</TD>
<TD align=center vAlign=top>泰语</TD>
<TD><A class=link href="/doc_sc/downsecinfo/UP-Thai.pdf"><IMG width=20 height=20 align=top alt="PDF Document" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A>&nbsp;</TD></TR>
<TR>
<TD>&nbsp;</TD>
<TD align=center vAlign=top>巴基斯坦语</TD>
<TD><A class=link href="/doc_sc/downsecinfo/UP-Urdu.pdf"><IMG width=20 height=20 align=top alt="PDF Document" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A>&nbsp;</TD></TR>
<TR>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD></TR></TBODY></TABLE><STRONG class=subjecthd><BR>青 少 年 服 务</STRONG> 
<TABLE width="100%" border=0 cellSpacing=2 cellPadding=3>
<TBODY class=desc_80>
<TR>
<TD width="60%" align=center vAlign=top bgColor=#762e6a>&nbsp;<FONT color=#ffffff><STRONG>内 容</STRONG></FONT></TD>
<TD width="15%" align=center vAlign=top bgColor=#762e6a><FONT color=#ffffff><STRONG>&nbsp;语 言</STRONG></FONT></TD>
<TD width="25%" align=center vAlign=top bgColor=#762e6a>&nbsp;<FONT color=#ffffff><STRONG>下 载</STRONG></FONT></TD></TR>
<TR>
<TD vAlign=top>香港青少年服务、戒毒治疗及康复服务及社区发展服务概览</TD>
<TD align=center vAlign=top>中 文</TD>
<TD vAlign=top><A class=link href="/doc_sc/yc/Overview%20on%20Youth%20Ser_201502c.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/sc/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A><BR><A class=link href="/doc_sc/yc/Overview%20on%20Youth%20Ser_201502c.doc"><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/sc/img/general/word.gif" border=0 hspace=2>Word 文件 (文字版)</A></TD></TR>
<TR>
<TD vAlign=top></TD>
<TD align=center vAlign=top>印度语</TD>
<TD align=left vAlign=top><A class=link href="/doc_sc/yc/Hindi_Overview%20on%20Youth%20Ser_201502.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/sc/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top></TD>
<TD align=center vAlign=top>印尼语</TD>
<TD align=left vAlign=top><A class=link href="/doc_sc/yc/Indonesia_Overview%20on%20Youth%20Ser_201502.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/sc/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top></TD>
<TD align=center vAlign=top>尼泊尔语</TD>
<TD align=left vAlign=top><A class=link href="/doc_sc/yc/Nepali_Overview%20on%20Youth%20Ser_201502.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/sc/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top></TD>
<TD align=center vAlign=top>菲律宾语</TD>
<TD align=left vAlign=top><A class=link href="/doc_sc/yc/Tagalog_Overview%20on%20Youth%20Ser_201502.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/sc/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top></TD>
<TD align=center vAlign=top>泰 语</TD>
<TD align=left vAlign=top><A class=link href="/doc_sc/yc/Thai_Overview%20on%20Youth%20Ser_201502.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/sc/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top></TD>
<TD align=center vAlign=top>巴基斯坦语</TD>
<TD align=left vAlign=top><A class=link href="/doc_sc/yc/Urdu_Overview%20on%20Youth%20Ser_201502.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/sc/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD align=left vAlign=top><BR></TD>
<TD align=center vAlign=top></TD>
<TD align=left vAlign=top></TD></TR></TBODY></TABLE><STRONG class=subjecthd>康 复 及 医 务 社 会 服 务</STRONG> 
<TABLE width="100%" border=0 cellSpacing=2 cellPadding=3>
<TBODY class=desc_80>
<TR>
<TD width="60%" align=center vAlign=top bgColor=#762e6a>&nbsp;<FONT color=#ffffff><STRONG>内 容</STRONG></FONT></TD>
<TD width="15%" align=center vAlign=top bgColor=#762e6a><FONT color=#ffffff><STRONG>&nbsp;语 言</STRONG></FONT></TD>
<TD width="25%" align=center vAlign=top bgColor=#762e6a>&nbsp;<FONT color=#ffffff><STRONG>下 载</STRONG></FONT></TD></TR>
<TR>
<TD vAlign=top>怎样根据《精神健康条例 》 (第13 6 章)申请监护令 </TD>
<TD align=center vAlign=top>中 文</TD>
<TD align=left vAlign=top><A class=link href="/doc_sc/downsecinfo/Guardianship%20order_chi_rev%2010%20Nov%202014.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/sc/img/general/acrobat.gif" border=0 hspace=2>PDF 文件<BR></A><A class=link href="/doc_sc/downsecinfo/Guardianship%20order_chi_rev%2010%20Nov%202014.doc"><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/sc/img/general/word.gif" border=0 hspace=2>Word 文件 (文字版)</A></TD></TR>
<TR bgColor=#ffffff>
<TD align=left vAlign=top><A class=link href="/sc/index/site_pubsvc/page_rehab/sub_bookshelff/">沟 通 训 练 相 片 库</A></TD>
<TD>
<P align=left><FONT class=desc face=Arial size=2></FONT>&nbsp;</P></TD>
<TD>&nbsp;</TD></TR>
<TR>
<TD align=left vAlign=top><A class=link href="/sc/index/site_pubsvc/page_rehab/sub_bookshelff/">写 字 系 列／握 笔 姿 势</A></TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD></TR>
<TR>
<TD align=left vAlign=top bgColor=#ffffff><A class=link href="/sc/index/site_pubsvc/page_rehab/sub_listofserv/id_hkpf/">香 港 展 能 精 英 运 动 员 基 金</A></TD>
<TD align=center vAlign=top bgColor=#ffffff><FONT class=desc>&nbsp;</FONT></TD>
<TD vAlign=top bgColor=#ffffff><FONT class=desc>&nbsp;</FONT></TD></TR>
<TR>
<TD align=left vAlign=top>残 疾 人 士 如 何 接 触 及 学 习 资 讯 科 技</TD>
<TD align=center vAlign=top>中 文</TD>
<TD align=left vAlign=top><A class=link href="/doc_sc/downsecinfo/bk_it_c.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/sc/img/general/acrobat.gif" border=0 hspace=2>PDF 文件<BR></A><A class=link href="/doc_sc/downsecinfo/bk_it_c.doc"><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/sc/img/general/word.gif" border=0 hspace=2>Word 文件 (文字版)</A></TD></TR>
<TR>
<TD><BR>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD></TR></TBODY></TABLE><STRONG class=subjecthd>社 会 保 障</STRONG> 
<TABLE width="100%" border=0 cellSpacing=2 cellPadding=3>
<TBODY class=desc_80>
<TR>
<TD width="60%" align=center vAlign=top bgColor=#762e6a>&nbsp;<FONT color=#ffffff><STRONG>内 容</STRONG></FONT></TD>
<TD width="15%" align=center vAlign=top bgColor=#762e6a><FONT color=#ffffff><STRONG>&nbsp;语 言</STRONG></FONT></TD>
<TD width="25%" align=center vAlign=top bgColor=#762e6a>&nbsp;<FONT color=#ffffff><STRONG>下 载</STRONG></FONT></TD></TR>
<TR>
<TD vAlign=top>综合社会保障援助计划小册子</TD>
<TD align=center vAlign=top>中 文</TD>
<TD vAlign=top><A class=link href="/doc_sc/social-sec1/CSSAP052016c.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A><BR><A class=link href="/doc_sc/social-sec1/CSSAP052016c.doc"><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2>Word 文件 (文字版)</A></TD></TR>
<TR bgColor=#ffffff>
<TD vAlign=top>综合社会保障援助指引</TD>
<TD align=center vAlign=top>中 文</TD>
<TD vAlign=top><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2><A class=link href="/doc_sc/social-sec1/CSSAG0716(chi).pdf">PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top>综合社会保障援助计划申请表(样本)</TD>
<TD align=center vAlign=top>双 语</TD>
<TD vAlign=top><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2><A class=link href="/doc_sc/social-sec1/Application%20Form%20for%20CSSA%20Scheme%20(Sample%20only)_2013.pdf">PDF 文件</A></TD></TR>
<TR>
<TR>
<TD vAlign=top bgColor=#ffffff>综合社会保障援助计划简介 (少数族裔语言版)</TD>
<TD align=center vAlign=top bgColor=#ffffff>印度语</TD>
<TD vAlign=top bgColor=#ffffff><A class=link href="/doc_sc/social-sec1/CSSAP0516_Hindi.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top bgColor=#ffffff><FONT class=desc>&nbsp;</FONT></TD>
<TD align=center vAlign=top bgColor=#ffffff>印尼语</TD>
<TD vAlign=top bgColor=#ffffff><A class=link href="/doc_sc/social-sec1/CSSAP0516_Indonesian.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top bgColor=#ffffff><FONT class=desc>&nbsp;</FONT></TD>
<TD align=center vAlign=top bgColor=#ffffff>尼泊尔语</TD>
<TD vAlign=top bgColor=#ffffff><A class=link href="/doc_sc/social-sec1/CSSAP0516_Nepali.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top bgColor=#ffffff><FONT class=desc>&nbsp;</FONT></TD>
<TD align=center vAlign=top bgColor=#ffffff>菲律宾语</TD>
<TD vAlign=top bgColor=#ffffff><A class=link href="/doc_sc/social-sec1/CSSAP0516_Tagalog.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top bgColor=#ffffff><FONT class=desc>&nbsp;</FONT></TD>
<TD align=center vAlign=top bgColor=#ffffff>泰语</TD>
<TD vAlign=top bgColor=#ffffff><A class=link href="/doc_sc/social-sec1/CSSAP0516_Thai.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top bgColor=#ffffff><FONT class=desc>&nbsp;</FONT></TD>
<TD align=center vAlign=top bgColor=#ffffff>巴基斯坦语</TD>
<TD vAlign=top bgColor=#ffffff><A class=link href="/doc_sc/social-sec1/CSSAP0516_Urdu.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top>自力更生支援计划单张</TD>
<TD align=center vAlign=top>中 文</TD>
<TD vAlign=top><A class=link href="/doc_sc/social-sec/SFSI1107c(rev).pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件<BR></A><A class=link href="/doc_sc/social-sec/SFSI1107c(rev).doc"><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2>Word 文件 (文字版)</A>&nbsp;</TD></TR>
<TR>
<TD vAlign=top>豁免计算入息单张 </TD>
<TD align=center vAlign=top>中 文</TD>
<TD vAlign=top><A class=link href="/doc_sc/social-sec/CSSADE0209c.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件<BR></A><A class=link href="/doc_sc/social-sec/CSSADE0209c.doc"><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2>Word 文件 (文字版)</A></TD></TR>
<TR>
<TD vAlign=top bgColor=#ffffff>综援长者广东及福建省养老计划单张</TD>
<TD align=center vAlign=top bgColor=#ffffff>中 文</TD>
<TD vAlign=top bgColor=#ffffff><A class=link href="/doc_sc/social-sec/PCSSALeaflet1015-textonly.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件<BR></A><A class=link href="/doc_sc/social-sec/PCSSALeaflet1015.docx"><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2>Word 文件 (文字版)</A></TD></TR>
<TR>
<TD vAlign=top>公共福利金计划小册子</TD>
<TD align=center vAlign=top>中 文</TD>
<TD vAlign=top><A class=link href="/doc_sc/social-sec/SSAP_0815c.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件<BR></A><A class=link href="/doc_sc/social-sec/SSAP0815c.doc"><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2>Word 文件 (文字版)</A></TD></TR>
<TR>
<TD vAlign=top bgColor=#ffffff>公共福利金计划申请表</TD>
<TD align=center vAlign=top bgColor=#ffffff>双 语</TD>
<TD vAlign=top bgColor=#ffffff><A class=link href="/doc_sc/social-sec1/Application%20Form%20for%20SSA1013.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top>公共福利金计划申请指引</TD>
<TD align=center vAlign=top>中 文</TD>
<TD vAlign=top><A class=link href="/doc_sc/social-sec/Online SSAGN_chi_SWD675A_062016.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top bgColor=#ffffff>公共福利金计划简介 (少数族裔语言版)</TD>
<TD align=center vAlign=top bgColor=#ffffff>印度语</TD>
<TD vAlign=top bgColor=#ffffff><A class=link href="/doc_sc/social-sec1/SSAP1214_Hindi.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top bgColor=#ffffff><FONT class=desc>&nbsp;</FONT></TD>
<TD align=center vAlign=top bgColor=#ffffff>印尼语</TD>
<TD vAlign=top bgColor=#ffffff><A class=link href="/doc_sc/social-sec1/SSAP1214_Indonesian.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top bgColor=#ffffff><FONT class=desc>&nbsp;</FONT></TD>
<TD align=center vAlign=top bgColor=#ffffff>尼泊尔语</TD>
<TD vAlign=top bgColor=#ffffff><A class=link href="/doc_sc/social-sec1/SSAP1214_Nepali.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top bgColor=#ffffff><FONT class=desc>&nbsp;</FONT></TD>
<TD align=center vAlign=top bgColor=#ffffff>菲律宾语</TD>
<TD vAlign=top bgColor=#ffffff><A class=link href="/doc_sc/social-sec1/SSAP1214_Tagalog.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top bgColor=#ffffff><FONT class=desc>&nbsp;</FONT></TD>
<TD align=center vAlign=top bgColor=#ffffff>泰语</TD>
<TD vAlign=top bgColor=#ffffff><A class=link href="/doc_sc/social-sec1/SSAP1214v_Thai.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top bgColor=#ffffff><FONT class=desc>&nbsp;</FONT></TD>
<TD align=center vAlign=top bgColor=#ffffff>巴基斯坦语</TD>
<TD vAlign=top bgColor=#ffffff><A class=link href="/doc_sc/social-sec1/SSAP1214_Urdu.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top>暴力及执法伤亡赔偿计划申请人须知摘要</TD>
<TD align=center vAlign=top>中 文</TD>
<TD vAlign=top><A class=link href="/doc_sc/social-sec/CLEIC%20Brief_Chi_201403.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件<BR></A><A class=link href="/doc_sc/social-sec/CLEIC%20Brief_Chi_201403.doc"><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2>Word 文件 (文字版)</A></TD></TR>
<TR>
<TD vAlign=top bgColor=#ffffff>暴力及执法伤亡赔偿计划单张</TD>
<TD align=center vAlign=top bgColor=#ffffff>双 语</TD>
<TD vAlign=top bgColor=#ffffff><A class=link href="/doc_sc/social-sec/CLEICL1107.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top>暴力及执法伤亡赔偿计划单张 (少数族裔语言版)</TD>
<TD align=center vAlign=top>印度语</TD>
<TD vAlign=top><A class=link href="/doc_sc/social-sec/CLEIC%20-%20Hindi.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top><FONT class=desc>&nbsp;</FONT></TD>
<TD align=center vAlign=top>印尼语</TD>
<TD vAlign=top><A class=link href="/doc_sc/social-sec/CLEIC%20-%20Indonesian.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top><FONT class=desc>&nbsp;</FONT></TD>
<TD align=center vAlign=top>尼泊尔语</TD>
<TD vAlign=top><A class=link href="/doc_sc/social-sec/CLEIC%20-%20Nepali.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top><FONT class=desc>&nbsp;</FONT></TD>
<TD align=center vAlign=middle>菲律宾语</TD>
<TD vAlign=top>
<P align=left><A class=link href="/doc_sc/social-sec/CLEIC%20-%20Tagalog.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></P></TD></TR>
<TR>
<TD vAlign=top><FONT class=desc>&nbsp;</FONT></TD>
<TD align=center vAlign=top>泰语</TD>
<TD vAlign=top><A class=link href="/doc_sc/social-sec/CLEIC%20-%20Thai.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top><FONT class=desc>&nbsp;</FONT></TD>
<TD align=center vAlign=top>巴基斯坦语</TD>
<TD vAlign=top><A class=link href="/doc_sc/social-sec/CLEIC%20-%20Urdu.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top bgColor=#ffffff>暴力及执法伤亡赔偿计划发放细则</TD>
<TD align=center vAlign=top bgColor=#ffffff>中 文</TD>
<TD vAlign=top bgColor=#ffffff><A class=link href="/doc_sc/social-sec/2016_04_CLEIC_Payment%20Schedule_Chi.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件<BR></A><A class=link href="/doc_sc/social-sec/2016_04_CLEIC_Payment Schedule_Chi.doc"><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2>Word 文件 (文字版)</A></TD></TR>
<TR>
<TD vAlign=top>暴力及执法伤亡赔偿委员会主席郭栋明发表的第四十二年度报告书 (截至二零一五年三月三十一日止)</TD>
<TD align=center vAlign=top>中 文</TD>
<TD vAlign=top><A class=link href="/doc_sc/social-sec/42nd%20CLEIC%20Boards%20Annual%20Report_Chi_rev.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件<BR></A><A class=link href="/doc_sc/social-sec/42nd%20CLEIC%20Boards%20Annual%20Report_Chi.docx"><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2>Word 文件 (文字版)</A></TD></TR>
<TR>
<TD vAlign=top bgColor=#ffffff>交通意外伤亡援助计划申请人须知摘要</TD>
<TD align=center vAlign=top bgColor=#ffffff>中 文</TD>
<TD vAlign=top bgColor=#ffffff><A class=link href="/doc_sc/social-sec/TAVA%20Brief_Chi_201403.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件<BR></A><A class=link href="/doc_sc/social-sec/TAVA%20Brief_Chi_201403.doc"><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2>Word 文件 (文字版)</A></TD></TR>
<TR>
<TD vAlign=top>交通意外伤亡援助计划单张</TD>
<TD align=center vAlign=top>双 语</TD>
<TD vAlign=top><A class=link href="/doc_sc/social-sec/TAVA%20Leaflet_2014.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top bgColor=#ffffff>交通意外伤亡援助计划单张 (少数族裔语言版)</TD>
<TD align=center vAlign=top bgColor=#ffffff>印度语</TD>
<TD vAlign=top bgColor=#ffffff><A class=link href="/doc_sc/social-sec/TAVA%20-%20Hindi_2014.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top bgColor=#ffffff><FONT class=desc>&nbsp;</FONT></TD>
<TD align=center vAlign=top bgColor=#ffffff>印尼语</TD>
<TD vAlign=top bgColor=#ffffff><A class=link href="/doc_sc/social-sec/TAVA%20-%20Indonesian_2014.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top bgColor=#ffffff><FONT class=desc>&nbsp;</FONT></TD>
<TD align=center vAlign=top bgColor=#ffffff>尼泊尔语</TD>
<TD vAlign=top bgColor=#ffffff><A class=link href="/doc_sc/social-sec/TAVA%20-%20Nepali_2014.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top bgColor=#ffffff><FONT class=desc>&nbsp;</FONT></TD>
<TD align=center vAlign=top bgColor=#ffffff>菲律宾语</TD>
<TD vAlign=top bgColor=#ffffff><A class=link href="/doc_sc/social-sec/TAVA%20-%20Tagalog_2014.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top bgColor=#ffffff><FONT class=desc>&nbsp;</FONT></TD>
<TD align=center vAlign=top bgColor=#ffffff>泰语</TD>
<TD vAlign=top bgColor=#ffffff><A class=link href="/doc_sc/social-sec/TAVA%20-%20Thai_2014.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top bgColor=#ffffff><FONT class=desc>&nbsp;</FONT></TD>
<TD align=center vAlign=top bgColor=#ffffff>巴基斯坦语</TD>
<TD vAlign=top bgColor=#ffffff><A class=link href="/doc_sc/social-sec/TAVA%20-%20Urdu_2014.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top>交通意外伤亡援助计划发放细则</TD>
<TD align=center vAlign=top>中 文</TD>
<TD vAlign=top><A class=link href="/doc_sc/social-sec/2016_04_TAVA_Payment%20Schedule_Chi.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件<BR></A><A class=link href="/doc_sc/social-sec/2016_04_TAVA_Payment Schedule_Chi.doc"><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2>Word 文件 (文字版)</A></TD></TR>
<TR>
<TD vAlign=top bgColor=#ffffff>交通意外伤亡援助基金二零一四至一五年度年报</TD>
<TD align=center vAlign=top bgColor=#ffffff>中 文</TD>
<TD vAlign=top bgColor=#ffffff><A class=link href="/doc_sc/social-sec/2014-15_TAVA%20Fund%20Annual%20Report_Chi.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件<BR></A><A class=link href="/doc_sc/social-sec/2014-15_TAVA%20Fund%20Annual%20Report_Chi.docx"><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2>Word 文件 (文字版)</A> </TD></TR>
<TR>
<TD vAlign=top>紧急救济单张</TD>
<TD align=center vAlign=top>中 文</TD>
<TD vAlign=top><A class=link href="/doc_sc/social-sec/ERI1007.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件<BR></A><A class=link href="/doc_sc/social-sec/ERI1007(CH).doc"><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2>Word 文件 (文字版)</A><A class=link href="/doc_sc/social-sec/ERI1007.pdf"><FONT color=#000000> </FONT></A></TD></TR>
<TR>
<TD vAlign=top bgColor=#ffffff>紧急救援基金单张</TD>
<TD align=center vAlign=top bgColor=#ffffff>双 语</TD>
<TD vAlign=top bgColor=#ffffff><A class=link href="/doc_sc/social-sec/ERFI0807.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A></TD></TR>
<TR>
<TD vAlign=top>紧急救援基金基金受托人年报(截至二零一五年三月三十一日止)</TD>
<TD align=center vAlign=top>中 文</TD>
<TD vAlign=top><A class=link href="/doc_sc/social-sec/201415_ERF%20Annual%20Report_Chi.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件<BR></A><A class=link href="/doc_sc/social-sec/201415_ERF%20Annual%20Report_Chi.docx"><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2>Word 文件 (文字版)</A></TD></TR>
<TR>
<TD vAlign=top bgColor=#ffffff>紧急救援基金发放细则(仅A项)</TD>
<TD align=center vAlign=top bgColor=#ffffff>中 文</TD>
<TD vAlign=top bgColor=#ffffff><A class=link href="/doc_sc/social-sec/2016_04_ERF_Payment%20Schedule_Chi.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件<BR></A><A class=link href="/doc_sc/social-sec/2016_04_ERF_Payment Schedule_Chi.doc"><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2>Word 文件 (文字版)</A></TD></TR>
<TR>
<TD vAlign=top>社会保障上诉简介</TD>
<TD align=center vAlign=top>中 文</TD>
<TD vAlign=top><A class=link href="/doc_sc/social-sec/SSABL0506c.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件<BR></A><A class=link href="/doc_sc/social-sec/SSABL0506c.doc"><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2>Word 文件 (文字版)</A></TD></TR>
<TR>
<TD vAlign=top bgColor=#ffffff>社会保障上诉委员会第三十七周年报告二零一四/二零一五</TD>
<TD align=center vAlign=top bgColor=#ffffff>中 文</TD>
<TD vAlign=top bgColor=#ffffff><A class=link href="/doc_sc/social-sec/37th%20SSAB%20Annual%20Report%202014-15(Chinese).pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件<BR></A><A class=link href="/doc_sc/social-sec/37th%20SSAB%20Annual%20Report%202014-15(Chinese).doc"><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2>Word 文件 (文字版)</A></TD></TR>
<TR>
<TD><BR>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD></TR></TBODY></TABLE><STRONG class=subjecthd>安 老 服 务</STRONG> 
<TABLE width="100%" border=0 cellSpacing=2 cellPadding=3>
<TBODY class=desc_80>
<TR>
<TD width="60%" align=center vAlign=top bgColor=#762e6a>&nbsp;<FONT color=#ffffff><STRONG>内 容</STRONG></FONT></TD>
<TD width="15%" align=center vAlign=top bgColor=#762e6a><FONT color=#ffffff><STRONG>&nbsp;语 言</STRONG></FONT></TD>
<TD width="25%" align=center vAlign=top bgColor=#762e6a>&nbsp;<FONT color=#ffffff><STRONG>下 载</STRONG></FONT></TD></TR>
<TR>
<TD vAlign=top>安 老 服 务 ( 单 张 )</TD>
<TD align=center vAlign=top>英文及中文</TD>
<TD><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/ERCS/1Bilingual-revised.pdf">PDF 文件</A><BR><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/Leaflet%20on%20Elderly%20Services%20(Text%20Version_Bilingual).doc">Word 文件 (文字版)</A> </TD></TR>
<TR>
<TD>&nbsp;</TD>
<TD align=center vAlign=top>英文及印度文</TD>
<TD><A class=link href="/doc_sc/elderly/ERCS/2Hindi-revised.pdf"><IMG width=20 height=20 alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A>&nbsp;</TD></TR>
<TR>
<TD>&nbsp;</TD>
<TD align=center vAlign=top>英文及印尼文</TD>
<TD><A class=link href="/doc_sc/elderly/ERCS/3Indonesian-revised.pdf"><IMG width=20 height=20 alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A>&nbsp;</TD></TR>
<TR>
<TD>&nbsp;</TD>
<TD align=center vAlign=top>英文及尼泊尔文</TD>
<TD>
<P align=left><A class=link href="/doc_sc/elderly/200912/4Nepali.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A>&nbsp;</P></TD></TR>
<TR>
<TD>&nbsp;</TD>
<TD align=center vAlign=top>英文及菲律宾文</TD>
<TD>
<P align=left><A class=link href="/doc_sc/elderly/ERCS/5Tagalog-revised.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A>&nbsp;</P></TD></TR>
<TR>
<TD>&nbsp;</TD>
<TD align=center vAlign=top>英文及泰国文</TD>
<TD><A class=link href="/doc_sc/elderly/ERCS/6Thai-revised.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A>&nbsp;</TD></TR>
<TR>
<TD vAlign=top>&nbsp;</TD>
<TD align=center vAlign=top>英文及巴基斯坦文</TD>
<TD><A class=link href="/doc_sc/elderly/ERCS/7Urdu-revised.pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2>PDF 文件</A>&nbsp;</TD></TR>
<TR bgColor=#ffffff>
<TD vAlign=top>长 期 护 理 服 务 简 介 ( 单 张 )</TD>
<TD align=center vAlign=top>中 文</TD>
<TD><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/ERCS/Leaflet%20on%20Central%20Waiting%20List%20(Chi)(20130710)-revised.pdf">PDF 文件</A><BR><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/Leaflet%20on%20Long%20Term%20Care%20Services%20(Text%20Version_Chinese).doc">Word 文件 (文字版)</A> </TD></TR>
<TR>
<TD vAlign=top>安 老 服 务 统 一 评 估 机 制 (单 张)</TD>
<TD align=center vAlign=top>中 文 </TD>
<TD><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/ERCS/Leaflet%20on%20SCNAMES%20(Chi)-revised.pdf">PDF 文件</A><BR><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/Leaflet%20on%20SCNAMES%20(Text%20Version_Chinese).doc">Word 文件 (文字版)</A> </TD></TR>
<TR bgColor=#ffffff>
<TD vAlign=top>长 者 地 区 中 心 (单 张)</TD>
<TD align=center vAlign=top>双语</TD>
<TD><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/DECC_New2007(2).pdf">PDF 文件</A> </TD></TR>
<TR bgColor=#ffffff>
<TD vAlign=top><FONT class=desc face=新细明体 size=3>&nbsp;</FONT></TD>
<TD align=center vAlign=top>中文</TD>
<TD><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/DECC_2007_Chinese.doc">Word 文件 (文字版)</A> </TD></TR>
<TR>
<TD vAlign=top>长 者 支 援 服 务 队 (单 张)</TD>
<TD align=center vAlign=top>双语</TD>
<TD><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/STE_New2007(2).pdf">PDF 文件</A> </TD></TR>
<TR>
<TD vAlign=top><FONT class=desc face=新细明体 size=3>&nbsp;</FONT></TD>
<TD align=center vAlign=top>中文</TD>
<TD><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/STE_2007_Chinese.doc">Word 文件 (文字版)</A> </TD></TR>
<TR bgColor=#ffffff>
<TD vAlign=top>长 者 邻 舍 中 心 (单 张)</TD>
<TD align=center vAlign=top>双语</TD>
<TD><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/NEC_rightNew2007(2).pdf">PDF 文件</A> </TD></TR>
<TR bgColor=#ffffff>
<TD vAlign=top>
<P><FONT class=desc face=新细明体 size=3>&nbsp;</FONT></P></TD>
<TD align=center vAlign=top>中文</TD>
<TD vAlign=top><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/NEC_2007_Chinese.doc">Word 文件 (文字版)</A></TD></TR>
<TR>
<TD vAlign=top>长 者 社 区 照 顾 服 务 (单 张)</TD>
<TD align=center vAlign=top>双语</TD>
<TD><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/CCS2007.pdf">PDF 文件</A><BR><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/CCS2007.doc">Word 文件 (文字版)</A> </TD></TR>
<TR bgColor=#ffffff>
<TD vAlign=top bgColor=#ffffff>长 者 日 间 护 理 中 心 / 单 位 (单 张)</TD>
<TD align=center vAlign=top>双语</TD>
<TD><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/DCC%20(Nov%202015).pdf">PDF 文件</A><BR><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/DCC%20(Nov%202015).doc">Word 文件 (文字版)</A> </TD></TR>
<TR>
<TD vAlign=top>改 善 家 居 及 社 区 照 顾 服 务 (单 张) </TD>
<TD align=center vAlign=top>双语</TD>
<TD><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/EHCCS%20(Nov%202015).pdf">PDF 文件</A><BR><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/EHCCS%20(Nov%202015).doc">Word 文件 (文字版)</A> </TD></TR>
<TR bgColor=#ffffff>
<TD vAlign=top>综 合 家 居 照 顾 服 务 (单 张)</TD>
<TD align=center vAlign=top>双语</TD>
<TD><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/IHCS%20(Nov%202015).pdf">PDF 文件</A><BR><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/IHCS%20(Nov%202015).doc">Word 文件 (文字版)</A> </TD></TR>
<TR>
<TD vAlign=top>长 者 暂 托 服 务</TD>
<TD align=center vAlign=top>双 语</TD>
<TD><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/Respite%20Service%20for%20Elders%20(September%202015)%20(rev1).pdf">PDF 文件</A> <BR><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/RSE-September%202015%20(rev1).doc">Word 文件 (文字版)</A></TD></TR>
<TR bgColor=#ffffff>
<TD vAlign=top>长 者 住 宿 照 顾 服 务 (单 张)</TD>
<TD align=center vAlign=top>双 语</TD>
<TD><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/(P13).pdf">PDF 文件</A><BR><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/(P13).doc">Word 文件 (文字版)</A> </TD></TR>
<TR>
<TD vAlign=top>长 者 宿 舍 (单 张)</TD>
<TD align=center vAlign=top>双 语</TD>
<TD><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/(P14).pdf">PDF 文件</A><BR><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/(P14).doc">Word 文件 (文字版)</A> </TD></TR>
<TR bgColor=#ffffff>
<TD vAlign=top>安 老 院 (单 张)</TD>
<TD align=center vAlign=top>双 语</TD>
<TD><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/(P15).pdf">PDF 文件</A><BR><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/(P15).doc">Word 文件 (文字版)</A> </TD></TR>
<TR>
<TD vAlign=top>护 理 安 老 院 (单 张)</TD>
<TD align=center vAlign=top>双 语</TD>
<TD><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/(P16).pdf">PDF 文件</A><BR><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/(P16).doc">Word 文件 (文字版)</A> </TD></TR>
<TR bgColor=#ffffff>
<TD vAlign=top>护 养 院 (单 张)</TD>
<TD align=center vAlign=top>双 语</TD>
<TD><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/(P17).pdf">PDF 文件</A><BR><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/(P17).doc">Word 文件 (文字版)</A> </TD></TR>
<TR>
<TD vAlign=top>长 者 紧 急 住 宿 照 顾 服 务 (单 张)</TD>
<TD align=center vAlign=top>双 语</TD>
<TD><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/(P18).pdf">PDF 文件</A><BR><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/(P18).doc">Word 文件 (文字版)</A> </TD></TR>
<TR bgColor=#ffffff>
<TD vAlign=top>长 者 住 宿 暂 托 服 务 (单 张)</TD>
<TD align=center vAlign=top>双 语</TD>
<TD><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/ERCS/LeafletRRSE%2020150730.pdf">PDF 文件</A><BR><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/ERCS/LeafletRRSE%2020150730-1.doc">Word 文件 (文字版)</A></TD></TR>
<TR>
<TD vAlign=top>疗 养&nbsp;护 理 单 位 (单 张)</TD>
<TD align=center vAlign=top>双 语</TD>
<TD><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/ERCS/P20.pdf">PDF 文件</A><BR><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/ERCS/(P20).doc">Word 文件 (文字版)</A> </TD></TR>
<TR bgColor=#ffffff>
<TD vAlign=top>紧 急 召 援 系 统 ( 单 张 )</TD>
<TD align=center vAlign=top>中 文</TD>
<TD><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/EAS%20Leaflet_July%202015(Chin).pdf">PDF 文件</A><BR><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/EAS%20leaflet%20(Chi)%207%20May%202015.doc">Word 文件 (文字版)</A> </TD></TR>
<TR>
<TD vAlign=top>支 援 照 顾 者 服 务 (单 张)</TD>
<TD align=center vAlign=top>双 语</TD>
<TD><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/carers_leaflet_detail(2).pdf">PDF 文件</A><BR><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/carers_leaflet_detail.doc">Word 文件 (文字版)</A> </TD></TR>
<TR bgColor=#ffffff>
<TD vAlign=top>长 者 社 区 支 援 服 务 小 锦 囊</TD>
<TD align=center vAlign=top>中 文</TD>
<TD><IMG width=20 height=20 align=top alt="PDF 文件" src="/en/img/general/acrobat.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/Useful%20Tips%20on%20CSS%20Chi_Sept08.pdf">PDF 文件</A><BR><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/en/img/general/word.gif" border=0 hspace=2><A class=link href="/doc_sc/elderly/Useful%20Tips%20on%20Community%20Support%20Services%20for%20the%20Elderly_EB%20(chi).doc">Word 文件 (文字版)</A> </TD></TR>
<TR>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD></TR></TBODY></TABLE><STRONG class=subjecthd><BR>治 疗 中 心 ( 药 物 倚 赖 者 治 疗 及 康 复 中 心 ) 发 牌 制 度</STRONG> 
<TABLE width="100%" border=0 cellSpacing=2 cellPadding=3>
<TBODY class=desc_80>
<TR>
<TD width="60%" align=center vAlign=top bgColor=#762e6a>&nbsp;<FONT color=#ffffff><STRONG>内 容</STRONG></FONT></TD>
<TD width="15%" align=center vAlign=top bgColor=#762e6a><FONT color=#ffffff><STRONG>&nbsp;语 言</STRONG></FONT></TD>
<TD width="25%" align=center vAlign=top bgColor=#762e6a>&nbsp;<FONT color=#ffffff><STRONG>下 载</STRONG></FONT></TD></TR>
<TR>
<TD align=left vAlign=top>&nbsp;认 可 人 士 名 册<A class=link href="http://www.info.gov.hk/bd/chineseT/inform/index_ap.html"><BR>http://www.info.gov.hk/bd/chineseT/inform/index_ap.html</A> </TD>
<TD align=center vAlign=top>中 文</TD>
<TD align=left vAlign=top></TD></TR>
<TR>
<TD align=left vAlign=top bgColor=#ffffff>&nbsp;消 防 装 置 承 办 商<A class=link href="http://www.hkfsd.gov.hk/home/sc/cert.html"><BR>http://www.hkfsd.gov.hk/home/chi/cert.html</A> </TD>
<TD align=center vAlign=top bgColor=#ffffff>中 文</TD>
<TD bgColor=#ffffff>&nbsp;</TD></TR>
<TR>
<TD align=left vAlign=top>认 可 / 已 批 核 的 消 防 装 置 及 设 备<A class=link href="http://www.hkfsd.gov.hk/home/sc/accep_eq.html"><BR>http://www.hkfsd.gov.hk/home/chi/accep_eq.html</A> </TD>
<TD align=center vAlign=top>中 文</TD>
<TD>&nbsp;</TD></TR>
<TR>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD></TR></TBODY></TABLE><STRONG class=subjecthd><BR>临床心理服务</STRONG> 
<TABLE width="100%" border=0 cellSpacing=2 cellPadding=3>
<TBODY class=desc_80>
<TR>
<TD width="60%" align=center vAlign=top bgColor=#762e6a>&nbsp;<FONT color=#ffffff><STRONG>内 容</STRONG></FONT></TD>
<TD width="15%" align=center vAlign=top bgColor=#762e6a><FONT color=#ffffff><STRONG>&nbsp;语 言</STRONG></FONT></TD>
<TD width="25%" align=center vAlign=top bgColor=#762e6a>&nbsp;<FONT color=#ffffff><STRONG>下 载</STRONG></FONT></TD></TR>
<TR>
<TD align=left vAlign=top>&nbsp;单张 : 究竟心理治疗是什么 ? </TD>
<TD align=center vAlign=top>中 文</TD>
<TD align=left vAlign=top><A class=link href="http://www.swd.gov.hk/doc_sc/Clinical%20Psychological%20Service%20Branch-CPSB/Pamphlets/(2)%20What%20is%20Psychotherapy%20(Chinese).pdf"><IMG width=20 height=20 align=top alt="PDF 文件" src="/sc/img/general/acrobat.gif" border=0 hspace=2>PDF 文件<BR></A><A class=link href="/doc_sc/Clinical%20Psychological%20Service/(2)%20What%20is%20psychotherapy%20(Chinese).doc"><IMG width=20 height=20 align=top alt="Word 文件 (文字版)" src="/sc/img/general/word.gif" border=0 hspace=2>Word 文件 (文字版)</A></TD></TR></TBODY></TABLE>
<P></P>
<P>&nbsp;</P></TD></TR></TBODY></TABLE>
	<p>&nbsp;</p>
	<!-- Include file end -->
	</td>
    </tr>
    <tr> 
	<td colspan=2>&nbsp;</td>
    </tr>
    </table>
   </td>
  </tr>
</table>
	    <!-- Content end here -->
	    <br>
	     <table width="100%">
	     	  <tr valign="top"> 
		    <td colspan="2" background="/sc/img/clf/botdot.gif"> <img src="/sc/img/general/spacer.gif" width="139" height="2" alt=""></td>
		  </tr>
		  <tr valign="top"> 
		    <td align="left" class="copyright">2005<img src="/sc/img/general/copy.gif" alt="copyright logo" width="12" height="11"> | <a href="/sc/index/site_notice/" class="footerlink">重要告示</a> | <a href="/sc/index/site_privacypolicy/" class="footerlink">私隐政策</a></td>
		    <td align="right" class="copyright">修订日期: 2016 年 7 月 27 日</td>
		  </tr>
  	     </table>
	   </td>
        </tr>
      </table></td>
  </tr>
</table>
<script type="text/javascript"> 


function eventScroll(direction){
	    
		var objMarquee = document.getElementById("rightScroll"); 
        if (direction<0) 
                objMarquee.direction = "down"; 
        else 
                objMarquee.direction = "up"; 

		
}

changeFontTitle(myfonttitle);

/*
$(function () {
        
        $('div.event marquee').mouseover(function () {
            $(this).trigger('stop');
        }).mouseout(function () {
            $(this).trigger('start');
        });
    }); 
	
	$(function () {
        
        $('div.newsticker marquee').mouseover(function () {
            $(this).trigger('stop');
        }).mouseout(function () {
            $(this).trigger('start');
        });
    }); 
	
	
	$('div.event marquee').marquee('pointer').mouseover(function () {
  $(this).trigger('stop');
}).mouseout(function () {
  $(this).trigger('start');
}).mousemove(function (event) {
  if ($(this).data('drag') == true) {
    this.scrollLeft = $(this).data('scrollX') + ($(this).data('x') - event.clientX);
  }
}).mousedown(function (event) {
  $(this).data('drag', true).data('x', event.clientX).data('scrollX', this.scrollLeft);
}).mouseup(function () {
  $(this).data('drag', false);
});

$('div.newsticker marquee').marquee('pointer').mouseover(function () {
  $(this).trigger('stop');
}).mouseout(function () {
  $(this).trigger('start');
}).mousemove(function (event) {
  if ($(this).data('drag') == true) {
    this.scrollLeft = $(this).data('scrollX') + ($(this).data('x') - event.clientX);
  }
}).mousedown(function (event) {
  $(this).data('drag', true).data('x', event.clientX).data('scrollX', this.scrollLeft);
}).mouseup(function () {
  $(this).data('drag', false);
});
*/

</script> 
</body>
</html>

"""
soup = BeautifulSoup(html_doc, "lxml")
print '---------------------------------'

try:
    con1 = soup.find('table', width = '625')
    con2 = soup.find('div', class_ = 'col-main')
    con3 = soup.find('td', width = '579')
    if con1:
        print '+++++++++++++++++++'
        all_p = con1.get_text().strip()
    elif con2:
        print '-------------------'
        all_p = con2.get_text().strip()
    elif con3:
        print '///////////////////'
        all_p = con3.get_text().strip()

    
    all_p = all_p.encode('GBK', 'ignore')

    all_p = re.sub(r'\n', "", all_p)
    all_p = re.sub(r'\t', "", all_p)
    content = all_p
    print all_p
except:
    print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'

print '---------------------------------'  
