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

  <title>香港政府一站通：搜寻结果</title>
  
  <script src="/js/jquery-1.11.2.min.js"></script>
  <script src="/js/jquery-ui-1.11.4.min.js"></script>
  <link rel="stylesheet" href="/css/jquery-ui.1.11.4.css" />
  
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
    var page_site = 'customs_r2_home';
    
    function rkwAjax() {
    	var url = '/ajaxRkw?query=%E6%AF%92%E5%93%81&ui_lang=zh-cn&tpl_id=customs_r2&page=1&p_size=10&output=xml_no_dtd&ui_charset=utf-8&a_submit=false&toASubmit=false&gp0=customs_r2_home&gp1=customs_r2_home&doc_type=all&sort=&web=this&txtonly=0&site=customs_r2_home&last_mod=%23-1&exact_q=&any_q=&none_q=';
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
	    		var url = '/updateAutoKeyword?keyword=%E6%AF%92%E5%93%81&ui_lang=zh-cn';
	    		
	    		$("#updateKeyword").load(url);
	    	}
    	}
    }
    
    function clickCount(action) {
    	clickCount(action, '');
    } 
    
    function clickCount(action, clickUrl, keyword) {
    	
    	var url = '/stat.html?ui_lang=zh-cn&keyword=%E6%AF%92%E5%93%81';
    	
    	if (url.length > 0) {
    		url = url + "&action=" + action + "&clickUrl=" + clickUrl + "&searchKeyword=" + keyword;
    	
    		$("#updateKeyword").load(url);
    	}
    	
    }
    /*]]>*/
  </script>
  <script type="text/javascript" src="/js/gov_adv_search_20090619.js"></script>
  <script type="text/javascript" src="/js/gov_search_image.js"></script>

  <link rel="stylesheet" type="text/css" href="/css/dimensionsearchpage.css" />
  
  <link rel="stylesheet" type="text/css" href="/css/typographytc.css" />
  <link rel="stylesheet" type="text/css" href="/css/searchpage_20130625.css" />
  
  
  <link media="screen" type="text/css" rel="stylesheet" href="/css/rkwCss.css" />
  
  <link rel="stylesheet" type="text/css" href="/css/topnav.css" />
  <link rel="stylesheet" type="text/css" href="/css/footer.css" />
  <link rel="stylesheet" type="text/css" href="/css/screenreader.css" />
  <link rel="stylesheet" type="text/css" href="/css/clustertab.css" />
  <link rel="stylesheet" type="text/css" href="/css/rightaddarea.css" />
  <link rel="stylesheet" type="text/css" href="/css/searchbar_dept_20130625.css" />
  <link rel="stylesheet" type="text/css" href="/css/pagination_20130625.css" />
  <link rel="stylesheet" type="text/css" href="/css/gov_adv_search_20130625.css" />
  
  
  
  
  
  

  <!--[if IE 7]>
  <link media="screen" type="text/css" rel="stylesheet" th:href="@{/css//advance/ie7.css}"/>
  <![endif]-->
  <!--[if lt IE 7]>
  <link media="screen" type="text/css" rel="stylesheet" th:href="@{/css/advance/ie6.css}"/>
  <![endif]-->
  
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
  <script type="text/javascript" src="/js/dept/customs_r2.js"></script>
  <link media="screen" type="text/css" rel="stylesheet" href="/css/dept/customs_r2.css" />
  
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
		var msgKeyword = '\u8BF7\u8F93\u5165\u5173\u952E\u5B57\u3002';
		var msgDateRange = '\u8BF7\u9009\u62E9\u6B63\u786E\u7684\u66F4\u65B0\u65F6\u95F4\u8303\u56F4';
	    lang = 'zh-cn';
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
	        var akurl = 'autokeyword?ui_lang=zh-cn';

			//Do not applied auto-complete function for dept template
	        var isStandard = false;
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
  <script>
    /*<![CDATA[*/
    var lang = 'zh-cn';
    
    var deptPageTile = deptPageTileMap[lang];
    var deptMenu = deptMenuMap[lang];
    var deptLogoWidth = deptLogoWidthMap[lang];
    var deptLogoHeight = deptLogoHeightMap[lang];
    var deptLogo = deptLogoMap[lang];
    var deptLink = deptLinkMap[lang];
    var deptAlt = deptAltMap[lang];
    var deptContact = deptContactMap[lang];
    var deptSiteMap = deptSiteMapMap[lang];
    var deptNotice = deptNoticeMap[lang];
    var deptPP = deptPPMap[lang];
    var deptAdvSearch = deptAdvSearchMap[lang];
    var deptAdvSearchTxt = deptAdvSearchTxtMap[lang];
    var deptHeaderTxt = deptHeaderTxtMap[lang];
    var deptFooterTxt = deptFooterTxtMap[lang];
    
    document.title = deptPageTile;
    var tpl_id = 'customs_r2';
    
    var tempUrl = tpl_id + '?query=%E6%AF%92%E5%93%81';
    //alert(tempUrl);
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
<body onload="resetForms();rkwAjax();keyUpdate()" dir="ltr"> <!-- Please enter html code below. -->
<div id="updateKeyword"></div>
<!--  Share the ui for both standard and dept -->
<div id="dmnSpResultPage">
	<!-- Standard template tool bar -->
	
	
	
	
	<!-- End of Standard search header -->
	         
  <!-- Dept template Header -->       
  <div id="dmnSpTopNav" class="dept">
  	<!-- Original header -->
    <div id="deptTopNavHeader">
      <div id="deptTopNavHeaderLeft">
        <div id="deptTopNavHeaderLeftUpper">
          <script>
            printDeptLogo();
          </script>
        </div>
        <div id="deptTopNavHeaderLeftLower">
          <div id="topNavRedButton" class="dept">
            <div class="topNavImageHolder"><a href="http://www.gov.hk/sc/residents/"><img id="topnav01" class="border0" height="20" alt="GovHK香港政府一站通" onfocus="javascript:swapImage(this,&#39;/search/bd_mainbar1_f2_sc_v2.gif&#39;)" onblur="javascript:swapImage(this,&#39;/search/bd_mainbar1_sc_v2.gif&#39;)" onmouseover="javascript:swapImage(this,&#39;/search/bd_mainbar1_f2_sc_v2.gif&#39;)" onmouseout="javascript:swapImage(this,&#39;/search/bd_mainbar1_sc_v2.gif&#39;)" src="/search/bd_mainbar1_sc_v2.gif" /></a></div>
            <div class="topNavImageHolder"><a href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-hk&amp;tpl_id=customs_r2&amp;page=1&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;a_submit=false&amp;gp0=customs_r2_home&amp;gp1=customs_r2_home&amp;doc_type=all&amp;sort=&amp;web=this&amp;txtonly=0&amp;site=customs_r2_home&amp;last_mod=%23-1">
                    <img onclick="clickCount('langSwitchButtons', '', '')" id="topnav03" class="border0" height="20" alt="繁體版" onfocus="javascript:swapImage(this,&#39;/search/bd_mainbar3_f2_en.gif&#39;)" onblur="javascript:swapImage(this,&#39;/search/bd_mainbar3_en.gif&#39;)" onmouseover="javascript:swapImage(this,&#39;/search/bd_mainbar3_f2_en.gif&#39;)" onmouseout="javascript:swapImage(this,&#39;/search/bd_mainbar3_en.gif&#39;)" src="/search/bd_mainbar3_en.gif" /></a>
            </div>
            <div class="topNavImageHolder"><a href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=en&amp;tpl_id=customs_r2&amp;page=1&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;a_submit=false&amp;gp0=customs_r2_home&amp;gp1=customs_r2_home&amp;doc_type=all&amp;sort=&amp;web=this&amp;txtonly=0&amp;site=customs_r2_home&amp;last_mod=%23-1">
                    <img onclick="clickCount('langSwitchButtons', '', '')" id="topnav04" class="border0" height="20" alt="简体版" onfocus="javascript:swapImage(this,&#39;/search/bd_mainbar4_f2_sc_v2.gif&#39;)" onblur="javascript:swapImage(this,&#39;/search/bd_mainbar4_sc_v2.gif&#39;)" onmouseover="javascript:swapImage(this,&#39;/search/bd_mainbar4_f2_sc_v2.gif&#39;)" onmouseout="javascript:swapImage(this,&#39;/search/bd_mainbar4_sc_v2.gif&#39;)" src="/search/bd_mainbar4_sc_v2.gif" /></a>
            </div>
            <div class="topNavImageHolder"><img id="topnav05" class="border0" height="20" alt="" src="/search/bd_mainbar5_sc_v2.gif" /></div>
          </div>
        </div>
      </div>
      <div id="deptTopNavHeaderRight">
        <script>
          function headerFormSubmit() {
            if (document.getElementById('hksarg_search0').query.value.length == 0) {
              alert('Please enter keyword.');
            } else {
              document.getElementById('hksarg_search0').submit();
            }
            return;
          }
        </script>
        <form id="hksarg_search0" onsubmit="if( document.getElementById('hksarg_search0').query.value.length == 0 ) alert('Please enter keyword.');                 else  document.getElementById('hksarg_search0').submit(); return false;" method="get" action="/search">

          <input type="hidden" name="site" value="customs_r2_home" />
          <input type="hidden" name="output" value="xml_no_dtd" />
          <input type="hidden" name="gp1" value="customs_r2_home" />
          <input type="hidden" name="gp0" value="customs_r2_home" />
          <input type="hidden" name="web" value="this" />
          <input type="hidden" name="a_submit" value="false" />
          <input type="hidden" name="txtonly" value="0" />
          <input type="hidden" name="tpl_id" value="customs_r2" />
          <input type="hidden" name="ui_lang" value="zh-cn" />
          <input type="hidden" name="sort" value="" />
          
          <div id="deptTopNavHeaderRightUpper"><a href="http://www.brandhk.gov.hk/" target="_blank"><img alt="Brand Hong Kong" src="/search/bd_brandhk_20100331_tc.gif" /></a></div>
          <div id="deptTopNavHeaderRightLower">
            <div id="topNavRedButton1" class="dept">
              <div class="topNavImageHolder"><a href="javascript:headerFormSubmit()"><img id="topnav06" class="border0" alt="Search" onfocus="javascript:swapImage(this,&#39;/search/bd_mainbar6_f2_sc.gif&#39;)" onblur="javascript:swapImage(this,&#39;/search/bd_mainbar6_sc.gif&#39;)" onmouseover="javascript:swapImage(this,&#39;/search/bd_mainbar6_f2_sc.gif&#39;)" onmouseout="javascript:swapImage(this,&#39;/search/bd_mainbar6_sc.gif&#39;)" height="19" src="/search/bd_mainbar6_sc.gif" /></a>
              </div>
              <div class="topNavImageHolder"><label for="topNavSearchBox" class="hidden">Search Query:</label>
              <input type="text" name="query" value="" id="topNavSearchBox" /></div>
              <div class="topNavImageHolder"><a href="javascript:headerFormSubmit()"><img id="topnav08" class="border0" alt="Search" onfocus="javascript:swapImage(this,&#39;/search/bd_mainbar8_f2_sc_2.gif&#39;)" onblur="javascript:swapImage(this,&#39;/search/bd_mainbar8_sc_2.gif&#39;)" onmouseover="javascript:swapImage(this,&#39;/search/bd_mainbar8_f2_sc_2.gif&#39;)" onmouseout="javascript:swapImage(this,&#39;/search/bd_mainbar8_sc_2.gif&#39;)" height="19" src="/search/bd_mainbar8_sc_2.gif" /></a></div>
              <div class="topNavImageHolder">
                <script>     <!-- Please enter html code below. -->
                /*<![CDATA[*/
                document.write('<a href="' + deptSiteMap + '">');
                /*]]>*/
                </script>
                <img id="topnav09" class="border0" alt="Site Map" onfocus="javascript:swapImage(this,&#39;/search/bd_mainbar9_f2_sc_2.gif&#39;)" onblur="javascript:swapImage(this,&#39;/search/bd_mainbar9_sc_2.gif&#39;)" onmouseover="javascript:swapImage(this,&#39;/search/bd_mainbar9_f2_sc_2.gif&#39;)" onmouseout="javascript:swapImage(this,&#39;/search/bd_mainbar9_sc_2.gif&#39;)" height="19" src="/search/bd_mainbar9_sc_2.gif" />
                  <script>
                    /*<![CDATA[*/
                    document.write('</a> ');
                    if (deptSiteMap == '')
                      document.getElementById('topnav09').style.display = 'none';
                    /*]]>*/
                  </script>
                </div>
              <div class="topNavImageHolder">
                <script>     <!-- Please enter html code below. -->
                /*<![CDATA[*/
                document.write('<a href="' + deptContact + '">');
                /*]]>*/
                </script>
                <img id="topnav10" class="border0" alt="Contact Us" onfocus="javascript:swapImage(this,&#39;/search/bd_mainbar10_f2_sc_2.gif&#39;)" onblur="javascript:swapImage(this,&#39;/search/bd_mainbar10_sc_2.gif&#39;)" onmouseover="javascript:swapImage(this,&#39;/search/bd_mainbar10_f2_sc_2.gif&#39;)" onmouseout="javascript:swapImage(this,&#39;/search/bd_mainbar10_sc_2.gif&#39;)" height="19" src="/search/bd_mainbar10_sc_2.gif" />
                  <script>
                    /*<![CDATA[*/
                    document.write('</a> ');
                    if (deptContact == '')
                      document.getElementById('topnav10').style.display = 'none';
                    /*]]>*/
                  </script>
                </div>
            </div>
          </div>
        </form>
      </div>
    </div>
    
    <!-- Text header -->
    
  </div>
	<!--  End of Dept template header -->


	<!-- Standard template body -->
   	
	<!-- End of standard template body -->

	<!-- Department template body -->
  <!-- Please enter html code below. -->
  <div id="dmnSpMid" class="dept">
    <script>
      if (deptMenu == '') {
        printNoLeftMenuCSS();
      }
    </script>
    <div id="dmnSpMidLeftLeft" class="dept">
      <div id="deptNavMenu" style="border-width: 0px 0pt 0pt">
        <script>
          /*<![CDATA[*/
          printLeftMenu();
          /*]]>*/
        </script>
      </div>
    </div>
    
    <!-- Please enter html code below. -->
    <div id="dmnSpMidLeft" class="dept">
      <script>
        if (deptMenu == '') {
          document.getElementById("dmnSpMidLeft").style.width = "100%";
        }
      </script>
      <script>
        function blackKeyAlert() {
          alert('Please enter keyword!');
        }
      </script>
      <form name="gs" id="hksarg_searchyschtopsearch1" method="GET" onsubmit="if(document.getElementById('hksarg_searchyschtopsearch1').query.value.length==0)blackKeyAlert();else       document.getElementById('hksarg_searchyschtopsearch1').submit();return false;" action="/search">
        <script>
          printDeptSearchBarHeaderLayer1();
        </script>
        <!-- <div class="deptSearchBarHeader" id="withborder" style=""> -->
          <div class="deptSearchBarHeaderLeft">&nbsp;&nbsp;&nbsp;
          <label for="SearchBarBox" class="hidden">Departmental Search</label>
            <input class="deptSearchBarSearchInput" type="text" name="query" size="32" maxlength="256" id="SearchBarBox" value="毒品" /><span class="deptSearchBarSearch">&nbsp;<script>
            function formSubmit(id) {
              if (document.getElementById(id).query.value.length == 0) {
                alert('Please enter keyword!');
              } else {
                document.getElementById(id).submit();
              }
              return;
            }
          </script>
          
          <a href="javascript:formSubmit('hksarg_searchyschtopsearch1')"><img id="yschtopsearch1" onfocus="javascript:swapImage(this,&#39;/search/topsearch_sc_hover.gif&#39;)" onblur="javascript:swapImage(this,&#39;/search/topsearch_sc_off.gif&#39;)" onmouseover="javascript:swapImage(this,&#39;/search/topsearch_sc_hover.gif&#39;)" onmouseout="javascript:swapImage(this,&#39;/search/topsearch_sc_off.gif&#39;)" alt="查询" src="/search/topsearch_sc_off.gif" /></a>&nbsp;</span>
			<span class="deptSearchBarAdvSearch">
          <script>
            /*<![CDATA[*/
            var isTxtOnly = 0;
            var linkText = '\u8FDB\u9636\u641C\u5BFB';
            if (deptAdvSearch != "" && isTxtOnly == 0) {
              //deptAdvSearch = deptAdvSearch + '?gp0=news_archive_home&amp;gp1=&amp;all_q=&amp;exact_q=hello&amp;any_q=&amp;none_q=&amp;query=%22hello%22&amp;ui_lang=en&amp;tpl_id=news_archive&amp;ui_charset=utf-8&amp;p_size=10&amp;is_init=true&amp;init_query=%22hello%22&amp;init_exact_q=hello&amp;init_any_q=&amp;init_none_q=&amp;web=this';
              deptAdvSearch = deptAdvSearch + '?query=%E6%AF%92%E5%93%81&ui_lang=zh-cn&tpl_id=customs_r2&page=1&p_size=10&output=xml_no_dtd&ui_charset=utf-8&a_submit=false&gp0=customs_r2_home&gp1=customs_r2_home&doc_type=all&web=this&txtonly=0&site=customs_r2_home&last_mod=%23-1';
              printAdvancedSearch(deptAdvSearch, linkText);
            } else if (deptAdvSearchTxt != "" && isTxtOnly == 1) {
            	deptAdvSearchTxt = deptAdvSearchTxt + '?query=%E6%AF%92%E5%93%81&ui_lang=zh-cn&tpl_id=customs_r2&page=1&p_size=10&output=xml_no_dtd&ui_charset=utf-8&a_submit=false&gp0=customs_r2_home&gp1=customs_r2_home&doc_type=all&web=this&txtonly=0&site=customs_r2_home&last_mod=%23-1';
                printAdvancedSearch(deptAdvSearchTxt, linkText);
            }
            /*]]>*/
          </script>
          </span>
            <input type="hidden" name="output" value="xml_no_dtd" />
            <input type="hidden" name="client" value="depts" />
            <input type="hidden" name="proxystylesheet" value="depts" />
            <input type="hidden" name="getfields" value="subject" />
            <input type="hidden" name="numgm" value="6" />
            <input type="hidden" name="gp1" value="customs_r2_home" />
            <input type="hidden" name="gp0" value="customs_r2_home" />
            <input type="hidden" name="web" value="this" />
            <input type="hidden" name="a_submit" value="false" />
            <input type="hidden" name="txtonly" value="0" />
            <input type="hidden" name="tpl_id" value="customs_r2" />
            <input type="hidden" name="ui_lang" value="zh-cn" />
            <input type="hidden" name="oe" value="UTF-8" />
            <input type="hidden" name="ie" value="UTF-8" />
            <input type="hidden" name="filter" value="0" />
            <input type="hidden" name="sort" value="" />
            <input type="hidden" name="entqr" value="3" />
            <input type="hidden" name="entqrm" value="0" />
            <input type="hidden" name="entsp" value="a" />
            <input type="hidden" name="ud" value="1" />

          </div>
          <script>
            printDeptSearchBarHeaderLayer2();
          </script>
        <!-- </div> -->
        <div class="deptSearchBarHeaderBottom">
          <fieldset>
            <table class="border0">
              <tbody>
              <tr>
                <td>
                  <table class="border0">
                    <tbody>
                    <tr>
                      <td>显示：</td>
                    </tr>
                    </tbody>
                  </table>
                </td>
                <td>
                  <table class="border0">
                    <tbody>
                    <tr>
                      <td>&nbsp;<input type="radio" id="yschtopsearch1all_ck_top" name="site" value="default_collection" />
                      </td>
                      <td>&nbsp;<label for="yschtopsearch1all_ck_top">所有政府网站</label>
                      </td>
                    </tr>
                    </tbody>
                  </table>
                </td>
                <td>
                  <table class="border0">
                    <tbody>
                    <tr>
                      <td>&nbsp;&nbsp;
                      <input type="radio" id="yschtopsearch1this_ck_top" name="site" checked="checked" value="customs_r2_home" /></td>
                      <td>&nbsp;<label for="yschtopsearch1this_ck_top">此网站</label></td>
                    </tr>
                    </tbody>
                  </table>
                </td>
              </tr>
              </tbody>
            </table>
          </fieldset>
        </div>
      </form>


      <table class="resultStatTable">
        <tbody>
        <tr>
          <td>&nbsp;</td>
          <td class="resultStatTableInfo">
			<span>约找到 <strong>828</strong> 个结果，显示第 <strong>1</strong> 至 <strong>10</strong> 个。 </span>
			
			<span>用时 <strong>0.089</strong> 秒。</span>
          </td>
        </tr>
        </tbody>
      </table>
      <table class="resultHeadTable">
        <tbody>
        <tr>
          <td class="resultHeadTableInfoLeft">
            &nbsp;
            <span></span>&nbsp;
            <span><a onclick="clickCount('paginationTool', '', '')" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-cn&amp;tpl_id=customs_r2&amp;page=2&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;a_submit=false&amp;gp0=customs_r2_home&amp;gp1=customs_r2_home&amp;doc_type=all&amp;sort=&amp;web=this&amp;txtonly=0&amp;site=customs_r2_home&amp;last_mod=%23-1">下一页&gt;</a></span>
          </td>
          <td class="resultHeadTableInfoRight">
			<span>
				<a onclick="clickCount(&#39;sort_by_date&#39;, '', '')" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-cn&amp;tpl_id=customs_r2&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;a_submit=false&amp;gp0=customs_r2_home&amp;gp1=customs_r2_home&amp;doc_type=all&amp;sort=date&amp;web=this&amp;txtonly=0&amp;site=customs_r2_home&amp;last_mod=%23-1">根据日期排序</a>
				
				/
				<span>根据相关程度排序</span>
				
			</span>
          </td>
        </tr>
        </tbody>
      </table>
		
      <!--tro2-->
	<!-- Recommend link -->
	
	
      <div>

        <div id="yschnorel" style="padding-left:10px;">
          <div id="dmnSpLeftMiddle" class="dept">
          	<!-- Error table here -->
			          	
          	<!-- Error table end -->
            <div id="yschres" style="visibility:visible">
              <ol start="1">
                <!--search result list start-->

                <li>
                  <div>
					
                    <a class="yschttl" onkeydown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.customs.gov.hk%2Ffilemanager%2Fcommon%2Fpdf%2Fpdf_publications%2Fdept_review03_04%2Ftxt_sc%2Fhtml%2Fchapter05.htm&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" onmousedown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.customs.gov.hk%2Ffilemanager%2Fcommon%2Fpdf%2Fpdf_publications%2Fdept_review03_04%2Ftxt_sc%2Fhtml%2Fchapter05.htm&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" id="waSearchResultTitle1" href="http://www.customs.gov.hk/filemanager/common/pdf/pdf_publications/dept_review03_04/txt_sc/html/chapter05.htm">
                      <span>缉<strong>毒</strong></span>
                    </a>
                    </div>
                  <p>
                  </p>

                  <div class="yschabstr">
                    <span>庞大，<strong>毒</strong>贩往往伺机进行偷运<strong>毒品</strong>活动。大批的<strong>毒品</strong>相信是收藏在大量运入本港的商业货<strong>品</strong>中偷运入境。偷运少量<strong>毒品</strong>...</span>
                  </div>
                  <!--/p-->
                  <p>
                    <!-- Last Modified Date: 2011-11-09 -->
                    <span class="yschurl">www.customs.gov.hk/.../pdf_publications/dept_review03_04/txt_sc/html/chapter05.htm</span>
                    - 
                    <span>9.9K</span>
                    <span> - </span>
                    <span>18/12/2012</span>
                    <span> - </span>
                    <!--/p-->
                    <a class="yschmore" href="http://lp.search.gov.hk:8080/Action=View&amp;NoACI=true&amp;reference=http%3A%2F%2Fwww.customs.gov.hk%2Ffilemanager%2Fcommon%2Fpdf%2Fpdf_publications%2Fdept_review03_04%2Ftxt_sc%2Fhtml%2Fchapter05.htm" onkeydown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);" onmousedown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);">
					<span>页库存档</span></a>
                  </p>
                 </li>

                <li>
                  <div>
					
                    <a class="yschttl" onkeydown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.customs.gov.hk%2Fsc%2Fpublication_press%2Fpress%2Findex_current.html&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" onmousedown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.customs.gov.hk%2Fsc%2Fpublication_press%2Fpress%2Findex_current.html&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" id="waSearchResultTitle2" href="http://www.customs.gov.hk/sc/publication_press/press/index_current.html">
                      <span>香港海关 - 新闻公报</span>
                    </a>
                    </div>
                  <p>
                  </p>

                  <div class="yschabstr">
                    <span>疑可卡因<strong>毒品</strong>及冰<strong>毒</strong>（附图）
香港海关在一名前往澳门旅客身上检获怀疑可卡因<strong>毒品</strong>及冰<strong>毒</strong>（附图）...</span>
                  </div>
                  <!--/p-->
                  <p>
                    <!-- Last Modified Date: 2011-11-09 -->
                    <span class="yschurl">www.customs.gov.hk/sc/publication_press/press/index_current.html</span>
                    - 
                    <span>57.7K</span>
                    <span> - </span>
                    <span>18/06/2010</span>
                    <span> - </span>
                    <!--/p-->
                    <a class="yschmore" href="http://lp.search.gov.hk:8080/Action=View&amp;NoACI=true&amp;reference=http%3A%2F%2Fwww.customs.gov.hk%2Fsc%2Fpublication_press%2Fpress%2Findex_current.html" onkeydown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);" onmousedown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);">
					<span>页库存档</span></a>
                  </p>
                 </li>

                <li>
                  <div>
					
                    <a class="yschttl" onkeydown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.customs.gov.hk%2Fsc%2Fenforcement%2Fnarcotics_interdiction%2Findex.html&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" onmousedown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.customs.gov.hk%2Fsc%2Fenforcement%2Fnarcotics_interdiction%2Findex.html&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" id="waSearchResultTitle3" href="http://www.customs.gov.hk/sc/enforcement/narcotics_interdiction/index.html">
                      <span>香港海关 - 缉<strong>毒</strong></span>
                    </a>
                    </div>
                  <p>
                  </p>

                  <div class="yschabstr">
                    <span>项"将不能使用。如要前往其他部分或页面，请按"网页指南"。

香港海关其中一项主要职责是堵截按此去<strong>毒品</strong>
<strong>毒品</strong>  (在新视窗开启) 。海关人员驻守于各出</span>
                  </div>
                  <!--/p-->
                  <p>
                    <!-- Last Modified Date: 2011-11-09 -->
                    <span class="yschurl">www.customs.gov.hk/sc/enforcement/narcotics_interdiction/index.html</span>
                    - 
                    <span>10.3K</span>
                    <span> - </span>
                    <span>15/06/2010</span>
                    <span> - </span>
                    <!--/p-->
                    <a class="yschmore" href="http://lp.search.gov.hk:8080/Action=View&amp;NoACI=true&amp;reference=http%3A%2F%2Fwww.customs.gov.hk%2Fsc%2Fenforcement%2Fnarcotics_interdiction%2Findex.html" onkeydown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);" onmousedown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);">
					<span>页库存档</span></a>
                  </p>
                 </li>

                <li>
                  <div>
					
                    <a class="yschttl" onkeydown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.customs.gov.hk%2Fsc%2Fpublication_press%2Fpress%2Findex_id_173.html&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" onmousedown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.customs.gov.hk%2Fsc%2Fpublication_press%2Fpress%2Findex_id_173.html&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" id="waSearchResultTitle4" href="http://www.customs.gov.hk/sc/publication_press/press/index_id_173.html">
                      <span>香港海关 - 新闻公报</span>
                    </a>
                    </div>
                  <p>
                  </p>

                  <div class="yschabstr">
                    <span>直至十二月十九日，海关在陆路边境管制站共拘捕二十六名二十一岁以下涉及<strong>毒品</strong>案人士，检获约值八十九万元的<strong>毒品</strong>，涉及的<strong>毒品</strong>包括氯胺胴、硝甲西</span>
                  </div>
                  <!--/p-->
                  <p>
                    <!-- Last Modified Date: 2011-11-09 -->
                    <span class="yschurl">www.customs.gov.hk/sc/publication_press/press/index_id_173.html</span>
                    - 
                    <span>10.1K</span>
                    <span> - </span>
                    <span>04/03/2010</span>
                    <span> - </span>
                    <!--/p-->
                    <a class="yschmore" href="http://lp.search.gov.hk:8080/Action=View&amp;NoACI=true&amp;reference=http%3A%2F%2Fwww.customs.gov.hk%2Fsc%2Fpublication_press%2Fpress%2Findex_id_173.html" onkeydown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);" onmousedown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);">
					<span>页库存档</span></a>
                  </p>
                 </li>

                <li>
                  <div>
					
                    <a class="yschttl" onkeydown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.customs.gov.hk%2Fsc%2Fpublication_press%2Fpress%2Findex_id_286.html&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" onmousedown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.customs.gov.hk%2Fsc%2Fpublication_press%2Fpress%2Findex_id_286.html&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" id="waSearchResultTitle5" href="http://www.customs.gov.hk/sc/publication_press/press/index_id_286.html">
                      <span>香港海关 - 新闻公报</span>
                    </a>
                    </div>
                  <p>
                  </p>

                  <div class="yschabstr">
                    <span>外，亦会利用海关缉<strong>毒</strong>犬协助侦查<strong>毒品</strong>。」

在今日的记者会上，海关人员示范如何利用<strong>毒品</strong>探测器，侦缉旅客贩运<strong>毒品</strong>的不法...</span>
                  </div>
                  <!--/p-->
                  <p>
                    <!-- Last Modified Date: 2011-11-09 -->
                    <span class="yschurl">www.customs.gov.hk/sc/publication_press/press/index_id_286.html</span>
                    - 
                    <span>10.3K</span>
                    <span> - </span>
                    <span>05/03/2010</span>
                    <span> - </span>
                    <!--/p-->
                    <a class="yschmore" href="http://lp.search.gov.hk:8080/Action=View&amp;NoACI=true&amp;reference=http%3A%2F%2Fwww.customs.gov.hk%2Fsc%2Fpublication_press%2Fpress%2Findex_id_286.html" onkeydown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);" onmousedown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);">
					<span>页库存档</span></a>
                  </p>
                 </li>

                <li>
                  <div>
					
                    <a class="yschttl" onkeydown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.customs.gov.hk%2Fsc%2Fpublication_press%2Fpress%2Findex_id_153.html&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" onmousedown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.customs.gov.hk%2Fsc%2Fpublication_press%2Fpress%2Findex_id_153.html&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" id="waSearchResultTitle6" href="http://www.customs.gov.hk/sc/publication_press/press/index_id_153.html">
                      <span>香港海关 - 新闻公报</span>
                    </a>
                    </div>
                  <p>
                  </p>

                  <div class="yschabstr">
                    <span>青少年北上吸食<strong>毒品</strong>的问题，海关亦会在各管制站留意青少年的进出情况。他又呼籲青少年切勿以身试法贩运<strong>毒品</strong>，因为贩运<strong>毒品</strong>...</span>
                  </div>
                  <!--/p-->
                  <p>
                    <!-- Last Modified Date: 2011-11-09 -->
                    <span class="yschurl">www.customs.gov.hk/sc/publication_press/press/index_id_153.html</span>
                    - 
                    <span>10.0K</span>
                    <span> - </span>
                    <span>03/03/2010</span>
                    <span> - </span>
                    <!--/p-->
                    <a class="yschmore" href="http://lp.search.gov.hk:8080/Action=View&amp;NoACI=true&amp;reference=http%3A%2F%2Fwww.customs.gov.hk%2Fsc%2Fpublication_press%2Fpress%2Findex_id_153.html" onkeydown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);" onmousedown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);">
					<span>页库存档</span></a>
                  </p>
                 </li>

                <li>
                  <div>
					
                    <a class="yschttl" onkeydown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.customs.gov.hk%2Fsc%2Fpublication_press%2Fpress%2Findex_id_327.html&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" onmousedown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.customs.gov.hk%2Fsc%2Fpublication_press%2Fpress%2Findex_id_327.html&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" id="waSearchResultTitle7" href="http://www.customs.gov.hk/sc/publication_press/press/index_id_327.html">
                      <span>香港海关 - 新闻公报</span>
                    </a>
                    </div>
                  <p>
                  </p>

                  <div class="yschabstr">
                    <span>察<strong>毒品</strong>调查科（警方）联同香港海关<strong>毒品</strong>调查科（海关）完成一项反<strong>毒品</strong>行动，主力针对<strong>毒</strong>贩假扮旅客由各陆路边...</span>
                  </div>
                  <!--/p-->
                  <p>
                    <!-- Last Modified Date: 2011-11-09 -->
                    <span class="yschurl">www.customs.gov.hk/sc/publication_press/press/index_id_327.html</span>
                    - 
                    <span>9.7K</span>
                    <span> - </span>
                    <span>06/03/2010</span>
                    <span> - </span>
                    <!--/p-->
                    <a class="yschmore" href="http://lp.search.gov.hk:8080/Action=View&amp;NoACI=true&amp;reference=http%3A%2F%2Fwww.customs.gov.hk%2Fsc%2Fpublication_press%2Fpress%2Findex_id_327.html" onkeydown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);" onmousedown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);">
					<span>页库存档</span></a>
                  </p>
                 </li>

                <li>
                  <div>
					
                    <a class="yschttl" onkeydown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.customs.gov.hk%2Ffilemanager%2Fcommon%2Fpdf%2Fpdf_publications%2Fdept_review05_06%2Ftxt_sc%2Fch_05.htm&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" onmousedown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.customs.gov.hk%2Ffilemanager%2Fcommon%2Fpdf%2Fpdf_publications%2Fdept_review05_06%2Ftxt_sc%2Fch_05.htm&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" id="waSearchResultTitle8" href="http://www.customs.gov.hk/filemanager/common/pdf/pdf_publications/dept_review05_06/txt_sc/ch_05.htm">
                      <span>Annual Review 2006</span>
                    </a>
                    </div>
                  <p>
                  </p>

                  <div class="yschabstr">
                    <span>要来自印度。<strong>毒</strong>贩将<strong>毒品</strong>伪装成食<strong>品</strong>藏于行李或包裹中、或收藏在锡纸包或行李的暗格，甚至将<strong>毒品</strong>系于身上偷运入境。二...</span>
                  </div>
                  <!--/p-->
                  <p>
                    <!-- Last Modified Date: 2011-11-09 -->
                    <span class="yschurl">www.customs.gov.hk/.../pdf/pdf_publications/dept_review05_06/txt_sc/ch_05.htm</span>
                    - 
                    <span>9.1K</span>
                    <span> - </span>
                    <span>18/12/2012</span>
                    <span> - </span>
                    <!--/p-->
                    <a class="yschmore" href="http://lp.search.gov.hk:8080/Action=View&amp;NoACI=true&amp;reference=http%3A%2F%2Fwww.customs.gov.hk%2Ffilemanager%2Fcommon%2Fpdf%2Fpdf_publications%2Fdept_review05_06%2Ftxt_sc%2Fch_05.htm" onkeydown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);" onmousedown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);">
					<span>页库存档</span></a>
                  </p>
                 </li>

                <li>
                  <div>
					
                    <a class="yschttl" onkeydown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.customs.gov.hk%2Fsc%2Fpublication_press%2Fpress%2Findex_id_127.html&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" onmousedown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.customs.gov.hk%2Fsc%2Fpublication_press%2Fpress%2Findex_id_127.html&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" id="waSearchResultTitle9" href="http://www.customs.gov.hk/sc/publication_press/press/index_id_127.html">
                      <span>香港海关 - 新闻公报</span>
                    </a>
                    </div>
                  <p>
                  </p>

                  <div class="yschabstr">
                    <span>年北上吸食<strong>毒品</strong>的问题，海关亦会在各管制站留意青少年的进出情况。

他又呼籲青少年切勿以身试法贩运<strong>毒品</strong>，因为贩...</span>
                  </div>
                  <!--/p-->
                  <p>
                    <!-- Last Modified Date: 2011-11-09 -->
                    <span class="yschurl">www.customs.gov.hk/sc/publication_press/press/index_id_127.html</span>
                    - 
                    <span>10.2K</span>
                    <span> - </span>
                    <span>02/03/2010</span>
                    <span> - </span>
                    <!--/p-->
                    <a class="yschmore" href="http://lp.search.gov.hk:8080/Action=View&amp;NoACI=true&amp;reference=http%3A%2F%2Fwww.customs.gov.hk%2Fsc%2Fpublication_press%2Fpress%2Findex_id_127.html" onkeydown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);" onmousedown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);">
					<span>页库存档</span></a>
                  </p>
                 </li>

                <li>
                  <div>
					
                    <a class="yschttl" onkeydown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.customs.gov.hk%2Fsc%2Fpublication_press%2Fpress%2Findex_id_442.html&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" onmousedown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.customs.gov.hk%2Fsc%2Fpublication_press%2Fpress%2Findex_id_442.html&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" id="waSearchResultTitle10" href="http://www.customs.gov.hk/sc/publication_press/press/index_id_442.html">
                      <span>香港海关 - 新闻公报</span>
                    </a>
                    </div>
                  <p>
                  </p>

                  <div class="yschabstr">
                    <span> <strong>毒</strong>

在打击贩<strong>毒</strong>工作方面，二○○九年海关检获各类<strong>毒品</strong>共652公斤，数量比二○○八年上升8%。检获的<strong>毒品</strong>最多的是氯胺酮（即K仔），共380公斤，数量是过</span>
                  </div>
                  <!--/p-->
                  <p>
                    <!-- Last Modified Date: 2011-11-09 -->
                    <span class="yschurl">www.customs.gov.hk/sc/publication_press/press/index_id_442.html</span>
                    - 
                    <span>16.7K</span>
                    <span> - </span>
                    <span>12/03/2010</span>
                    <span> - </span>
                    <!--/p-->
                    <a class="yschmore" href="http://lp.search.gov.hk:8080/Action=View&amp;NoACI=true&amp;reference=http%3A%2F%2Fwww.customs.gov.hk%2Fsc%2Fpublication_press%2Fpress%2Findex_id_442.html" onkeydown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);" onmousedown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);">
					<span>页库存档</span></a>
                  </p>
                 </li>

                <!--search result list end-->
              </ol>
            </div>
          </div>
          <script>
            if (deptMenu == '') {
              document.getElementById("dmnSpLeftMiddle").style.width = "98%";
            }
          </script>
        </div>
        <script>
          printFooterLayer1();
        </script>

		<!-- Related keyword for department -->
		<div id="ajaxResult">
				
		</div>
		<!-- Use AJAX in this part
		<div th:if="${rkwListArr != null}">
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
		 -->
		<div>
        <div class="yschpg">
        	<!-- yschindex -->
          <div class="yschindex">
	      	<span>
				
			</span>&nbsp;
		      <span>
		        <strong><span class="current">1</span>&nbsp;</strong>
		        
		      </span>
		      <span>
		        
		        <a onclick="clickCount('paginationTool', '', '')" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-cn&amp;tpl_id=customs_r2&amp;page=2&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;gp0=customs_r2_home&amp;gp1=customs_r2_home&amp;doc_type=all&amp;sort=&amp;web=this&amp;txtonly=0&amp;site=customs_r2_home&amp;last_mod=%23-1">
		        <span>2</span>&nbsp;</a>
		      </span>
		      <span>
		        
		        <a onclick="clickCount('paginationTool', '', '')" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-cn&amp;tpl_id=customs_r2&amp;page=3&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;gp0=customs_r2_home&amp;gp1=customs_r2_home&amp;doc_type=all&amp;sort=&amp;web=this&amp;txtonly=0&amp;site=customs_r2_home&amp;last_mod=%23-1">
		        <span>3</span>&nbsp;</a>
		      </span>
		      <span>
		        
		        <a onclick="clickCount('paginationTool', '', '')" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-cn&amp;tpl_id=customs_r2&amp;page=4&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;gp0=customs_r2_home&amp;gp1=customs_r2_home&amp;doc_type=all&amp;sort=&amp;web=this&amp;txtonly=0&amp;site=customs_r2_home&amp;last_mod=%23-1">
		        <span>4</span>&nbsp;</a>
		      </span>
		      <span>
		        
		        <a onclick="clickCount('paginationTool', '', '')" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-cn&amp;tpl_id=customs_r2&amp;page=5&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;gp0=customs_r2_home&amp;gp1=customs_r2_home&amp;doc_type=all&amp;sort=&amp;web=this&amp;txtonly=0&amp;site=customs_r2_home&amp;last_mod=%23-1">
		        <span>5</span>&nbsp;</a>
		      </span>
		      <span>
		        
		        <a onclick="clickCount('paginationTool', '', '')" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-cn&amp;tpl_id=customs_r2&amp;page=6&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;gp0=customs_r2_home&amp;gp1=customs_r2_home&amp;doc_type=all&amp;sort=&amp;web=this&amp;txtonly=0&amp;site=customs_r2_home&amp;last_mod=%23-1">
		        <span>6</span>&nbsp;</a>
		      </span>
		      <span>
		        
		        <a onclick="clickCount('paginationTool', '', '')" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-cn&amp;tpl_id=customs_r2&amp;page=7&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;gp0=customs_r2_home&amp;gp1=customs_r2_home&amp;doc_type=all&amp;sort=&amp;web=this&amp;txtonly=0&amp;site=customs_r2_home&amp;last_mod=%23-1">
		        <span>7</span>&nbsp;</a>
		      </span>
		      <span>
		        
		        <a onclick="clickCount('paginationTool', '', '')" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-cn&amp;tpl_id=customs_r2&amp;page=8&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;gp0=customs_r2_home&amp;gp1=customs_r2_home&amp;doc_type=all&amp;sort=&amp;web=this&amp;txtonly=0&amp;site=customs_r2_home&amp;last_mod=%23-1">
		        <span>8</span>&nbsp;</a>
		      </span>
		      <span>
		        
		        <a onclick="clickCount('paginationTool', '', '')" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-cn&amp;tpl_id=customs_r2&amp;page=9&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;gp0=customs_r2_home&amp;gp1=customs_r2_home&amp;doc_type=all&amp;sort=&amp;web=this&amp;txtonly=0&amp;site=customs_r2_home&amp;last_mod=%23-1">
		        <span>9</span>&nbsp;</a>
		      </span>
		      <span>
		        
		        <a onclick="clickCount('paginationTool', '', '')" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-cn&amp;tpl_id=customs_r2&amp;page=10&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;gp0=customs_r2_home&amp;gp1=customs_r2_home&amp;doc_type=all&amp;sort=&amp;web=this&amp;txtonly=0&amp;site=customs_r2_home&amp;last_mod=%23-1">
		        <span>10</span>&nbsp;</a>
		      </span>
			<span>
			  <a onclick="clickCount('paginationTool', '', '')" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-cn&amp;tpl_id=customs_r2&amp;page=2&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;gp0=customs_r2_home&amp;gp1=customs_r2_home&amp;doc_type=all&amp;sort=&amp;web=this&amp;txtonly=0&amp;site=customs_r2_home&amp;last_mod=%23-1" title="下一页">下一页</a>
			</span>
		  </div>
        </div>
        <script>
          function blackKeyAlert() {
            alert('Please enter keyword!');
          }
        </script>
        <form name="gs" id="hksarg_searchyschtopsearch2" method="GET" onsubmit="if(document.getElementById('hksarg_searchyschtopsearch2').query.value.length==0)blackKeyAlert();else       document.getElementById('hksarg_searchyschtopsearch2').submit();return false;" action="/search">
          <script>
            printDeptSearchBarHeaderLayer1();
          </script>
          <!-- <div class="deptSearchBarHeader" id="withborder" style=""> -->
            <div class="deptSearchBarHeaderLeft">&nbsp;&nbsp;&nbsp;<label for="SearchBarBox2" class="hidden">Departmental
              Search</label><input class="deptSearchBarSearchInput" type="text" name="query" size="32" maxlength="256" id="SearchBarBox2" value="毒品" /><span class="deptSearchBarSearch">&nbsp;<script>
              function formSubmit(id) {
                if (document.getElementById(id).query.value.length == 0) {
                  alert('Please enter keyword!');
                } else {
                  document.getElementById(id).submit();
                }
                return;
              }
            </script><a href="javascript:formSubmit('hksarg_searchyschtopsearch2')"><img id="yschtopsearch2" alt="Search" onfocus="javascript:swapImage(this,&#39;/search/topsearch_sc_hover.gif&#39;)" onblur="javascript:swapImage(this,&#39;/search/topsearch_sc_off.gif&#39;)" onmouseover="javascript:swapImage(this,&#39;/search/topsearch_sc_hover.gif&#39;)" onmouseout="javascript:swapImage(this,&#39;/search/topsearch_sc_off.gif&#39;)" src="/search/topsearch_sc_off.gif" /></a>&nbsp;</span>
                    <span class="deptSearchBarAdvSearch">

          <script>
            /*<![CDATA[*/
			var isTxtOnly = 0;
			var linkText = '\u8FDB\u9636\u641C\u5BFB';
            if (deptAdvSearch != "" && isTxtOnly == 0) {
              if (deptAdvSearch != "") {
                deptAdvSearch = deptAdvSearch + '?query=%E6%AF%92%E5%93%81&ui_lang=zh-cn&tpl_id=customs_r2&page=1&p_size=10&output=xml_no_dtd&ui_charset=utf-8&a_submit=false&gp0=customs_r2_home&gp1=customs_r2_home&doc_type=all&web=this&txtonly=0&site=customs_r2_home&last_mod=%23-1';
                printAdvancedSearch(deptAdvSearch, linkText);
              }
            } else if (deptAdvSearchTxt != "" && isTxtOnly == 1) {
            	deptAdvSearchTxt = deptAdvSearchTxt + '?query=%E6%AF%92%E5%93%81&ui_lang=zh-cn&tpl_id=customs_r2&page=1&p_size=10&output=xml_no_dtd&ui_charset=utf-8&a_submit=false&gp0=customs_r2_home&gp1=customs_r2_home&doc_type=all&web=this&txtonly=0&site=customs_r2_home&last_mod=%23-1';
                printAdvancedSearch(deptAdvSearchTxt, linkText);
            }
            /*]]>*/
            </script>
            </span>
              <input type="hidden" name="output" value="xml_no_dtd" />
              <input type="hidden" name="gp1" value="customs_r2_home" />
              <input type="hidden" name="gp0" value="customs_r2_home" />
              <input type="hidden" name="web" value="${web}" />
              <input type="hidden" name="a_submit" value="false" />
              <input type="hidden" name="txtonly" value="0" />
              <input type="hidden" name="tpl_id" value="customs_r2" />
              <input type="hidden" name="ui_lang" value="zh-cn" />
              <input type="hidden" name="sort" value="" />
            </div>
            <script>
              printDeptSearchBarHeaderLayer2();
            </script>
          <!-- </div> -->
          <div class="deptSearchBarHeaderBottom">
            <fieldset>
              <table class="border0">
                <tbody>
                <tr>
                  <td>
                    <table class="border0">
                      <tbody>
                      <tr>
                        <td>显示：</td>
                      </tr>
                      </tbody>
                    </table>
                  </td>
                  <td>
                    <table class="border0">
                      <tbody>
                      <tr>
                        <td>&nbsp;<input type="radio" id="yschtopsearch2all_ck_top" name="site" value="default_collection" /></td>
                        <td>&nbsp;<label for="yschtopsearch2all_ck_top">所有政府网站</label></td>
                      </tr>
                      </tbody>
                    </table>
                  </td>
                  <td>
                    <table class="border0">
                      <tbody>
                      <tr>
                        <td>&nbsp;&nbsp;<input type="radio" id="yschtopsearch2this_ck_top" name="site" checked="checked" value="customs_r2_home" /></td>
                        <td>&nbsp;<label for="yschtopsearch2this_ck_top">此网站</label></td>
                      </tr>
                      </tbody>
                    </table>
                  </td>
                </tr>
                </tbody>
              </table>
              &nbsp;&nbsp;
            </fieldset>
          </div>
        </form>
        </div>
        <br /> <!-- Please enter html code below. -->
        <div id="dmnSpLowLeft" class="dept">
          <div id="dmnSpsearchBarBtm">
            <div id="dmnSpFooter" class="dept1">
              <div id="footerArea" class="dept1"> 2010 <img alt="Copyright" src="/search/bd_copy.gif" />
                <script>
                /*<![CDATA[*/
                	var impNotice = '\u91CD\u8981\u544A\u793A';
                	var privacy = '\u79C1\u96B1\u653F\u7B56';
                  if (deptNotice != '') {
                    document.write(' | <a class="link5" href="' + deptNotice + '">' + impNotice + '</a>');
                  }
                  if (deptPP != '') {
                    document.write(' | <a class="link5" href="' + deptPP + '">' + privacy +'</a>');
                  }
                /*]]>*/
                </script>
              </div>
              
              <!-- Please enter html code below. -->
            </div>
          </div>
        </div>
      </div>
      <script>
        printFooterLayer2();
      </script>
    </div>
  </div>
  <!-- End of Department template body -->
  
  <!-- Standard search footer -->

  <!-- End of standard search footer -->
  <script>
    var ogcioUserKeyword = "${query}";
  </script>
</div>
</body>
</html>
"""


soup = BeautifulSoup(html_doc, "lxml")

print '---------------------------------'
# 解析得到网页链接

founds = soup.find('div', id = 'yschres').find_all('li')
print len(founds)

item_list = []
print '------------url---------------'
id = 0
for found in founds:
    id += 1
    print id
    # item = items.PostItem()
    title = found.find('div').get_text().strip()
    url = found.find('div').find('a').get('href')
    # print title
    print url
    m = md5.new() 
    m.update(url)
    md_str = m.hexdigest()
    print md_str

    post_time = found.find_all('p')[1].find_all('span')[3].get_text().strip()
    # post_time = re.findall(self.tt_pa, post_time)[0]
    post_time = post_time[6:] + '-' + post_time[3:5] + '-' + post_time[0:2] + ' ' + '00:00:00'
    print post_time


#得到下一页链接，寻找最后一个span标签

next_pages = soup.find('div', class_ = 'yschindex').find_all('span')
# next_pages = soup.div.class_['yschindex'].find_all('span')
l = len(next_pages)
try:
    next_page = next_pages[l-1].a['href']
    next_page = 'http://lp.search.gov.hk/search' + next_page
    print next_page
except:
    print 'last page-----'



