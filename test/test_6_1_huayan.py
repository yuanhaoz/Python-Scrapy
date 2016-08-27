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
<html lang="zh-cn"><!-- InstanceBegin template="/Templates/TChinese_Template2.dwt" codeOutsideHTMLIsLocked="false" -->
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<!-- InstanceBeginEditable name="doctitle" -->
<title>政府化验所 - 分析及咨询事务部 - 中药组</title>
<!-- InstanceEndEditable -->
<!-- InstanceBeginEditable name="head" -->
<meta name="keywords" content="">
<meta name="description" content="">
<!-- InstanceEndEditable -->
    <link href="../css/screen_sc.css" rel="stylesheet" type="text/css" media="screen">
    <link href="../css/print_sc.css" rel="stylesheet" type="text/css" media="print">
    <link rel="stylesheet" type="text/css" href="../css/superfish_sc.css" media="screen">
    <link rel="stylesheet" type="text/css" href="../css/superfish-vertical.css" media="screen">
    <script type="text/javascript" src="../js/lastupdate.js"></script>
    <script type="text/javascript" src="../js/common.js"></script>
    <script type="text/javascript" src="../menu.js"></script>
    <script type="text/javascript" src="../js/sc_menu.js"></script>
</head>
<body id="page_bg" onload="Javascript:PageOnLoad();">
<div id="wrapper">
    <script type="text/javascript">
	    showframe();
    </script>
<div id="middle_zone">	
<div id="left_zone">
    <script type="text/javascript">
	    showmenu();
    </script>	
<div id="icon_zone">
<!-- InstanceBeginEditable name="icons" -->
<!-- InstanceEndEditable -->
</div>
</div>
    <script type="text/javascript">
	    showprint();
    </script> 
<div id="right_zone">
	<div id="right_zonetitle">
    <!-- InstanceBeginEditable name="sectiontitle" -->
		<img src="../images/title_image.gif" alt="政府化验所标志" align="right"><h1>分析及咨询事务部</h1>
    <!-- InstanceEndEditable -->
  </div>
  <div id="right_zonecontent">
    <!-- InstanceBeginEditable name="content" -->
    <h2>中 药 组</h2>
    <p class="shortcut">[ <a href="#AboutTheSection">本组简介</a> | <a href="#responsibilities">职责范围</a> | <a href="#personnel">主要人员</a> | <a href="#QA">质量保证</a> | <a href="#instrument">主要仪器</a> | <a href="#targets">目标及指针</a> ]<br>
      [ <a href="abt_aasd_cmmc.htm">上一页</a> | <a href="abt_aasd_eca.htm">下一页</a> ]</p>    
    <h3><a name="AboutTheSection" id="AboutTheSection"></a>本 组 简 介</h3>
    <div class="photo_left"><img border="0" src="../g/cm-1.jpg" alt="中药样本" width="300" height="195"><br>
      <span class="gallery_caption">中药样本</span></div>
    <p>本 组 在 1998 年 10 月 7 日 成 立 ， 为 监 察 市 面 上 出 售 的 中 成 药 及 中 草 药 之 安 全 使 用 ， 提 供 测 试 及 相 关 的 技 术 支 援 ， 及 
      发 展 中 药 的 化 学 分 析 方 法 。</p>
    <p>&nbsp;</p>
    <p>&nbsp;</p>
    <p>&nbsp;</p>
    <p>&nbsp;</p>
    <p>&nbsp;</p>
    <hr>
    <h3><a name="responsibilities" id="responsibilities"></a>职 责 范 围</h3>
    <p>测 试 由 卫 生 署 所 提 供 的 中 成 药 及 中 草 药 样 本 。</p>
    <p>本 组 对 市 面 上 出 售 的 中 成 药 及 中 草 药 样 本 进 行 安 全 和 质 量 测 试 。 其 中 包 括 重 金 属 ／ 有 毒 元 素 和 农 药 残 留 的 含 量 测 定 ， 同 时 亦 协 助 卫 生 署 调 查 怀 疑 中 药 中 毒 及 中 药 不 良 反 应 个 案。</p>
    <p>有 关 香 港 实 验 所 认 可 计 划 之 认 可 测 试 的 详 细 资 料， 请 在 <a href="../g/HOKLAS_CM.pdf" target="_blank">此 按</a>。</p>
    <hr>
    <h3><a name="personnel" id="personnel"></a>主 要 人 员</h3>
    <p align="center">高级化验师：邓炜堂 博士<br>
      (电话 : 2319-8398 电邮地址： <a href="mailto:wttang@govtlab.gov.hk">wttang@govtlab.gov.hk</a>)</p>
    <table width="100%" border="0" cellpadding="5" cellspacing="1" class="tableborder">
      <tr>
        <th width="70%" class="chiTabTitle"><p>化验师<br>
          (电邮地址)</p></th>
        <th width="30%" class="chiTabTitle"><p>电话</p></th>
      </tr>
      <tr>
        <td class="chiTabCon">陈卓文 先生，化验师<br>
          (<a href="mailto:cmchan@govtlab.gov.hk">cmchan@govtlab.gov.hk</a>)</td>
        <td class="chiTabCon1">2319-8402</td>
      </tr>
      <tr>
        <td class="chiTabCon">嘉蔼庭 博士，化验师<br>
          (<a href="mailto:sotcurreem@govtlab.gov.hk">sotcurreem@govtlab.gov.hk</a>)</td>
        <td class="chiTabCon1">2319-8397</td>
      </tr>
      <tr>
        <td class="chiTabCon">梁宇律 博士，化验师<br>
          (<a href="mailto:ylleung@govtlab.gov.hk">ylleung@govtlab.gov.hk</a>)</td>
        <td class="chiTabCon1">2319-8397</td>
      </tr>
      <tr>
        <td class="chiTabCon">邵凯恩 博士，化验师<br>
          (<a href="mailto:hyshiu@govtlab.gov.hk">hyshiu@govtlab.gov.hk</a>)</td>
        <td class="chiTabCon1">2319-8397</td>
      </tr>
    </table>
    <br>
    <hr>
    <h3><a name="QA" id="QA"></a>品 质 保 证</h3>
    <p>有 关 质 量 保 证 的 测 试 ， 约 占 总 测 试 的 百 分 之 十 。</p>
    <hr>
    <h3><a name="instrument" id="instrument"></a>主 要 仪 器</h3>
    <div class="photo_right"> <img border="0" src="../g/../g/cm-2.jpg" alt="提纯样本中钚的电沉积装置" width="300" height="210"><br>
      <span class="gallery_caption">高效液相色谱联用质谱/质谱仪</span></div>
    <p>以 下 是 本 组 常 用 的 化 学 分 析 仪 器 ：</p>
    <ul>
      <li>气 相 色 谱 仪 ： 装 置 电 子 捕 获 检 测 器 、 火 焰 光 度 检 测 器 及 质 量 选 择 检 测 器</li>
      <li>高 效 液 相 色 谱 仪 ： 装 置 蒸 发 激 光 散 射 检 测 器 、 光 电 二 极 管 陈 列 检 测 器 及 扫 描 萤 光 检 测 器</li>
      <li>紫 外 光 分 光 光 谱 仪</li>
      <li>傅 里 业 红 外 光 分 光 光 谱 仪</li>
      <li>高 效 液 相 色 谱 电 洒 离 子 阱 质 谱 仪</li>
      <li>高 效 液 相 色 谱 联 用 质 谱 / 质 谱 仪</li>
      <li>电 感 藕 合 等 离 子 体 质 谱 仪</li>
    </ul>
    <p>&nbsp;</p>
<hr>
    <h3><a name="targets" id="targets"></a>目 标 及 指 标</h3>
    <h4>有 关 中 药 法 定 化 验 工 作 的 衡 量 服 务 表 现 准 则</h4>
    <p><strong>目 标 <sup>#</sup></strong></p>
    <table width="100%" border="0" cellpadding="5" cellspacing="1" class="tableborder">
      <tr>
        <th id="t1" width="52%" class="chiTabTitle">为 下 列 中 药 进 行 化 验</th>
        <th id="t2" width="12%" class="chiTabTitle">目 标</th>
        <th id="t3" width="12%" class="chiTabTitle">2014<br>
          (实际)</th>
        <th id="t4" width="12%" class="chiTabTitle">2015<br>
          (实际)</th>
        <th id="t5" width="12%" class="chiTabTitle">2016<br>
        (计划)</th>
      </tr>
      <tr>
        <td headers="t1" class="chiTabCon">中 药 &mdash; 平 均 在 30 个 工 作 天 内 完 成 报 告 (%)<sup>&para;</sup></td>
        <td headers="t2" class="chiTabCon1">95</td>
        <td headers="t3" class="chiTabCon1">98</td>
        <td headers="t4" class="chiTabCon1">98</td>
        <td headers="t5" class="chiTabCon1">不适用</td>
      </tr>
      <tr>
        <td headers="t1" class="chiTabCon">与 中 药 事 故 有 关 的 紧 急 样 本 &mdash; 在 2 个 工 作 天 内 完 成 化 验 工 作 (%)<sup>@</sup></td>
        <td headers="t2" class="chiTabCon1">95</td>
        <td headers="t3" class="chiTabCon1">不适用</td>
        <td headers="t4" class="chiTabCon1">不适用</td>
        <td headers="t5" class="chiTabCon1">95</td>
      </tr>
      <tr>
        <td headers="t1" class="chiTabCon">其 他 中 药 样 本 &mdash; 平 均 在 30 个 工 作 天 内 完 成 报 告 (%)<sup>@</sup></td>
        <td headers="t2" class="chiTabCon1">95</td>
        <td headers="t3" class="chiTabCon1">不适用</td>
        <td headers="t4" class="chiTabCon1">不适用</td>
        <td headers="t5" class="chiTabCon1">95</td>
      </tr>
    </table>
    <br>
    <table width="100%" border="0" cellpadding="0" cellspacing="0">
      <tr valign="top">
        <td>#&nbsp;</td>
        <td>就 上 述 提 及 完 成 报 告 所 需 时 间 的 目 标 而 言，由 于 不 同 样 本 的 分 析 程 序 各 异，因 此 完 成 报 告 所 需 时 间 也 有 所 不 同。所 述 的 完 成 报 告 时 间，是 指 在 同 一 类 别 的 不 同 样 本 及 化 验 要 求 下，完 成 化 验 报 告 平 均 所 需 工 作 天 数；目 标 (以 百 分 率 标 示) 则 指 在 同 一 类 别 的 样 本 及 化 验 要 求 下，按 所 订 目 标 时 间 完 成 化 验 报 告 的 总 功 率。</td>
      </tr>
      <tr valign="top">
        <td>&para;</td>
        <td>由 二 零 一 六 年 起，这 个 目 标 由 以 @ 标 示 与 中 药 有 关 的 新 目 标 所 取 代。</td>
      </tr>
      <tr valign="top">
        <td>@</td>
        <td>这 些 是 由 二 零 一 六 年 起 采 用 的 新 目 标，分 为「紧 急」和「其 他」样 本，以 更 确 切 地 反 映 不 同 紧 急 程 度。</td>
      </tr>
    </table>
    <p><strong>指 标</strong></p>
    <p><strong>有 关 中 药 法 定 化 验 的 工 作 指 标</strong></p>
    <table width="100%" border="0" cellpadding="5" cellspacing="1" class="tableborder">
      <tr>
        <th id="t1" width="55%" class="chiTabTitle">进 行 的 中 药 化 验 数 目</th>
        <th id="t2" width="15%" class="chiTabTitle">2014<br>
          (实际)</th>
        <th id="t3" width="15%" class="chiTabTitle">2015<br>
          (实际)</th>
        <th id="t4" width="15%" class="chiTabTitle">2016<br>
        (预算)</th>
      </tr>
      <tr>
        <td headers="t1" class="chiTabCon">中 药<sup>^</sup></td>
        <td headers="t2" class="chiTabCon1">85,719</td>
        <td headers="t3" class="chiTabCon1">82,930</td>
        <td headers="t4" class="chiTabCon1">不适用</td>
      </tr>
      <tr>
        <td headers="t1" class="chiTabCon">与 中 药 事 故 有 关 的 紧 急 样 本<sup>*</sup></td>
        <td headers="t2" class="chiTabCon1">不适用</td>
        <td headers="t3" class="chiTabCon1">不适用</td>
        <td headers="t4" class="chiTabCon1">不适用<sup>&sect;</sup></td>
      </tr>
      <tr>
        <td headers="t1" class="chiTabCon">其 他 中 药 样 本<sup>*</sup></td>
        <td headers="t2" class="chiTabCon1">不适用</td>
        <td headers="t3" class="chiTabCon1">不适用</td>
        <td headers="t4" class="chiTabCon1">80,000</td>
      </tr>
    </table>
    <br>
    <table width="100%" border="0" cellpadding="0" cellspacing="0">
      <tr valign="top">
        <td>^&nbsp;</td>
        <td>由 二 零 一 六 年 起，这 个 指 标 由 以 * 标 示 与 中 药 有 关 的 新 指 标 所 取 代 。</td>
      </tr>
      <tr valign="top">
        <td>*</td>
        <td>这 些 是 由 二 零 一 六 年 起 采 用 的 新 目 标，分 为 「紧 急」和「其 他」样 本，以 更 确 切 地 反 映 不 同 紧 急 程 度。</td>
      </tr>
      <tr valign="top">
        <td>&sect;</td>
        <td>以 往 数 年 与 中 药 事 故 有 关 的 样 本 紧 急 化 验 需 求 有 所 波 动，因 此 难 以 预 算 这 类 事 故 发 生 的 次 数 或 化 验 需 求 数 字。</td>
      </tr>
    </table>
    <p>&nbsp;</p>
    <!-- InstanceEndEditable -->
<script type="text/javascript">
//<![CDATA[
        <!--//
            cfooter();
            //-->
//]]>
</script> 
</div>
</div>
</div>
</div>
</body>
<!-- InstanceEnd -->
</html>


"""
soup = BeautifulSoup(html_doc, "lxml")
print '---------------------------------'
all_p = soup.find_all('div', id = 'right_zonecontent')[0].get_text().strip()
all_p = all_p.encode('GBK', 'ignore')
all_p = re.sub(r'<!--//\s+\w+\(\)\;\s+//-->', "", all_p)
all_p = re.sub(r'//', "", all_p)
# all_p = re.sub(r'\n', "", all_p)
# all_p = re.sub(r'\t', "", all_p)
print all_p
print '---------------------------------'  