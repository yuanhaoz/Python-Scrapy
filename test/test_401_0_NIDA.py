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
<html lang='en' xml:lang='en' xmlns='http://www.w3.org/1999/xhtml'>
<head>
<!-- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -->
<!--                                  Powered by DigitalGov Search                                   -->
<!-- helping government create a great search experience. Learn more at http://search.digitalgov.gov -->
<!-- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -->
<link href="http://www.drugabuse.gov/sites/all/themes/nida_vic_adaptive/favicon.ico" rel="shortcut icon" type="image/vnd.microsoft.icon" />
<meta content="NOINDEX, NOFOLLOW" name="ROBOTS" />
<link href="https://d15vqlr7iz6e8x.cloudfront.net/assets/searches-3c7c5daebef4ce78b3b6ca1aec5b7311.css" media="screen" rel="stylesheet" type="text/css" />
<style>
  .header-footer .header-wrapper{padding:0px 20px 0px 20px;background:#fff;border-radius:8px 8px 0px 0px}.header-footer .audience-menu-wrapper{float:right;font-family:Verdana,Helvetica,sans-serif;border-bottom:1px solid #d9d9d9;padding-bottom:6px;padding-top:6px}.header-footer ul.audience-menu{padding:0px;margin:0px}.header-footer .audience-menu li{display:inline;line-height:11px;list-style:none outside none;margin:0;padding:0px 0px 0px 0px}.header-footer .audience-menu li a{border-right:1px solid #d9d9d9;font-size:9px;line-height:14px;color:#004863;padding:0 5px 0 1px;font-size:11px;text-decoration:none}.header-footer .audience-menu li.last a{border-right:0px}.header-footer ul.sf-menu{margin:12px 0px 36px 0px;padding:0px 0px 0px 0px}.header-footer .clearfix:after{visibility:hidden;display:block;font-size:0;content:" ";clear:both;height:0}.header-footer ul.sf-menu li a{display:block;margin:0;text-decoration:none;padding:0;background:transparent;border:0;position:relative;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0}.header-footer ul.sf-menu>li{display:block;float:left;margin:0;padding:0;background:transparent;border:0;width:146px;text-align:center;position:relative;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0;overflow:hidden}.header-footer ul.sf-menu>li>a{color:#fff;font-family:Arial,Helvetica,sans-serif;background:url(http://www.drugabuse.gov/sites/all/themes/nida_vic_adaptive/images/collapsed_nav_bg.gif) repeat-x 100% 0;border-left:1px solid #398eb5;border-right:1px solid #013751;border-top:1px solid #398eb5;border-bottom:1px solid #024965;height:37px;line-height:37px;text-align:center;font-size:14px;padding:0px 0px;text-decoration:none;white-space:nowrap}.header-footer ul.sf-menu>li.first{width:44px}.header-footer ul.sf-menu>li.first>a{width:42px;padding:0px;background:url(http://www.drugabuse.gov/sites/all/themes/nida_vic_adaptive/images/collapsed_nav_home_bg.gif) 0 0 repeat-x #4194bc;text-indent:-9999px;-webkit-border-top-left-radius:6px;-webkit-border-bottom-left-radius:6px;-moz-border-radius-topleft:6px;-moz-border-radius-bottomleft:6px;border-top-left-radius:6px;border-bottom-left-radius:6px}.header-footer ul.sf-menu>li.last>a{-webkit-border-top-right-radius:6px;-webkit-border-bottom-right-radius:6px;-moz-border-radius-topright:6px;-moz-border-radius-bottomright:6px;border-top-right-radius:6px;border-bottom-right-radius:6px}.header-footer ul.sf-menu>li:hover>a{color:#004863;border-bottom:1px solid #004863;border-top:1px solid #004863;background:url(http://www.drugabuse.gov/sites/all/themes/nida_vic_adaptive/images/collapsed_nav_bg.gif) bottom left}.header-footer ul.sf-menu>li.first:hover>a{background:url(http://www.drugabuse.gov/sites/all/themes/nida_vic_adaptive/images/collapsed_nav_home_bg.gif) 0px -78px repeat-x #4194bc;border-bottom:1px solid #004863;border-left:1px solid #004863}
</style>
<style>
  #container{background-color:#fff}body.with-content-border #container,body.with-content-border #usasearch_footer{border:1px solid #cacaca}body.with-content-box-shadow #container{-moz-box-shadow:#555 0 0 5px;-webkit-box-shadow:#555 0 0 5px;-o-box-shadow:#555 0 0 5px;box-shadow:#555 0 0 5px}body.with-content-box-shadow #usasearch_footer{-moz-box-shadow:#555 0 1px 5px;-webkit-box-shadow:#555 0 1px 5px;-o-box-shadow:#555 0 1px 5px;box-shadow:#555 0 1px 5px}#header.managed,#usasearch_footer.managed{background-color:#fff;color:#095876}#header.managed a,#header.managed a:visited,#usasearch_footer.managed a,#usasearch_footer.managed a:visited{color:#095876}#search_button,#cdr_search_button{background-color:#095876;border:1px solid #095876;color:#fff}.navigations li div,.time-filters li div,.sort-filters li div{border-left-color:#a52200;color:#a52200}#left_column h3,#left_nav_label,#left_column .facet-name,#left_column .facet .selected{color:#a52200}.default .affiliate_autocomplete .ui-menu-item a,.default .affiliate_autocomplete .ui-menu-item span{font-family:"Maven Pro","Helvetica Neue",Helvetica,Arial,sans-serif}#search,#search_query{font-family:"Maven Pro","Helvetica Neue",Helvetica,Arial,sans-serif}#search,#serp-alert{color:#444}#search a,#serp-alert a{color:#095876}#search a:visited,#serp-alert a:visited{color:#095876}#search #left_column a:visited,#search #left_column #show_options,#search #left_column #hide_options,#search #left_column .more-facets,#search #left_column .less-facets,#serp-alert #left_column a:visited,#serp-alert #left_column #show_options,#serp-alert #left_column #hide_options,#serp-alert #left_column .more-facets,#serp-alert #left_column .less-facets{color:#095876}#search #left_column .triangle.show-options,#serp-alert #left_column .triangle.show-options{border-top-color:#095876}#search #left_column .triangle.hide-options,#serp-alert #left_column .triangle.hide-options{border-bottom-color:#095876}#skiplink a,#skiplink a:visited,#results .time-filters a,#results .time-filters a:visited,#results .sort-filters a,#results .sort-filters a:visited{color:#095876}#skiplink a.selected,#skiplink a:visited.selected,#results .time-filters a.selected,#results .time-filters a:visited.selected,#results .sort-filters a.selected,#results .sort-filters a:visited.selected{color:#a52200}#results .current-time-filter,#results .current-sort-filter,#results .clear-filter a{color:#a52200}#results .current-time-filter .triangle.show-options,#results .current-sort-filter .triangle.show-options,#results .clear-filter a .triangle.show-options{border-top-color:#a52200}#results .current-time-filter .triangle.hide-options,#results .current-sort-filter .triangle.hide-options,#results .clear-filter a .triangle.hide-options{border-bottom-color:#a52200}#results .searchresult .agency h3,#results .searchresult .agency .official-tag,#results .searchresult .agency .date-label,#results .searchresult .medline h3,#results .searchresult .medline .official-tag,#results .searchresult .medline .date-label,#results .searchresult #form_govbox h3,#results .searchresult #form_govbox .official-tag,#results .searchresult #form_govbox .date-label{color:#a52200}#results .searchresult h3 a,#results .searchresult h4 .feed-name,#results .searchresult h3.result-url{color:#a52200}#results .govbox h3.alt,#results .govbox h3.alt a{color:#a52200}#results .featured-collection h2,#results .featured-collection h2 a{color:#a52200}#results #form_govbox .check-mark{background-color:#095876;border-color:#095876}#results .pagination a,#results .pagination a:visited{color:#095876}#results .pagination a:hover,#results .pagination em{background-color:#095876;color:#fff}#twitter_govbox h3.alt,#jobs_govbox h3.alt{color:#a52200}#search .page-not-found h3.message{color:#a52200}#search form.advanced legend{color:#444}#usasearch_footer_container{background-color:#027095}#usasearch_footer_container #usasearch_footer{background-color:#fff}#usasearch_footer_container #usasearch_footer_button{color:#fff;background-color:#095876}
</style>
<!--[if IE 7]>
<link href="https://d15vqlr7iz6e8x.cloudfront.net/assets/searches_ie7-944486aa71d996e769fcf3bb6edd136f.css" media="screen" rel="stylesheet" type="text/css" />
<![endif]-->

<title>China - Drugabuse.gov Search Results</title>
</head>
<body class='one-serp default en with-content-border with-content-box-shadow' style='background-color: #027095'>
<div id='skiplink'>
<a href='#main_content'>Skip to Main Content</a>
</div>
<div id='container'>
<div class="header-footer" id="header"><div class="header-wrapper-outer">
<div class="header-wrapper">
<div class="audience-menu-wrapper">
<ul class="audience-menu">
<li class="first">
<a href="http://www.drugabuse.gov/researchers">Researchers</a>
</li>
<li>
<a href="http://www.drugabuse.gov/nidamed-medical-health-professionals">Medical &amp; Health Professionals</a>
</li>
<li>
<a href="http://www.drugabuse.gov/patients-families">Patients &amp; Families</a>
</li>
<li>
<a href="http://www.drugabuse.gov/parents-teachers">Parents &amp; Teachers</a>
</li>
<li class="last">
<a href="http://www.drugabuse.gov/students-young-adults">Students &amp; Young Adults</a>
</li>
</ul>
</div>

<div class="region-inner region-logo-bar-left-inner">
<a href="http://www.drugabuse.gov" title=""><img src="http://www.drugabuse.gov/sites/all/themes/nida_vic_adaptive/images/nih-nida-logo.gif" alt="NIDA"></a>
</div>

<div class="main-menu">
<ul class="sf-menu clearfix">
<li class="first"><a href="http://www.drugabuse.gov">Home</a></li>
<li><a href="http://www.drugabuse.gov/drugs-abuse">Drugs of Abuse</a></li>
<li><a href="http://www.drugabuse.gov/related-topics">Related Topics</a></li>
<li><a href="http://www.drugabuse.gov/publications">Publications</a></li>
<li><a href="http://www.drugabuse.gov/funding">Funding</a></li>
<li><a href="http://www.drugabuse.gov/news-events">News &amp; Events</a></li>
<li class="last"><a href="http://www.drugabuse.gov/about-nida">About NIDA</a></li>
</ul>
</div>

</div>
</div></div>
<div id='search'>
<h1>Search</h1>
<div id='search_box'>
<form accept-charset="UTF-8" action="/search" id="search_form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
<label class="hide" for="search_query">Enter your search term</label>
<input id="sc" name="sc" type="hidden" value="0" />
<input autocomplete="off" class="usagov-search-autocomplete" id="search_query" maxlength="255" name="query" size="49" type="text" value="China" />
<input id="m" name="m" type="hidden" value="" />

<input id="affiliate" name="affiliate" type="hidden" value="www.drugabuse.gov" />



<input id="search_button" name="commit" type="submit" value="Search" />
</form>


<div class='left-nav-label-wrapper'>&nbsp;</div>
<div class='summary-wrapper'>

<div id="summary"><p>Page 2 of about 241 results</p></div>&nbsp;&nbsp;&bull;&nbsp;&nbsp;
<div class='advancedsearch'>
<a href="/search/advanced?affiliate=www.drugabuse.gov&amp;enable_highlighting=true&amp;page=2&amp;per_page=20&amp;query=China" id="advanced_search_link">Advanced Search</a>
</div>
</div>
</div>
<div id='left_column'>
<script type="text/javascript">
//<![CDATA[
var original_query = "China";
//]]>
</script>
<ul class="navigations"><li><div>Everything</div></li>
<li><a href="/search/images?affiliate=www.drugabuse.gov&amp;query=China" class="updatable">Images</a></li></ul>

</div>
<div id='main_content' name='main_content'></div>
<div id='results'>
<div class='searchresult' id='searchresult21'>
<h2>

<a href="https://www.drugabuse.gov/international/in-womens-2016-conference-set-friday-june-10-2016" onmousedown="return clk('China',this.href, 21, 'www.drugabuse.gov', 'BWEB', 1471960073, 'web', 'en', '')" >NIDA International: In Women’s 2016 Conference Set for ...</a>
</h2>
<h3 class='result-url'>https://www.drugabuse.gov/international/in-womens-2016-conference-set-friday-june-10-2016</h3>
<h3>In Women’s 2016 Conference Set for Friday, June 10, 2016. La Quinta Hotel, Palm Springs, California. For more ...</h3>
</div>

<div class='searchresult' id='searchresult22'>
<h2>

<a href="https://www.drugabuse.gov/international/abstracts/methamphetamine-use-among-hiv-negative-drug-users-in-methadone-maintenance-therapy-clinics-in-yunnan" onmousedown="return clk('China',this.href, 22, 'www.drugabuse.gov', 'BWEB', 1471960073, 'web', 'en', '')" >Methamphetamine Use Among HIV-Negative Drug Users in ...</a>
</h2>
<h3 class='result-url'>https://www.drugabuse.gov/international/abstracts/methamphetamine-use-among-hiv-negative-drug-users-in-methadone-maintenance-therapy-clinics-in-yunnan</h3>
<h3>Methamphetamine Use Among HIV-Negative Drug Users in Methadone Maintenance Therapy Clinics in Yunnan, <strong>China</strong></h3>
</div>

<div class='searchresult' id='searchresult23'>
<h2>

<a href="https://www.drugabuse.gov/international/abstracts/performance-lay-outreach-workers-in-needle-exchange-program-in-china" onmousedown="return clk('China',this.href, 23, 'www.drugabuse.gov', 'BWEB', 1471960073, 'web', 'en', '')" >Performance of lay outreach workers in a needle exchange ...</a>
</h2>
<h3 class='result-url'>https://www.drugabuse.gov/international/abstracts/performance-lay-outreach-workers-in-needle-exchange-program-in-china</h3>
<h3>Performance of lay outreach workers in a needle exchange program in <strong>China</strong>. Wenjun Liu. W. Liu 1,2, H. Li 3, L. Duo 4, Z. Luo 2 ...</h3>
</div>

<div class='searchresult' id='searchresult24'>
<h2>

<a href="https://www.drugabuse.gov/international/abstracts/pilot-study-relapse-prevention-intervention-heroin-addicts-in-prison-in-china" onmousedown="return clk('China',this.href, 24, 'www.drugabuse.gov', 'BWEB', 1471960073, 'web', 'en', '')" >A Pilot Study of Relapse Prevention Intervention for ...</a>
</h2>
<h3 class='result-url'>https://www.drugabuse.gov/international/abstracts/pilot-study-relapse-prevention-intervention-heroin-addicts-in-prison-in-china</h3>
<h3>Conclusion: An RP intervention seems feasible and effective for heroin addicts in prison in <strong>China</strong>. It might be necessary for more study to further ...</h3>
</div>

<div class='searchresult' id='searchresult25'>
<h2>

<a href="https://www.drugabuse.gov/international/abstracts/tetrahydrocannabinol-effect-sivmac251-infection-in-chinese-macaques" onmousedown="return clk('China',this.href, 25, 'www.drugabuse.gov', 'BWEB', 1471960073, 'web', 'en', '')" >Tetrahydrocannabinol effect on SIVmac251 infection in ...</a>
</h2>
<h3 class='result-url'>https://www.drugabuse.gov/international/abstracts/tetrahydrocannabinol-effect-sivmac251-infection-in-chinese-macaques</h3>
<h3>Z. Chen 1,2,3. 1 AIDS Institute Shenzhen Laboratory of Li Ka Shing Faculty of Medicine, The University of Hong Kong, <strong>China</strong>; 2 Institute of Laboratory ...</h3>
</div>

<div class='searchresult' id='searchresult26'>
<h2>

<a href="https://www.drugabuse.gov/international/abstracts/comparison-injection-drug-users-in-shanghai-china-miami-florida" onmousedown="return clk('China',this.href, 26, 'www.drugabuse.gov', 'BWEB', 1471960073, 'web', 'en', '')" >Comparison of Injection Drug Users in Shanghai, <strong>China</strong>, and ...</a>
</h2>
<h3 class='result-url'>https://www.drugabuse.gov/international/abstracts/comparison-injection-drug-users-in-shanghai-china-miami-florida</h3>
<h3>Clyde B. McCoy 1, M. Zhao 2, M. Comerford 1. 1 University of Miami, United States; 2 Shanghai Jiao Tong University School of Medicine, <strong>China</strong>. ...</h3>
</div>

<div class='searchresult' id='searchresult27'>
<h2>

<a href="https://www.drugabuse.gov/international/abstracts/effects-randomized-comprehensive-psychosocial-intervention-heroin-dependence-in-community-in" onmousedown="return clk('China',this.href, 27, 'www.drugabuse.gov', 'BWEB', 1471960073, 'web', 'en', '')" >Effects of a randomized comprehensive psychosocial ...</a>
</h2>
<h3 class='result-url'>https://www.drugabuse.gov/international/abstracts/effects-randomized-comprehensive-psychosocial-intervention-heroin-dependence-in-community-in</h3>
<h3>Effects of a randomized comprehensive psychosocial intervention for heroin dependence in a community in Shanghai, <strong>China</strong></h3>
</div>

<div class='searchresult' id='searchresult28'>
<h2>

<a href="https://www.drugabuse.gov/international/abstracts/association-between-personality-smoking-behaviors-in-chinese-adult-male-smokers" onmousedown="return clk('China',this.href, 28, 'www.drugabuse.gov', 'BWEB', 1471960073, 'web', 'en', '')" >Association Between Personality and Smoking Behaviors in ...</a>
</h2>
<h3 class='result-url'>https://www.drugabuse.gov/international/abstracts/association-between-personality-smoking-behaviors-in-chinese-adult-male-smokers</h3>
<h3>L. Zhang, C. Chu, Sichuan University, <strong>China</strong>. To examine the relationship between personality traits and smoking behaviors in male smokers in <strong>China</strong>, a ...</h3>
</div>

<div class='searchresult' id='searchresult29'>
<h2>

<a href="https://www.drugabuse.gov/drugs-abuse/heroin" onmousedown="return clk('China',this.href, 29, 'www.drugabuse.gov', 'BWEB', 1471960073, 'web', 'en', '')" >Heroin | National Institute on Drug Abuse (NIDA)</a>
</h2>
<h3 class='result-url'>https://www.drugabuse.gov/drugs-abuse/heroin</h3>
<h3>Brief Description Heroin is an opioid drug that is synthesized from morphine, a naturally occurring substance extracted from the seed pod of the Asian ...</h3>
</div>

<div class='searchresult' id='searchresult30'>
<h2>

<a href="https://www.drugabuse.gov/publications/drugfacts/anabolic-steroids" onmousedown="return clk('China',this.href, 30, 'www.drugabuse.gov', 'BWEB', 1471960073, 'web', 'en', '')" >DrugFacts: Anabolic Steroids | National Institute on Drug ...</a>
</h2>
<h3 class='result-url'>https://www.drugabuse.gov/publications/drugfacts/anabolic-steroids</h3>
<h3>How do anabolic steroids affect the brain? Anabolic steroids work differently from other drugs of abuse; they do not have the same short-term effects ...</h3>
</div>

<div class='searchresult' id='searchresult31'>
<h2>

<a href="https://www.drugabuse.gov/international/abstracts/characteristics-heroin-users-in-methadone-maintenance-treatment-clinics-in-wuhan-china" onmousedown="return clk('China',this.href, 31, 'www.drugabuse.gov', 'BWEB', 1471960073, 'web', 'en', '')" >Characteristics of Heroin Users in Methadone Maintenance ...</a>
</h2>
<h3 class='result-url'>https://www.drugabuse.gov/international/abstracts/characteristics-heroin-users-in-methadone-maintenance-treatment-clinics-in-wuhan-china</h3>
<h3>Zhou, Wang; Liu, P.; Luo, L.; Schottenfeld, R.S.; Chawarski, M.C. Division of HIV/AIDS Prevention, Wuhan Center for Disease Control and Prevention, <strong>Ch</strong> ...</h3>
</div>

<div class='searchresult' id='searchresult32'>
<h2>

<a href="https://www.drugabuse.gov/international/abstracts/patterns-adolescent-betel-nut-chewing-later-drug-use-in-adults" onmousedown="return clk('China',this.href, 32, 'www.drugabuse.gov', 'BWEB', 1471960073, 'web', 'en', '')" >Patterns of adolescent betel nut chewing and later drug ...</a>
</h2>
<h3 class='result-url'>https://www.drugabuse.gov/international/abstracts/patterns-adolescent-betel-nut-chewing-later-drug-use-in-adults</h3>
<h3>Y.C. Lan 1,2, Y.I. Hser 3, Y.K. Ho 2, W.Y. Tsay 4, J. Hsu 4, J.J. Kang 4. 1 Department of Health Risk Management, School of Management, <strong>China</strong> Medical ...</h3>
</div>

<div class='searchresult' id='searchresult33'>
<h2>

<a href="https://www.drugabuse.gov/international/abstracts/harm-reduction-in-china-literature-analysis" onmousedown="return clk('China',this.href, 33, 'www.drugabuse.gov', 'BWEB', 1471960073, 'web', 'en', '')" >Harm reduction in <strong>China</strong>: Literature Analysis | National ...</a>
</h2>
<h3 class='result-url'>https://www.drugabuse.gov/international/abstracts/harm-reduction-in-china-literature-analysis</h3>
<h3>Harm reduction in <strong>China</strong>: Literature Analysis . Chengzheng Zhao. Zhao, Chengzheng; Haifeng Zhai; Yanhong Liu; Dong Zhao; Lan Zeng; Yuquan An; Zhimin ...</h3>
</div>

<div class='searchresult' id='searchresult34'>
<h2>

<a href="https://www.drugabuse.gov/international/abstracts/psychosocial-context-tobacco-use-among-secondary-school-students-in-china" onmousedown="return clk('China',this.href, 34, 'www.drugabuse.gov', 'BWEB', 1471960073, 'web', 'en', '')" >Psychosocial Context Of Tobacco Use Among Secondary School ...</a>
</h2>
<h3 class='result-url'>https://www.drugabuse.gov/international/abstracts/psychosocial-context-tobacco-use-among-secondary-school-students-in-china</h3>
<h3>Psychosocial Context Of Tobacco Use Among Secondary School Students In <strong>China</strong>. Qun Zhao. Qun Zhao 1, Xiaoming Li 2, Lingran Zhong 1 ...</h3>
</div>

<div class='searchresult' id='searchresult35'>
<h2>

<a href="https://www.drugabuse.gov/international/abstracts/short-term-safety-buprenorphine-naloxone-in-hiv-seronegative-opioid-dependent-chinese-thai-drug" onmousedown="return clk('China',this.href, 35, 'www.drugabuse.gov', 'BWEB', 1471960073, 'web', 'en', '')" >Short-Term Safety of Buprenorphine/ Naloxone in HIV ...</a>
</h2>
<h3 class='result-url'>https://www.drugabuse.gov/international/abstracts/short-term-safety-buprenorphine-naloxone-in-hiv-seronegative-opioid-dependent-chinese-thai-drug</h3>
<h3>Short-Term Safety of Buprenorphine/ Naloxone in HIV-Seronegative Opioid- Dependent Chinese and Thai Drug Injectors ... (50 each at two sites in <strong>China</strong> ...</h3>
</div>

<div class='searchresult' id='searchresult36'>
<h2>

<a href="https://www.drugabuse.gov/international/abstracts/catechol-o-methyltransferase-gene-variants-are-associated-novelty-seeking-self-directiveness-in" onmousedown="return clk('China',this.href, 36, 'www.drugabuse.gov', 'BWEB', 1471960073, 'web', 'en', '')" >Catechol-O-Methyltransferase Gene Variants Are Associated ...</a>
</h2>
<h3 class='result-url'>https://www.drugabuse.gov/international/abstracts/catechol-o-methyltransferase-gene-variants-are-associated-novelty-seeking-self-directiveness-in</h3>
<h3>Catechol-O-Methyltransferase Gene Variants Are Associated With Novelty Seeking and Self-Directiveness in Chinese Heroin-Dependent Patients</h3>
</div>

<div class='searchresult' id='searchresult37'>
<h2>

<a href="https://www.drugabuse.gov/international/abstracts/linking-heroin-users-in-china-to-drug-treatment-other-resources-in-community-direct-indirect-effect" onmousedown="return clk('China',this.href, 37, 'www.drugabuse.gov', 'BWEB', 1471960073, 'web', 'en', '')" >Linking heroin users in <strong>China</strong> to drug treatment and other ...</a>
</h2>
<h3 class='result-url'>https://www.drugabuse.gov/international/abstracts/linking-heroin-users-in-china-to-drug-treatment-other-resources-in-community-direct-indirect-effect</h3>
<h3>Linking heroin users in <strong>China</strong> to drug treatment and other resources in the community: Direct and indirect effect of a recovery management intervention</h3>
</div>

<div class='searchresult' id='searchresult38'>
<h2>

<a href="https://www.drugabuse.gov/international/abstracts/contextualizing-drug-use-in-china-gender-differences-in-family-relationship-social-network-among" onmousedown="return clk('China',this.href, 38, 'www.drugabuse.gov', 'BWEB', 1471960073, 'web', 'en', '')" >Contextualizing Drug Use in <strong>China</strong>: Gender Differences in ...</a>
</h2>
<h3 class='result-url'>https://www.drugabuse.gov/international/abstracts/contextualizing-drug-use-in-china-gender-differences-in-family-relationship-social-network-among</h3>
<h3>Contextualizing Drug Use in <strong>China</strong>: Gender Differences in Family Relationship and Social Network Among Drug Users</h3>
</div>

<div class='searchresult' id='searchresult39'>
<h2>

<a href="https://www.drugabuse.gov/international/abstracts/risk-factors-hiv-infection-among-drug-users-in-beijing-china" onmousedown="return clk('China',this.href, 39, 'www.drugabuse.gov', 'BWEB', 1471960073, 'web', 'en', '')" >Risk Factors for HIV Infection Among Drug Users in Beijing ...</a>
</h2>
<h3 class='result-url'>https://www.drugabuse.gov/international/abstracts/risk-factors-hiv-infection-among-drug-users-in-beijing-china</h3>
<h3>Home » NIDA International Home » Abstract Database » Risk Factors for HIV Infection Among Drug Users in Beijing, <strong>China</strong> .</h3>
</div>

<div class='searchresult' id='searchresult40'>
<h2>

<a href="https://www.drugabuse.gov/international/abstracts/evaluation-peer-education-programs-among-injection-drug-users-idus" onmousedown="return clk('China',this.href, 40, 'www.drugabuse.gov', 'BWEB', 1471960073, 'web', 'en', '')" >Evaluation of Peer Education Programs among Injection Drug ...</a>
</h2>
<h3 class='result-url'>https://www.drugabuse.gov/international/abstracts/evaluation-peer-education-programs-among-injection-drug-users-idus</h3>
<h3>H. Chen, F. Cheng, et al Chinese Center for Disease Control and Prevention Beijing, <strong>China</strong>/ <strong>China</strong>-UK HIV/AIDS Prevention and Care Project, Beijing, <strong>Chi</strong> ...</h3>
</div>


<div class='pagination-and-logo'>
<div class="pagination" id="usasearch_pagination"><a class="previous_page" rel="prev start" href="/search?affiliate=www.drugabuse.gov&amp;commit=Search&amp;m=&amp;page=1&amp;query=China&amp;sc=0&amp;utf8=%E2%9C%93">Previous</a> <a rel="prev start" href="/search?affiliate=www.drugabuse.gov&amp;commit=Search&amp;m=&amp;page=1&amp;query=China&amp;sc=0&amp;utf8=%E2%9C%93">1</a> <em class="current">2</em> <a rel="next" href="/search?affiliate=www.drugabuse.gov&amp;commit=Search&amp;m=&amp;page=3&amp;query=China&amp;sc=0&amp;utf8=%E2%9C%93">3</a> <a href="/search?affiliate=www.drugabuse.gov&amp;commit=Search&amp;m=&amp;page=4&amp;query=China&amp;sc=0&amp;utf8=%E2%9C%93">4</a> <a href="/search?affiliate=www.drugabuse.gov&amp;commit=Search&amp;m=&amp;page=5&amp;query=China&amp;sc=0&amp;utf8=%E2%9C%93">5</a> <a href="/search?affiliate=www.drugabuse.gov&amp;commit=Search&amp;m=&amp;page=6&amp;query=China&amp;sc=0&amp;utf8=%E2%9C%93">6</a> <a href="/search?affiliate=www.drugabuse.gov&amp;commit=Search&amp;m=&amp;page=7&amp;query=China&amp;sc=0&amp;utf8=%E2%9C%93">7</a> <a href="/search?affiliate=www.drugabuse.gov&amp;commit=Search&amp;m=&amp;page=8&amp;query=China&amp;sc=0&amp;utf8=%E2%9C%93">8</a> <a href="/search?affiliate=www.drugabuse.gov&amp;commit=Search&amp;m=&amp;page=9&amp;query=China&amp;sc=0&amp;utf8=%E2%9C%93">9</a> <span class="gap">&hellip;</span> <a href="/search?affiliate=www.drugabuse.gov&amp;commit=Search&amp;m=&amp;page=12&amp;query=China&amp;sc=0&amp;utf8=%E2%9C%93">12</a> <a href="/search?affiliate=www.drugabuse.gov&amp;commit=Search&amp;m=&amp;page=13&amp;query=China&amp;sc=0&amp;utf8=%E2%9C%93">13</a> <a class="next_page" rel="next" href="/search?affiliate=www.drugabuse.gov&amp;commit=Search&amp;m=&amp;page=3&amp;query=China&amp;sc=0&amp;utf8=%E2%9C%93">Next</a></div>
<img alt="Results by Bing" class="results-by-logo bing" src="https://d15vqlr7iz6e8x.cloudfront.net/assets/searches/binglogo_en-bedf952d0c1978b8782cfb3aa1a87b4b.gif" />
</div>

</div>
<div id='right_column'>



</div>

</div>
<div id='usasearch_footer_container'>
<a id='usasearch_footer_button' title='Show footer'>&#9660;</a>

</div>
</div>
<script type="text/javascript">
//<![CDATA[
var usagov_sayt_url = "https://search.usa.gov/sayt?aid=3753&extras=true&";
//]]>
</script>
<script src="https://d15vqlr7iz6e8x.cloudfront.net/assets/searches-55066fe5c8fe8871aa0f01f9f6d4b7b7.js" type="text/javascript"></script>
<script>
  jQuery('#usasearch_footer_button').data('tooltip', { showText: 'Show footer', hideText: 'Hide footer' });
</script>
<script>
    //<![CDATA[
    (function() {
        var fa = document.createElement('script');
        fa.id = '_fed_an_ua_tag';
        fa.type = 'text/javascript';
        fa.async = true;
        fa.src = 'https://dap.digitalgov.gov/Universal-Federated-Analytics-Min.js?agency=GSA';
        document.getElementsByTagName('head')[0].appendChild(fa);
    })();
    //]]>
</script>


<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-16639817-1', 'auto');
  ga('send', 'pageview');

</script>

<!--
Tracking:

-->

</body>
</html>

"""


soup = BeautifulSoup(html_doc, "lxml")

print '---------------------------------'
# 解析得到网页链接

founds = soup.find('div', id='results').find_all('div', class_='searchresult')
print len(founds)

item_list = []
print '------------url---------------'
id = 0
for found in founds:
    id += 1
    print id
    # item = items.PostItem()
    title = found.find('h2').get_text().strip()
    url = found.find('h2').find('a').get('href')
    print title
    print url
    m = md5.new() 
    m.update(url)
    md_str = m.hexdigest()
    print md_str

    # post_time = found.find_all('p')[1].find_all('span')[3].get_text().strip()
    # # post_time = re.findall(self.tt_pa, post_time)[0]
    # post_time = post_time[6:] + '-' + post_time[3:5] + '-' + post_time[0:2] + ' ' + '00:00:00'
    # print post_time

print '-------------------------------'
#得到下一页链接，寻找最后一个span标签

next_pages = soup.find('div', id='usasearch_pagination').find('a', class_='next_page')
try:
    next_page = next_pages.get('href')
    next_page = 'https://search.usa.gov' + next_page
    print next_page
except:
    print 'last page-----'
