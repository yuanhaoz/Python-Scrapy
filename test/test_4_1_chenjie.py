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
<html lang="sc_chi">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<title>香港便览</title>

<meta name="robots" content="index,follow">
<meta name="keywords" content="Welcome,Welcome,">
<meta name="description" content="">
<meta http-equiv="Content-Style-Type" content="text/css">
<meta http-equiv="Content-Script-Type" content="type">
<meta content="no-cache" http-equiv="cache-control">
<meta content="no-cache" http-equiv="Pragma">

<link href="/common/image/design/favicon_new.ico" rel="icon" type="image/x-icon">
<link href="/common/image/design/favicon_new.ico" rel="shortcut icon" type="image/x-icon">

<link rel="stylesheet" type="text/css" href="/common/css/bootstrap.css">
<link rel="stylesheet/less" type="text/less" href="/common/css/menu.less">
<link rel="stylesheet/less" href="/sc_chi/css/style.less" type="text/less">

<script type="text/javascript" src="/common/js/lib/less.min.js"></script>
<script type="text/javascript" src="/common/js/lib/jquery-1.9.1.min.js"></script>
<script type="text/javascript" src="/common/js/lib/jquery.rs.slideshow.js"></script>
<script type="text/javascript" src="/common/js/lib/global.js"></script>
<script type="text/javascript" src="/common/js/lib/all.js"></script>
<script type="text/javascript" src="/common/js/lib/bootstrap.min.js"></script>
<script type="text/javascript" src="/common/js/lib/jquery.fancybox.js?v=2.1.4"></script>
<link rel="stylesheet" type="text/css" href="/common/css/jquery.fancybox.css?v=2.1.4" media="screen">

<link rel="stylesheet" type="text/css" href="/common/js/lib/helpers/jquery.fancybox-buttons.css?v=1.0.5">
<script type="text/javascript" src="/common/js/lib/helpers/jquery.fancybox-buttons.js?v=1.0.5"></script>
    <script type="text/javascript" src="/common/js/lib/LightBoxHandle.js"></script>
	<script type="text/javascript" src="/common/js/lib/swfobject.js"></script>
	<script type="text/javascript" src="/common/js/lib/menucontrol.js"></script>
    <script type="text/javascript" src="/common/js/lib/jwplayer.js"></script>
<!--/********************************************************* Mid Slider ***********************************************************/-->
	<script type="text/javascript">

$.fn.infiniteCarousel = function () {

    function repeat(str, num) {
        return new Array( num ).join( str );
    }
  
    return this.each(function () {
        var $wrapper = $('> div', this).css('overflow', 'hidden'),
            $slider = $wrapper.find('> ul'),
            $items = $slider.find('> li'),
            $single = $items.filter(':first'),
            
            singleWidth = $single.outerWidth(), 
            visible = Math.ceil($wrapper.innerWidth() / singleWidth), // note: doesn't include padding or border
            currentPage = 1,
            pages = Math.ceil($items.length / visible);            


        // 1. Pad so that 'visible' number will always be seen, otherwise create empty items
        if (($items.length % visible) != 0) {
            $slider.append(repeat('<li class="empty" />', visible - ($items.length % visible)));
            $items = $slider.find('> li');
        }

        // 2. Top and tail the list with 'visible' number of items, top has the last section, and tail has the first
        $items.filter(':first').before($items.slice(0, visible).clone().addClass('cloned'));
        $items.filter(':last').after($items.slice(- visible).clone().addClass('cloned'));
        $items = $slider.find('> li'); // reselect
        
        // 3. Set the left position to the first 'real' item
        $wrapper.scrollLeft(singleWidth * visible);
        
        // 4. paging function
        function gotoPage(page) {
            var dir = page < currentPage ? -1 : 1,
                n = Math.abs(currentPage - page),
                left = singleWidth * dir * visible * n;
            
            $wrapper.filter(':not(:animated)').animate({
                scrollLeft : '+=' + left
            }, 500, function () {
                if (page == 0) {
                    $wrapper.scrollLeft(singleWidth * visible * pages);
                    page = pages;
                } else if (page > pages) {
                    $wrapper.scrollLeft(singleWidth * visible);
                    // reset back to start position
                    page = 1;
                } 

                currentPage = page;
            });                
            
            return false;
        }
        
         $wrapper.after('<div class="arrow back" /><div class="arrow forward" />');
        
        $(".back").addClass('active');

        // 5. Bind to the forward and back buttons
        $('div.back', this).click(function () {
            $(".back").addClass('active');
            $(".forward").removeClass('active');
            return gotoPage(1);                
        });
        
        $('div.forward', this).click(function () {
            $(".forward").addClass('active');
            $(".back").removeClass('active');
            return gotoPage(2);
        });
        
        // create a public interface to move to a specific page
        $(this).bind('goto', function (event, page) {
            gotoPage(page);
        });
    });  
};

$(document).ready(function () {
  $('.infiniteCarousel').infiniteCarousel();
});
</script>
<!--/****************************************************** Home Shortcut ********************************************************/-->
<script type="text/javascript">
  $(function() {
 
      // $("#power_by img[title]").tooltip();

    });
</script>
<style type="text/css" media="print">
a{color:#000;}#skiptocontent,#menulv3{display: none;} #csd-hklogo{float: right;margin-top: -58px;} .govhk{width:181px;width:171px\9;*width:171px;height: 100%;padding: 0 0 12px 0px;padding: 0 0 12px 0px\9;*padding: 0 0 12px 0px;min-height:0px;font-size: 14p;}  .tcver{width:75px; *width:73px; height: 100%; padding: 0 0 12px 0px; padding: 0 0 12px 0px\9; *padding: 0 0 12px 0px; min-height:0px; font-size: 14px; }.engver{width:56px; height: 100%; padding: 0 0 12px 0px; min-height:0px; font-size: 14px; }.tcver img,.scver img,.engver img{height:20px; height:20px\9; *height:20px\9; }td.bg{width:447px;} td.mail span.mail {display: none;} td.font-small{padding-bottom: 7px;padding-bottom: 9px\9;*padding-bottom: 11px;width: 7px;width:8px\9;font-size: 12px;} td.font-small a{color: red;text-decoration: none;} td.font-medium{font-size:15px;width:10px;padding-bottom: 9px;padding-bottom: 11px\9;*padding-bottom: 13px;} td.font-medium a{color: #000000;text-decoration: none;} td.font-large{font-size:18px;width:10px;padding-bottom: 11px;padding-bottom: 13px\9;*padding-bottom: 13px;} td.font-large a{color: #000000;text-decoration: none;} #csd-menu-nav{font-size: 14px;height: 39px;position: relative;top: 5px;top: 5px\9;width: 1000px;z-index: 2;} span.csd-nav-text{color:#ffffff;margin: -28px 4px 0;} .csd-nav-search{float:right;width:85px;} .csd-nav-mobile{width: 215px; margin-top: 3px; float: left; margin-left: 410px; } .csd-nav-sitemap{float:left; width:100px; margin-top:3px; } .csd-nav-print{float:left; width:120px; margin-top: 3px; } .jump-to-content{float:left; margin-left:5px; width:150px; margin-top: 3px; } .skip-to-content {position:absolute; left:0px; top:-500px; width:1px; height:1px; overflow:hidden; }.menuback{display: none;} .menutable ul,.menutable li{list-style-type: none;padding: 0;margin: 0;}.menutable li{list-style-type: none;}.menutable a{color: #000;}#leftmenuDiv,#About{float: left;}.csd-w3c {position: absolute; z-index: 2; width: 88px; margin-left: 50px; top: 500px; } #csd-footer{display: block; margin-left:auto; margin-right:auto; width: 1000px; position: relative; z-index: 1; float: left; background-color: gray; } .csd-footer-hklogo{width:96px; height:36px; } .csd-footer-bar{width:2px; height:36px; margin: -35px 110px 0; } .csd-policy{color:#ffffff; height:30px; font-size:13px; position:relative; padding-top: 10px; margin-left:20px; } .csd-policy a{color:#ffffff; } .csd-policy a:hover{color:#ffffff; } .csd-version{color: #ffffff; float: right; font-size: 11px; } .menu_icon{position: absolute; z-index: 2; width: 88px; margin-left: 0px; top: 650px; }
</style>
</head>
<body>
	<div id="skipwrapper">
		<a name="skiptocontent" id="skiptocontent" href="#content" class="skip-to-content">Skip to main content</a>
	</div>
	<!-- header start -->
	<form name="searchform" method="get" action="http://search.gov.hk/search.html">
	<div id="csd-header">
		<div id="csd-logo">
			<a href="/index.html" tabindex="1"> <img src="/images/sc_chi/design/36_logo.png" alt="香港特别行政区政府 | 香港惩教署" title="香港特别行政区政府 | 香港惩教署" /></a>
		</div>
		<div class="noprint">
			<div id="csd-hklogo">
				<a href="http://www.brandhk.gov.hk/brandhk/index.htm" rel="external" tabindex="2"> <img src="/images/design/_tcindex.gif"
					alt="香港品牌形象-亚洲国际都会" title="香港品牌形象-亚洲国际都会" /></a>
			</div>
			<!-- 		<script type="text/javascript">
				function headerFormSubmit() {
					if (document.getElementById('hksarg_search0').q.value.length == 0) {
						alert('Please enter keyword.');
					} else {
						document.getElementById('hksarg_search0').submit();
					}
					return;
				}
			</script>-->

			<table class="header-nav">
				<tr>
					<td class="govhk"><a href="http://www.gov.hk/en/residents/" onblur="MM_swapImgRestore()" onfocus="MM_swapImage(&quot;mainbar1e&quot;,&quot;&quot;,&quot;/images/mainbar1_f2e.gif&quot;,1)" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage(&quot;mainbar1e&quot;,&quot;&quot;,&quot;/images/mainbar1_f2e.gif&quot;,1)" tabindex="3"><img alt="GovHK 香港政府一站通" id="mainbar1e" name="mainbar1e" src="/images/mainbar1e.gif" style="border:0 px" title="GovHK 香港政府一站通" /></a></td>
					
					<td class="engver"><a href="javascript:chglang('en')" onblur="MM_swapImgRestore()" onfocus="MM_swapImage(&quot;mainbar5&quot;,&quot;&quot;,&quot;/images/mainbar5_f2.gif&quot;,1)" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage(&quot;mainbar5&quot;,&quot;&quot;,&quot;/images/mainbar5_f2.gif&quot;,1)" tabindex="4"><img alt="ENGLISH" id="mainbar5" name="mainbar5" src="/images/mainbar5.gif" style="border:0 px" title="ENGLISH" /></a></td>

					<td class="tcver"><a href="javascript:chglang('tc')" onblur="MM_swapImgRestore()" onfocus="MM_swapImage(&quot;mainbar3&quot;,&quot;&quot;,&quot;/images/mainbar3_f2.gif&quot;,1)" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage(&quot;mainbar3&quot;,&quot;&quot;,&quot;/images/mainbar3_f2.gif&quot;,1)" tabindex="5"><img alt="繁體版" id="mainbar3" name="mainbar3" src="/images/mainbar3.gif" style="border:0 px" title="繁體版" /><img src="/images/mainbar6.gif" alt="barcon"/></a></td>

					<!--td class="scver"><a href="javascript:chglang('sc')" tabindex="6" lang="zh-cn">简体版</a></td-->

					<td class="bg"></td>
					<td class="font-small"><a href="javascript:changeFontSize(0)" id="fontSizeM" onclick="this.style.color='red';document.getElementById('fontSizeL').style.color='black';document.getElementById('fontSizeEx').style.color='black'" tabindex="6"><span class="font-small">A</span></a></td>
					<td class="font-medium"><a href="javascript:changeFontSize(0)" id="fontSizeL" onclick="this.style.color='red';document.getElementById('fontSizeM').style.color='black';document.getElementById('fontSizeEx').style.color='black'" tabindex="7"><span class="font-normal">A</span></a></td>
					<td class="font-large"><a href="javascript:changeFontSize(0)" id="fontSizeEx" onclick="this.style.color='red';document.getElementById('fontSizeM').style.color='black';document.getElementById('fontSizeL').style.color='black'" tabindex="8"><span class="font-large">A</span></a></td>
					<td class="csd-nav-search-box">
						<div class="input-append">
							<input name="query" onblur="if(this.value=='')this.value='';" onclick="if(this.value=='输入查询字串')this.value=''" onfocus="this.select();" onkeypress="if(this.value=='输入查询字串')this.value=''" onmouseout="if(this.value=='')this.value='';" onmouseover="this.focus();" size="21" tabindex="9" title="输入查询字串" type="text" value="输入查询字串" /> <input name="tpl_id" tabindex="9" type="hidden" value="stdsearch" /> <input name="ui_lang" tabindex="11" type="hidden" value="zh-cn" /> <input name="ui_charset" tabindex="12" type="hidden" value="utf-8" /> <input name="site" type="hidden" value="csd_home" /> <input name="gp1" type="hidden" value="csd_home" /> <input name="gp0" type="hidden" value="csd_home" /> <input name="web" type="hidden" value="this" /> <input name="exact_q" type="hidden" value="" /> <input name="any_q" type="hidden" value="" /> <input name="a_submit" type="hidden" value="false" /><input id="searchIcon" type="submit" value="" style="display: none" />
						</div>
					</td>
					<td class="searchimg"><a href="javascript:document.searchform.submit();" tabindex="10"  onblur="javascript()" onfocus="javascript()" onmouseover="this.src='/images/design/_hover_ico_magnifier_hover.png'"
							onmouseout="this.src='/images/design/__ico_magnifier_head.png'" ><img id="input-append" alt="提交搜寻内容" title="提交搜寻内容"
							src="/images/design/__ico_magnifier_head.png" /></a></td>
					<td class="mail"><a href="/sc_chi/contactus/other_contact.html" tabindex="11" onblur="javascript()" onfocus="javascript()" onmouseover="this.src='/images/design/_hover_ico_mail_hover.png'"
							onmouseout="this.src='/images/design/__ico_mail.png'" ><img src="/images/design/__ico_mail.png" alt="联络我们"  title="联络我们" /><span class="mail">1</span></a></td>					</tr>
				</tbody>
			</table>
			<div id="csd-menu-nav">
				<div class="jump-to-content">
					<a href="#content" tabindex="12"><img src="/sc_chi/image/general/__btn_jump.png" alt="跳至內容" title="跳至內容"><span class="csd-nav-text">跳至內容</span></a>
				</div>
				<div class="csd-nav-mobile">
					<a href="javascript:gotoMobileVersion();" tabindex="13"><img src="/sc_chi/image/general/__btn_moblie.png" alt="流动／无障碍浏览版本" title="流动／无障碍浏览版本"><span class="csd-nav-text">流动／无障碍浏览版本</span></a>
				</div>
				<div class="csd-nav-print">
					<a href="javascript:printPage();" tabindex="14"><img src="/sc_chi/image/general/__btn_print.png" alt="列印版本" title="列印版本"><span class="csd-nav-text">列印版本</span></a>
				</div>													
				<div class="csd-nav-sitemap">
					<a href="/sc_chi/sitemap/sitemap.html" tabindex="15"><img src="/sc_chi/image/general/__map.png" alt="网页指南" title="网页指南"><span class="csd-nav-text">网页指南</span></a>
				</div>					
			</div>
<!--div class="banner-title">
				<img src="/sc_chi/common/image/design/__banner_csd.png" alt="csdTitle" />
				<p>Research Fund Secretariat</p>
			</div-->		</div>
		<div class="no-print">
			<div class="menulogo">
				&nbsp;</div>
		</div>
	</div>
</form>
<!--form name="searchform" method="get" action="http://search.gov.hk/search.html">
	<div id="csd-header">
		<div class="no-print">
		<img src="/CSD/sc_chi/image/general/__B_header.png" alt="header">
			<div class="menulogo"><a href="/CSD/sc_chi/welcome/welcome.html"></a></div>
		</div>
	</div>
</form-->

	<div class="container">
	<div class="noprint">
	</div>
	<div id="leftmenuDiv">
		<script type='text/javascript'>
    function activeMenu() {
        var w = window.location + '';
        var folders = w.split('/');
        var menu_li;

        if (folders.length < 6) {
            $('.menu_li_lv1').first().removeClass('in-active').addClass(
                    'active');

        } else {
            $('.menu_li_lv1 a[href="/' + folders[3] + '/' + folders[4] + '"]')
                    .parent().removeClass('in-active').addClass('active');

        }
    }

    $(window).load(
            function() {

                $('ul.sf-menu').find('li').removeClass('in-active active')
                        .addClass('in-active');

                $('ul.sf-menu .menu_li_lv1')
                        .mouseover(
                                function() {
                                    $('ul.sf-menu').find('li').removeClass('in-active active').addClass('in-active');
                                    $('ul.sf-menu').find('ul').removeClass('in-active active').addClass('in-active');
                                    $(this).removeClass('in-active').addClass('active');

                                });
                $('ul.sf-menu .menu_li_lv2')
                        .mouseover(
                                function() {
                                    $('ul.sf-menu').find('li').removeClass('in-active active').addClass('in-active');
                                    $('ul.sf-menu').find('ul').removeClass('in-active active').addClass('in-active');
                                    $(this).removeClass('in-active').addClass('active');

                                });

                $('ul.sf-menu .menu_li_lv1').mouseout(function() {
                    $(this).removeClass('active').addClass('in-active');
                    activeMenu();
                });


                $('ul.sf-menu a').focus(
                        function() {
                            $('ul.sf-menu').find('li').removeClass('in-active active').addClass('in-active');
                            $(this).parent().parent().addClass('active').removeClass('in-active');
                            $(this).parent().parent().parent().parent().addClass('active').removeClass('in-active');
                            $(this).parent().parent().parent().parent().parent().parent().addClass('active').removeClass('in-active'); 

                        });
                        
                $('ul.sf-menu a').blur(  
                        function() {
                            $(this).parent().parent().parent().find('ul').removeClass('active').addClass('in-active');
                            activeMenu();
                        });
                        
                        
                $('ul.sf-menu a').last().blur(
                        function() {
                            $('ul.sf-menu ul').removeClass('active').addClass('in-active');
                        });

                activeMenu();
            });
</script><div class='noprint' id='content'><table class='menutable'><tr><td><div class='menuback'><img src="/images/design/_-31.png" alt="CSD"></div><div class='menuvalue'><ul class='sf-menu sf-vertical menulv2' id='menulv1'><li class='menu_layer1_li layer1_0'><div class='csd-leftmenu-nav'><a class='menu_lv1 TextFGSelected_2_1' href="/sc_chi/home/home.html" target='_top'>主页</a></div><div class='separate-line'></div></li><li class='hover-menu menu_layer1_li layer1_1'><div class='csd-leftmenu-nav'><a class='menu_lv1 TextFGSelected_2_1' href="/sc_chi/news/news.html" target='_top'>新闻及活动</a></div><div class='separate-line'></div><ul class='actions no-style' id='menulv3'><li class='menu_li_lv2'><a href="/sc_chi/news/news_pr/news_pr.html" target='_top'>新闻</a><div class='separate-line'></div></li><li class='menu_li_lv2'><a href="/sc_chi/news/news_st/news_st.html" target='_top'>专题报导</a><div class='separate-line'></div></li></ul></li><li class='hover-menu menu_layer1_li layer1_2'><div class='csd-leftmenu-nav'><a class='menu_lv1 TextFGSelected_2_1' href="/sc_chi/about/abt.html" target='_top'>关于我们</a></div><div class='separate-line'></div><ul class='actions no-style' id='menulv3'><li class='menu_li_lv2'><a href="/sc_chi/about/about_ccs/abt_mess.html" target='_top'>欢迎辞</a><div class='separate-line'></div></li><li class='menu_li_lv2'><a href="/sc_chi/about/about_vmv/abt_vis.html" target='_top'>抱负、任务及价值观</a><div class='separate-line'></div></li><li class='menu_li_lv2'><a href="/sc_chi/about/about_org/abt_org.html" target='_top'>组织架构</a><div class='separate-line'></div></li><li class='menu_li_lv2'><a href="/sc_chi/about/about_history/abt_his.html" target='_top'>历史</a><div class='separate-line'></div></li><li class='menu_li_lv2'><a href="/sc_chi/about/about_healthy/lifestyle.html" target='_top'>健康均衡生活</a><div class='separate-line'></div></li><li class='menu_li_lv2'><a href="/sc_chi/about/about_4factors/reh_over_4csf.html" target='_top'>建立更安全及共融社会的四个主要成功因素</a><div class='separate-line'></div></li><li class='menu_li_lv2'><a href="/sc_chi/about/about_museum/hong_kong_correctional_services_museum.html" target='_top'>香港惩教博物馆</a><div class='separate-line'></div></li></ul></li><li class='hover-menu menu_layer1_li layer1_3'><div class='csd-leftmenu-nav'><a class='menu_lv1 TextFGSelected_2_1' href="/sc_chi/facility/ins_over.html" target='_top'>设施概览</a></div><div class='separate-line'></div><ul class='actions no-style' id='menulv3'><li class='menu_li_lv2'><a href="/sc_chi/facility/facility_type/ins_ins.html" target='_top'>设施类别</a><div class='separate-line'></div></li><li class='menu_li_lv2'><a href="/sc_chi/facility/facility_ind/ins_ind.html" target='_top'>设施资料</a><div class='separate-line'></div></li><li class='menu_li_lv2'><a href="/sc_chi/facility/facility_mgt/ins_pen.html" target='_top'>院所管理</a><div class='separate-line'></div></li></ul></li><li class='menu_layer1_li layer1_4'><div class='csd-leftmenu-nav'><a class='menu_lv1 TextFGSelected_2_1' href="/sc_chi/socialvisit/ins_vis_guide.html" target='_top'>亲友探访安排</a></div><div class='separate-line'></div></li><li class='hover-menu menu_layer1_li layer1_5'><div class='csd-leftmenu-nav'><a class='menu_lv1 TextFGSelected_2_1' href="/sc_chi/reh/reh_overview/reh_over.html" target='_top'>更生事务</a></div><div class='separate-line'></div><ul class='actions no-style' id='menulv3'><li class='hover-menu menu_li_lv2'><a href="/sc_chi/reh/reh_overview/reh_over.html" target='_top'>概览</a><div class='separate-line'></div><ul class='actions no-style' id='menulv4'><li class='menu_li_lv3'><a href="/sc_chi/reh/reh_overview/reh_overview_assessment/reh_ru1_asmt.html" target='_top'>评估</a><div class='separate-line'></div></li><li class='menu_li_lv3'><a href="/sc_chi/reh/reh_overview/reh_overview_education/reh_edu.html" target='_top'>教育</a><div class='separate-line'></div></li><li class='menu_li_lv3'><a href="/sc_chi/reh/reh_overview/reh_overview_psy/reh_ps.html" target='_top'>心理服务</a><div class='separate-line'></div></li><li class='menu_li_lv3'><a href="/sc_chi/reh/reh_overview/reh_overview_welfare/reh_ru2_prog.html" target='_top'>福利及辅导</a><div class='separate-line'></div></li><li class='menu_li_lv3'><a href="/sc_chi/reh/reh_overview/reh_overview_religious/reh_over_rs.html" target='_top'>宗教服务</a><div class='separate-line'></div></li><li class='menu_li_lv3'><a href="/sc_chi/reh/reh_overview/reh_overview_prerelease/reh_over_pr.html" target='_top'>就业服务</a><div class='separate-line'></div></li><li class='menu_li_lv3'><a href="/sc_chi/reh/reh_overview/reh_overview_supervision/reh_ru_supn.html" target='_top'>监管服务</a><div class='separate-line'></div></li><li class='menu_li_lv3'><a href="/sc_chi/reh/reh_overview/reh_overview_halfway/reh_over_hhs.html" target='_top'>中途宿舍</a><div class='separate-line'></div></li></ul></li><li class='menu_li_lv2'><a href="/sc_chi/reh/reh_ivt/reh_ind_vt.html" target='_top'>工业及职业训练</a><div class='separate-line'></div></li><li class='menu_li_lv2'><a href="/sc_chi/reh/reh_publicity/reh_pub.html" target='_top'>宣传活动</a><div class='separate-line'></div></li><li class='hover-menu menu_li_lv2'><a href="/sc_chi/reh/reh_community/reh_over_csi.html" target='_top'>社区支援及参与</a><div class='separate-line'></div><ul class='actions no-style' id='menulv4'><li class='menu_li_lv3'><a href="/sc_chi/reh/reh_community/reh_community_ccsro/reh_over_csro.html" target='_top'>社区参与助更生委员会</a><div class='separate-line'></div></li><li class='menu_li_lv3'><a href="/sc_chi/reh/reh_community/reh_community_rpp/reh_over_peps.html" target='_top'>更生先锋计划</a><div class='separate-line'></div></li><li class='menu_li_lv3'><a href="/sc_chi/reh/reh_community/reh_community_vg/reh_over_vg.html" target='_top'>惩教更生义工团</a><div class='separate-line'></div></li></ul></li><li class='menu_li_lv2'><a href="/sc_chi/reh/reh_other/tv_and_radio_apis_and_posters.html" target='_top'>宣传片段及海报</a><div class='separate-line'></div></li></ul></li><li class='hover-menu menu_layer1_li layer1_6'><div class='csd-leftmenu-nav'><a class='menu_lv1 TextFGSelected_2_1' href="/sc_chi/recruit/recruit.html" target='_top'>招聘事宜</a></div><div class='separate-line'></div><ul class='actions no-style' id='menulv3'><li class='menu_li_lv2'><a href="/sc_chi/recruit/recruit_abtpost/other_car_detail.html" target='_top'>关于惩教署职位</a><div class='separate-line'></div></li><li class='menu_li_lv2'><a href="/sc_chi/recruit/recruit_vacancy/other_car_vac.html" target='_top'>职位空缺</a><div class='separate-line'></div></li><li class='menu_li_lv2'><a href="/sc_chi/recruit/recruit_form/recruit_form.html" target='_top'>表格及资源</a><div class='separate-line'></div></li></ul></li><li class='hover-menu menu_layer1_li layer1_7'><div class='csd-leftmenu-nav'><a class='menu_lv1 TextFGSelected_2_1' href="/sc_chi/pub/pub.html" target='_top'>刊物</a></div><div class='separate-line'></div><ul class='actions no-style' id='menulv3'><li class='menu_li_lv2'><a href="/sc_chi/pub/pub_guardian/pub_tg.html" target='_top'>爱羣</a><div class='separate-line'></div></li><li class='menu_li_lv2'><a href="/sc_chi/pub/pub_ar/pub_ar.html" target='_top'>年报</a><div class='separate-line'></div></li><li class='menu_li_lv2'><a href="/sc_chi/pub/2016_02_03_04_21_40/statistics_2015.html" target='_top'>惩教署2015年统计数字</a><div class='separate-line'></div></li><li class='menu_li_lv2'><a href="/sc_chi/pub/pub_off/pub_newsletter.html" target='_top'>在囚人士刊物</a><div class='separate-line'></div></li><li class='menu_li_lv2'><a href="/sc_chi/pub/pub_hkfs/pub_hkfs.html" target='_top'>香港便览</a><div class='separate-line'></div></li><li class='menu_li_lv2'><a href="/sc_chi/pub/csd_series_with_ta_kung_pao/csd_series_with_ta_kung_pao.html" target='_top'>惩教内望系列</a><div class='separate-line'></div></li><li class='menu_li_lv2'><a href="/sc_chi/pub/pub_society_guardian/society_s_guardians.html" target='_top'>香港惩教 任重道远</a><div class='separate-line'></div></li></ul></li><li class='menu_layer1_li layer1_8'><div class='csd-leftmenu-nav'><a class='menu_lv1 TextFGSelected_2_1' href="/sc_chi/statistics/statistics.html" target='_top'>统计资料</a></div><div class='separate-line'></div></li><li class='hover-menu menu_layer1_li layer1_9'><div class='csd-leftmenu-nav'><a class='menu_lv1 TextFGSelected_2_1' href="/sc_chi/mmc/reh_over_newmedia.html" target='_top'>多媒体中心</a></div><div class='separate-line'></div><ul class='actions no-style' id='menulv3'><li class='menu_li_lv2'><a href="/sc_chi/mmc/mmc_tv/pub_tv.html" target='_top'>电视节目</a><div class='separate-line'></div></li><li class='menu_li_lv2'><a href="/sc_chi/mmc/mmc_video/pub_video.html" target='_top'>影片</a><div class='separate-line'></div></li><li class='menu_li_lv2'><a href="/sc_chi/mmc/mmc_song/pub_songs.html" target='_top'>歌曲集</a><div class='separate-line'></div></li><li class='menu_li_lv2'><a href="/sc_chi/mmc/mmc_ecard/e_card.html" target='_top'>电子贺卡</a><div class='separate-line'></div></li></ul></li><li class='hover-menu menu_layer1_li layer1_10'><div class='csd-leftmenu-nav'><a class='menu_lv1 TextFGSelected_2_1' href="/sc_chi/info/info.html" target='_top'>资讯台</a></div><div class='separate-line'></div><ul class='actions no-style' id='menulv3'><li class='menu_li_lv2'><a href="/sc_chi/info/info_accinfo/other_acc.html" target='_top'>公开资料守则</a><div class='separate-line'></div></li><li class='menu_li_lv2'><a href="/sc_chi/info/info_aos/info_aos.html" target='_top'>无障碍统筹经理和无障碍主任的制度</a><div class='separate-line'></div></li><li class='menu_li_lv2'><a href="/sc_chi/info/info_privacy/other_pri.html" target='_top'>私隐声明</a><div class='separate-line'></div></li><li class='menu_li_lv2'><a href="/sc_chi/info/info_complaint/other_complaint.html" target='_top'>投诉渠道</a><div class='separate-line'></div></li><li class='menu_li_lv2'><a href="/sc_chi/info/info_bwc/info_bwc.html" target='_top'>使用随身摄录机</a><div class='separate-line'></div></li><li class='menu_li_lv2'><a href="/sc_chi/info/info_aircraft/info_aircraft.html" target='_top'>在惩教院所范围内操作无人驾驶飞机系统的资讯</a><div class='separate-line'></div></li><li class='menu_li_lv2'><a href="/sc_chi/info/indoor_air_quality_iaq_certification_scheme/indoor_air_quality_of_correctional_services_department_csd_s_offices_or_public_places.html" target='_top'>办公室及公众场所室内空气质素检定计划</a><div class='separate-line'></div></li><li class='menu_li_lv2'><a href="/sc_chi/info/info_link/other_links.html" target='_top'>相关连结</a><div class='separate-line'></div></li></ul></li><li class='menu_layer1_li layer1_11'><div class='csd-leftmenu-nav'><a class='menu_lv1 TextFGSelected_2_1' href="/sc_chi/tender/other_tender.html" target='_top'>招标通告</a></div><div class='separate-line'></div></li></ul></div></td></tr></table><div class="menu_icon"><table cellpadding="0" cellspacing="0">
	<tbody>
		<tr>
			<td colspan="2">
				<a href="http://www.ogcio.gov.hk/sc/community/web_accessibility/recognition_scheme/" target="_blank"><img alt="无障碍网页嘉许计划" src="/images/english/design/wa_gold.jpg" title="无障碍网页嘉许计划" width="84" /></a></td>
		</tr>
		<tr>
			<td colspan="2">
				<a href="http://www.sb.gov.hk/sc/news/mobileapp/" target="_blank"><img alt="保安局「保安一站通」流动应用程式" src="/images/sc_chi/design/sb_mobile.gif" title="保安局「保安一站通」流动应用程式" width="84" /></a></td>
		</tr>
		<tr>
			<td colspan="2">
				<a href="http://www.ceo.gov.hk/report-yearfour/sim/index.html" target="_blank"><img alt="本届政府上任第四年施政汇报" src="/images/sc_chi/design/Mid-report_banner_84x50_SC.gif" title="本届政府上任第四年施政汇报" width="84" /></a></td>
		</tr>
		<tr>
			<td colspan="2">
				<a href="http://www.elections.gov.hk/legco2016/sim/index.html# " target="_blank"><img alt="2016立法会选举" src="/images/sc_chi/design/84x50 -SC.jpg" title="2016立法会选举" width="84" /></a></td>
		</tr>
<!--<tr>
			<td colspan="2">
				<a href="http://www.budget.gov.hk/2016/sim/index.html" target="_blank"><img alt="2016-17 财政预算案" src="/images/sc_chi/design/budget17.gif" title="2016-17 财政预算案" width="84" /></a></td>
		</tr>-->	</tbody>
</table>
<p>
	&nbsp;</p>
</div><table class="getHeight2" id="getHeight2"><tr><td></td></tr></table></div>
	</div><div class="Pubbanner" id="About"><img src="/images/sc_chi/images/general/banner-19.png" alt="Publication"></div><h1>香港便览</h1><div class='breadcrumbs'><a href='/sc_chi/pub/pub.html'>刊物</a> &nbsp; &gt; &nbsp; <a href='/sc_chi/pub/pub_hkfs/pub.html'>香港便览</a></div><br/><div class='separatorLine'><img src='/images/design/line.png' alt='line'></div><div class="getHeight" id="getHeight"><!-- BEGIN CONTENT --><ul class="index_bullet_star_abt">  	<li>  		<a href="/images/doc/pub/pub_off/fact_sheet_sc.pdf" target="_blank">下载PDF版本 </a></li>  </ul>  <h1>  	惩教事务</h1>  <p>  	香港的惩教制度对改造罪犯及协助他们更生这两方面均越来越重视，经过多年的发展，备受国际推许。惩教署特为各类在囚人士，包括年轻犯人、吸毒者、初犯和积犯，制订了多项周详的更生计划。<br />  	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;惩教署的职员编制为6&nbsp;907人，负责管理29间惩教设施，当中包括有惩教院所、中途宿舍和设于公立医院的羁留病房。惩教院所包括低度设防、中度设防和高度设防监狱、精神病治疗中心、教导所、劳教中心、更生中心及戒毒所。除24间惩教院所外，惩教署有三间中途宿舍，以及两间羁留病房，合共收纳约8&nbsp;400名在囚人士。惩教署还提供协助更生人士重返社会的法定监管，截至2015年底，近2&nbsp;000人现正接受监管。<br />  	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;为在囚人士的身心健康着想，惩教署积极配合政 府政策，推行反吸烟措施，通过教育、宣传、辅导及戒烟课程等不同层面的工作，向在囚人士推广无烟文化。惩教署于2013年1月1日将东头惩教所设定为首间「无烟惩教设施」，再于2014年12月1日将白沙湾惩教所设定为第二间「无烟惩教设施」，只收押不吸烟成年在囚人士。<br />  	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;为了推动保育珍贵资源和减低污染，惩教署秉持注重环保及关心社会的管理模式，致力减少院所厨余。惩教署于2013年及2014年先后在罗湖惩教院所、大榄女惩教所、励顾惩教所及大榄惩教所的年长在囚人士组别推出「真識食– 珍惜食」计划，推广减少浪费、珍惜食物的文化以示支持环保。除了节省粮食，减少厨余外，罗湖惩教所及赤柱监狱亦分别于2013及2015年引入厨余机，将剩余食物转化为有用的有机肥料。<br />  	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;此外，为响应「惜食香港运动」，罗湖惩教所和部门签署了「惜食约章」。</p>  <p>  	<strong>成年男性在囚人士：</strong>惩教署辖下有九间惩教院所专门收纳成年男性在囚人士。荔枝角收押所收押候审的在囚人士及刚被定罪而仍须等候归类编入适当惩教院所的在囚人士。<br />  	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;赤柱监狱是本港最大的高度设防监狱，囚禁被判终身监禁或较长刑期的在囚人士。石壁监狱是另一间高度设防监狱，专门囚禁被判中等至较长刑期的在囚人士，包括终身监禁人士。<br />  	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;塘福惩教所、喜灵洲惩教所及白沙湾惩教所均为囚禁成年男性在囚人士的中度设防监狱。<br />  	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;低度设防监狱共有三间，包括东头惩教所、壁屋监狱及大榄惩教所。年老低保安风险的在囚人士（一般指超过65岁者）均收纳于大榄惩教所。</p>  <p>  	<strong>青少年男性在囚人士：</strong>壁屋惩教所是一间高度设防院所，用作收押候审及被定罪的青少年在囚人士。大潭峡惩教所是一间低度设防院所，用作收纳被判监禁的年轻在囚人士。歌连臣角惩教所是专为14岁起但不足21岁的年轻在囚人士而设的教导所。被判入教导所的青少年在囚人士训练期最短为六个月，最长为三年，获释后必须接受为期三年的法定监管。以上青少年在囚人士须参加一个半日上课和半日接受职业训练的计划。<br />  	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;沙咀惩教所为一所低度设防院所，用作收纳劳教中心受训生。劳教中心着重严格纪律、勤劳工作和心理辅导。14岁起但不足21岁的受训生在中心的羁留期限由一个月至六个月不等，而21岁起但不足25岁的受训生，则由三个月至12个月不等。他们于获释后均须接受12个月的监管。<br />  	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;励志和励行更生中心为男青少年在囚人士而设，合计入住期由三至九个月不等。「更生中心计划」着重改造青少年在囚人士，他们获释后须接受一年的监管。</p>  <p>  	<strong>成年女性在囚人士：</strong>惩教署设有两间惩教院所收纳成年女性在囚人士。大榄女惩教所是一间高度设防院所，用作收押和囚禁成年女性在囚人士。罗湖惩教所是本港最新的惩教院所，设有一个低度设防及两个中度设防监区以囚禁成年女性在囚人士，该院所采取惩教事务管理模式，强调以人为本、着重环保、关心社会。</p>  <p>  	<strong>青少年女性在囚人士：</strong>励敬惩教所是一间低度设防院所，用作14岁起但不足21岁青少年女性在囚人士的收押中心、教导所、戒毒所及监狱。芝兰和蕙兰更生中心根据「更生中心计划」收纳女青少年在囚人士。<br />  	<br />  	<strong>戒毒治疗：</strong>惩教署施行强迫戒毒计划，为已定罪的吸毒者提供治疗。法庭倘不拟判吸毒者入狱，可判他们入戒毒所接受治疗。喜灵洲戒毒所收纳成年男性戒毒者，而励新惩教所则收纳成年及年轻男性戒毒者。励顾惩教所及励敬惩教所分别收纳成年及年轻女性戒毒者。戒毒者须接受戒毒计划治疗，为期两个月至12个月不等。戒毒计划以纪律及户外体力活动为基础，强调工作及治疗并重。戒毒者获释后，还须接受为期一年的法定监管。</p>  <p>  	<strong>精神评估及治疗：</strong>精神失常的刑事罪犯及危险凶暴的罪犯均在小榄精神病治疗中心接受治疗。根据《精神健康条例》被判刑及须接受精神评估或治疗的在囚人士会被囚禁于该中心。定期到访该中心的医院管理局精神科医生会为法庭评估在囚人士的精神状况。该中心收纳的男性和女性在囚人士均会被分开囚禁。</p>  <p>  	<strong>工业及职业训练组：</strong>惩教署安排已判刑的在囚人士从事有意义的工作，使他们遵循一个有秩序和规律的生活作业模式，从而协助维持监狱稳定。辖下的工业及职业训练组秉持更生为本的方针，通过提供职业训练及工业生产的技能训练提高在囚人士的就业能力，以协助他们重投社会。<br />  	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在2015年，平均每日有4&nbsp;244名在囚人士从事生产工作，以具成本效益的方式为公营机构提供各类产品及服务。产品计有办公室家具、职员制服、医院被服、过滤口罩、玻璃纤维垃圾桶，以及基建工程所需的交通标志 、铁栏杆和路边石壆等。在囚人士并为医院管理局、卫生署和消防处提供洗熨服务，为公共图书馆和本地大学装订书籍，也为政府部门提供印刷服务和制造文件夹、信封等。<br />  	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;为在囚人士提供职业训练是更生服务的重要一环。惩教署为青年及成年在囚人士安排具社会认可及市场导向的多元化职业训练课程，以助提高他们的个人能力。<br />  	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;惩教署为年轻在囚人士提供半日强制性的工商及服务行业课程。这些课程理论与实践并重，有助他们获释后接受进一步的职业训练。<br />  	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;惩教署亦为成年在囚人士提供自愿释前职业训练，包括全日制及部份时间制短期课程。此外，被定罪的成年在囚人士均须参与工业生产，并接受所需的技能训练。如情况合适，惩教署会安排他们参加职业训练机构的相关中级工艺测试，或通过向资历架构申请参加过往资历认可计划，以取得职业技能认可资格。</p>  <p>  	<strong>法定监管：</strong>惩教署为青少年在囚人士及从教导所、劳教中心、更生中心和戒毒所获释的更生人士，以及根据「监管下释放计划」、「释前就业计划」、「监管释囚计划」、「有条件释放计划」及「释后监管计划」释放的更生人士提供法定监管，以确保他们继续得到照顾和指导。监管人员与在囚人士的家人紧密联系，有助在囚人士与其家人培养良好的关系，并协助他们做好准备，以应付日后重返社会可能面对的考验及需要。监管人员会定期与在囚人士接触，而在他们获释后，监管人员会经常前往他们的居所或工作地点探访，予以密切的监管和辅导。<br />  	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;惩教署设有三间中途宿舍，位于龙欣道的丰力楼，主要收纳从劳教中心、教导所和戒毒所释放的年轻男性受监管者；另外是附设于丰力楼的百勤楼，主要收纳根据「监管下释放计划」、「释前就业计划」和「有条件释放计划」释放的男性在囚人士、来自戒毒所的男受监管者及根据「监管释囚计划」释放而有住屋需要的男受监管者；位于大榄涌的紫荆楼则收纳根据「监管下释放计划」、「释前就业计划」和「有条件释放计划」释放的女性在囚人士及来自教导所和戒毒所的女受监管者。中途宿舍可协助受监管者在离开惩教院所后，逐步适应社会生活。<br />  	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;法定监管的成功率，以法定监管期内没有再被法庭定罪的更生人士所占百分率计算。就戒毒者而言，更须在该期间内不再吸毒。2015年，各类惩教院所及监管计划的成功率分别如下：劳教中心96%；教导所75%；戒毒所53%；更生中心98%；监狱计划下的青少年在囚人士97%；「监管下释放计划」95%；「释前就业计划」100%；「释后监管计划」100%；「有条件释放计划」100%；「监管释囚计划」87%。在年内监管期满的男受监管者有1&nbsp;537人，女受监管者有315人；而在同年年底仍接受监管的男受监管者有1&nbsp;643人，女受监管者则有348人。</p>  <p>  	<strong>福利及辅导服务：</strong>辅导主任负责照顾在囚人士的福利事宜，协助和指导他们解决因入狱而引起的个人问题及困难。辅导主任亦在院所内组织更生活动，例如鼓励长刑期的在囚人士善用时间的「犯人服刑计划」、协助在囚人士于获释后顺利重返社会的「重新融入社会释前启导课程」等各项计划。<br />  	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;社区参与能进一步改善更生计划。因此，惩教署与超过80间非政府机构紧密合作，在院所筹办辅导、宗教以及大型的文化和康乐活动。</p>  <p>  	<strong>心理服务：</strong>惩教署的心理服务组为在囚人士提供心理辅导，以改善他们的心理健康和纠正犯罪行为。服务范围包括就其心理状况拟备心理评估报告，以供法庭、有关覆检委员会及惩教院所的管理当局在作出决定和管理在囚人士时作参考之用。此外，心理服务组亦为在囚人士提供多项辅导，包括为青少年在囚人士提供的系统化治疗计划「心导计划--从少做起」以减少他们的重犯诱因，及为戒毒所所员而设的「预防吸食毒品心理治疗计划」；性罪犯会被安排于「心理评估心理治疗组」接受系统化的心理治疗课程以改变其犯罪行为。部分惩教院所更为成年在囚人士开展「预防暴力心理治疗计划」以改变参与者的暴力行为。「健心馆 ─ 女性个人成长及情绪治疗中心」为女性在囚人士提供针对女性而设计的系统化心理治疗计划，以帮助她们建立积极的生活。此外，为鼓励青少年在囚人士的家长参与子女的更生历程，心理服务组亦于2015年推出新猷「家爱计划--从心出发」，以便更有效针对现今家庭和年轻在囚人士的心理需要。<br />  	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;心理服务组亦顾及职员的心理健康及需要，自2010年初起积极推广健康均衡生活。</p>  <p>  	<strong>教育：</strong>惩教署为青少年在囚人士提供半日制强制性普通科和实用科目课程，提升他们的学历水平，有助他们日后重返社会。该署亦鼓励在囚人士参加多项本地及海外的公开考试。惩教署在收纳成年在囚人士的惩教院所开办由义工导师主持的小组导修课程及兴趣班，让在囚人士以自愿性质参与。此外，该署亦鼓励成年在囚人士参加各种自学或遥距专上课程，以善用各认可教育机构的资源。</p>  <p>  	<strong>促进社区参与</strong><strong>：</strong>惩教署积极争取社会支持，促进社区参与在囚人士的更生工作。在众多伙伴中，成员包括来自不同界别领袖与专业人士的社区参与助更生委员会，就更生策略（特别是宣传计划）向署方提供意见。<br />  	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;惩教更生义工团举办多项活动以补充服务，务求切合在囚人士的需要。义工团共有一百多名活跃义工，于年内为惩教院所的在囚人士举办语文、电脑等研习班及其他文化兴趣活动。<br />  	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;助更生宣传活动自1999年起展开，为在囚人士与社会建立一道桥梁。惩教署多年来通过各种活动，包括电视宣传短片及电台宣传声带、电视特备节目、「全城响应助更生」、更生人士就业研讨会、「聘」出未来－－更生人士视像招聘会、在囚人士证书颁发典礼、非政府机构论坛、在囚人士感恩活动、与各分区扑灭罪行委员会合办的社区参与活动、委任更生大使，以及惩教更生义工团义工颁奖礼等，让市民大众明白社会的接纳及参与对在囚人士更生的重要性。</p>  <p>  	<strong>更生先锋计划</strong><strong>：</strong>「更生先锋计划」包括一系列的社区教育活动，如教育讲座、面晤在囚人士计划、绿岛计划、参观香港惩教博物馆、延展训练营、青少年座谈会、「创艺展更生」话剧音乐汇演及思囚之路等。教育讲座提供香港刑事司法体系和惩教署羁管及更生计划的基本资料。「面晤在囚人士计划」安排青少年学生参观惩教院所，并与在囚人士面对面交流，让他们了解犯罪的后果，强化灭罪讯息。「绿岛计划」向青少年宣传禁毒信息及环境保护的重要性，计划安排参加者与设于喜灵洲的戒毒院所的青少年在囚人士会面，了解吸毒的祸害。参观香港惩教博物馆可加深参观者对惩教工作的了解，尤其是大众的支持对罪犯更生的重要性。「延展训练营」是一项为期三日两夜、于马坑监狱及喜灵洲岛上进行的纪律训练项目，目的是透过纪律训练，帮助青少年加强自信心、建立正确价值观、团队合作性及提升独立思考判断能力。青少年座谈会以「论坛剧场」形式进行，由专业话剧团体设计互动式的话剧。内容讲述一位更生人士曾经误入歧途，然后于重新融入社会路途上的挣扎过程，还有暴风少年如何面对毒品的诱惑。于赤柱监狱内举行的「创艺展更生」话剧音乐汇演提供了平台让在囚人士回馈社会，向学生亲述犯罪为他们带来的沉重代价和守法的重要性，藉以警惕学生必须洁身自爱。「思囚之路」活动运用了惩教院所的真实环境，让学生设身处地体验由被捕、审讯、定罪、收押、训练到释放的一段模拟在囚过程，目的是希望加深参加者对香港刑事司法制度及惩教工作的认知，以及促使参加者反思犯罪的沉重代价。</p>  <p>  	<strong>宗教服务：</strong>宗教服务由一名全职司铎策划及提供，并获得多名自愿作探访及主持礼拜的义务司铎协助。不少志愿人士及非政府机构亦在惩教院所内提供各类灵修及社会服务。</p>  <p>  	<strong>在囚人士的医疗护理：</strong>所有惩教院所均设有医院，由合资格医护人员当值，并与卫生署协作下，提供24小时的基本医疗服务。如在囚人士需要进一步检查和治疗，他们会获转介予到诊专科或至公立医院继续跟进。</p>  <p>  	<strong>巡狱太平绅士：</strong>两名巡狱太平绅士每隔两星期或一个月共同巡视每所惩教院所，相隔时间视乎院所类别而定。巡狱太平绅士须履行若干法定任务，包括调查在囚人士向他们提出的投诉、视察膳食，以及巡视惩教院所内的建筑和住宿设施。太平绅士须在指定期间内巡视惩教院所，但确实日期和时间则自行决定，事前不必知会有关院所。</p>  <p>  	<strong>职员训练：</strong>惩教署的职员训练院负责策划及举办各项训练课程，向职员灌输有关的工作知识，让他们履行部门的任务和实践所定的抱负及价值观。<br />  	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;新招募的惩教主任及惩教助理须分别接受26及23个星期的入职训练，包括在惩教院所实习。该院亦定期举办各项发展训练课程如复修课程、各种专业训练和指挥训练课程，以提高职员的个人效能及促进其事业前途发展。职员训练亦着重处境训练及实况分析。<br />  	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;为推广持续进修及终身学习文化，惩教署自2010年起，启用名为知识管理系统的一站式网上学习、经验及知识分享平台，以加强职员利用互联网或内联网学习与工作有关的知识。</p>  <p>  	<strong>关怀各方：</strong>除了履行日常职务外，惩教署亦鼓励人员参与各项慈善活动，以加强他们关怀社会的精神。这些活动包括派遣义工人员协助组织筹募善款，以及向为更生人士提供服务的非政府组织提供意见。<br />  	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;惩教署于2015/16年度，继续获得香港社会服务联会颁发「10年Plus同心展关怀」标志，之前在2007/08年度亦获得知名的「全面关怀大奖」，以表扬该署持续全力关怀署内人员和家人，以至社会各阶层。</p><!-- END CONTENT --></div><div class="csd-w3c"><a href="http://www.w3.org/WAI/WCAG2AA-Conformance"><img src="/images/design/wcag2AA.gif" alt="符合万维网联盟有关无障碍网页设计指引中2A级别的要求" title="符合万维网联盟有关无障碍网页设计指引中2A级别的要求"></a></div><div id="csd-footer">
	<div class='back_btn'><a href='javascript:history.go(-1)'><img src='/images/design/_-25_1.png'> 上一页</a></div>
				<div class='top_btn'><a href='#'>页首 <img src='/images/design/_-26_1.png'></a></div>
	<div class="csd-policy">
		<table border="0" cellpadding="0" cellspacing="0" width="50%">
			<tbody>
				<tr>
					<th></th>
						<td style="width:40%;">2014 ©</td>
					<th></th><td valign="middle">
						<a href="/sc_chi/importantnotices/importantnotices.html">重要告示</a></td>
					<th></th><td>
						<a href="/sc_chi/privacy/privacy.html">私隐政策</a></td>
					<th></th><td>
						<a href="/sc_chi/contactus/other_contact.html">联络我们</a></td>
				</tr>
			</tbody>
		</table>
	</div>
	<!-- div class="csd-version">
		Last revision date : 8 April 2013</div -->
</div>
<div class='revisionDate'>最近修订日期 : 2016年05月04日</div></div></body></html>
"""
soup = BeautifulSoup(html_doc, "lxml")
print '---------------------------------'
con1 = soup.find('div', class_ = 'contenttext')
con2 = soup.find('div', id = 'getHeight')
try:
    if con1:
        all_p = con1.get_text().strip()
        all_p = all_p.encode('GBK', 'ignore') # 在对unicode字符编码时，添加ignore参数，忽略无法无法编码的字符，这样就可以正常编码为 GBK了
        print all_p
    elif con2:
        all_p = con2.get_text().strip()
        all_p = all_p.encode('GBK', 'ignore') # 控制台显示用，写到数据库注释掉该语句
        print all_p
except:
    print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
print '---------------------------------'  

# # 打开一个文件
# fo = open("D:\\Workspace\\Python\\Scrapy\\test\\1.txt", "wb+")
# fo.write( all_p);
# fo.close()