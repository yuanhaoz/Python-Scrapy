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

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html lang="zh-cn" dir="ltr">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>卫 生 署 - 表格一览表</title>
	<meta name="keywords" content="Welcome message,Welcome message,">
    <meta http-equiv="Content-Style-Type" content="text/css">
    <link rel="stylesheet" href="../../../css/reset.css" type="text/css" media="screen">
  	<link rel="stylesheet" type="text/css" href="../../../css/layout.css">
    <link rel="stylesheet" type="text/css" href="../../../css/default.css">
 	<link rel="stylesheet" type="text/css" href="../../../css/typography.css">    
    <link rel="stylesheet" id="theme" href="../../../common/css/Theme/default-green.css" type="text/css">
	<link rel="stylesheet" id="themeMenu" href="../../../common/css/Theme/green_menu.css" type="text/css">    
    <link rel="stylesheet" href="../../../css/default-content.css" type="text/css">
    <script type="text/javascript" src="../../../js/jquery-1.8.1.min.js"></script>
    <script type="text/javascript" src="../../../js/jquery.easing.1.3.js"></script>
	<script type="text/javascript" src="../../../js/jquery.simplyscroll-1.0.4.js"></script>
    <script type="text/javascript" src="../../../js/jquery-ui.min.js"></script>    
   	<script type="text/javascript" src="../../../js/global.js"></script>
  	<script type="text/javascript" src="../../../js/print_version.js"></script>
	<script type="text/javascript" src="../../../js/menu_sc.js"></script>   
</head>
<!--<body id="page_bg" onLoad="MM_preloadImages('../images/backBtnOver.png')">-->
<body id="page_bg">
  <div id="skipwrapper">
        <a name="skiptocontent" id="skiptocontent" href="#mainContent" class="access">跳至主要内容</a>
    </div>    
	<script type="text/javascript">getHeader();</script> 
    <div class="header_inside"><div  id="titleImage"></div></div>
<div class="header2_shadow">
        <!--<div id="rightImage" style="float:right; padding:10px 20px;"></div>-->
<div style="width:180px; margin-top:2px;">
<span class="leftMenu" style="float: left;">

<span id="left_menu" class="left_menu">
<script type="text/javascript">leftmenu();</script><span id="w3c" style="padding-bottom:5px; padding-right:15px;"><script type="text/javascript">var wcag2_link = "http://www.w3.org/WAI/WCAG2AA-Conformance";var wacg2_img = "../../../images/w3c_wcag2_0.gif";var html4_link = "http://validator.w3.org/check?uri=referer";var html4_img = "../../../images/w3c_html4_01.gif";	genW3C();getIPv6();</script></span>
</span>
</span>

<div style="width: 180px; text-align: center; padding-top: 5px; padding-bottom: 10px;">
<script type="text/javascript">
	//genBanner();
</script>
</div>


</div>
	<div style="margin-top:0px; margin-left:180px;">
      
    <script type="text/javascript">
		mainWidth();
	</script>

        <div style="margin:10px 0 18px 0;"> 

    	</div> 
        <div>       	  	      
    	<div id="mainContent" class="mainContent"><a name="mainContent"></a>
		 <div><span class="header"><a href="../../../scindex.html">主页</a> &gt;&gt; <a class="navlink" href="../useful.html" >有用资料</a>  &gt;&gt;  表格一览表 
 </span></div>
          
           <a name="top"></a>
       <h1 class="access">有用资料</h1>
<!-- BEGIN CONTENT -->
   
  <!-- BEGIN CONTENT --> 
  <h2> 表  格  一  览  表 </h2> 
  <table style="width:100%" border="0" cellspacing="0" cellpadding="2"> 
   <tbody>
    <tr> 
     <td style="width:3%"><img src="../../images/general/arr1.gif"  alt=""></td> 
     <td style="width:97%"> <span class="subhd"><a href="useful_forms_ani.html"> 动  物  ( 实  验  管  制  )</a></span> ( 只 备 繁 体 版 )</td> 
    </tr> 
    <tr> 
     <td style="width:3%">&nbsp;</td> 
     <td style="width:97%" class="subhd">&nbsp;</td> 
    </tr> 
    <tr> 
     <td style="width:3%"><img src="../../images/general/arr1.gif"  alt=""></td> 
     <td style="width:97%" class="subhd"><a href="useful_forms_dai.html"> 药  物  滥  用  资  料  </a></td> 
    </tr> 
    <tr> 
     <td style="width:3%">&nbsp;</td> 
     <td style="width:97%" class="subhd">&nbsp;</td> 
    </tr> 
    <tr> 
     <td style="width:3%"><img src="../../images/general/arr1.gif"  alt=""></td> 
     <td style="width:97%"><span  class="subhd"><a href="useful_forms_Exemption.html">受  规  管  产  品  的  豁  免  </a></span>(暂  时  只  备  英  文  版 )</td> 
    </tr> 
    <tr> 
     <td style="width:3%">&nbsp;</td> 
     <td style="width:97%" class="subhd">&nbsp;</td> 
    </tr> 
    <tr> 
     <td style="width:3%"><img src="../../images/general/arr1.gif"  alt=""></td> 
     <td style="width:97%"> <span class="subhd"> <a href="useful_forms_fhs.html"> 家  庭  健  康  服  务  </a></span>( 只 备 繁 体 版 )</td> 
    </tr> 
    <tr> 
     <td style="width:3%">&nbsp;</td> 
     <td style="width:97%" class="subhd">&nbsp;</td> 
    </tr> 
    <tr> 
     <td style="width:3%"><img src="../../images/general/arr1.gif"  alt=""></td> 
     <td style="width:97%"> <span class="subhd"><a href="useful_forms_hi.html"> 医  护  机  构  </a></span>( 只 备 繁 体 版 )</td> 
    </tr> 
    <tr> 
     <td style="width:3%">&nbsp;</td> 
     <td style="width:97%" class="subhd">&nbsp;</td> 
    </tr> 
    <tr> 
     <td style="width:3%"><img src="../../images/general/arr1.gif"  alt=""></td> 
     <td style="width:97%"> <span class="subhd"><a href="useful_forms_hp.html"> 医  护  专  业  人  员  </a></span></td> 
    </tr> 
    <tr> 
     <td style="width:3%">&nbsp;</td> 
     <td class="subhd">&nbsp;</td> 
    </tr> 
    <tr> 
     <td style="width:3%"><img src="../../images/general/arr1.gif"  alt=""></td> 
     <td style="width:97%"> <span class="subhd"><a href="files/2293.pdf">爱  滋  病  病  毒  / 爱  滋  病  呈  报  表  格 </a></span> ( 只 备 繁 体 版  )</td> 
    </tr> 
    <tr> 
     <td style="width:3%">&nbsp;</td> 
     <td style="width:97%" class="subhd">&nbsp;</td> 
    </tr> 
    <tr> 
     <td style="width:3%"><img src="../../images/general/arr1.gif"  alt=""></td> 
     <td style="width:97%"> <span class="subhd"><a href="useful_forms_hot.html"> 人  体  器  官  移  植</a></span></td> 
    </tr> 
    <tr> 
     <td style="width:3%">&nbsp;</td> 
     <td style="width:97%" class="subhd">&nbsp;</td> 
    </tr> 
    <tr> 
     <td style="width:3%"><img src="../../images/general/arr1.gif"  alt=""></td> 
     <td style="width:97%"> <span class="subhd"><a href="useful_forms_ncm.html"> 申  报  出  生  婴  儿  患  有  先  天  性  异  常</a></span> ( 只  有  英  文  版  )</td> 
    </tr> 
    <tr> 
     <td style="width:3%">&nbsp;</td> 
     <td style="width:97%" class="subhd">&nbsp;</td> 
    </tr> 
    <tr> 
     <td style="width:3%"><img src="../../images/general/arr1.gif"  alt=""></td> 
     <td style="width:97%"> <span class="subhd"><a href="useful_forms_pp.html"> 药  剂  及  毒  药  </a> </span></td> 
    </tr> 
    <tr> 
     <td style="width:3%">&nbsp;</td> 
     <td style="width:97%" class="subhd">&nbsp;</td> 
    </tr> 
    <tr> 
     <td style="width:3%"><img src="../../images/general/arr1.gif"  alt=""></td> 
     <td style="width:97%" class="subhd"><a href="useful_forms_pne.html"> 肺  尘  埃  沉  着  病  ( 补  偿  )</a></td> 
    </tr> 
    <tr> 
     <td style="width:3%">&nbsp;</td> 
     <td style="width:97%" class="subhd">&nbsp;</td> 
    </tr> 
    <tr> 
     <td style="width:3%"><img src="../../images/general/arr1.gif"  alt=""></td> 
     <td style="width:97%"> <span class="subhd"><a href="useful_forms_qpd.html"> 预  防  及  控  制  疾  病 </a></span>( 只 备 繁 体 版 )</td> 
    </tr> 
    <tr> 
     <td>&nbsp;</td> 
     <td class="subhd">&nbsp;</td> 
    </tr>     
    <tr> 
     <td><img src="../../images/general/arr1.gif"  alt=""></td> 
     <td style="width:97%"> <span class="subhd"><a href="useful_forms_top.html"> 终  止  妊  娠 </a></span>( 只 备 繁 体 版 )</td> 
    </tr> 
   </tbody> 
  </table> 
<p class="content"> 根  据  《 <a href="http://www.ogcio.gov.hk/sc/regulation/eto/index.htm" rel="external"><span class="access">这连结会以新视窗打开。</span> 电  子  交  易  条  例  </a> 》 提  交  电  子  资  讯  的  <a href="http://www.ogcio.gov.hk/sc/regulation/eto/ordinance/submission/" rel="external"><span class="access">这连结会以新视窗打开。</span> 一  般  规  格  、 方  式  及  程  序  </a></p> 
  <!-- END CONTENT -->
  
 <!-- END CONTENT -->

       
    	</div>
        <div  id="btnImage"></div>
	</div> 
    </div>
        <div style="margin-top:0px; margin-left:180px; font-size: 1.2em; color: #1e486e;">
            <div style="float:left; width:100%; padding-top:2px;">       
                <div style="padding-bottom:5px;">
                    <span class="ft_split_line">&nbsp;</span>
                    <span style="float:left; width:400px; padding-left:5px"><script type="text/javascript">footer()</script></span>
                    <span style="float:right; width:300px; text-align:right; padding-right:5px">修订日期 : 二零一五年二月二十七日</span>
                </div>
            </div>
        </div> 
    </div>    
	<script type="text/javascript">init();</script>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, "lxml")
print '---------------------------------'
try:
    all_p = soup.find_all('div', id = 'mainContent')[0].get_text().strip()
    all_p = all_p.encode('GBK', 'ignore')
    all_p = re.sub(r'footer\(\)', "", all_p)
    all_p = re.sub(r'init\(\)\;', "", all_p)
    all_p = re.sub(r'\n', "", all_p)
    all_p = re.sub(r'\t', "", all_p)
    print all_p
except:
    print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
print '---------------------------------'  

# # 打开一个文件
# fo = open("D:\\Workspace\\Python\\Scrapy\\test\\1.txt", "wb+")
# fo.write( all_p);
# fo.close()