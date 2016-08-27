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
    var page_site = 'swd_home';
    
    function rkwAjax() {
    	var url = '/ajaxRkw?query=%E6%AF%92%E5%93%81&ui_lang=zh-cn&tpl_id=stdsearch&page=1&p_size=10&output=xml_no_dtd&ui_charset=utf-8&a_submit=false&toASubmit=false&gp0=swd_home&gp1=swd_home&doc_type=all&sort=date&web=this&txtonly=0&site=swd_home&last_mod=%23-1&exact_q=&any_q=&none_q=';
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
<body onload="resetForms();rkwAjax();keyUpdate()" dir="ltr" lang="zh-cn" class="tc about"> <!-- Please enter html code below. -->
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
              <a onclick="clickCount(&#39;langSwitchButtons&#39;, '', '')" id="en" title="English" lang="en" class="en" rel="alternate" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=en&amp;tpl_id=stdsearch&amp;page=1&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;a_submit=false&amp;toASubmit=false&amp;gp0=swd_home&amp;gp1=swd_home&amp;doc_type=all&amp;sort=date&amp;web=this&amp;txtonly=0&amp;site=swd_home&amp;last_mod=%23-1&amp;tab=&amp;tab_depts=">English</a>
              |
              </li>
              <li id="subItem">
              
              <a onclick="clickCount(&#39;langSwitchButtons&#39;, '', '')" id="zh-hk" title="繁體" lang="zh-hk" class="zh-HK" rel="alternate" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-hk&amp;tpl_id=stdsearch&amp;page=1&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;a_submit=false&amp;toASubmit=false&amp;gp0=swd_home&amp;gp1=swd_home&amp;doc_type=all&amp;sort=date&amp;web=this&amp;txtonly=0&amp;site=swd_home&amp;last_mod=%23-1&amp;tab=&amp;tab_depts=">繁體</a>
              
              </li>
              
            </ul>
            <div class="access">Header Menu</div>
            <ul id="quickLinks">
              <li><a id="waGovDirectory" title="政府機構" href="http://www.gov.hk/sc/about/govdirectory/">政府机构</a></li>
              <li><a id="onlineservices" title="網上服務" href="http://www.gov.hk/sc/residents/onlineservices/">网上服务</a></li>
              <li><a id="forms" title="表格" href="http://www.gov.hk/sc/residents/forms/">表格</a></li>
              <li><a id="waAboutHK" title="關於香港" href="http://www.gov.hk/sc/about/abouthk/">关于香港</a></li>

              <li class="mygovhkLinks">
                <div id="mygovhk_header" class="A tc">
                  <div id="mygovhk_header_text">
                    <a id="mygovhk_header_login" title="登入我的政府一站通" href="http://www.gov.hk/sc/apps/mygovhk.htm">
                    <span>登入</span></a>
                      |
                    <a id="mygovhk_header_register" title="登記我的政府一站通" href="http://www.gov.hk/sc/theme/mygovhk/">
                    <span>登记</span></a>
                  </div>
                </div>
              </li>
            </ul>
		</div>
	</div>
	<div id="pageContainer">
		<div id="govhkBar">
			<div id="govhkLogo"><a title="GovHK 香港政府一站通 " href="http://www.gov.hk/sc/residents/"><img title="GovHK 香港政府一站通 " alt="GovHK 香港政府一站通 " src="/images/govhk.png" /></a></div>
            <div class="access">GovHK Usergroups</div>
            <div id="userGroups">
                  <ul>
                     <li id="usrGrpResidents"><a title="Residents" href="http://www.gov.hk/sc/residents/">本港居民</a></li>
                     <li id="usrGrpBusiness"><a title="Business &amp; Trade" href="http://www.gov.hk/sc/business/">商务及贸易</a></li>
                     <li id="usrGrpNonResidents"><a title="Non-Residents" href="http://www.gov.hk/sc/nonresidents/">非本港居民</a></li>
                     <li id="usrGrpYouth">
					<a id="waUsrGrp4" href="#" data-hasqtip="0" title="">社会群体</a>

					<div id="socialGroupsDiv1">
		        		<div id="socialGroupsDiv2">
		                <div id="socialGroupsDiv3"></div>
		                <div id="socialGroupsDiv4">
	                        <ul id="socialGroupsList">
	
                                <li><a rel="external" title="康复数码网络" href="http://cyberable.swd.gov.hk/sim/index.html">
                                <img src="http://www.gov.hk/sc/images/socialgroups/cyberable.gif" alt="康复数码网络" /></a></li>
                                
                                <li><a rel="external" title="长青网" href="http://www.e123.hk/pro/sc">
                                <img src="http://www.gov.hk/sc/images/socialgroups/e123.png" alt="长青网" /></a></li>

                                <li><a rel="external" title="开心家庭网络" href="http://www.familycouncil.gov.hk/sc_chi/index.htm">
                                <img src="http://www.gov.hk/sc/images/socialgroups/HappyFamily.png" alt="开心家庭网络" /></a></li>

                                <li><a rel="external" title="政府青少年网站" href="http://sc.youth.gov.hk/TuniS/www.youth.gov.hk/tc/">
                                <img src="http://www.gov.hk/sc/images/socialgroups/youth.png" alt="政府青少年网站" /></a></li>

                                <li><a rel="external" title="妇女事务委员会" href="http://www.women.gov.hk/colour/sc/home/index.htm">
                                <img src="http://www.gov.hk/sc/images/socialgroups/women.png" alt="妇女事务委员会" /></a></li>
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
                              <input type="hidden" name="ui_lang" value="zh-cn" />
                              <input type="hidden" name="gp1" value="swd_home" />
                              <input type="hidden" name="gp0" value="swd_home" />
                              <input type="hidden" name="web" value="this" />
                              <input type="hidden" name="txtonly" value="0" />
                              <input type="hidden" name="tpl_id" value="stdsearch" />
                              <input type="hidden" name="sort" value="date" />
                              <input type="hidden" name="site" value="swd_home" />
                              
		             		  
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
                     <h1>搜寻结果</h1>
                     
                  </div>
                  <div id="breadCrumb">
                     <div class="access">Your current location in the website</div>
                     <a title="Home" href="http://www.gov.hk/sc/residents/">主页</a> &gt;
                     	<strong><span>搜寻结果</span></strong>
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
		                   <label for="searchBox2" class="access">查询</label>
		                   <input type="text" class="searchBox ui-autocomplete-input" name="query" id="searchBox2" autocomplete="off" value="毒品" />
		                   <label for="searchIcon2" class="access">Search Submit</label>
		                   <input type="submit" title="Search" class="searchIcon2" id="searchIcon2" name="search_but" value="" />
		                   </div>
		                </div>
		             </div>
		             <div class="advSearch"><a href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-cn&amp;tpl_id=stdsearch&amp;page=1&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;a_submit=false&amp;toASubmit=true&amp;last_mod=%23-1&amp;gp0=swd_home&amp;gp1=swd_home&amp;doc_type=all&amp;sort=date&amp;web=this&amp;txtonly=0&amp;site=swd_home">进阶搜寻</a></div>
		             <div class="faqSearch"><a href="http://www.gov.hk/sc/about/helpdesk/search/">有关搜寻服务的常见问题</a></div>
		             <input type="hidden" name="output" value="xml_no_dtd" />
		             <input type="hidden" name="ui_lang" value="zh-cn" />
		             <input type="hidden" name="gp1" value="swd_home" />
		             <input type="hidden" name="gp0" value="swd_home" />
		             <input type="hidden" name="web" value="this" />
		             <input type="hidden" name="txtonly" value="0" />
		             <input type="hidden" name="tpl_id" value="stdsearch" />
		             <input type="hidden" name="sort" value="date" />
		             <input type="hidden" name="doc_type" value="all" />
		             
		             
		             
		             <div id="stdTplRadioButton" class="clearthis">
		             <fieldset><legend class="hidden">显示：</legend>
		             <span>显示：</span>&nbsp;
		             <input type="radio" id="yschtopsearch1all_ck_top_1" name="site" value="default_collection" />
		             <label for="yschtopsearch1all_ck_top_1">所有政府网站</label>
					 <input type="radio" id="yschtopsearch1this_ck_top_1" name="site" checked="checked" value="swd_home" />
					 <label for="yschtopsearch1this_ck_top_1">社会福利署</label>
					 
					 </fieldset>
					 </div>
					</div>
				</form>
                </div>
				<div class="searchResultTitle">
					<h2>
						<span>约找到 <strong>572</strong> 个结果，显示第 <strong>1</strong> 至 <strong>10</strong> 个。 </span>
						
						<span>用时 <strong>0.496</strong> 秒。</span>
					</h2>
				</div>
				
				<!-- Spell suggestion -->
				
				<div class="faqSearch">
					
					<span>根据日期排序</span>
					/
					
					<a onclick="clickCount(&#39;sort_by_relevance&#39;, '', '')" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-cn&amp;tpl_id=stdsearch&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;gp0=swd_home&amp;gp1=swd_home&amp;doc_type=all&amp;web=this&amp;txtonly=0&amp;site=swd_home&amp;last_mod=%23-1&amp;tab=&amp;tab_depts=">根据相关程度排序</a>
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
		                  	
		                    <a class="itemDetailsTitle" onkeydown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.swd.gov.hk%2Fsc%2Findex%2Fsite_pubsvc%2Fpage_rehab%2Fsub_healthprot%2F&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" onmousedown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.swd.gov.hk%2Fsc%2Findex%2Fsite_pubsvc%2Fpage_rehab%2Fsub_healthprot%2F&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" id="waSearchResultTitle1" href="http://www.swd.gov.hk/sc/index/site_pubsvc/page_rehab/sub_healthprot/">
		                      <span>社会福利署 - 康复服务单位的卫生防护资讯</span>
		                    </a>
		                   </h3>
		                  <p>
		                  	<span class="itemDetailsDescription">宗外地传入人类感染甲型禽流感(H7N9)病<strong>毒</strong>个案」通告 PDF 文件
...</span>
		                  </p>
		
		                  <!--/p-->
		                  <p>
		                    <!-- Last Modified Date: 2011-11-09 -->
		                    <span class="itemDetailsLink">www.swd.gov.hk/sc/index/site_pubsvc/page_rehab/sub_healthprot</span>
		                    - 
		                    <span>44.8K</span>
		                    <span> - </span>
		                    <span>10/08/2016</span>
		                    <span> - </span>
		                    <!--/p-->
		                    <!-- Add cache here -->
		                    <a class="moreFromThisSiteLink" href="http://lp.search.gov.hk:8080/Action=View&amp;NoACI=true&amp;reference=http%3A%2F%2Fwww.swd.gov.hk%2Fsc%2Findex%2Fsite_pubsvc%2Fpage_rehab%2Fsub_healthprot%2F" onkeydown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);" onmousedown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);">
		                    <span>页库存档</span></a>
		                  </p>
		                 </li>
		
		                <li>
		                  <h3>
		                  	
		                    <a class="itemDetailsTitle" onkeydown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.swd.gov.hk%2Fsc%2Findex%2Fsite_download%2Fpage_listofserv%2F&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" onmousedown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.swd.gov.hk%2Fsc%2Findex%2Fsite_download%2Fpage_listofserv%2F&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" id="waSearchResultTitle2" href="http://www.swd.gov.hk/sc/index/site_download/page_listofserv/">
		                      <span>社会福利署 - 服务单位名单</span>
		                    </a>
		                   </h3>
		                  <p>
		                  	<span class="itemDetailsDescription">社会福利署 - 服务单位名单. 跳至主要内容 

	

	

	

	社会福利署
	香港<strong>品</strong>...</span>
		                  </p>
		
		                  <!--/p-->
		                  <p>
		                    <!-- Last Modified Date: 2011-11-09 -->
		                    <span class="itemDetailsLink">www.swd.gov.hk/sc/index/site_download/page_listofserv</span>
		                    - 
		                    <span>81.9K</span>
		                    <span> - </span>
		                    <span>08/08/2016</span>
		                    <span> - </span>
		                    <!--/p-->
		                    <!-- Add cache here -->
		                    <a class="moreFromThisSiteLink" href="http://lp.search.gov.hk:8080/Action=View&amp;NoACI=true&amp;reference=http%3A%2F%2Fwww.swd.gov.hk%2Fsc%2Findex%2Fsite_download%2Fpage_listofserv%2F" onkeydown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);" onmousedown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);">
		                    <span>页库存档</span></a>
		                  </p>
		                 </li>
		
		                <li>
		                  <h3>
		                  	
		                    <a class="itemDetailsTitle" onkeydown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.swd.gov.hk%2Fsc%2Findex%2Fsite_download%2Fpage_india%2F&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" onmousedown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.swd.gov.hk%2Fsc%2Findex%2Fsite_download%2Fpage_india%2F&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" id="waSearchResultTitle3" href="http://www.swd.gov.hk/sc/index/site_download/page_india/">
		                      <span>社会福利署 - 印度</span>
		                    </a>
		                   </h3>
		                  <p>
		                  	<span class="itemDetailsDescription">社会福利署 - 印度. 跳至主要内容 

	

	

	

	社会福利署
	香港<strong>品</strong>...</span>
		                  </p>
		
		                  <!--/p-->
		                  <p>
		                    <!-- Last Modified Date: 2011-11-09 -->
		                    <span class="itemDetailsLink">www.swd.gov.hk/sc/index/site_download/page_india</span>
		                    - 
		                    <span>35.4K</span>
		                    <span> - </span>
		                    <span>05/08/2016</span>
		                    <span> - </span>
		                    <!--/p-->
		                    <!-- Add cache here -->
		                    <a class="moreFromThisSiteLink" href="http://lp.search.gov.hk:8080/Action=View&amp;NoACI=true&amp;reference=http%3A%2F%2Fwww.swd.gov.hk%2Fsc%2Findex%2Fsite_download%2Fpage_india%2F" onkeydown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);" onmousedown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);">
		                    <span>页库存档</span></a>
		                  </p>
		                 </li>
		
		                <li>
		                  <h3>
		                  	
		                    <a class="itemDetailsTitle" onkeydown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.swd.gov.hk%2Fsc%2Findex%2Fsite_download%2Fpage_rru%2F&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" onmousedown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.swd.gov.hk%2Fsc%2Findex%2Fsite_download%2Fpage_rru%2F&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" id="waSearchResultTitle4" href="http://www.swd.gov.hk/sc/index/site_download/page_rru/">
		                      <span>社会福利署 - 少数族裔服务资料</span>
		                    </a>
		                   </h3>
		                  <p>
		                  	<span class="itemDetailsDescription">社会福利署 - 少数族裔服务资料. 跳至主要内容 

	

	

	

	社会福利署
	香港<strong>品</strong>...</span>
		                  </p>
		
		                  <!--/p-->
		                  <p>
		                    <!-- Last Modified Date: 2011-11-09 -->
		                    <span class="itemDetailsLink">www.swd.gov.hk/sc/index/site_download/page_rru</span>
		                    - 
		                    <span>25.1K</span>
		                    <span> - </span>
		                    <span>04/08/2016</span>
		                    <span> - </span>
		                    <!--/p-->
		                    <!-- Add cache here -->
		                    <a class="moreFromThisSiteLink" href="http://lp.search.gov.hk:8080/Action=View&amp;NoACI=true&amp;reference=http%3A%2F%2Fwww.swd.gov.hk%2Fsc%2Findex%2Fsite_download%2Fpage_rru%2F" onkeydown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);" onmousedown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);">
		                    <span>页库存档</span></a>
		                  </p>
		                 </li>
		
		                <li>
		                  <h3>
		                  	
		                    <a class="itemDetailsTitle" onkeydown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.swd.gov.hk%2Fsc%2Findex%2Fsite_pubsvc%2Fpage_medical%2Fsub_supportfun%2F&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" onmousedown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.swd.gov.hk%2Fsc%2Findex%2Fsite_pubsvc%2Fpage_medical%2Fsub_supportfun%2F&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" id="waSearchResultTitle5" href="http://www.swd.gov.hk/sc/index/site_pubsvc/page_medical/sub_supportfun/">
		                      <span>社会福利署 - 爱滋病患者及家属援助金</span>
		                    </a>
		                   </h3>
		                  <p>
		                  	<span class="itemDetailsDescription">社会福利署 - 爱滋病患者及家属援助金. 跳至主要内容 

	

	

	

	社会福利署
	香港<strong>品</strong>...</span>
		                  </p>
		
		                  <!--/p-->
		                  <p>
		                    <!-- Last Modified Date: 2011-11-09 -->
		                    <span class="itemDetailsLink">www.swd.gov.hk/sc/index/site_pubsvc/page_medical/sub_supportfun</span>
		                    - 
		                    <span>23.0K</span>
		                    <span> - </span>
		                    <span>29/07/2016</span>
		                    <span> - </span>
		                    <!--/p-->
		                    <!-- Add cache here -->
		                    <a class="moreFromThisSiteLink" href="http://lp.search.gov.hk:8080/Action=View&amp;NoACI=true&amp;reference=http%3A%2F%2Fwww.swd.gov.hk%2Fsc%2Findex%2Fsite_pubsvc%2Fpage_medical%2Fsub_supportfun%2F" onkeydown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);" onmousedown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);">
		                    <span>页库存档</span></a>
		                  </p>
		                 </li>
		
		                <li>
		                  <h3>
		                  	
		                    <a class="itemDetailsTitle" onkeydown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.swd.gov.hk%2Fsc%2Findex%2Fsite_pubsvc%2Fpage_young%2Fsub_seryouthrisk%2Fid_committeeo%2F&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" onmousedown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.swd.gov.hk%2Fsc%2Findex%2Fsite_pubsvc%2Fpage_young%2Fsub_seryouthrisk%2Fid_committeeo%2F&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" id="waSearchResultTitle6" href="http://www.swd.gov.hk/sc/index/site_pubsvc/page_young/sub_seryouthrisk/id_committeeo/">
		                      <span>社会福利署 - 边缘青少年服务委员会</span>
		                    </a>
		                   </h3>
		                  <p>
		                  	<span class="itemDetailsDescription">社会福利署 - 边缘青少年服务委员会. 跳至主要内容 

	

	

	

	社会福利署
	香港<strong>品</strong>...</span>
		                  </p>
		
		                  <!--/p-->
		                  <p>
		                    <!-- Last Modified Date: 2011-11-09 -->
		                    <span class="itemDetailsLink">www.swd.gov.hk/sc/index/site_pubsvc/page_young/sub_seryouthrisk/id_committeeo</span>
		                    - 
		                    <span>19.7K</span>
		                    <span> - </span>
		                    <span>26/07/2016</span>
		                    <span> - </span>
		                    <!--/p-->
		                    <!-- Add cache here -->
		                    <a class="moreFromThisSiteLink" href="http://lp.search.gov.hk:8080/Action=View&amp;NoACI=true&amp;reference=http%3A%2F%2Fwww.swd.gov.hk%2Fsc%2Findex%2Fsite_pubsvc%2Fpage_young%2Fsub_seryouthrisk%2Fid_committeeo%2F" onkeydown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);" onmousedown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);">
		                    <span>页库存档</span></a>
		                  </p>
		                 </li>
		
		                <li>
		                  <h3>
		                  	<span class="searchResultType">[PDF]</span>
		                    <a class="itemDetailsTitle" onkeydown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.swd.gov.hk%2Fdoc_sc%2Frehab%2Fvrs%2FHIT%2520letter%252011032016.PDF&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" onmousedown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.swd.gov.hk%2Fdoc_sc%2Frehab%2Fvrs%2FHIT%2520letter%252011032016.PDF&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" id="waSearchResultTitle7" href="http://www.swd.gov.hk/doc_sc/rehab/vrs/HIT%20letter%2011032016.PDF">
		                      <span>HIT letter 11032016.PDF</span>
		                    </a>
		                   </h3>
		                  <p>
		                  	<span class="itemDetailsDescription">護膚<strong>品</strong>；

依照指示重複使用昆蟲驅避劑。

出外旅遊須知

外遊人士尤其是有免疫系統疾病或長期病患者...</span>
		                  </p>
		
		                  <!--/p-->
		                  <p>
		                    <!-- Last Modified Date: 2011-11-09 -->
		                    <span class="itemDetailsLink">www.swd.gov.hk/doc_sc/rehab/vrs/HIT%20letter%2011032016.PDF</span>
		                    - 
		                    <span>259.6K</span>
		                    <span> - </span>
		                    <span>22/07/2016</span>
		                    <span> - </span>
		                    <!--/p-->
		                    <!-- Add cache here -->
		                    <a class="moreFromThisSiteLink" href="http://lp.search.gov.hk:8080/Action=View&amp;NoACI=true&amp;reference=http%3A%2F%2Fwww.swd.gov.hk%2Fdoc_sc%2Frehab%2Fvrs%2FHIT%2520letter%252011032016.PDF" onkeydown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);" onmousedown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);">
		                    <span>页库存档</span></a>
		                  </p>
		                 </li>
		
		                <li>
		                  <h3>
		                  	<span class="searchResultType">[PDF]</span>
		                    <a class="itemDetailsTitle" onkeydown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.swd.gov.hk%2Fdoc_sc%2Frehab%2Fvrs%2FHIT%2520letter%252021032016.PDF&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" onmousedown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.swd.gov.hk%2Fdoc_sc%2Frehab%2Fvrs%2FHIT%2520letter%252021032016.PDF&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" id="waSearchResultTitle8" href="http://www.swd.gov.hk/doc_sc/rehab/vrs/HIT%20letter%2021032016.PDF">
		                      <span>HIT letter 21032016.PDF</span>
		                    </a>
		                   </h3>
		                  <p>
		                  	<span class="itemDetailsDescription">公眾地方；

和

最少每日一次用適當的消<strong>毒</strong>劑清潔及消<strong>毒</strong>經常接觸的表面、傢佩物

<strong>品</strong>、玩具、共用物<strong>品</strong>和地面（非金屬表面可把1份家用漂白水與...</span>
		                  </p>
		
		                  <!--/p-->
		                  <p>
		                    <!-- Last Modified Date: 2011-11-09 -->
		                    <span class="itemDetailsLink">www.swd.gov.hk/doc_sc/rehab/vrs/HIT%20letter%2021032016.PDF</span>
		                    - 
		                    <span>166.1K</span>
		                    <span> - </span>
		                    <span>22/07/2016</span>
		                    <span> - </span>
		                    <!--/p-->
		                    <!-- Add cache here -->
		                    <a class="moreFromThisSiteLink" href="http://lp.search.gov.hk:8080/Action=View&amp;NoACI=true&amp;reference=http%3A%2F%2Fwww.swd.gov.hk%2Fdoc_sc%2Frehab%2Fvrs%2FHIT%2520letter%252021032016.PDF" onkeydown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);" onmousedown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);">
		                    <span>页库存档</span></a>
		                  </p>
		                 </li>
		
		                <li>
		                  <h3>
		                  	<span class="searchResultType">[PDF]</span>
		                    <a class="itemDetailsTitle" onkeydown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.swd.gov.hk%2Fdoc_sc%2Frehab%2Fvrs%2FHIT%2520letter%252020042016.PDF&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" onmousedown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.swd.gov.hk%2Fdoc_sc%2Frehab%2Fvrs%2FHIT%2520letter%252020042016.PDF&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" id="waSearchResultTitle9" href="http://www.swd.gov.hk/doc_sc/rehab/vrs/HIT%20letter%2020042016.PDF">
		                      <span>HIT letter 20042016.PDF</span>
		                    </a>
		                   </h3>
		                  <p>
		                  	<span class="itemDetailsDescription">氣流通情況欠佳的公眾地方；

和●
最少每日一次用適當的消<strong>毒</strong>劑清潔及消<strong>毒</strong>經常接觸的表面、傢佩物

<strong>品</strong>、玩具、共用物<strong>品</strong>和地面（非金屬表面可把1份</span>
		                  </p>
		
		                  <!--/p-->
		                  <p>
		                    <!-- Last Modified Date: 2011-11-09 -->
		                    <span class="itemDetailsLink">www.swd.gov.hk/doc_sc/rehab/vrs/HIT%20letter%2020042016.PDF</span>
		                    - 
		                    <span>168.8K</span>
		                    <span> - </span>
		                    <span>22/07/2016</span>
		                    <span> - </span>
		                    <!--/p-->
		                    <!-- Add cache here -->
		                    <a class="moreFromThisSiteLink" href="http://lp.search.gov.hk:8080/Action=View&amp;NoACI=true&amp;reference=http%3A%2F%2Fwww.swd.gov.hk%2Fdoc_sc%2Frehab%2Fvrs%2FHIT%2520letter%252020042016.PDF" onkeydown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);" onmousedown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);">
		                    <span>页库存档</span></a>
		                  </p>
		                 </li>
		
		                <li>
		                  <h3>
		                  	<span class="searchResultType">[PDF]</span>
		                    <a class="itemDetailsTitle" onkeydown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.swd.gov.hk%2Fdoc%2Frehab%2Fvrs%2FHIT%2520letter%252011032016.PDF&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" onmousedown="clickCount(&#39;searchResult&#39;, &#39;http%3A%2F%2Fwww.swd.gov.hk%2Fdoc%2Frehab%2Fvrs%2FHIT%2520letter%252011032016.PDF&#39;, &#39;%E6%AF%92%E5%93%81&#39;);" id="waSearchResultTitle10" href="http://www.swd.gov.hk/doc/rehab/vrs/HIT%20letter%2011032016.PDF">
		                      <span>HIT letter 11032016.PDF</span>
		                    </a>
		                   </h3>
		                  <p>
		                  	<span class="itemDetailsDescription">護膚<strong>品</strong>；

依照指示重複使用昆蟲驅避劑。

出外旅遊須知

外遊人士尤其是有免疫系統疾病或長期病患者...</span>
		                  </p>
		
		                  <!--/p-->
		                  <p>
		                    <!-- Last Modified Date: 2011-11-09 -->
		                    <span class="itemDetailsLink">www.swd.gov.hk/doc/rehab/vrs/HIT%20letter%2011032016.PDF</span>
		                    - 
		                    <span>259.6K</span>
		                    <span> - </span>
		                    <span>22/07/2016</span>
		                    <span> - </span>
		                    <!--/p-->
		                    <!-- Add cache here -->
		                    <a class="moreFromThisSiteLink" href="http://lp.search.gov.hk:8080/Action=View&amp;NoACI=true&amp;reference=http%3A%2F%2Fwww.swd.gov.hk%2Fdoc%2Frehab%2Fvrs%2FHIT%2520letter%252011032016.PDF" onkeydown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);" onmousedown="clickCount(&#39;cacheUrl Onclick&#39;, &#39;&#39;, &#39;&#39;);">
		                    <span>页库存档</span></a>
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
				                   <label for="searchBox3" class="access">查询</label>
				                   <input type="text" class="searchBox ui-autocomplete-input" name="query" id="searchBox3" autocomplete="off" value="毒品" />
				                   <label for="searchIcon3" class="access">Search Submit</label>
				                   <input type="submit" title="Search" class="searchIcon2" id="searchIcon2" name="search_but" value="" />
				                   </div>
				                </div>
				             </div>
				             <div class="advSearch"><a href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-cn&amp;tpl_id=stdsearch&amp;page=1&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;a_submit=false&amp;toASubmit=true&amp;gp0=swd_home&amp;gp1=swd_home&amp;doc_type=all&amp;sort=date&amp;web=this&amp;txtonly=0&amp;site=swd_home&amp;exact_q=&amp;any_q=&amp;none_q=&amp;tab=&amp;tab_depts=">进阶搜寻</a></div>
				             <input type="hidden" name="output" value="xml_no_dtd" />
				             <input type="hidden" name="ui_lang" value="zh-cn" />
				             <input type="hidden" name="gp1" value="swd_home" />
				             <input type="hidden" name="gp0" value="swd_home" />
				             <input type="hidden" name="web" value="this" />
				             <input type="hidden" name="txtonly" value="0" />
				             <input type="hidden" name="tpl_id" value="stdsearch" />
				             <input type="hidden" name="sort" value="date" />
				             <input type="hidden" name="doc_type" value="all" />
				             
				             
							 
							 <div id="stdTplRadioButton" class="clearthis">
				             <fieldset><legend class="hidden">显示：</legend>
								<span>显示：</span>&nbsp;
								<input type="radio" id="yschtopsearch1all_ck_top_1" name="site" value="default_collection" />
								<label for="yschtopsearch1all_ck_top_1">所有政府网站</label>
								<input type="radio" id="yschtopsearch1this_ck_top_1" name="site" checked="checked" value="swd_home" />
								<label for="yschtopsearch1this_ck_top_1">社会福利署</label>
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
				        <a onclick="clickCount('paginationTool', '', '')" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-cn&amp;tpl_id=stdsearch&amp;page=2&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;a_submit=false&amp;gp0=swd_home&amp;gp1=swd_home&amp;doc_type=all&amp;web=this&amp;txtonly=0&amp;site=swd_home&amp;last_mod=%23-1&amp;tab=&amp;tab_depts=&amp;sort=date">
				        <span>2</span></a>
				        <span>&nbsp;-</span>
				      </span>
				    <span>
				        <strong></strong>
				        <a onclick="clickCount('paginationTool', '', '')" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-cn&amp;tpl_id=stdsearch&amp;page=3&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;a_submit=false&amp;gp0=swd_home&amp;gp1=swd_home&amp;doc_type=all&amp;web=this&amp;txtonly=0&amp;site=swd_home&amp;last_mod=%23-1&amp;tab=&amp;tab_depts=&amp;sort=date">
				        <span>3</span></a>
				        <span>&nbsp;-</span>
				      </span>
				    <span>
				        <strong></strong>
				        <a onclick="clickCount('paginationTool', '', '')" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-cn&amp;tpl_id=stdsearch&amp;page=4&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;a_submit=false&amp;gp0=swd_home&amp;gp1=swd_home&amp;doc_type=all&amp;web=this&amp;txtonly=0&amp;site=swd_home&amp;last_mod=%23-1&amp;tab=&amp;tab_depts=&amp;sort=date">
				        <span>4</span></a>
				        <span>&nbsp;-</span>
				      </span>
				    <span>
				        <strong></strong>
				        <a onclick="clickCount('paginationTool', '', '')" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-cn&amp;tpl_id=stdsearch&amp;page=5&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;a_submit=false&amp;gp0=swd_home&amp;gp1=swd_home&amp;doc_type=all&amp;web=this&amp;txtonly=0&amp;site=swd_home&amp;last_mod=%23-1&amp;tab=&amp;tab_depts=&amp;sort=date">
				        <span>5</span></a>
				        <span>&nbsp;-</span>
				      </span>
				    <span>
				        <strong></strong>
				        <a onclick="clickCount('paginationTool', '', '')" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-cn&amp;tpl_id=stdsearch&amp;page=6&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;a_submit=false&amp;gp0=swd_home&amp;gp1=swd_home&amp;doc_type=all&amp;web=this&amp;txtonly=0&amp;site=swd_home&amp;last_mod=%23-1&amp;tab=&amp;tab_depts=&amp;sort=date">
				        <span>6</span></a>
				        <span>&nbsp;-</span>
				      </span>
				    <span>
				        <strong></strong>
				        <a onclick="clickCount('paginationTool', '', '')" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-cn&amp;tpl_id=stdsearch&amp;page=7&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;a_submit=false&amp;gp0=swd_home&amp;gp1=swd_home&amp;doc_type=all&amp;web=this&amp;txtonly=0&amp;site=swd_home&amp;last_mod=%23-1&amp;tab=&amp;tab_depts=&amp;sort=date">
				        <span>7</span></a>
				        <span>&nbsp;-</span>
				      </span>
				    <span>
				        <strong></strong>
				        <a onclick="clickCount('paginationTool', '', '')" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-cn&amp;tpl_id=stdsearch&amp;page=8&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;a_submit=false&amp;gp0=swd_home&amp;gp1=swd_home&amp;doc_type=all&amp;web=this&amp;txtonly=0&amp;site=swd_home&amp;last_mod=%23-1&amp;tab=&amp;tab_depts=&amp;sort=date">
				        <span>8</span></a>
				        <span>&nbsp;-</span>
				      </span>
				    <span>
				        <strong></strong>
				        <a onclick="clickCount('paginationTool', '', '')" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-cn&amp;tpl_id=stdsearch&amp;page=9&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;a_submit=false&amp;gp0=swd_home&amp;gp1=swd_home&amp;doc_type=all&amp;web=this&amp;txtonly=0&amp;site=swd_home&amp;last_mod=%23-1&amp;tab=&amp;tab_depts=&amp;sort=date">
				        <span>9</span></a>
				        <span>&nbsp;-</span>
				      </span>
				    <span>
				        <strong></strong>
				        <a onclick="clickCount('paginationTool', '', '')" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-cn&amp;tpl_id=stdsearch&amp;page=10&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;a_submit=false&amp;gp0=swd_home&amp;gp1=swd_home&amp;doc_type=all&amp;web=this&amp;txtonly=0&amp;site=swd_home&amp;last_mod=%23-1&amp;tab=&amp;tab_depts=&amp;sort=date">
				        <span>10</span></a>
				        
				      </span>
					<span class="b">
					  <a onclick="clickCount('paginationTool', '', '')" class="next" href="?query=%E6%AF%92%E5%93%81&amp;ui_lang=zh-cn&amp;tpl_id=stdsearch&amp;page=2&amp;p_size=10&amp;output=xml_no_dtd&amp;ui_charset=utf-8&amp;a_submit=false&amp;gp0=swd_home&amp;gp1=swd_home&amp;doc_type=all&amp;web=this&amp;txtonly=0&amp;site=swd_home&amp;last_mod=%23-1&amp;tab=&amp;tab_depts=&amp;sort=date" title="下一页">下一页</a>
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
          <li><a title="About Us" href="http://www.gov.hk/sc/about/aboutus.htm">关于我们</a></li>
          <li><a title="Accessibility" href="http://www.gov.hk/sc/about/accessibility/">无障碍浏览</a></li>
          <li><a title="Linking to GovHK" href="http://www.gov.hk/sc/about/linkpolicy/">连结到香港政府一站通</a></li>
          <li><a title="Site Map" href="http://www.gov.hk/sc/about/sitemap.htm">网页指南</a></li>
          <li class="shortFooter"><a title="Site Map" href="http://www.gov.hk/sc/about/helpdesk/">帮助</a></li>
          <li><a title="Copyright Notice" href="http://www.gov.hk/sc/about/copyright.htm">版权告示</a></li>
          <li><a title="Privacy Policy" href="http://www.gov.hk/sc/about/privacy.htm">私隐政策</a></li>
          <li><a title="Disclaimer" href="http://www.gov.hk/sc/about/disclaimer.htm">免责声明</a></li>
		</ul>
		<div id="brandhk"><a href="http://www.brandhk.gov.hk/" rel="external" title="Brand Hong Kong">
		<img alt="Brand Hong Kong" title="Brand Hong Kong" src="/search/gov_footer_brandhk_20100331_tc.gif" /></a>
		</div>
	</div>
	<div id="badges">
		<ul id="conformance">
			<li class="w3"><a href="http://www.w3.org/WAI/WCAG2AA-Conformance" rel="external" title="2A无障碍说明">
			<img src="http://www.gov.hk/images/footer/wcag2AA.gif" alt="符合萬維網聯盟有關無障礙網頁設計指引中2A級別的要求" /></a>
			</li>
			<li><a rel="external" href="http://www.webforall.gov.hk/sc/recognition_scheme" title="无障碍网页嘉许计划">
			<img src="http://www.gov.hk/sc/images/footer/gold_logo.png" alt="无障碍网页嘉许计划" /></a>
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

print '---------------------------------'
# 解析得到网页链接

founds = soup.find('div', class_='searchResultArea').find_all('li')
print len(founds)

item_list = []
print '------------url---------------'
id = 0
for found in founds:
    id += 1
    print id
    # item = items.PostItem()
    title = found.find('h3').get_text().strip()
    url = found.find('h3').find('a').get('href')
    print title
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

# next_pages = soup.find('div', class_ = 'advancedIndex').find_all('span')
# print len(next_pages)
next_pages = soup.find('div', class_ = 'advancedIndex').find_all('span')
# next_pages = soup.div.class_['yschindex'].find_all('span')
l = len(next_pages)
try:
    next_page = next_pages[l-1].a['href']
    next_page = 'http://lp.search.gov.hk/search.html' + next_page
    print next_page
except:
    print 'last page-----'
