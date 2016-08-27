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

html_doc1 = """

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-HK" lang="zh-hk">

<head>
<meta name="Keywords" content="保安局禁毒處, 毒品資料常見問題">
<meta name="description" content="保安局禁毒處 - 毒品資料常見問題">
<meta name="description-2" content="Security Bureau, Narcotics Division Website">
<meta name="author" content="Security Bureau, Narcotics Division">
	<script language="JavaScript" src="/js/jquery-1.11.0.min.js" type="text/javascript"></script>
	<link href="/css/print.css" rel="stylesheet" type="text/css" media="print">
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<script language="JavaScript" src="../js/advMenu.js" type="text/javascript"></script>
	<script language="JavaScript" src="../js/genLayer.js" type="text/javascript"></script>
	<script language="JavaScript" src="../js/common.js" type="text/javascript"></script>
	<script language="JavaScript" src="../js/data.js" type="text/javascript"></script>
	<script language="JavaScript" src="../js/swf.js" type="text/javascript"></script>
	<link href="/css/format.css" rel="stylesheet" type="text/css">
	<title>保安局禁毒處 - 毒品資料常見問題</title>
	<script language=javascript type="text/javascript">
	</script>
	<script language="JavaScript" type="text/javascript">
		<!--
		var currentSection = '7,1';

		function MM_swapImgRestore() { //v3.0
			var i, x, a = document.MM_sr;
			for (i = 0; a && i < a.length && (x = a[i]) && x.oSrc; i++) x.src = x.oSrc;
		}

		function MM_preloadImages() { //v3.0
			var d = document;
			if (d.images) {
				if (!d.MM_p) d.MM_p = new Array();
				var i, j = d.MM_p.length,
					a = MM_preloadImages.arguments;
				for (i = 0; i < a.length; i++)
					if (a[i].indexOf("#") != 0) {
						d.MM_p[j] = new Image;
						d.MM_p[j++].src = a[i];
					}
			}
		}

		function MM_findObj(n, d) { //v4.01
			var p, i, x;
			if (!d) d = document;
			if ((p = n.indexOf("?")) > 0 && parent.frames.length) {
				d = parent.frames[n.substring(p + 1)].document;
				n = n.substring(0, p);
			}
			if (!(x = d[n]) && d.all) x = d.all[n];
			for (i = 0; !x && i < d.forms.length; i++) x = d.forms[i][n];
			for (i = 0; !x && d.layers && i < d.layers.length; i++) x = MM_findObj(n, d.layers[i].document);
			if (!x && d.getElementById) x = d.getElementById(n);
			return x;
		}

		function MM_swapImage() { //v3.0
			var i, j = 0,
				x, a = MM_swapImage.arguments;
			document.MM_sr = new Array;
			for (i = 0; i < (a.length - 2); i += 3)
				if ((x = MM_findObj(a[i])) != null) {
					document.MM_sr[j++] = x;
					if (!x.oSrc) x.oSrc = x.src;
					x.src = a[i + 2];
				}
		}
		//-->
	</script>
	<style type="text/css">

	</style>
	<script language="JavaScript" type="text/javascript">
		<!--
		<!--
		function MM_reloadPage(init) { //reloads the window if Nav4 resized
			if (init == true) with(navigator) {
				if ((appName == "Netscape") && (parseInt(appVersion) == 4)) {
					document.MM_pgW = innerWidth;
					document.MM_pgH = innerHeight;
					onresize = MM_reloadPage;
				}
			}
			else if (innerWidth != document.MM_pgW || innerHeight != document.MM_pgH) location.reload();
		}
		MM_reloadPage(true);
		// -->
		function MM_openBrWindow(theURL, winName, features) { //v2.0
			window.open(theURL, winName, features);
		}
		//-->
	</script>
</head>

<body>
	<h1 style="display:none">Title</h1>
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
			<td align="left" valign="top" width="154" height="550">
				<script language="JavaScript" type="text/javascript">
					getLeftMenu();
				</script>
			</td>
			<td align="left" valign="top" bgcolor="#FFFFFF" width="606">
				<table width="100%" border="0" cellpadding="5" cellspacing="5">
					<!-- <tr>
						<td>
							<script language="JavaScript" type="text/javascript">
								generateTopMenu();
							</script>
						</td>
					</tr>  -->
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
						<td valign="top" align="left"><img src="images/1_pixel.gif" alt="" width="8" height="15">
							<a name="top"></a>
						</td>
					</tr>
					<tr>
					<a name="main-content" id="main-content" tabindex="0"></a>
						<td valign="top"><span><strong>有 用 資 料</strong></span>
							<!-- <img src="images/chi/c_drug_handing.jpg" alt="毒品資料" width="126" height="35"> --></td>
					</tr>
					<tr>
						<td valign="top" align="left">
							<p style="font-weight: bold;">常 見 問 題
								<!-- <img src="images/chi/di_title_01.gif" alt="常見問題"> --></p>
							<!-- 				<p><strong>常 見 的 藥 物 問 題</strong></p> -->
							<!--<script type="text/javascript">getTemplateHeader(0);</script>
				<p><img src="images/chi/q_01.gif" border="0" alt="如 果 您 想 知 道 答 案 ， 請 按 這 裏 ！ "></p>
			  <script type="text/javascript">getTemplateMiddle(0);</script>
				<p><span>濫 用 藥 物 是 指 沒 有 依 照 醫 務 人 員 的 指 導 或 處 方 而 服 用 藥 物 ， 又 或 隨 便 服 用 危 險 藥 物 而 非 作 治 病 用 途 。 </span></p>
			  <script type="text/javascript">getTemplateFooter(0);</script>-->
							<script type="text/javascript">
								getTemplateHeader(0);
							</script>
							<p>吸 食 毒 品 有 甚 麼 後 果 ？
								<!-- <img src="images/chi/q_01.gif" border="0" alt="如 果 您 想 知 道 答 案 ， 請 按 這 裏 ！ "> --></p>
							<script type="text/javascript">
								getTemplateMiddle(0);
							</script>
							<p><span>每 一 種 毒 品 都 有 其 潛 在 危 險 ， 而 危 險 程 度 視 乎 其 所 含 雜 質 或 攙 雜 成 份 ， 以 及 每 個 服 食 者 的 特 殊 反 應 。 在 非 法 市 場 上 售 賣 的 毒 品 ， 往 往 含 有 雜 質 或 攙 雜 物 ， 並 非 貨 真 價 實 。 而 毒 品 若 混 和 酒 精 服 食 ， 會 更 容 易 產 生 危 險 ， 甚 至 會 致 命 。</span></p>
							<script type="text/javascript">
								getTemplateFooter(0);
							</script>
							<script type="text/javascript">
								getTemplateHeader(0);
							</script>
							<p>若 同 時 吸 食 多 於 一 種 毒 品 的 後 果 如 何 ？
								<!-- <img src="images/chi/q_02.gif" border="0" alt="如 果 您 想 知 道 答 案 ， 請 按 這 裏 ！ "> --></p>
							<script type="text/javascript">
								getTemplateMiddle(0);
							</script>
							<p><span>同 時 吸 食 超 過 一 種 毒 品 是 十 分 危 險 的 ， 即 使 每 種 毒 品 的 劑 量 大 大 低 於 正 常 劑 量 ， 也 足 以 致 命 ， 混 合 不 同 種 類 毒 品 吸 食 ， 會 引 起 複 雜 的 相 互 作 用 ， 導 致 傷 害 或 死 亡 的 危 險 性 亦 因 此 增 加 。 </span></p>
							<script type="text/javascript">
								getTemplateFooter(0);
							</script>
							<script type="text/javascript">
								getTemplateHeader(0);
							</script>
							<p>吸 食 危 害 精 神 毒 品 的 後 果 是 否 很 輕 微 ？
								<!-- <img src="images/chi/q_03.gif" border="0" alt="如 果 您 想 知 道 答 案 ， 請 按 這 裏 ！ "> --></p>
							<script type="text/javascript">
								getTemplateMiddle(0);
							</script>
							<p><span>絕 對 不 是 ！ 長 期 大 量 吸 食 危 害 精 神 毒 品 ， 容 易 歪 曲 一 個 人 對 環 境 的 觀 感 和 反 應 ， 即 使 服 食 劑 量 不 高 ， 亦 會 影 響 肌 肉 活 動 ， 延 長 反 應 時 間 及 降 低 集 中 精 神 的 能 力 ， 當 吸 毒 者 操 作 機 器 、 駕 駛 汽 車 或 橫 過 馬 路 時 ， 很 容 易 對 自 己 或 他 人 構 成 危 險 。 </span></p>
							<script type="text/javascript">
								getTemplateFooter(0);
							</script>
							<script type="text/javascript">
								getTemplateHeader(0);
							</script>
							<p>吸 食 毒 品 能 令 人 快 樂 嗎 ？
								<!-- <img src="images/chi/q_04.gif" border="0" alt="如 果 您 想 知 道 答 案 ， 請 按 這 裏 ！ "> --></p>
							<script type="text/javascript">
								getTemplateMiddle(0);
							</script>
							<p><span>不 會 ！ 許 多 毒 品 都 會 影 響 情 緒 ， 若 吸 食 者 發 怒 、 焦 慮 或 沮 喪 時 ， 毒 品 可 使 他 們 的 情 緒 變 得 更 加 壞 ， 即 使 是 一 些 有 鎮 靜 效 果 的 毒 品 （ 如 鎮 靜 劑 ） ， 也 能 引 起 過 份 的 衝 動 ， 更 會 影 響 個 人 社 交 行 為 及 抑 制 力 ， 使 其 做 出 一 些 後 悔 的 事 。 很 多 時 ， 導 致 吸 毒 者 或 他 人 嚴 重 傷 害 或 死 亡 的 暴 力 事 件 、 性 罪 行 及 友 姦 等 行 為 都 是 在 毒 品 影 響 下 發 生 的 。  </span></p>
							<script type="text/javascript">
								getTemplateFooter(0);
							</script>
							<script type="text/javascript">
								getTemplateHeader(0);
							</script>
							<p>毒 品 會 令 人 上 癮 嗎 ？
								<!-- <img src="images/chi/q_05.gif" border="0" alt="如 果 您 想 知 道 答 案 ， 請 按 這 裏 ！ "> --></p>
							<script type="text/javascript">
								getTemplateMiddle(0);
							</script>
							<p><span>會 ！ 毒 品 不 但 改 變 人 的 行 為 ， 並 會 對 人 造 成 不 同 程 度 的 生 理 及 心 理 依 賴 。 生 理 上 的 依 賴 ， 會 使 人 在 停 止 吸 食 毒 品 後 ， 出 現 斷 癮 症 狀 。 心 理 上 的 依 賴 ， 則 會 令 吸 毒 者 產 生 心 理 上 對 毒 品 的 渴 求 ， 因 而 需 要 更 高 劑 量 及 更 頻 密 服 用 ， 才 能 滿 足 個 人 的 渴 求 或 抑 制 斷 癮 症 狀 。 當 吸 毒 者 開 始 依 賴 毒 品 時 ， 他 便 需 要 源 源 不 絕 的 金 錢 來 滿 足 其 毒 癮 ， 藉 著 犯 案 以 達 到 目 的 ， 以 致 泥 足 深 陷 ， 難 以 自 拔 。 吸 毒 者 最 後 更 有 可 能 因 為 服 食 過 量 毒 品 而 引 致 死 亡 。</span></p>
							<script type="text/javascript">
								getTemplateFooter(0);
							</script>
							<p style="font-weight: bold;">有 用 資 料
								<!-- <img src="images/chi/di_title_02.gif" alt="毒品資料"> --></p>
							<!-- 
			甚 麼 是 藥 物 濫 用? <br>
              藥 物 濫 用 即 是 在 沒 有 醫 務 人 員 的 正 確 指 導 下 使 用 任 何 藥 物 ; 後 果. . . . . 
              . 不 堪 設 想 ! 
              <p>不 錯 ! 濫 用 藥 物 會 造 成 非 常 嚴 重 的 後 果, 甚 至 會 致 命!藥 物 混 和 酒 精 使 用 
                也 非 常 危 險。</p>
              <p>濫 用 藥 物 後. . . . . . <br>
                <br>
              </p> -->
						</td>
					</tr>
					<table width="92%" border="0">
						<tr>
							<td><img src="images/photo/durginformation.gif" alt="毒品資料 " width="328" height="252"></td>
							<td width="42%" valign="top">
								<table width="100%" border="0">
									<tr>
										<td valign="top">
											<br> <img src="images/bullet_ball2.gif" alt="" width="12" height="12"></td>
										<td width="100%">
											<a href="narcotic.htm">
												<br> 麻 醉 鎮 痛 劑 </a>
										</td>
									</tr>
									<tr>
										<td valign="top"><img src="images/bullet_ball2.gif" alt="" width="12" height="12"></td>
										<td width="100%"><a href="hallucinogens.htm"> 迷 幻 劑  </a>
											<br> </td>
									</tr>
									<tr>
										<td valign="top"><img src="images/bullet_ball2.gif" alt="" width="12" height="12"></td>
										<td width="100%"><a href="depressants.htm">鎮 抑 劑 </a>
											<br> </td>
									</tr>
									<tr>
										<td valign="top"><img src="images/bullet_ball2.gif" alt="" width="12" height="12"></td>
										<td width="100%"><a href="stimulants.htm"> 興 奮 劑 </a></td>
									</tr>
									<tr>
										<td valign="top"><img src="images/bullet_ball2.gif" alt="" width="12" height="12"></td>
										<td width="100%"><a href="tranquillizers.htm">鎮 靜 劑 </a>
											<br> </td>
									</tr>
									<tr>
										<td valign="top"><img src="images/bullet_ball2.gif" alt="" width="12" height="12"></td>
										<td width="100%"><a href="others.htm"> 其 他</a></td>
									</tr>
								</table>
							</td>
						</tr>
					</table>
					
					<table width="85%" border="0" cellspacing="0" cellpadding="0" align="center">
<tr>
	<td valign="top" align="center">
		<br> <img src="images/botdot.jpg" width="602" height="2" alt="" style="width:603px;">
		<br>
		<table width="98%" border="0" cellspacing="0" cellpadding="0" align="center">
			<tr>
				<td>
					<script language="JavaScript" src="/js/footer.js" type="text/javascript"></script>
					<script language="JavaScript" type="text/javascript">
						footer();
					</script>
				</td>
				<td>
					<div align="right">
						<span>
							<script type="text/javascript">var manual_date ="";lastrevision();</script>
						</span> 
					</div>
				</td>
			</tr>
			<!--<script language="JavaScript" type="text/javascript"> footer_wcag(); </script>-->
		</table>
	</td>
</tr>
					</table>
					<p>
						<br>
						<br> </p>
				</table>
			</td>
		</tr>
	</table>
	<script type="text/javascript">
		<!--
		genfooterLayer();
		//-->
	</script>
</body>

</html>
"""

html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
  
  <!-- Prevent Clickjacking Defense -->
  <style id="antiClickjack">body{display:none !important;}</style>
  <script>
    /*<![CDATA[*/
    if (self === top) {
      var antiClickjack = document.getElementById("antiClickjack");
      antiClickjack.parentNode.removeChild(antiClickjack);
    } else {
      top.location = self.location;
    }
    /*]]>*/
  </script>
  <!-- End of Clickjacking Defense -->
  
  <meta name="robots" content="NOINDEX,NOFOLLOW" />
  <link rel="icon" type="image/ico" href="/images/favicon.gif" />
  <link rel="shortcut icon" href="/images/favicon.gif" />

  <title>香港政府一站通：搜尋結果</title>
  
  <script src="/js/jquery-1.11.2.min.js"></script>
  <script src="/js/jquery-ui-1.11.4.min.js"></script>
  <link rel="stylesheet" href="/css/jquery-ui.1.11.4.css" />
  <script type="text/javascript" src="/js/advance/advSearch.js"></script>
  <script type="text/javascript" src="/js/jquery.qtip.min.js"></script>
  
  <link rel="stylesheet" href="/css/jquery.qtip.min.css" />

  <script>
    /*<![CDATA[*/
    var isAdv = false;
    function resetForms() {
    	if (isAdv) {
    		return;
    	}
    	
      for (var i = 0; i < document.forms.length; i++ ) {
        document.forms[i].reset();
      }
    }
    // Search query
    var page_query = '\u6BD2\u54C1';
    // Starting page offset, usually 0 for 1st page, 10 for 2nd, 20 for 3rd.
    var page_start = "";
    // Front end that served the page.
    var page_site = 'nd_home';
    
    function rkwAjax() {
    	var url = '/ajaxRkw?query=%E6%AF%92%E5%93%81&ui_lang=zh-hk&tpl_id=stdsearch&page=1&p_size=10&output=xml_no_dtd&ui_charset=utf-8&a_submit=false&toASubmit=false&gp0=nd_home&gp1=nd_home&doc_type=all&sort=&web=this&txtonly=0&site=nd_home&last_mod=%23-1&exact_q=&any_q=&none_q=';
    	var tab = null;
    	var rkwEnable = false;
    	
    	if (tab != 'online' && rkwEnable) {
    		$("#ajaxResult").load(url);
    	}
    }
    
    function keyUpdate() {
    	var docListCount = 10;
    	var page = 1;
    	var keywordUpdate = true;
    	
    	if (keywordUpdate) {
	    	if (docListCount > 0 && page == 1) {
	    		var url = '/updateAutoKeyword?keyword=%E6%AF%92%E5%93%81&ui_lang=zh-hk';
	    		
	    		$("#updateKeyword").load(url);
	    	}
    	}
    }
    
    function clickCount(action) {
    	clickCount(action, '');
    } 
    
    function clickCount(action, clickUrl, keyword) {
    	
    	var url = '/stat.html?ui_lang=zh-hk&keyword=%E6%AF%92%E5%93%81';
    	
    	if (url.length > 0) {
    		url = url + "&action=" + action + "&clickUrl=" + clickUrl + "&searchKeyword=" + keyword;
    	
    		$("#updateKeyword").load(url);
    	}
    	
    }
    /*]]>*/
  </script>
  <script type="text/javascript" src="/js/gov_adv_search_20090619.js"></script>
  <script type="text/javascript" src="/js/gov_search_image.js"></script>

  
  
  
  
  
  <link media="screen" type="text/css" rel="stylesheet" href="/css/advance/style20130807.css" />
  <link media="screen" type="text/css" rel="stylesheet" href="/css/rkwCss.css" />
  
  <link rel="stylesheet" type="text/css" href="/css/topnav.css" />
  <link rel="stylesheet" type="text/css" href="/css/footer.css" />
  <link rel="stylesheet" type="text/css" href="/css/screenreader.css" />
  <link rel="stylesheet" type="text/css" href="/css/clustertab.css" />
  <link rel="stylesheet" type="text/css" href="/css/rightaddarea.css" />
  <link rel="stylesheet" type="text/css" href="/css/searchbar_dept_20130625.css" />
  <link rel="stylesheet" type="text/css" href="/css/pagination_20130625.css" />
  <link rel="stylesheet" type="text/css" href="/css/gov_adv_search_20130625.css" />
  
  <link media="screen" type="text/css" rel="stylesheet" href="/css/advance/layout20150522.css" />
  <link media="screen" type="text/css" rel="stylesheet" href="/css/advance/typography.css" />
  <link media="screen" type="text/css" rel="stylesheet" href="/css/advance/reset.css" />
  <link media="screen" type="text/css" rel="stylesheet" href="/css/advance/search20150522.css" />
  

  <!--[if IE 7]>
  <link media="screen" type="text/css" rel="stylesheet" th:href="@{/css//advance/ie7.css}"/>
  <![endif]-->
  <!--[if lt IE 7]>
  <link media="screen" type="text/css" rel="stylesheet" th:href="@{/css/advance/ie6.css}"/>
  <![endif]-->
  <link media="screen" type="text/css" rel="stylesheet" href="/css/advance/typography.css" />
  <!--script type="text/javascript" src="http://sp.search.gov.hk/search/advance/jquery.js"></script-->
  <script type="text/javascript" src="/js/advance/search.js"></script>
  <!--[if lt IE 7]>
  <script type="text/javascript" th:src="@{/js/advance/DD_belatedPNG.js}"></script>
  <script type="text/javascript" th:src="@{/js/advance/ie6.js}"></script>
  <![endif]-->

  <script>
    /*<![CDATA[*/
    var deptLogoMap = new Object();
    var deptLogoWidthMap = new Object();
    var deptLogoHeightMap = new Object();
    var deptLinkMap = new Object();
    var deptAltMap = new Object();
    var deptMenuMap = new Object();
    var deptContactMap = new Object();
    var deptSiteMapMap = new Object();
    var deptNoticeMap = new Object();
    var deptPPMap = new Object();
    var deptAdvSearchMap = new Object();
    var deptPageTileMap = new Object();
    var deptAdvSearchTxtMap = new Object();
    var deptHeaderTxtMap = new Object();
    var deptFooterTxtMap = new Object();

    null

    /*]]>*/
  </script>
  
  
  
  <script type="text/javascript" src="/js/govhk_suntek.js"></script>
  
	<script>
		//******************************************************
		// 	Project name: Hosted Service web page
		//	Written by: Magic Ho
		//	Version : 0.00
		//******************************************************
		//All javascript must be inculded by javascript
		/*<![CDATA[*/
	    // For govhk_suntek.js use
	    var lang3, lang;
		var msgKeyword = '\u8ACB\u8F38\u5165\u95DC\u9375\u5B57\u3002';
		var msgDateRange = '\u8ACB\u9078\u64C7\u6B63\u78BA\u7684\u66F4\u65B0\u6642\u9593\u7BC4\u570D';
	    lang = 'zh-hk';
	    if (lang=='zh-hk' || lang=='zh-cnhk') {
	    	lang3 = 'tc';
	    } else if (lang=='zh-cn') {
	    	lang3 = 'sc';
	    } else {
	    	lang3 = 'en';
	    }
	    // End of govhk_suntek js use
	    
	    /* use same method for three search box 
	    function barFormSubmit() {
			if (document.getElementById('bar_search0').query.value.length == 0 ) {
				alert('請輸入關鍵字。');
				try {
					window.event.returnValue = false;
				} catch( dummy ) {
					return false;
				}
			} else { 
				document.getElementById('bar_search0').submit(); 
			}
		} */
	    
	    function searchFormSubmit(form) {
			if (form.query.value.length == 0 ) {
				alert(msgKeyword);
				try {
					window.event.returnValue = false;
				} catch( dummy ) {
					return false;
				}
			} else { 
				form.submit(); 
			}
		}

		function selectWebSites(thisOption) {
			if (thisOption == 2 ) {
				document.getElementById("adv_search0").wb_v[2].checked = true;
			}
			if (thisOption == 1 ) {
				document.getElementById("adv_search0").wb_v[1].checked = true;
			}		
		}
		
		function selectGovHKWebSites(obj) {
			if (obj.checked) {
				selectWebSites(1);
			}
			if (obj.value == 'govhk_res') {
				var allSubOptions = document.getElementById("adv_search0").wb_within_rsd_v;
				if (obj.checked) {
					for (var i=0;i < allSubOptions.length;i++) {
						allSubOptions[i].checked = true;
					}
				} else {
					for (var i=0;i < allSubOptions.length;i++) {
						allSubOptions[i].checked = false;
					}			
				}
			}
			if (obj.value == 'social_groups') {
				var allSubOptions = document.getElementById("adv_search0").wb_within_sgs_v;
				if (obj.checked) {
					for (var i=0;i < allSubOptions.length;i++) {
						allSubOptions[i].checked = true;
					}
				} else {
					for (var i=0;i < allSubOptions.length;i++) {
						allSubOptions[i].checked = false;
					}			
				}
			}
		}
		
		function selectGovHKSubWebSites(obj) {
			if (obj.checked) {
				selectWebSites(1);
			}
		}


	  //search by websites;
	  function getWebsites(){
		  //all 
		 var webRSDSites=new Array();
		 var webWINSites=new Array();
		 var siteStr="";
		  if (document.getElementById("wb_all").checked) {
	                        document.getElementById('adv_search0').web.value = "all";
	          } else {
	                        document.getElementById('adv_search0').web.value = "this";
	          }
		  if (document.getElementById("wb_all").checked)
		  {
				document.getElementById('adv_search0').site.value = "default_collection";
		  }
		  //within GOV
		  if (document.getElementById("wb_within").checked)
		  {
	 
				//residents checked 
				webRSDSites=document.getElementsByName("wb_within_rsd_v");
				for (i=0;i <11 ;i++ )
				{
					if (webRSDSites[i].checked)
					{
					siteStr+=webRSDSites[i].value+"|";
					}
				
				}
				webWINSites=document.getElementsByName("wb_within_v");
				for (j=0;j <4 ;j++ )
				{
					if (webWINSites[j].checked)
					{
					siteStr+=webWINSites[j].value+"|";
					}
				
				}
				webSGSites=document.getElementsByName("wb_within_sgs_v");
				for (j=0; j < 5; j++)
				{
					if (webSGSites[j].checked)
					{
					siteStr+=webSGSites[j].value+"|";
					}
				}
			
				//modify stie
				modiSiteStr(siteStr);

		  }
		  
		  //special website
		  if (document.getElementById("wb_spec").checked)
		  {
				//Bug fix for IE7
				var specWebSite=document.getElementById('adv_search0').wb_dept_list;
				var tempSiteStr = specWebSite.options[specWebSite.selectedIndex].value;
				document.getElementById('adv_search0').site.value = tempSiteStr;

		  }
		
		  //modify the site string;
		function modiSiteStr(siteStr)
		  {
			  var sites = document.getElementsByName("site");
				  for( n = 0 ; n  < sites.length;n++)
				  {   
				  sites[n].value=siteStr.substring(0,siteStr.length-1);
				  }
		  }

		}	
	  
		function advFormSubmit() {
			if (document.getElementById('adv_search0').query.value.length == 0
					&& document.getElementById('adv_search0').exact_q.value.length == 0
					&& document.getElementById('adv_search0').any_q.value.length == 0
					&& document.getElementById('adv_search0').none_q.value.length == 0 ) {
				alert(msgKeyword);
				try {
					window.event.returnValue = false;
				} catch( dummy ) {
				}
			} else { 
				document.getElementById('adv_search0').submit(); 
			}
			
		}	
		
		function packLeadingZero(inStr, expectLen) {
			var resStr = inStr;
			while (resStr.length < expectLen) {
				resStr = "0" + resStr;
			}
			
			return resStr;
		}
		
		  function getdate(){
			  var dateStr = "#-1";		//Default value
			  //anytime
			  if (document.getElementById("date_any").checked)
			  {
			  //alert(" anytime chenked");
			  }
			  if (document.getElementById("date_within").checked)
			  {
			  //date_within
			  dateStr=document.getElementById("date_last").value;
			  }
			  if (document.getElementById("date_fromto").checked)
			  {
				  var sYear;
				  var sMonth;
				  var sDay;
				  var eYear;
				  var eMonth;
				  var eDay;
				  sYear=document.getElementById("s_date_year").value;
				  sMonth=document.getElementById("s_date_month").value;
				  sDay=document.getElementById("s_date_day").value;
				 
				  sMonth = packLeadingZero(sMonth, 2);
				  sDay= packLeadingZero(sDay, 2);
				
				  eYear=document.getElementById("e_date_year").value;
				  eMonth=document.getElementById("e_date_month").value;
				  eDay=document.getElementById("e_date_day").value;
				  eMonth = packLeadingZero(eMonth, 2);
				  eDay = packLeadingZero(eDay, 2);
				  
				  if ((sYear+sMonth+sDay)<=(eYear+eMonth+eDay))
				  {
					   //from
					  ftime=sYear+""+sMonth+""+sDay;
					   //to
					  ttime=eYear+""+eMonth+""+eDay;
					  dateStr = ftime + "," + ttime;
				  } else {
					  alert(msgDateRange);
					  window.event.returnValue = false;
				  }
			  }
			  
			  var last_mods = document.getElementsByName("last_mod");
			  for ( n = 0 ; n  < last_mods.length;n++)
			  {   
				  last_mods[n].value=dateStr;
			  }
		  }
		  
			//Added by Phoenix for auto-complete
	      $(document).ready(
	    		  function(){
	        var akurl = 'autokeyword?ui_lang=zh-hk';

			//Do not applied auto-complete function for dept template
	        var isStandard = true;
	        if (!isStandard) {
	        	return;
	        }
	        
	        //$( "#SearchBarBox" ).autocomplete({
	        //  delay: 300,
	        //  minLength: '2',
	        //  position: { my : "left top", at: "left bottom" },
	        //  source: akurl
	        //});
	        $( "#searchBox2" ).autocomplete({
		          delay: 300,
		          minLength: '2',
		          position: { my : "left top", at: "left bottom" },
		          source: akurl
		        });
	        $( "#searchBox3" ).autocomplete({
		          delay: 300,
		          minLength: '2',
		          position: { my : "left top", at: "left bottom" },
		          source: akurl
		        });
	        //$( "#SearchBarBox2" ).autocomplete({
		    //      delay: 300,
		    //      minLength: '2',
		    //      position: { my : "left top", at: "left bottom" },
		    //      source: akurl
		    //    });
	        $( "#searchBox" ).autocomplete({
		          delay: 300,
		          minLength: '2',
		          //Collision detection is nono. Keep the box at left bottom for the text box even have a very long word
		          //position: { my : "left top", at: "left bottom", collision: "none" },
		          //position: { my : "left top", at: "left bottom" },
		          source: akurl,
		          open: function() {
		              var position = $("#searchBox").position(),
		                  left = position.left, top = position.top;
		          }
		        });
	        //Seems OK to solve overflow problem. (HSDESK-115)
	        //jQuery.ui.autocomplete.prototype._resizeMenu = function () {
			//  var ul = this.menu.element;
			//  ul.outerWidth(this.element.outerWidth() * 1.4);
			//}
	      });
	  /*]]>*/
	</script>
  

  <script type="text/javascript" src="/js/template_function.js"></script>

  <script type="text/javascript" src="/js/framekiller.js"></script>

  <style>
    .overflow {
      height: 200px;
      width: 200px;
      font-size: 13px;
    }

    #tabs_en li a span {
      padding-top: 3px;
    }

    #tab_dept_url {
      padding-top: 3px;
    }

    #web_dept_list_span {
      vertical-align: middle;
      height: 24px;
      margin-top: 9px;
      margin-left: 5px;
      color: #000;
    }

    #web_dept_list_span .ui-icon {
      background-image: url("/css/images/ui-icons_888888_256x240.png");
      vertical-align: middle;
      right: 0.5em;
      left: auto;
      margin-top: -8px;
      position: absolute;
      top: 50%;
      background-position: -64px -16px;
      width: 16px;
      height: 16px;
      display: block;
      padding: 0px;
      z-index: 100;
    }

    #web_dept_list_span .ui-state-default {
      height: 24px;
      line-height: 24px;
      vertical-align: middle;
    }

    #web_dept_list_span .ui-selectmenu-text {
      height: 24px;
      line-height: 24px;
      background-image: none;
      vertical-align: middle;
      width: 220px;
      color: #000;
      padding-top: 0px;
      padding-left: 6px;
    }

    .ui-corner-all, .ui-corner-bottom, .ui-corner-right, .ui-corner-br, .ui-corner-all, .ui-corner-top, .ui-corner-right, .ui-corner-tr {
      border-radius: 0
    }

    .ui-state-default, .ui-widget-content .ui-state-default, .ui-widget-header .ui-state-default {
      background: #fff
    }

    .ui-selectmenu-icon {
      margin-top: -11px;
      right: 3px
    }
  </style>
</head>
<body onload="resetForms();rkwAjax();keyUpdate()" dir="ltr" lang="zh-hk" class="tc about"> <!-- Please enter html code below. -->
<div id="updateKeyword"></div>
<!--  Share the ui for both standard and dept -->
<div id="wrapper">
	<!-- Standard template tool bar -->
	<div id="header">
		<div id="topbar">
            <div class="access">Toolbar</div>
            <ul id="toolbar">
              <li id="languages">
              
              <!-- No need exact query parameter for normal case -->
              <a onclick="clickCount(&#39;langSwitchButtons&#39;, '', '')" id="en" title="English" lang="en" class="en" rel="alternate" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=en&amp;tpl_id=stdsearch&amp;page=1&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;a_submit=false&amp;toASubmit=false&amp;gp0=nd_home&amp;gp1=nd_home&amp;doc_type=all&amp;sort=&amp;web=this&amp;txtonly=0&amp;site=nd_home&amp;last_mod=%23-1&amp;tab=&amp;tab_depts=">English</a>
              |
              </li>
              
              <li class="subItem">
              
              <a onclick="clickCount(&#39;langSwitchButtons&#39;, '', '')" id="zh-CN" title="简体" lang="zh-CN" class="zh-CN" rel="alternate" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-cn&amp;tpl_id=stdsearch&amp;page=1&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;a_submit=false&amp;toASubmit=false&amp;gp0=nd_home&amp;gp1=nd_home&amp;doc_type=all&amp;sort=&amp;web=this&amp;txtonly=0&amp;site=nd_home&amp;last_mod=%23-1&amp;tab=&amp;tab_depts=">简体</a>
              </li>
            </ul>
            <div class="access">Header Menu</div>
            <ul id="quickLinks">
              <li><a id="waGovDirectory" title="政府機構" href="http://www.gov.hk/tc/about/govdirectory/">政府機構</a></li>
              <li><a id="onlineservices" title="網上服務" href="http://www.gov.hk/tc/residents/onlineservices/">網上服務</a></li>
              <li><a id="forms" title="表格" href="http://www.gov.hk/tc/residents/forms/">表格</a></li>
              <li><a id="waAboutHK" title="關於香港" href="http://www.gov.hk/tc/about/abouthk/">關於香港</a></li>

              <li class="mygovhkLinks">
                <div id="mygovhk_header" class="A tc">
                  <div id="mygovhk_header_text">
                    <a id="mygovhk_header_login" title="登入我的政府一站通" href="http://www.gov.hk/tc/apps/mygovhk.htm">
                    <span>登入</span></a>
                      |
                    <a id="mygovhk_header_register" title="登記我的政府一站通" href="http://www.gov.hk/tc/theme/mygovhk/">
                    <span>登記</span></a>
                  </div>
                </div>
              </li>
            </ul>
		</div>
	</div>
	<div id="pageContainer">
		<div id="govhkBar">
			<div id="govhkLogo"><a title="GovHK 香港政府一站通 " href="http://www.gov.hk/tc/residents/"><img title="GovHK 香港政府一站通 " alt="GovHK 香港政府一站通 " src="/images/govhk.png" /></a></div>
            <div class="access">GovHK Usergroups</div>
            <div id="userGroups">
                  <ul>
                     <li id="usrGrpResidents"><a title="Residents" href="http://www.gov.hk/tc/residents/">本港居民</a></li>
                     <li id="usrGrpBusiness"><a title="Business &amp; Trade" href="http://www.gov.hk/tc/business/">商務及貿易</a></li>
                     <li id="usrGrpNonResidents"><a title="Non-Residents" href="http://www.gov.hk/tc/nonresidents/">非本港居民</a></li>
                     <li id="usrGrpYouth">
					<a id="waUsrGrp4" href="#" data-hasqtip="0" title="">社會群體</a>

					<div id="socialGroupsDiv1">
		        		<div id="socialGroupsDiv2">
		                <div id="socialGroupsDiv3"></div>
		                <div id="socialGroupsDiv4">
	                        <ul id="socialGroupsList">
	
                                <li><a rel="external" title="康復數碼網絡" href="http://cyberable.swd.gov.hk/b5/index.html">
                                <img src="http://www.gov.hk/tc/images/socialgroups/cyberable.gif" alt="康復數碼網絡" /></a></li>
                                
                                <li><a rel="external" title="長青網" href="http://www.e123.hk/pro">
                                <img src="http://www.gov.hk/tc/images/socialgroups/e123.png" alt="長青網" /></a></li>

                                <li><a rel="external" title="開心家庭網絡" href="http://www.familycouncil.gov.hk/tc_chi/index.htm">
                                <img src="http://www.gov.hk/tc/images/socialgroups/HappyFamily.png" alt="開心家庭網絡" /></a></li>

                                <li><a rel="external" title="政府青少年網站" href="http://www.youth.gov.hk/tc/">
                                <img src="http://www.gov.hk/tc/images/socialgroups/youth.png" alt="政府青少年網站" /></a></li>

                                <li><a rel="external" title="婦女事務委員會" href="http://www.women.gov.hk/colour/tc/home/index.htm">
                                <img src="http://www.gov.hk/tc/images/socialgroups/women.png" alt="婦女事務委員會" /></a></li>
	                        </ul>
		                </div>
		        		</div>
					</div>
				</li>
                     <li id="govhkSearch">
                        <div class="access">Search</div>
                        <form name="gs" method="GET" onsubmit="searchFormSubmit(this); return false;" id="bar_search0" action="/search">
                           <div id="searchBoxContainer" class="ui-widget"><label for="searchBox" class="access">Search government websites</label>
                           <input type="text" id="searchBox" name="query" size="20" class="ui-autocomplete-input" autocomplete="off" value="毒品" />
                              <input type="hidden" name="ui_charset" value="utf-8" />
                              <label for="searchIcon" class="access">Search Submit</label>
                              <input type="submit" id="searchIcon" title="Search" name="search_but" value="" />
                              <input type="hidden" name="output" value="xml_no_dtd" />
                              <input type="hidden" name="ui_lang" value="zh-hk" />
                              <input type="hidden" name="gp1" value="nd_home" />
                              <input type="hidden" name="gp0" value="nd_home" />
                              <input type="hidden" name="web" value="this" />
                              <input type="hidden" name="txtonly" value="0" />
                              <input type="hidden" name="tpl_id" value="stdsearch" />
                              <input type="hidden" name="sort" value="" />
                              <input type="hidden" name="site" value="nd_home" />
                              
		             		  
		             		</div>
                        </form>
                     </li>
                  </ul>
               </div>
            </div>
	</div>
	
	
	<!-- End of Standard search header -->
	         
  <!-- Dept template Header -->       
  
	<!--  End of Dept template header -->


	<!-- Standard template body -->
   <div id="pageContainerTopKeywords">
      <div id="articlePageTopKeywords" class="page">
         <div class="about" id="mainTopKeywords">
            <div id="info">
               <div id="govhkTopKeywords">&nbsp;</div>
            </div>
            
            <div id="articlePage" class="page">
               <div id="main" class="about">
                  <div id="pageHeader">
                     <h1>搜尋結果</h1>
                     
                  </div>
                  <div id="breadCrumb">
                     <div class="access">Your current location in the website</div>
                     <a title="Home" href="http://www.gov.hk/tc/residents/">主頁</a> &gt;
                     	<strong><span>搜尋結果</span></strong>
                     	<strong></strong>
                   </div>
               </div>
            </div>
            
            <!-- Show result here -->
            <div id="articleContainer" class="topdown">
            <a id="content"></a>
            <div class="searchResultContent">
            
            <!-- For template OSP -->
            
			<div class="advancedRow clearthis">
		       <form name="gs1" method="GET" onsubmit="searchFormSubmit(this);return false;" id="gs1" action="/search">
		          <div class="clearthis">
		             <div class="searchBoxContainer2">
		                <div class="searchBoxContainer2 ui-widget">
		                   <div>
		                   <label for="searchBox2" class="access">搜尋</label>
		                   <input type="text" class="searchBox ui-autocomplete-input" name="query" id="searchBox2" autocomplete="off" value="毒品" />
		                   <label for="searchIcon2" class="access">Search Submit</label>
		                   <input type="submit" title="Search" class="searchIcon2" id="searchIcon2" name="search_but" value="" />
		                   </div>
		                </div>
		             </div>
		             <div class="advSearch"><a href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-hk&amp;tpl_id=stdsearch&amp;page=1&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;a_submit=false&amp;toASubmit=true&amp;last_mod=%23-1&amp;gp0=nd_home&amp;gp1=nd_home&amp;doc_type=all&amp;sort=&amp;web=this&amp;txtonly=0&amp;site=nd_home">進階搜尋</a></div>
		             <div class="faqSearch"><a href="http://www.gov.hk/tc/about/helpdesk/search/">有關搜尋服務的常見問題</a></div>
		             <input type="hidden" name="output" value="xml_no_dtd" />
		             <input type="hidden" name="ui_lang" value="zh-hk" />
		             <input type="hidden" name="gp1" value="nd_home" />
		             <input type="hidden" name="gp0" value="nd_home" />
		             <input type="hidden" name="web" value="this" />
		             <input type="hidden" name="txtonly" value="0" />
		             <input type="hidden" name="tpl_id" value="stdsearch" />
		             <input type="hidden" name="sort" value="" />
		             <input type="hidden" name="doc_type" value="all" />
		             
		             
		             
		             <div id="stdTplRadioButton" class="clearthis">
		             <fieldset><legend class="hidden">顯示：</legend>
		             <span>顯示：</span>&nbsp;
		             <input type="radio" id="yschtopsearch1all_ck_top_1" name="site" value="default_collection" />
		             <label for="yschtopsearch1all_ck_top_1">所有政府網站</label>
					 <input type="radio" id="yschtopsearch1this_ck_top_1" name="site" checked="checked" value="nd_home" />
					 <label for="yschtopsearch1this_ck_top_1">禁毒處</label>
					 
					 </fieldset>
					 </div>
					</div>
				</form>
                </div>
				<div class="searchResultTitle">
					<h2>
						<span>約找到 <strong>818</strong> 個結果，顯示第 <strong>1</strong> 至 <strong>10</strong> 個。 </span>
						
						<span>需時 <strong>0.064</strong> 秒。</span>
					</h2>
				</div>
				
				<!-- Spell suggestion -->
				
				<div class="faqSearch">
					<a onclick="clickCount(&#39;sort_by_date&#39;, '', '')" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-hk&amp;tpl_id=stdsearch&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;gp0=nd_home&amp;gp1=nd_home&amp;doc_type=all&amp;sort=date&amp;web=this&amp;txtonly=0&amp;site=nd_home&amp;last_mod=%23-1&amp;tab=&amp;tab_depts=">根據日期排序</a>
					
					/
					<span>根據相關程度排序</span>
					
				</div>
					
				<!-- Recommend link -->
				
				
				<!-- search result for stdsearch -->
				<div>
				<div class="searchResultArea">
                   	<div lang="zh-hk" class="searchListing" id="searchListing" style="visibility:visible">
                    	<ol>
		                <!--search result list start-->
		
		                <li>
		                  <h3>
		                  	
		                    <a class="itemDetailsTitle" onkeydown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.nd.gov.hk%2Ftc%2Fstatistics_list.htm&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" onmousedown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.nd.gov.hk%2Ftc%2Fstatistics_list.htm&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" id="waSearchResultTitle1" href="http://www.nd.gov.hk/tc/statistics_list.htm">
		                      <span>保安局禁<strong>毒</strong>處 - 藥物濫用資料中央檔案室及<strong>毒品</strong>統計數字 - <strong>毒品</strong>統計數字</span>
		                    </a>
		                   </h3>
		                  <p>
		                  	<span class="itemDetailsDescription">保安局禁<strong>毒</strong>處 - 藥物濫用資料中央檔案室及<strong>毒品</strong>統計數字 - <strong>毒品</strong>統計數字. 藥物濫用資料中央檔案室及<strong>毒品</strong>...</span>
		                  </p>
		
		                  <!--/p-->
		                  <p>
		                    <!-- Last Modified Date: 2011-11-09 -->
		                    <span class="itemDetailsLink">www.nd.gov.hk/tc/statistics_list.htm</span>
		                    - 
		                    <span>49.7K</span>
		                    <span> - </span>
		                    <span>31/03/2016</span>
		                    <span> - </span>
		                    <!--/p-->
		                    <!-- Add cache here -->
		                    <a class="moreFromThisSiteLink" href="http://lp.search.gov.hk:8080/Action=View&amp;NoACI=true&amp;reference=http%3A%2F%2Fwww.nd.gov.hk%2Ftc%2Fstatistics_list.htm" onkeydown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);" onmousedown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);">
		                    <span>頁庫存檔</span></a>
		                  </p>
		                 </li>
		
		                <li>
		                  <h3>
		                  	
		                    <a class="itemDetailsTitle" onkeydown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.nd.gov.hk%2Ftc%2Fdruginfo.htm&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" onmousedown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.nd.gov.hk%2Ftc%2Fdruginfo.htm&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" id="waSearchResultTitle2" href="http://www.nd.gov.hk/tc/druginfo.htm">
		                      <span>保安局禁<strong>毒</strong>處 - <strong>毒品</strong>資料常見問題</span>
		                    </a>
		                   </h3>
		                  <p>
		                  	<span class="itemDetailsDescription">罪 行 及 友 姦 等 行 為 都 是 在  <strong>毒</strong> <strong>品</strong>  影 響 下 發 生 的 。 

<strong>毒</strong> <strong>品</strong>  會 令 人 上 癮 嗎 ？ 

會 ！ <strong>毒</strong> <strong>品</strong>...</span>
		                  </p>
		
		                  <!--/p-->
		                  <p>
		                    <!-- Last Modified Date: 2011-11-09 -->
		                    <span class="itemDetailsLink">www.nd.gov.hk/tc/druginfo.htm</span>
		                    - 
		                    <span>14.9K</span>
		                    <span> - </span>
		                    <span>14/03/2016</span>
		                    <span> - </span>
		                    <!--/p-->
		                    <!-- Add cache here -->
		                    <a class="moreFromThisSiteLink" href="http://lp.search.gov.hk:8080/Action=View&amp;NoACI=true&amp;reference=http%3A%2F%2Fwww.nd.gov.hk%2Ftc%2Fdruginfo.htm" onkeydown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);" onmousedown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);">
		                    <span>頁庫存檔</span></a>
		                  </p>
		                 </li>
		
		                <li>
		                  <h3>
		                  	
		                    <a class="itemDetailsTitle" onkeydown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.nd.gov.hk%2Ftc%2Fdrug_test.htm&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" onmousedown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.nd.gov.hk%2Ftc%2Fdrug_test.htm&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" id="waSearchResultTitle3" href="http://www.nd.gov.hk/tc/drug_test.htm">
		                      <span>保安局禁<strong>毒</strong>處 - <strong>毒品</strong>測試</span>
		                    </a>
		                   </h3>
		                  <p>
		                  	<span class="itemDetailsDescription">保安局禁<strong>毒</strong>處 - <strong>毒品</strong>測試. Title

				

	 

	<strong>毒品</strong>測試



 

	

		驗 <strong>毒</strong> ...</span>
		                  </p>
		
		                  <!--/p-->
		                  <p>
		                    <!-- Last Modified Date: 2011-11-09 -->
		                    <span class="itemDetailsLink">www.nd.gov.hk/tc/drug_test.htm</span>
		                    - 
		                    <span>23.3K</span>
		                    <span> - </span>
		                    <span>14/03/2016</span>
		                    <span> - </span>
		                    <!--/p-->
		                    <!-- Add cache here -->
		                    <a class="moreFromThisSiteLink" href="http://lp.search.gov.hk:8080/Action=View&amp;NoACI=true&amp;reference=http%3A%2F%2Fwww.nd.gov.hk%2Ftc%2Fdrug_test.htm" onkeydown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);" onmousedown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);">
		                    <span>頁庫存檔</span></a>
		                  </p>
		                 </li>
		
		                <li>
		                  <h3>
		                  	
		                    <a class="itemDetailsTitle" onkeydown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.nd.gov.hk%2Ftc%2Fantidrug_painting_panels.htm&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" onmousedown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.nd.gov.hk%2Ftc%2Fantidrug_painting_panels.htm&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" id="waSearchResultTitle4" href="http://www.nd.gov.hk/tc/antidrug_painting_panels.htm">
		                      <span>保安局禁<strong>毒</strong>處 - 「反青少年吸食危害精神<strong>毒品</strong>」繪畫比賽</span>
		                    </a>
		                   </h3>
		                  <p>
		                  	<span class="itemDetailsDescription"> <strong>品</strong>」繪畫比賽展板
 

	  

	此連結會於新視窗開啟
「反青少年吸食危害精神<strong>毒品</strong>」繪畫比賽展板
   此連結會於新視窗開啟
「反青少年吸食危害精神<strong>毒品</strong>」繪</span>
		                  </p>
		
		                  <!--/p-->
		                  <p>
		                    <!-- Last Modified Date: 2011-11-09 -->
		                    <span class="itemDetailsLink">www.nd.gov.hk/tc/antidrug_painting_panels.htm</span>
		                    - 
		                    <span>11.2K</span>
		                    <span> - </span>
		                    <span>14/03/2016</span>
		                    <span> - </span>
		                    <!--/p-->
		                    <!-- Add cache here -->
		                    <a class="moreFromThisSiteLink" href="http://lp.search.gov.hk:8080/Action=View&amp;NoACI=true&amp;reference=http%3A%2F%2Fwww.nd.gov.hk%2Ftc%2Fantidrug_painting_panels.htm" onkeydown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);" onmousedown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);">
		                    <span>頁庫存檔</span></a>
		                  </p>
		                 </li>
		
		                <li>
		                  <h3>
		                  	
		                    <a class="itemDetailsTitle" onkeydown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.nd.gov.hk%2Ftc%2Fsay_no.htm&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" onmousedown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.nd.gov.hk%2Ftc%2Fsay_no.htm&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" id="waSearchResultTitle5" href="http://www.nd.gov.hk/tc/say_no.htm">
		                      <span>保安局禁<strong>毒</strong>處 - 如何向<strong>毒品</strong>說「不」！</span>
		                    </a>
		                   </h3>
		                  <p>
		                  	<span class="itemDetailsDescription">保安局禁<strong>毒</strong>處 - 如何向<strong>毒品</strong>說「不」！. Title

				

	 

	如何向<strong>毒品</strong>...</span>
		                  </p>
		
		                  <!--/p-->
		                  <p>
		                    <!-- Last Modified Date: 2011-11-09 -->
		                    <span class="itemDetailsLink">www.nd.gov.hk/tc/say_no.htm</span>
		                    - 
		                    <span>6.2K</span>
		                    <span> - </span>
		                    <span>15/03/2016</span>
		                    <span> - </span>
		                    <!--/p-->
		                    <!-- Add cache here -->
		                    <a class="moreFromThisSiteLink" href="http://lp.search.gov.hk:8080/Action=View&amp;NoACI=true&amp;reference=http%3A%2F%2Fwww.nd.gov.hk%2Ftc%2Fsay_no.htm" onkeydown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);" onmousedown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);">
		                    <span>頁庫存檔</span></a>
		                  </p>
		                 </li>
		
		                <li>
		                  <h3>
		                  	
		                    <a class="itemDetailsTitle" onkeydown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.nd.gov.hk%2Ftc%2Freport_youth_drug_abuse.htm&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" onmousedown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.nd.gov.hk%2Ftc%2Freport_youth_drug_abuse.htm&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" id="waSearchResultTitle6" href="http://www.nd.gov.hk/tc/report_youth_drug_abuse.htm">
		                      <span>保安局禁<strong>毒</strong>處 - 青少年<strong>毒品</strong>問題專責小組報告</span>
		                    </a>
		                   </h3>
		                  <p>
		                  	<span class="itemDetailsDescription">保安局禁<strong>毒</strong>處 - 青少年<strong>毒品</strong>問題專責小組報告. Title

				

	 

	青 少 年 <strong>毒</strong> <strong>品</strong> ...</span>
		                  </p>
		
		                  <!--/p-->
		                  <p>
		                    <!-- Last Modified Date: 2011-11-09 -->
		                    <span class="itemDetailsLink">www.nd.gov.hk/tc/report_youth_drug_abuse.htm</span>
		                    - 
		                    <span>16.5K</span>
		                    <span> - </span>
		                    <span>15/03/2016</span>
		                    <span> - </span>
		                    <!--/p-->
		                    <!-- Add cache here -->
		                    <a class="moreFromThisSiteLink" href="http://lp.search.gov.hk:8080/Action=View&amp;NoACI=true&amp;reference=http%3A%2F%2Fwww.nd.gov.hk%2Ftc%2Freport_youth_drug_abuse.htm" onkeydown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);" onmousedown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);">
		                    <span>頁庫存檔</span></a>
		                  </p>
		                 </li>
		
		                <li>
		                  <h3>
		                  	
		                    <a class="itemDetailsTitle" onkeydown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.nd.gov.hk%2Ftc%2Fprevent_away_drugs.htm&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" onmousedown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.nd.gov.hk%2Ftc%2Fprevent_away_drugs.htm&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" id="waSearchResultTitle7" href="http://www.nd.gov.hk/tc/prevent_away_drugs.htm">
		                      <span>保安局禁<strong>毒</strong>處 - 《健康生活　遠離<strong>毒品</strong>》藥物教育教材套</span>
		                    </a>
		                   </h3>
		                  <p>
		                  	<span class="itemDetailsDescription">保安局禁<strong>毒</strong>處 - 《健康生活　遠離<strong>毒品</strong>》藥物教育教材套. Title

				

	

	《 健 康 生...</span>
		                  </p>
		
		                  <!--/p-->
		                  <p>
		                    <!-- Last Modified Date: 2011-11-09 -->
		                    <span class="itemDetailsLink">www.nd.gov.hk/tc/prevent_away_drugs.htm</span>
		                    - 
		                    <span>17.1K</span>
		                    <span> - </span>
		                    <span>13/05/2016</span>
		                    <span> - </span>
		                    <!--/p-->
		                    <!-- Add cache here -->
		                    <a class="moreFromThisSiteLink" href="http://lp.search.gov.hk:8080/Action=View&amp;NoACI=true&amp;reference=http%3A%2F%2Fwww.nd.gov.hk%2Ftc%2Fprevent_away_drugs.htm" onkeydown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);" onmousedown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);">
		                    <span>頁庫存檔</span></a>
		                  </p>
		                 </li>
		
		                <li>
		                  <h3>
		                  	
		                    <a class="itemDetailsTitle" onkeydown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.nd.gov.hk%2Ftc%2Freport_drug.htm&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" onmousedown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.nd.gov.hk%2Ftc%2Freport_drug.htm&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" id="waSearchResultTitle8" href="http://www.nd.gov.hk/tc/report_drug.htm">
		                      <span>保安局禁<strong>毒</strong>處 - 舉報<strong>毒品</strong>罪行</span>
		                    </a>
		                   </h3>
		                  <p>
		                  	<span class="itemDetailsDescription">保安局禁<strong>毒</strong>處 - 舉報<strong>毒品</strong>罪行. Title

				

	

	 

	舉 報 <strong>毒</strong> <strong>品</strong>  罪 行...</span>
		                  </p>
		
		                  <!--/p-->
		                  <p>
		                    <!-- Last Modified Date: 2011-11-09 -->
		                    <span class="itemDetailsLink">www.nd.gov.hk/tc/report_drug.htm</span>
		                    - 
		                    <span>7.2K</span>
		                    <span> - </span>
		                    <span>15/03/2016</span>
		                    <span> - </span>
		                    <!--/p-->
		                    <!-- Add cache here -->
		                    <a class="moreFromThisSiteLink" href="http://lp.search.gov.hk:8080/Action=View&amp;NoACI=true&amp;reference=http%3A%2F%2Fwww.nd.gov.hk%2Ftc%2Freport_drug.htm" onkeydown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);" onmousedown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);">
		                    <span>頁庫存檔</span></a>
		                  </p>
		                 </li>
		
		                <li>
		                  <h3>
		                  	
		                    <a class="itemDetailsTitle" onkeydown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.nd.gov.hk%2Ftc%2Fhallucinogens.htm&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" onmousedown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.nd.gov.hk%2Ftc%2Fhallucinogens.htm&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" id="waSearchResultTitle9" href="http://www.nd.gov.hk/tc/hallucinogens.htm">
		                      <span>保安局禁<strong>毒</strong>處 - <strong>毒品</strong>迷幻劑資料</span>
		                    </a>
		                   </h3>
		                  <p>
		                  	<span class="itemDetailsDescription">保安局禁<strong>毒</strong>處 - <strong>毒品</strong>迷幻劑資料. 有 用 資 料 

	迷 幻 劑 



	物質 	俗稱 	醫藥用途...</span>
		                  </p>
		
		                  <!--/p-->
		                  <p>
		                    <!-- Last Modified Date: 2011-11-09 -->
		                    <span class="itemDetailsLink">www.nd.gov.hk/tc/hallucinogens.htm</span>
		                    - 
		                    <span>8.9K</span>
		                    <span> - </span>
		                    <span>14/03/2016</span>
		                    <span> - </span>
		                    <!--/p-->
		                    <!-- Add cache here -->
		                    <a class="moreFromThisSiteLink" href="http://lp.search.gov.hk:8080/Action=View&amp;NoACI=true&amp;reference=http%3A%2F%2Fwww.nd.gov.hk%2Ftc%2Fhallucinogens.htm" onkeydown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);" onmousedown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);">
		                    <span>頁庫存檔</span></a>
		                  </p>
		                 </li>
		
		                <li>
		                  <h3>
		                  	
		                    <a class="itemDetailsTitle" onkeydown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.nd.gov.hk%2Ftc%2Fprevent_away_drugs_archives.htm&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" onmousedown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.nd.gov.hk%2Ftc%2Fprevent_away_drugs_archives.htm&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" id="waSearchResultTitle10" href="http://www.nd.gov.hk/tc/prevent_away_drugs_archives.htm">
		                      <span>保安局禁<strong>毒</strong>處 - 《健康生活　遠離<strong>毒品</strong>》藥物教育教材套 - 資料庫</span>
		                    </a>
		                   </h3>
		                  <p>
		                  	<span class="itemDetailsDescription">保安局禁<strong>毒</strong>處 - 《健康生活　遠離<strong>毒品</strong>》藥物教育教材套 - 資料庫. Title

				

	禁 <strong>毒</strong> ...</span>
		                  </p>
		
		                  <!--/p-->
		                  <p>
		                    <!-- Last Modified Date: 2011-11-09 -->
		                    <span class="itemDetailsLink">www.nd.gov.hk/tc/prevent_away_drugs_archives.htm</span>
		                    - 
		                    <span>18.4K</span>
		                    <span> - </span>
		                    <span>15/03/2016</span>
		                    <span> - </span>
		                    <!--/p-->
		                    <!-- Add cache here -->
		                    <a class="moreFromThisSiteLink" href="http://lp.search.gov.hk:8080/Action=View&amp;NoACI=true&amp;reference=http%3A%2F%2Fwww.nd.gov.hk%2Ftc%2Fprevent_away_drugs_archives.htm" onkeydown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);" onmousedown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);">
		                    <span>頁庫存檔</span></a>
		                  </p>
		                 </li>
		                <!--search result list end-->
		              </ol>
                   	</div>
				</div>
				
				</div>
				<!-- Related keyword suggestion -->
				<div id="ajaxResult">
				
				</div>
				<!-- Use AJAX in this part
				<div th:if="${rkwListArr != null}">
					<div class="clearthis">
                       <div class="lineseq"></div>
                    </div>
                    <br/>
                    <div  >
                    <span th:text="#{label.rkw.text}">相關搜尋</span>
                    <div style="overflow:hidden">
                    	<div th:each="rkwList: ${rkwListArr}" class="brs_col">
                    		<p th:each="currItem : ${rkwList}" class="rkwLink">
                    			<a th:href="@{${oriUrl}(query=${currItem},ui_lang=${ui_lang},tpl_id=${tpl_id},output=${output},ui_charset=${ui_charset},gp0=${gp0},gp1=${gp1},web=${web},txtonly=${txtonly},site=${site})}" 
                    			th:text="${currItem}" th:title="${currItem}"></a>
                    		</p>
                    	</div>
                    </div>
                    </div>
				</div>
				-->
                    <!-- Footer search box and paging -->
                    <div>
                    <div class="clearthis">
                       <div class="lineseq"></div>
                    </div>
                    <div class="advancedRow clearthis">
				       <form name="gs2" method="GET" onsubmit="searchFormSubmit(this);return false;" id="gs1" action="/search">
				          <div class="clearthis">
				             <div class="searchBoxContainer2">
				                <div class="searchBoxContainer2 ui-widget">
				                   <div>
				                   <label for="searchBox3" class="access">搜尋</label>
				                   <input type="text" class="searchBox ui-autocomplete-input" name="query" id="searchBox3" autocomplete="off" value="毒品" />
				                   <label for="searchIcon3" class="access">Search Submit</label>
				                   <input type="submit" title="Search" class="searchIcon2" id="searchIcon2" name="search_but" value="" />
				                   </div>
				                </div>
				             </div>
				             <div class="advSearch"><a href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-hk&amp;tpl_id=stdsearch&amp;page=1&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;a_submit=false&amp;toASubmit=true&amp;gp0=nd_home&amp;gp1=nd_home&amp;doc_type=all&amp;sort=&amp;web=this&amp;txtonly=0&amp;site=nd_home&amp;exact_q=&amp;any_q=&amp;none_q=&amp;tab=&amp;tab_depts=">進階搜尋</a></div>
				             <input type="hidden" name="output" value="xml_no_dtd" />
				             <input type="hidden" name="ui_lang" value="zh-hk" />
				             <input type="hidden" name="gp1" value="nd_home" />
				             <input type="hidden" name="gp0" value="nd_home" />
				             <input type="hidden" name="web" value="this" />
				             <input type="hidden" name="txtonly" value="0" />
				             <input type="hidden" name="tpl_id" value="stdsearch" />
				             <input type="hidden" name="sort" value="" />
				             <input type="hidden" name="doc_type" value="all" />
				             
				             
							 
							 <div id="stdTplRadioButton" class="clearthis">
				             <fieldset><legend class="hidden">顯示：</legend>
								<span>顯示：</span>&nbsp;
								<input type="radio" id="yschtopsearch1all_ck_top_1" name="site" value="default_collection" />
								<label for="yschtopsearch1all_ck_top_1">所有政府網站</label>
								<input type="radio" id="yschtopsearch1this_ck_top_1" name="site" checked="checked" value="nd_home" />
								<label for="yschtopsearch1this_ck_top_1">禁毒處</label>
							 </fieldset>
							 </div>
							</div>
						</form>
                	</div>
                	
                	<!-- Paging -->
                	<div class="advancedIndex">
                	<span class="b">
						
					</span>&nbsp;
				    <span>
				        <strong><span class="current">1</span></strong>
				        
				        <span>&nbsp;-</span>
				      </span>
				    <span>
				        <strong></strong>
				        <a onclick="clickCount('paginationTool', '', '')" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-hk&amp;tpl_id=stdsearch&amp;page=2&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;a_submit=false&amp;gp0=nd_home&amp;gp1=nd_home&amp;doc_type=all&amp;web=this&amp;txtonly=0&amp;site=nd_home&amp;last_mod=%23-1&amp;tab=&amp;tab_depts=&amp;sort=">
				        <span>2</span></a>
				        <span>&nbsp;-</span>
				      </span>
				    <span>
				        <strong></strong>
				        <a onclick="clickCount('paginationTool', '', '')" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-hk&amp;tpl_id=stdsearch&amp;page=3&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;a_submit=false&amp;gp0=nd_home&amp;gp1=nd_home&amp;doc_type=all&amp;web=this&amp;txtonly=0&amp;site=nd_home&amp;last_mod=%23-1&amp;tab=&amp;tab_depts=&amp;sort=">
				        <span>3</span></a>
				        <span>&nbsp;-</span>
				      </span>
				    <span>
				        <strong></strong>
				        <a onclick="clickCount('paginationTool', '', '')" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-hk&amp;tpl_id=stdsearch&amp;page=4&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;a_submit=false&amp;gp0=nd_home&amp;gp1=nd_home&amp;doc_type=all&amp;web=this&amp;txtonly=0&amp;site=nd_home&amp;last_mod=%23-1&amp;tab=&amp;tab_depts=&amp;sort=">
				        <span>4</span></a>
				        <span>&nbsp;-</span>
				      </span>
				    <span>
				        <strong></strong>
				        <a onclick="clickCount('paginationTool', '', '')" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-hk&amp;tpl_id=stdsearch&amp;page=5&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;a_submit=false&amp;gp0=nd_home&amp;gp1=nd_home&amp;doc_type=all&amp;web=this&amp;txtonly=0&amp;site=nd_home&amp;last_mod=%23-1&amp;tab=&amp;tab_depts=&amp;sort=">
				        <span>5</span></a>
				        <span>&nbsp;-</span>
				      </span>
				    <span>
				        <strong></strong>
				        <a onclick="clickCount('paginationTool', '', '')" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-hk&amp;tpl_id=stdsearch&amp;page=6&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;a_submit=false&amp;gp0=nd_home&amp;gp1=nd_home&amp;doc_type=all&amp;web=this&amp;txtonly=0&amp;site=nd_home&amp;last_mod=%23-1&amp;tab=&amp;tab_depts=&amp;sort=">
				        <span>6</span></a>
				        <span>&nbsp;-</span>
				      </span>
				    <span>
				        <strong></strong>
				        <a onclick="clickCount('paginationTool', '', '')" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-hk&amp;tpl_id=stdsearch&amp;page=7&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;a_submit=false&amp;gp0=nd_home&amp;gp1=nd_home&amp;doc_type=all&amp;web=this&amp;txtonly=0&amp;site=nd_home&amp;last_mod=%23-1&amp;tab=&amp;tab_depts=&amp;sort=">
				        <span>7</span></a>
				        <span>&nbsp;-</span>
				      </span>
				    <span>
				        <strong></strong>
				        <a onclick="clickCount('paginationTool', '', '')" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-hk&amp;tpl_id=stdsearch&amp;page=8&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;a_submit=false&amp;gp0=nd_home&amp;gp1=nd_home&amp;doc_type=all&amp;web=this&amp;txtonly=0&amp;site=nd_home&amp;last_mod=%23-1&amp;tab=&amp;tab_depts=&amp;sort=">
				        <span>8</span></a>
				        <span>&nbsp;-</span>
				      </span>
				    <span>
				        <strong></strong>
				        <a onclick="clickCount('paginationTool', '', '')" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-hk&amp;tpl_id=stdsearch&amp;page=9&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;a_submit=false&amp;gp0=nd_home&amp;gp1=nd_home&amp;doc_type=all&amp;web=this&amp;txtonly=0&amp;site=nd_home&amp;last_mod=%23-1&amp;tab=&amp;tab_depts=&amp;sort=">
				        <span>9</span></a>
				        <span>&nbsp;-</span>
				      </span>
				    <span>
				        <strong></strong>
				        <a onclick="clickCount('paginationTool', '', '')" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-hk&amp;tpl_id=stdsearch&amp;page=10&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;a_submit=false&amp;gp0=nd_home&amp;gp1=nd_home&amp;doc_type=all&amp;web=this&amp;txtonly=0&amp;site=nd_home&amp;last_mod=%23-1&amp;tab=&amp;tab_depts=&amp;sort=">
				        <span>10</span></a>
				        
				      </span>
					<span class="b">
					  <a onclick="clickCount('paginationTool', '', '')" class="next" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-hk&amp;tpl_id=stdsearch&amp;page=2&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;a_submit=false&amp;gp0=nd_home&amp;gp1=nd_home&amp;doc_type=all&amp;web=this&amp;txtonly=0&amp;site=nd_home&amp;last_mod=%23-1&amp;tab=&amp;tab_depts=&amp;sort=" title="下一頁">下一頁</a>
					</span>
                	</div>
                	</div>
                    <!-- End of footer search box and paging -->
				</div>
			</div>
		</div>
		
		<!-- Advanced search input form -->
		
	</div>
	<!-- pageContainerTopKeywords end -->
	</div>	
	<!-- End of standard template body -->

	<!-- Department template body -->
  <!-- Please enter html code below. -->
  
  <!-- End of Department template body -->
  
  <!-- Standard search footer -->
<div id="pageContainerFooter">
	<div id="footer">
		<div class="access">Footer Menu</div>
		<ul id="auxiliaryMenu">
          <li><a title="About Us" href="http://www.gov.hk/tc/about/aboutus.htm">關於我們</a></li>
          <li><a title="Accessibility" href="http://www.gov.hk/tc/about/accessibility/">無障礙瀏覽</a></li>
          <li><a title="Linking to GovHK" href="http://www.gov.hk/tc/about/linkpolicy/">連結到香港政府一站通</a></li>
          <li><a title="Site Map" href="http://www.gov.hk/tc/about/sitemap.htm">網頁指南</a></li>
          <li class="shortFooter"><a title="Site Map" href="http://www.gov.hk/tc/about/helpdesk/">幫助</a></li>
          <li><a title="Copyright Notice" href="http://www.gov.hk/tc/about/copyright.htm">版權告示</a></li>
          <li><a title="Privacy Policy" href="http://www.gov.hk/tc/about/privacy.htm">私隱政策</a></li>
          <li><a title="Disclaimer" href="http://www.gov.hk/tc/about/disclaimer.htm">免責聲明</a></li>
		</ul>
		<div id="brandhk"><a href="http://www.brandhk.gov.hk/" rel="external" title="Brand Hong Kong">
		<img alt="Brand Hong Kong" title="Brand Hong Kong" src="/search/gov_footer_brandhk_20100331_tc.gif" /></a>
		</div>
	</div>
	<div id="badges">
		<ul id="conformance">
			<li class="w3"><a href="http://www.w3.org/WAI/WCAG2AA-Conformance" rel="external" title="2A無障礙說明">
			<img src="http://www.gov.hk/images/footer/wcag2AA.gif" alt="符合萬維網聯盟有關無障礙網頁設計指引中2A級別的要求" /></a>
			</li>
			<li><a rel="external" href="http://www.webforall.gov.hk/tc/recognition_scheme" title="無障礙網頁嘉許計劃">
			<img src="http://www.gov.hk/tc/images/footer/gold_logo.png" alt="無障礙網頁嘉許計劃" /></a>
			</li>
		</ul>
	</div>
</div>
  <!-- End of standard search footer -->
  <script>
    var ogcioUserKeyword = "${query}";
  </script>
</div>
</body>
</html>

"""

soup = BeautifulSoup(html_doc, "lxml")
soup1 = BeautifulSoup(html_doc1, "lxml")

# founds = soup.find('div', class_='searchResultArea').find_all('li')
# for found in founds:
    # title = found.find('h3').get_text().strip()
    # url = found.find('h3').find('a').get('href')
    # print title, url
    # m = md5.new() #MD5是最常见的摘要算法，又称哈希算法、散列算法
    # m.update(url)
    # md_str = m.hexdigest() #MD5算法编码获得ID号
    # print md_str

    # post_time = found.find_all('p')[1].find_all('span')[3].get_text().strip()
    # # post_time = re.findall(self.tt_pa, post_time)[0] #正则匹配得到时间
    # print post_time

all_p = soup1.find_all('table')[0].get_text().strip()
all_p = soup1.find_all(id="content").find_all('td', bgcolor="#FFFFFF")[1]
content = all_p.get_text().strip()
print all_p
