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

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-cn" lang="zh-cn"> 

<head>
<title>香港海关</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<script type="text/javascript" src="/pda/js/script_sc.js"></script>
  
</head> <body onload="autoResize();" style="text-align : left;">
<script type="text/javascript">
Header_sc()
</script>

<div id="header">牌照及许可证的申请</div>


<p>任何人士如欲进口、出口、供应、取得、经营或处理、管有或制造受管制化学品，必须视情况申请下列牌照、许可证、授权书或储存批准书：</p>
<table class="tbl_format" border="0" cellspacing="0" cellpadding="0" summary="Hong Kong Customs and Excise Department - Licence and Permit Application 香港海关 - 牌照及许可证的申请">
<tbody>
<tr>
<th valign="top" class="th_width_0">类别</th><th valign="top" class="th_width_1">表格号码</th><th valign="top" class="th_width_2">证明文件</th><th align="left" valign="top" class="th_width_3">费用</th>
</tr>
<tr>
<td valign="top">牌照申请书</td>
<td valign="top"><a class="pdf" href="/filemanager/common/pdf/pdf_forms/ced359.pdf" target="_blank" title="按此去CED 359">CED 359<span class="tblank"> (在新视窗开启) </span></a></td>
<td valign="top">
<ul>
<li>商业登记证；</li>
<li>公司注册证书；</li>
<li>租约等</li>
</ul>
</td>
<td align="left" valign="top">$1,530<br />须每年续牌</td>
</tr>
<tr>
<td valign="top">受管制化学品进口或出口授权书</td>
<td valign="top"><a class="pdf" href="/filemanager/common/pdf/pdf_forms/ced312.pdf" target="_blank" title="按此去CED 312">CED 312<span class="tblank"> (在新视窗开启) </span></a>（入口）或<br /><a class="pdf" href="/filemanager/common/pdf/pdf_forms/ced313.pdf" target="_blank" title="按此去CED 313">CED 313<span class="tblank"> (在新视窗开启) </span></a>（出口）</td>
<td valign="top">
<ul>
<li>发票；</li>
<li>付货通知单；</li>
<li>空运提单或提单；</li>
<li>销售合同；</li>
<li>由进口商发出声明进口目的的函件；</li>
<li>由进口国家签发的进口授权书等</li>
</ul>
</td>
<td align="left" valign="top">免费</td>
</tr>
<tr>
<td valign="top">转口受管制化学品移走许可证</td>
<td valign="top"><a class="pdf" href="/filemanager/common/pdf/pdf_forms/ced347.pdf" target="_blank" title="按此去CED 347">CED 347<span class="tblank"> (在新视窗开启) </span></a></td>
<td valign="top">
<ul>
<li>商业登记证；</li>
<li>电话费单；</li>
<li>提单或空运提单；</li>
<li>付货通知单；</li>
<li>发票；</li>
<li>销售合同；</li>
<li>由进口商发出声明进口目的的函件；</li>
<li>由进口国家签发的进口授权书等</li>
</ul>
</td>
<td align="left" valign="top">每张许可证$950</td>
</tr>
<tr>
<td valign="top">香港法例第145章《化学品管制条例》<a href="http://www.legislation.gov.hk/blis_ind.nsf/CurAllChinDoc/4842AD9BAF3FD4DD48256528002E5DE1?OpenDocument" target="_blank" title="按此去附表1">附表1<span class="tblank"> (在新视窗开启) </span></a>或<a href="http://www.legislation.gov.hk/blis_ind.nsf/76544F70F760CCBD482564840019D2F7/40DA6E60BAE1628B48257D9D00262230?OpenDocument" target="_blank" title="按此去2">2<span class="tblank"> (在新视窗开启) </span></a>的受管制化学品的储存批准书</td>
<td valign="top"><a class="pdf" href="/filemanager/common/pdf/pdf_forms/ced360_c.pdf" target="_blank" title="按此去CED 360">CED 360<span class="tblank"> (在新视窗开启) </span></a></td>
<td valign="top">
<ul>
<li>香港身份证副本；</li>
<li>商业登记证副本；</li>
<li>电话费单等</li>
</ul>
</td>
<td align="left" valign="top">免费</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<h1>填妥的申请表请交回：</h1>
<p>香港海关<br />海关毒品调查科<br />化学品管制课<br />香港<br />北角渣华道222号<br />海关总部大楼3楼</p>
<h1>查询</h1>
<table class="blankstyle style_125" border="0" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td valign="top">电话： &nbsp;</td>
<td valign="top">(852) 2541 4383</td>
</tr>
<tr>
<td valign="top">传真：</td>
<td valign="top">(852) 2123 9152</td>
</tr>
<tr>
<td valign="top">电邮：</td>
<td valign="top"><a href="mailto:cedcdibccg@customs.gov.hk" title="按此去cedcdibccg@customs.gov.hk">cedcdibccg@customs.gov.hk</a></td>
</tr>
</tbody>
</table>





<script type="text/javascript">
Footer_sc()
</script>

</body>
</html>

"""
soup = BeautifulSoup(html_doc, "lxml")
print '---------------------------------'
# all_p = soup.find_all('table', id = 'inner-page')[0].get_text().strip() # 网页检查
all_p = soup.get_text().strip() # 网页源代码

# all_p = re.sub(r'\n', "", all_p)
# all_p = re.sub(r'\t', "", all_p)
all_p = all_p.encode('GBK', 'ignore')
print all_p
print '---------------------------------'  