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

<!DOCTYPE html>

<!--[if lt IE 7]>  <html class="ie ie6 lte9 lte8 lte7 no-js" lang="en" dir="ltr"> <![endif]-->
<!--[if IE 7]>     <html class="ie ie7 lte9 lte8 lte7 no-js" lang="en" dir="ltr"> <![endif]-->
<!--[if IE 8]>     <html class="ie ie8 lte9 lte8 no-js" lang="en" dir="ltr"> <![endif]-->
<!--[if IE 9]>     <html class="ie ie9 lte9 no-js" lang="en" dir="ltr"> <![endif]-->
<!--[if gt IE 9]>  <html class="not-ie no-js" lang="en" dir="ltr"> <![endif]-->
<!--[if !IE]><!--> <html class="test not-ie no-js" lang="en" dir="ltr">  <!--<![endif]-->
<head>
<script>(function(H){H.className=H.className.replace(/\bno-js\b/,'js')})(document.documentElement)</script>
  	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, minimum-scale=1, user-scalable=no" />
<link rel="dns-prefetch" href="//d14rmgtrwzf5a.cloudfront.net" />
<meta http-equiv="x-dns-prefetch-control" content="on" />
<link rel="shortcut icon" href="https://www.drugabuse.gov/sites/all/themes/nida_vic_adaptive/favicon.ico" type="image/vnd.microsoft.icon" />
<meta name="description" content="Li, Zhoulin, HIV/AIDS Prevention and Control   Office of Ruili City, China; Liu, Wei, University of Illinois   at Chicago, United States" />
<meta name="abstract" content="Li, Zhoulin, HIV/AIDS Prevention and Control   Office of Ruili City, China; Liu, Wei, University of Illinois   at Chicago, United States" />
<meta name="generator" content="Drupal 7 (http://drupal.org)" />
<meta name="rights" content="Unless otherwise specified, NIDA publications and videos are available for your use and may be reproduced in their entirety without permission from NIDA. Citation of the source is appreciated, using the following language: Source: National Institute on Drug Abuse; National Institutes of Health; U.S. Department of Health and Human Services." />
<link rel="canonical" href="https://www.drugabuse.gov/international/abstracts/motivation-treatment-readiness-methadone-maintenance-treatment-in-ruili-china" />
<link rel="shortlink" href="https://www.drugabuse.gov/node/15855" />
<link rel="publisher" href="https://www.drugabuse.gov" />
<link rel="author" href="https://plus.google.com/+NIDANIH" />
<meta http-equiv="content-language" content="en" />
<meta property="og:type" content="article" />
<meta property="og:title" content="Motivation and Treatment Readiness for Methadone Maintenance Treatment in Ruili, China" />
<meta property="og:url" content="https://www.drugabuse.gov/international/abstracts/motivation-treatment-readiness-methadone-maintenance-treatment-in-ruili-china" />
<meta property="og:description" content="Li, Zhoulin, HIV/AIDS Prevention and Control   Office of Ruili City, China; Liu, Wei, University of Illinois   at Chicago, United States" />
<meta property="og:image" content="https://www.drugabuse.gov/sites/default/files/nih_nida_logo_socialmedia.png" />
<meta property="og:see_also" content="https://www.drugabuse.gov/frequently-asked-questions" />
<meta name="twitter:card" content="summary" />
<meta name="twitter:site" content="@NIDAnews" />
<meta name="twitter:site:id" content="102234123" />
<meta name="twitter:creator" content="@NIDAnews" />
<meta name="twitter:creator:id" content="102234123" />
<meta name="twitter:title" content="Motivation and Treatment Readiness for Methadone Maintenance Treatment in Ruili, China" />
<meta name="twitter:url" content="https://www.drugabuse.gov/international/abstracts/motivation-treatment-readiness-methadone-maintenance-treatment-in-ruili-china" />
<meta name="twitter:description" content="Li, Zhoulin, HIV/AIDS Prevention and Control   Office of Ruili City, China; Liu, Wei, University of Illinois   at Chicago, United States" />
<meta name="twitter:image:src" content="https://www.drugabuse.gov/sites/default/files/" />
<meta property="og:locale" content="en_US" />
<meta property="article:author" content="https://www.facebook.com/NIDANIH" />
<meta property="article:section" content="Nora&#039;s Blog" />
<meta itemprop="name" content="Motivation and Treatment Readiness for Methadone Maintenance Treatment in Ruili, China" />
<meta itemprop="description" content="Li, Zhoulin, HIV/AIDS Prevention and Control   Office of Ruili City, China; Liu, Wei, University of Illinois   at Chicago, United States" />
<meta itemprop="image" content="https://www.drugabuse.gov/sites/default/files/" />
  	<title>Motivation and Treatment Readiness for Methadone Maintenance Treatment in Ruili, China | National Institute on Drug Abuse (NIDA)</title>
    <meta name="author" content="National Institute on Drug Abuse">
  	<link type="text/css" rel="stylesheet" href="https://d14rmgtrwzf5a.cloudfront.net/sites/default/files/cdn/css/http/css_t0CTZXMj8-1OK0r59phUFywX7_4qnyUEuanIsCkmecs.css" media="all" />
<link type="text/css" rel="stylesheet" href="https://d14rmgtrwzf5a.cloudfront.net/sites/default/files/cdn/css/http/css_qQOkEe_jHFPAMUP12Qlcj71LDrI7iykGY4H8Au_fKI4.css" media="all" />
<link type="text/css" rel="stylesheet" href="https://d14rmgtrwzf5a.cloudfront.net/sites/default/files/cdn/css/http/css_gHe_YdqaV_KHbA-DfOTGzGVie4s_KWsAuZJkWSn1L74.css" media="all" />
<link type="text/css" rel="stylesheet" href="https://d14rmgtrwzf5a.cloudfront.net/sites/default/files/cdn/css/http/css_0lpmipkDdQj5hpEnmqWchrucpBEcj7Sy1EdYdPeHviw.css" media="all" />
<link type="text/css" rel="stylesheet" href="https://d14rmgtrwzf5a.cloudfront.net/sites/default/files/cdn/css/http/css_9m2-ntDsw5RH9s4g3InKUUM1olf7IhoJiAkciWEwY6o.css" media="print" />
<link type="text/css" rel="stylesheet" href="https://d14rmgtrwzf5a.cloudfront.net/sites/default/files/cdn/css/http/css_pYDviDDiGeJ3QFroApoepuXtAp6Nz42yzDpYcY7UD3c.css" media="all" />

<!--[if (lt IE 9)&(!IEMobile)]>
<link type="text/css" rel="stylesheet" href="https://d14rmgtrwzf5a.cloudfront.net/sites/default/files/cdn/css/http/css_GhtG4Ul0eJ3RkghPBS5SonbPg9xG1zg8W1ArRd-GvbI.css" media="all" />
<![endif]-->

<!--[if gte IE 9]><!-->
<link type="text/css" rel="stylesheet" href="https://d14rmgtrwzf5a.cloudfront.net/sites/default/files/cdn/css/http/css_LoIQ6OhDui47bhsocYu3Y7pdtIAGgeta_qyjtZKhjOE.css" media="all" />
<!--<![endif]-->
  	<!--[if lt IE 9]><script src="https://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
  <![endif]-->
	<link rel="apple-touch-icon" href="/sites/all/themes/nida_vic_adaptive/nida-icon.png"/>
  <script language="javascript" id="_fed_an_ua_tag" src="/sites/all/themes/nida_vic_adaptive/js/Universal-Federated-Analytics-Min.js?agency=HHS&subagency=NIDA&dclink=true&exts=pdf,doc,docx,xls,xlsx,epub,mp3"></script>
</head>
<body class="html not-front not-logged-in page-node page-node- page-node-15855 node-type-abstract i18n-en context-international nocolumn-active">
<!-- Google Tag Manager -->
<noscript><iframe src="//www.googletagmanager.com/ns.html?id=GTM-5B8TQK"
									height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
		new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
		j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
		'//www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
	})(window,document,'script','dataLayer','GTM-5B8TQK');</script>
<!-- End Google Tag Manager -->
  	<div id="skip-link">
    	<a href="#main-content" class="element-invisible element-focusable">Skip to main content</a>
  	</div>
  	<div id="language-switcher" class="container-24">
  		<a href="/es/inicio">En espa&ntilde;ol</a>  	</div>
  	  	<div class="page clearfix layout-columns-1" id="page">
<!--googleoff: index--> 
<!--googleoff: snippet-->
      <header id="section-header" class="section section-header">
  <div id="zone-top-bar-wrapper" class="zone-wrapper zone-top-bar-wrapper clearfix">  
  <div id="zone-top-bar" class="zone zone-top-bar clearfix container-24">
    <div class="grid-7 region region-top-bar-left" id="region-top-bar-left">
  	 <div class="region-inner region-top-bar-left-inner">
  	</div> 
</div><div class="grid-24 region region-top-bar-right" id="region-top-bar-right">
  <div class="region-inner region-top-bar-right-inner">
    <div class="block block-block block-68 block-block-68 odd block-without-title" id="block-block-68">
  <div class="block-inner clearfix">
                
    <div class="content clearfix">
      <ul class="menu" style="margin-left:-5px"><li class="first">
		<a href="/researchers">Researchers</a></li>
	<li>
		<a href="/nidamed-medical-health-professionals">Medical &amp; Health Professionals</a></li>
	<li>
		<a href="/patients-families">Patients &amp; Families</a></li>
	<li>
		<a href="/parents-educators">Parents &amp; Educators</a></li>
	<li class="last">
		<a href="/children-and-teens">Children &amp; Teens</a></li>
</ul>    </div>
  </div>
</div>  </div>
</div>  </div>
</div><div id="zone-logo-bar-wrapper" class="zone-wrapper zone-logo-bar-wrapper clearfix">  
  <div id="zone-logo-bar" class="zone zone-logo-bar clearfix container-24">
    <div class="grid-7 region region-logo-bar-left" id="region-logo-bar-left">
  	<div class="region-inner region-logo-bar-left-inner">
    	 		    <a href="/" title=""><img src="/sites/all/themes/nida_vic_adaptive/images/nih-nida-logo.gif" alt="NIDA" /></a>
		  	</div>
</div>
<!--googleoff: snippet-->
<!--googleoff: index-->
<div class="grid-17 region region-logo-bar-right" id="region-logo-bar-right">
  	<div class="region-inner region-logo-bar-right-inner">
    	<div class="block block-block nobar usasearch iq-search-block iq-bar-button-content iq-bar-button-search-form block-337 block-block-337 odd block-without-title" id="block-block-337">
  <div class="block-inner clearfix">
                
    <div class="content clearfix">
        <form accept-charset="UTF-8" action="https://search.usa.gov/search" id="search_form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>

    <input id="affiliate" name="affiliate" type="hidden" value="www.drugabuse.gov" />
<label class="stealth" for="query">Search</label>
    <input autocomplete="off" class="usagov-search-autocomplete  form-text" id="query" name="query" type="text" placeholder="enter keywords"  /><input name="commit" type="submit" value="Search"  class="form-submit"/></form>
<script type="text/javascript">
//<![CDATA[
      var usasearch_config = { siteHandle:"www.drugabuse.gov" };

      var script = document.createElement("script");
      script.type = "text/javascript";
      script.src = "https://search.usa.gov/javascripts/remote.loader.js";
      document.getElementsByTagName("head")[0].appendChild(script);

//]]>
</script>    </div>
  </div>
</div>    	<div class="clear"></div>
    	<div id="social_icons" class="clearfix">
            <span class="at_conn connect-with-nida"><a href="/connect-nida">Connect with NIDA</a>:</span> 
            <span itemscope itemtype="http://schema.org/Organization">
                <link itemprop="url" href="https://www.drugabuse.gov">
                <a itemprop="sameAs" class="googleplus social-sprite" href="https://plus.google.com/+NIDANIH/posts" target="_blank"><i class="fa fa-google-plus-square"></i><span class="hidden-text">Google Plus</span></a>
                <a itemprop="sameAs" class="facebook social-sprite" href="https://www.facebook.com/NIDANIH" target="_blank"><i class="fa fa-facebook-square"></i><span class="hidden-text">Facebook</span></a>
                <a itemprop="sameAs" class="linkedin social-sprite" href="https://www.linkedin.com/company/the-national-institute-on-drug-abuse-nida" target="_blank"><i class="fa fa-linkedin-square"></i><span class="hidden-text">LinkedIn</span></a>
                <a itemprop="sameAs" class="twitter social-sprite" href="https://twitter.com/NIDAnews" target="_blank"><i class="fa fa-twitter-square"></i><span class="hidden-text">Twitter</span></a>
                <a itemprop="sameAs" class="youtube social-sprite" href="https://www.youtube.com/user/NIDANIH" target="_blank"><i class="fa fa-youtube-square"></i><span class="hidden-text">YouTube</span></a> 
                <a itemprop="sameAs" class="flickr social-sprite" href="https://www.flickr.com/photos/nida-nih/collections/" target="_blank"><i class="fa fa-flickr"></i><span class="hidden-text">Flickr</span></a>
                <a itemprop="sameAs" class="rss social-sprite" href="/nidanews.xml"><i class="fa fa-rss-square"></i><span class="hidden-text">RSS</span></a>
            </span>
		</div>
  	</div>
</div>
<!--googleon: snippet-->
<!--googleon: index-->  </div>
</div><div id="zone-menu-wrapper" class="zone-wrapper zone-menu-wrapper clearfix">  
  <div id="zone-menu" class="zone zone-menu clearfix container-24">
    <div class="grid-24 region region-main-menu" id="region-main-menu">
  <div class="region-inner region-main-menu-inner">
    <div class="block block-block iq-mobile-overlay iq-hide-on-desktop block-446 block-block-446 odd block-without-title" id="block-block-446">
  <div class="block-inner clearfix">
                
    <div class="content clearfix">
      <div></div>    </div>
  </div>
</div><section class="block block-menu-block iq-clear-both iq-main-menu block-61 block-menu-block-61 even" id="block-menu-block-61">
  <div class="block-inner clearfix">
              <h2 class="block-title"><span>Menu</span></h2>
            
    <div class="content clearfix">
      <div class="menu-block-wrapper menu-block-61 menu-name-main-menu parent-mlid-0 menu-level-1">
  <ul class="menu"><li class="first collapsed menu-mlid-6060"><a href="/" title=""><i class="fa fa-home fa-lg"></i> <span class="visually-hidden-above-tablet">Home</span></a></li>
<li class="expanded menu-mlid-8560"><a href="/drugs-abuse">Drugs of Abuse</a><ul class="menu"><li class="first leaf menu-mlid-12027"><a href="/drugs-abuse/commonly-abused-drugs-charts">Commonly Abused Drugs Charts</a></li>
<li class="leaf menu-mlid-19522"><a href="/drugs-abuse/emerging-trends-alerts">Emerging Trends and Alerts</a></li>
<li class="leaf menu-mlid-10191"><a href="/drugs-abuse/alcohol">Alcohol</a></li>
<li class="leaf menu-mlid-2954"><a href="/drugs-abuse/club-drugs">Club Drugs</a></li>
<li class="leaf menu-mlid-2955"><a href="/drugs-abuse/cocaine">Cocaine</a></li>
<li class="leaf menu-mlid-2879"><a href="/drugs-abuse/hallucinogens">Hallucinogens</a></li>
<li class="leaf menu-mlid-2956"><a href="/drugs-abuse/heroin">Heroin</a></li>
<li class="leaf menu-mlid-2957"><a href="/drugs-abuse/inhalants">Inhalants</a></li>
<li class="leaf has-children menu-mlid-2874"><a href="/drugs-abuse/marijuana">Marijuana</a></li>
<li class="leaf menu-mlid-2875"><a href="/drugs-abuse/mdma-ecstasymolly">MDMA (Ecstasy/Molly)</a></li>
<li class="leaf menu-mlid-2876"><a href="/drugs-abuse/methamphetamine">Methamphetamine</a></li>
<li class="leaf has-children menu-mlid-24969"><a href="/drugs-abuse/opioids">Opioids</a></li>
<li class="leaf has-children menu-mlid-2987"><a href="/drugs-abuse/prescription-drugs-cold-medicines">Prescription Drugs & Cold Medicines</a></li>
<li class="leaf menu-mlid-2988"><a href="/drugs-abuse/steroids-anabolic">Steroids (Anabolic)</a></li>
<li class="leaf menu-mlid-22598"><a href="/drugs-abuse/synthetic-cannabinoids-k2spice">Synthetic Cannabinoids (K2/Spice)</a></li>
<li class="leaf menu-mlid-22600"><a href="/drugs-abuse/synthetic-cathinones-bath-salts">Synthetic Cathinones (Bath Salts)</a></li>
<li class="leaf has-children menu-mlid-2878"><a href="/drugs-abuse/tobacco-nicotine">Tobacco/Nicotine</a></li>
<li class="last leaf menu-mlid-25359"><a href="/drugs-abuse/other-drugs" title="">Other Drugs</a></li>
</ul></li>
<li class="expanded menu-mlid-3012"><a href="/related-topics">Related Topics</a><ul class="menu"><li class="first leaf has-children menu-mlid-2734"><a href="/related-topics/addiction-science">Addiction Science</a></li>
<li class="leaf has-children menu-mlid-24977"><a href="/related-topics/adolescent-brain">Adolescent Brain</a></li>
<li class="leaf menu-mlid-3089"><a href="/related-topics/comorbidity">Comorbidity</a></li>
<li class="leaf has-children menu-mlid-24077"><a href="/related-topics/college-age-young-adults">College-Age & Young Adults</a></li>
<li class="leaf has-children menu-mlid-2735"><a href="/related-topics/criminal-justice-drug-abuse">Criminal Justice</a></li>
<li class="leaf menu-mlid-2736"><a href="/related-topics/drugged-driving">Drugged Driving</a></li>
<li class="leaf has-children menu-mlid-3079"><a href="/related-topics/drug-testing">Drug Testing</a></li>
<li class="leaf menu-mlid-24474"><a href="/related-topics/drugs-brain">Drugs and the Brain</a></li>
<li class="leaf menu-mlid-25020"><a href="/related-topics/genetics">Genetics</a></li>
<li class="leaf menu-mlid-3080"><a href="/related-topics/global-health">Global Health</a></li>
<li class="leaf has-children menu-mlid-22757"><a href="/related-topics/viral-hepatitis-very-real-consequence-substance-use">Hepatitis (Viral)</a></li>
<li class="leaf menu-mlid-3082"><a href="/related-topics/hivaids">HIV/AIDS</a></li>
<li class="leaf menu-mlid-6034"><a href="/related-topics/medical-consequences-drug-abuse">Medical Consequences</a></li>
<li class="leaf menu-mlid-24038"><a href="/related-topics/mental-health">Mental Health</a></li>
<li class="leaf menu-mlid-22519"><a href="/related-topics/military">Military</a></li>
<li class="leaf menu-mlid-24112"><a href="/related-topics/pain">Pain</a></li>
<li class="leaf menu-mlid-3085"><a href="/related-topics/prevention">Prevention</a></li>
<li class="leaf has-children menu-mlid-3086"><a href="/related-topics/treatment">Treatment</a></li>
<li class="leaf has-children menu-mlid-3088"><a href="/related-topics/trends-statistics">Trends & Statistics</a></li>
<li class="last leaf menu-mlid-24627"><a href="/related-topics/women-drugs">Women and Drugs</a></li>
</ul></li>
<li class="expanded menu-mlid-6229"><a href="/publications">Publications</a></li>
<li class="expanded menu-mlid-8558"><a href="/funding">Funding</a><ul class="menu"><li class="first leaf has-children menu-mlid-3235"><a href="/funding/funding-opportunities">Funding Opportunities</a></li>
<li class="leaf has-children menu-mlid-3234"><a href="/funding/clinical-research">Clinical Research</a></li>
<li class="leaf has-children menu-mlid-3236"><a href="/funding/post-award-concerns">Post-Award Concerns</a></li>
<li class="leaf menu-mlid-12549"><a href="/funding/general-information">General Information</a></li>
<li class="leaf has-children menu-mlid-10110"><a href="/funding/grant-contract-application-process">Grant & Contract Application Process</a></li>
<li class="leaf has-children menu-mlid-11488"><a href="/funding/funding-priorities">Funding Priorities</a></li>
<li class="last leaf has-children menu-mlid-12533"><a href="/funding/research-training-career-development">Research Training</a></li>
</ul></li>
<li class="expanded menu-mlid-2729"><a href="/news-events">News & Events</a><ul class="menu"><li class="first leaf menu-mlid-22155"><a href="/news-events/news">News</a></li>
<li class="leaf has-children menu-mlid-22869"><a href="/about-nida/noras-blog" title="">Nora's Blog</a></li>
<li class="leaf has-children menu-mlid-22180"><a href="/news-events/nida-in-news" title="">NIDA in the News</a></li>
<li class="leaf has-children menu-mlid-7801"><a href="/news-events/nida-notes">NIDA Notes</a></li>
<li class="leaf menu-mlid-22185"><a href="/news-events/podcasts">Podcasts</a></li>
<li class="leaf menu-mlid-21921"><a href="/news-events/e-newsletters" title="">E-Newsletters</a></li>
<li class="leaf has-children menu-mlid-22183"><a href="/news-events/public-education-projects">Public Education Projects</a></li>
<li class="leaf menu-mlid-3123"><a href="/news-events/contact-press-office">Contact the Press Office</a></li>
<li class="leaf has-children menu-mlid-22201"><a href="/news-events/meetings-events">Meetings & Events</a></li>
<li class="last leaf menu-mlid-21924"><a href="/publications/media-guide">Media Guide</a></li>
</ul></li>
<li class="last expanded menu-mlid-2730"><a href="/about-nida">About NIDA</a><ul class="menu"><li class="first leaf has-children menu-mlid-9961"><a href="/about-nida/directors-page">Director's Page</a></li>
<li class="leaf has-children menu-mlid-19616"><a href="/about-nida/organization">Organization</a></li>
<li class="leaf has-children menu-mlid-10068"><a href="/about-nida/legislative-activities">Legislative Activities</a></li>
<li class="leaf has-children menu-mlid-19848"><a href="/about-nida/advisory-boards-review-groups">Advisory Boards & Groups</a></li>
<li class="leaf has-children menu-mlid-3098"><a href="/about-nida/working-nida" title="">Working at NIDA</a></li>
<li class="leaf menu-mlid-10100"><a href="/about-nida/donating-to-nida">Donating to NIDA</a></li>
<li class="leaf has-children menu-mlid-3099"><a href="/about-nida/contact-us">Contact Us</a></li>
<li class="leaf menu-mlid-22923"><a href="/about-nida/sharing-tools-badges">Sharing Tools and Badges</a></li>
<li class="leaf menu-mlid-9554"><a href="/about-nida/other-resources">Other Resources</a></li>
<li class="last leaf has-children menu-mlid-24295"><a href="/about-nida/2016-2020-nida-strategic-plan">Strategic Plan</a></li>
</ul></li>
</ul></div>
    </div>
  </div>
</section><div class="block block-block iq-top-bar block-448 block-block-448 odd block-without-title" id="block-block-448">
  <div class="block-inner clearfix">
                
    <div class="content clearfix">
      <div id="bar-button-search" class="bar-button-wrapper">
<div class="bar-button"><i class="fa fa-search"></i><span class="label">Search</span></div>
</div>
<div id="bar-button-share" class="bar-button-wrapper">
<div class="bar-button"><i class="fa fa-share-alt"></i><span class="label">Share</span></div>
<div id="bar-button-share-form" class="bar-button-content">
</div>
</div>    </div>
  </div>
</div><div class="block block-block iq-hide-on-desktop iq-bar-button-content iq-bar-button-share-form block-447 block-block-447 even block-without-title" id="block-block-447">
  <div class="block-inner clearfix">
                
    <div class="content clearfix">
      <div class="addthis_toolbox">
<span class="fa-stack">
  <i class="fa fa-circle fa-stack-2x fa-inverse"></i>
  <a class="addthis_button_twitter">
  <i class="fa fa-twitter fa-stack-1x"></i>
  </a>
</span>
<span class="fa-stack">
  <i class="fa fa-circle fa-stack-2x fa-inverse"></i>
  <a class="addthis_button_facebook">
  <i class="fa fa-facebook fa-stack-1x"></i>
  </a>
</span>
<span class="fa-stack">
  <i class="fa fa-circle fa-stack-2x fa-inverse"></i>
  <a class="addthis_button_email">
  <i style="color:#777;" class="fa fa-envelope fa-stack-1x"></i>
  </a>
</span>
<!--
<span class="fa-stack">
  <i class="fa fa-circle fa-stack-2x fa-inverse"></i>
  <a class="addthis_button_pinterest_pinit"> 
  <i class="fa fa-pinterest fa-stack-1x"></i>
  </a>
</span>
-->
<span class="fa-stack">
  <i class="fa fa-circle fa-stack-2x fa-inverse"></i>
  <a class="addthis_button_google_plusone_share">  
  <i class="fa fa-google-plus fa-stack-1x"></i>
  </a>
</span>
<span class="fa-stack addthis-orange">
  <i class="fa fa-circle fa-stack-2x fa-inverse"></i>
  <a class="addthis_button_more">  
  <i class="fa fa-plus fa-stack-1x"></i>
  </a>
</span>
</div>    </div>
  </div>
</div>  </div>
</div>  </div>
</div></header>  
      <!--googleon: index--> 
   <!--googleon: snippet-->

      <section id="section-content" class="section section-content">
    
  <div id="zone-pre-content" class="zone zone-pre-content clearfix container-24">
    <div class="grid-24 region region-pre-content" id="region-pre-content">
  <div class="region-inner region-pre-content-inner">
    <div class="block block-blockify block-blockify-breadcrumb block-blockify-blockify-breadcrumb odd block-without-title" id="block-blockify-blockify-breadcrumb">
  <div class="block-inner clearfix">
                
    <div class="content clearfix">
      <div class="breadcrumb"><a href="/">Home</a><span class="separator"> » </span><a href="/international">NIDA International Home</a><span class="separator"> » </span><a href="/international/abstract-database">Abstract Database</a><span class="separator"> » </span><span class="current">Motivation and Treatment Readiness for Methadone Maintenance Treatment in Ruili, China</span></div>    </div>
  </div>
</div><div class="block block-blockify block-blockify-page-title block-blockify-blockify-page-title even block-without-title" id="block-blockify-blockify-page-title">
  <div class="block-inner clearfix">
                
    <div class="content clearfix">
      <h1>Motivation and Treatment Readiness for Methadone Maintenance Treatment in Ruili, China</h1>    </div>
  </div>
</div>          <div class="add-this-block">
        <!--googleoff: snippet-->
        <!--googleoff: index-->
        <maxamineignore>
          <div id="utility">
                          <script type="text/javascript">
                var addthistitlenk = document.getElementsByTagName('meta')['twitter:title'].getAttribute('content');;
                var addthistitlenk2 = " via @NIDAnews";
                var brandnewtitle = addthistitlenk.concat(addthistitlenk2);
                var addthis_config =
                {
                  ui_508_compliant: true
                }
                var addthis_share = {
                  title: brandnewtitle
                }
              </script>
                        <div class="addthis_toolbox addthis_default_style ">
					    <span class="externalLink">
						    <a class="addthis_counter addthis_pill_style"></a>
              </span>
            </div>
            <script type="text/javascript"
                    src="https://s7.addthis.com/js/250/addthis_widget.js#pubid=ra-4d6e5b9f65355e5e&async=1"></script>
            <!-- AddThis Button END -->
            <noscript>
                            <span class="noscript"><a
                  href="mailto:?subject=NIDA%3A%20Motivation%20and%20Treatment%20Readiness%20for%20Methadone%20Maintenance%20Treatment%20in%20Ruili%2C%20China&body=https%3A%2F%2Fwww.drugabuse.gov%2Finternational%2Fabstracts%2Fmotivation-treatment-readiness-methadone-maintenance-treatment-in-ruili-china">Email</a> </span>
              <span class="noscript"><a
                  href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.drugabuse.gov%2Finternational%2Fabstracts%2Fmotivation-treatment-readiness-methadone-maintenance-treatment-in-ruili-china">Facebook</a></span>
              <span class="noscript"><a
                  href="https://www.twitter.com/share?url=https%3A%2F%2Fwww.drugabuse.gov%2Finternational%2Fabstracts%2Fmotivation-treatment-readiness-methadone-maintenance-treatment-in-ruili-china">Twitter</a></span>
            </noscript>
          </div>
          <!-- /.utility -->
        </maxamineignore>
        <!--googleon: index-->
        <!--googleon: snippet-->
      </div>
      </div>
</div>  </div>
<div id="zone-content-wrapper" class="zone-wrapper zone-content-wrapper clearfix">  
  <div id="zone-content" class="zone zone-content clearfix container-24">    
        
        <div class="grid-24 region region-content" id="region-content">
  <div class="region-inner region-content-inner">
    <a id="main-content"></a>
                            <div class="block block-system block-main block-system-main odd block-without-title" id="block-system-main">
  <div class="block-inner clearfix">
                
    <div class="content clearfix">
      <div  id="node-abstract-15855" class="ds-1col node node-abstract node-promoted view-mode-full node-not-sticky author-sudrupal odd clearfix clearfix">

  
  <div class="field field-name-abstract-f-and-l-name field-type-ds field-label-hidden">
        <div class="field-items">
                <div class="field-item even"><h3>Zhoulin  Li</h3></div>
            </div>
</div>
<div class="field field-name-body field-type-text-with-summary field-label-hidden">
        <div class="field-items">
                <div class="field-item even"><p><strong>Li, Zhoulin,</strong> HIV/AIDS Prevention and Control
        Office of Ruili City, China; Liu, Wei, University of Illinois
        at Chicago, United States</p>
      <p><strong>Background:</strong> Facing a serious challenge
        of an epidemic of HIV/AIDS and drug use (mainly smoking and
        injecting heroin) in Ruili, China, a methadone maintenance
        treatment (MMT) clinic was set up in 2005 to serve participants
        in the downtown area, and the first mobile van in China was
        initiated in 2006 to deliver methadone to participants in rural
        areas. Currently, a total of 350 participants are enrolled
        in the program. The study aimed to assess clients' motivation
        and treatment readiness (MTR) for MMT and analyze its association
        with knowledge about HIV/AIDS and social support networks that
        influence participants' decisionmaking
        to enroll and remain in MMT programs.</p>
      <p><strong>Methods:</strong> A cross-sectional
        study in the Ruili MMT program was conducted. With informed
        consent, 298 clients were interviewed using a structured questionnaire
        that covered demographic background, MTR, knowledge about HIV/AIDS,
        and social support networks. Participants were asked to respond
        to 20 statements about MTR on a scale ranging from "not
        applicable," "not at all," "somewhat," and "very
        much." Twenty questions also were used to assess the
        level of knowledge about HIV transmission and prevention. Social
        support networks were assessed using a network inventory of
        perceived sources of emotional support, financial support,
        health advice, and drug use.</p>
      <p><strong>Results:</strong> The accumulated MTR score
        ranged from 26 to 59, with a mean of 53.8 and median of 54.
        Only 1 percent of participants fell in the lower score level.
        More than 95 percent of participants indicated that they were
        highly ready for treatment to stop using drugs; 94 percent
        realized that drug use was a very serious problem; 96 percent
        felt they needed to be completely drug free in order to live
        a better life; 85 percent were willing to stop seeing previous
        drug use friends; and 95 percent would like to stay in the
        program as long as they had to. The multiple regression analysis
        showed that the MTR score was positively associated with the
        size of financial support and the score of knowledge about
        HIV/AIDS with p
      </p><p><strong>Conclusions:</strong> Most of the participants
        interviewed in the Ruili MMT program had a high MTR level,
        which is one of the key determinants leading to a successful
        treatment outcome. The study indicated that the higher the
        level of knowledge about HIV/AIDS, the greater the MTR level
        was. Thus, this suggests that it would be advisable to provide
        more information and education on HIV/AIDS to participants
        in the MMT program in local languages as more than half of
        the participants are from a minority population. The study
        also suggests that increased financial support would increase
        the level of MTR and that providing social support from family
        or non-drug-using friends helps the participants to get ready
        for treatment.</p></div>
            </div>
</div>
<div class="field field-name-field-abstract-year field-type-number-integer field-label-inline clearfix">
        <div class="field-label">Abstract Year:&nbsp;</div>
        <div class="field-items">
                <div class="field-item even">2008</div>
            </div>
</div>
<div class="field field-name-field-abstract-region field-type-list-text field-label-inline clearfix">
        <div class="field-label">Abstract Region:&nbsp;</div>
        <div class="field-items">
                <div class="field-item even">East Asia</div>
            </div>
</div>
<div class="field field-name-field-abstract-country field-type-list-text field-label-inline clearfix">
        <div class="field-label">Abstract Country:&nbsp;</div>
        <div class="field-items">
                <div class="field-item even">China</div>
            </div>
</div>
<div class="field field-name-field-abstract-category field-type-list-text field-label-inline clearfix">
        <div class="field-label">Abstract Category:&nbsp;</div>
        <div class="field-items">
                <div class="field-item even">Prevention</div>
            </div>
</div>
<div class="field field-name-abstracts-back-button field-type-ds field-label-hidden">
        <div class="field-items">
                <div class="field-item even"><div style="margin-top:2.2em;" class="abstracts-back-button"><a href="https://www.drugabuse.gov/international/abstract-database">&laquo; Back to Search</a></div></div>
            </div>
</div>
</div>

    </div>
  </div>
</div>      </div>
</div>  </div>
</div></section>  <!--googleoff: snippet-->
<!--googleoff: index--> 
      <footer id="section-footer" class="section section-footer">
    
  <div id="zone-footer" class="zone zone-footer clearfix container-24">
    <div class="grid-24 region region-footer" id="region-footer">
    <div class="region-inner region-footer-inner">
        <div class="block block-menu block-menu-footer block-menu-menu-footer odd block-without-title" id="block-menu-menu-footer">
  <div class="block-inner clearfix">
                
    <div class="content clearfix">
      <ul class="menu"><li class="first leaf"><a href="/" title="NIDA Website">NIDA Home</a></li>
<li class="leaf"><a href="/sitemap" title="Site Map">Site Map</a></li>
<li class="leaf"><a href="/frequently-asked-questions">FAQs</a></li>
<li class="leaf"><a href="/accessibility">Accessibility</a></li>
<li class="leaf"><a href="/privacy">Privacy</a></li>
<li class="leaf"><a href="http://www.nih.gov/icd/od/foia/index.htm" title="FOIA(NIH)">FOIA(NIH)</a></li>
<li class="leaf"><a href="/about-nida/working-nida" title="Employment">Working at NIDA</a></li>
<li class="leaf"><a href="/about-nida/contact-us" title="Contact">Contact</a></li>
<li class="leaf"><a href="https://www.drugabuse.gov/connect-nida" title="">Subscribe</a></li>
<li class="last leaf"><a href="http://archives.drugabuse.gov" title="">Archives</a></li>
</ul>    </div>
  </div>
</div>
        <div class="footer_icon block block-block noIMGscale block-without-title">
            <div class="block-inner clearfix">
                <div class="content clearfix">
                    <div>
                  
                

                        <a href="https://www.usa.gov" title="USA.gov">
                            <img align="middle" alt="USA.gov" border="0" height="34" src="/sites/all/themes/nida_vic_adaptive/images/footer-logo-usagov.gif" width="98" />
                        </a>      
                        <a href="https://www.hhs.gov" title="U.S. Department of Health and Human Services">
                            <img align="middle" alt="HHS" border="0" height="34" src="/sites/all/themes/nida_vic_adaptive/images/footer-logo-hhs.gif" width="39" />
                        </a>
                        <a href="http://www.nih.gov" title="National Institutes of Health (NIH)">
                            <img align="middle" alt="NIH" border="0" src="/sites/all/themes/nida_vic_adaptive/images/footer-logo-nih-new.gif" />
                        </a>  

                    </div>
                </div>
            </div>
        </div>
                    <div class="footer_pdf_en block block-block block-without-title">
                <div class="block-inner clearfix">
                    <div class="content clearfix">
                        <p>PDF documents require the free <a class="plugins" href="https://get.adobe.com/reader/" target="_blank">Adobe Reader</a>. Microsoft Word documents require the free <a class="plugins" href="https://www.microsoft.com/download/en/details.aspx?id=4" target="_blank">Microsoft Word viewer</a>.<br />
                            Microsoft PowerPoint documents require the free <a class="plugins" href="https://www.microsoft.com/download/en/details.aspx?id=6" target="_blank">Microsoft PowerPoint viewer</a>. Flash content requires the free <a class="plugins" href="https://get.adobe.com/flashplayer/" target="_blank">Adobe Flash Player</a>.</p>
                        <p class="nih-tagline">NIH...Turning Discovery Into Health<sup>&reg;</sup></p>
                    </div>
                </div>
            </div>
            </div>
</div>  </div>
</footer>  <!--googleon: snippet-->
<!--googleon: index--> 
</div>  	<div class="region region-page-bottom" id="region-page-bottom">
  <div class="region-inner region-page-bottom-inner">
      </div>
</div>	

		
<script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
<script type="text/javascript">
<!--//--><![CDATA[//><!--
window.jQuery || document.write("<script src='/sites/all/modules/jquery_update/replace/jquery/1.7/jquery.min.js'>\x3C/script>")
//--><!]]>
</script>
<script type="text/javascript" src="https://www.drugabuse.gov/sites/default/files/js/js_3TykeRWpejhD4-J3vdlaNXdULg9xhOZhbsppK0o2bUs.js"></script>
<script type="text/javascript" src="https://www.drugabuse.gov/sites/default/files/js/js_MPuDMGRfAP763H40ccLZuNE707KBtCLkG3VpF7rR77k.js"></script>
<script type="text/javascript" src="https://www.drugabuse.gov/sites/default/files/js/js_eVmEVHJ5IjWmZuynwDy2UDK45UTRRUjQws9meb7pEx8.js"></script>
<script type="text/javascript" src="https://www.drugabuse.gov/sites/default/files/js/js_3aZZBQjPjgkchNnYMIlPhtNh40BOZeE8JdjI_Pg8W28.js"></script>
<script type="text/javascript" src="https://www.drugabuse.gov/sites/default/files/js/js_43n5FBy8pZxQHxPXkf-sQF7ZiacVZke14b0VlvSA554.js"></script>
<script type="text/javascript">
<!--//--><![CDATA[//><!--
jQuery.extend(Drupal.settings, {"basePath":"\/","pathPrefix":"","ajaxPageState":{"theme":"nida_vic_adaptive","theme_token":"IVehLqAu4CWbgmm7W0MhwOgQB9EEXLz4qCvsnd56_dc","js":{"\/\/ajax.googleapis.com\/ajax\/libs\/jquery\/1.7.2\/jquery.min.js":1,"0":1,"misc\/jquery.once.js":1,"misc\/drupal.js":1,"sites\/all\/modules\/nida\/content_accordion\/js\/content_accordion.js":1,"sites\/all\/modules\/content_colorbox\/content_colorbox.js":1,"sites\/all\/modules\/nida\/content_shortcodes\/js\/twitter.js":1,"sites\/all\/modules\/funding_embed\/js\/funding_embed.js":1,"sites\/all\/modules\/funding_tool\/js\/jquery.tablesorter.min.js":1,"sites\/all\/modules\/funding_tool\/js\/funding_app.js":1,"sites\/all\/modules\/nnpage\/nnpage.js":1,"sites\/all\/modules\/nida\/pubfinder\/js\/pubfinder.js":1,"sites\/all\/modules\/nida\/pubfinder\/js\/pubfinder.top_nodes.js":1,"sites\/all\/modules\/tabular-data\/js\/tabular_data.js":1,"sites\/all\/libraries\/colorbox\/jquery.colorbox-min.js":1,"sites\/all\/modules\/colorbox\/js\/colorbox.js":1,"sites\/all\/modules\/funding_widget\/js\/funding_widget_mobile.js":1,"sites\/all\/modules\/govextlink\/govextlink.js":1,"sites\/all\/libraries\/chosen\/chosen.jquery.js":1,"sites\/all\/themes\/nida_vic_adaptive\/js\/jquery.jcarousel.min.js":1,"sites\/all\/themes\/nida_vic_adaptive\/js\/jquery.cycle2.min.js":1,"sites\/all\/themes\/nida_vic_adaptive\/js\/jquery.cycle2.swipe.min.js":1,"sites\/all\/themes\/nida_vic_adaptive\/js\/jquery.cycle2.carousel.min.js":1,"sites\/all\/themes\/nida_vic_adaptive\/js\/jquery.flexslider-min.js":1,"sites\/all\/themes\/nida_vic_adaptive\/js\/jquery.cluetip.js":1,"sites\/all\/themes\/nida_vic_adaptive\/js\/jquery.carouFredSel-6.1.0.js":1,"sites\/all\/themes\/nida_vic_adaptive\/js\/jquery.youtubeplaylist.js":1,"sites\/all\/themes\/nida_vic_adaptive\/js\/jquery.unveil.js":1,"sites\/all\/themes\/nida_vic_adaptive\/js\/jquery.transit.js":1,"sites\/all\/themes\/nida_vic_adaptive\/js\/nida_vic_adaptive.js":1,"sites\/all\/themes\/nida_vic_adaptive\/js\/smartresize.jquery.js":1,"sites\/all\/themes\/nida_vic_adaptive\/js\/iq-main-menu.jquery.js":1,"sites\/all\/themes\/nida_vic_adaptive\/js\/pull_hash.js":1,"sites\/all\/themes\/nida_vic_adaptive\/js\/Universal-Federated-Analytics-Min.js":1,"sites\/all\/themes\/omega\/omega\/js\/jquery.formalize.js":1,"sites\/all\/themes\/omega\/omega\/js\/omega-mediaqueries.js":1},"css":{"modules\/system\/system.base.css":1,"modules\/system\/system.menus.css":1,"modules\/system\/system.messages.css":1,"modules\/system\/system.theme.css":1,"modules\/book\/book.css":1,"modules\/comment\/comment.css":1,"sites\/all\/modules\/nida\/content_accordion\/css\/content_accordion.css":1,"sites\/all\/modules\/content_colorbox\/content_colorbox.css":1,"sites\/all\/modules\/date\/date_api\/date.css":1,"sites\/all\/modules\/date\/date_popup\/themes\/datepicker.1.7.css":1,"modules\/field\/theme\/field.css":1,"sites\/all\/modules\/funding_embed\/css\/funding_embed.css":1,"sites\/all\/modules\/funding_tool\/css\/funding_tool_admin.css":1,"sites\/all\/modules\/funding_tool\/css\/funding_app.css":1,"sites\/all\/modules\/graph_rollover\/css\/graph_rollover.css":1,"sites\/all\/modules\/mollom\/mollom.css":1,"sites\/all\/modules\/nida\/nmassist_api\/css\/nmassist_api.css":1,"sites\/all\/modules\/nnpage\/css\/ppcpages.css":1,"modules\/node\/node.css":1,"sites\/all\/modules\/nida\/pubfinder\/css\/pubfinder.css":1,"sites\/all\/modules\/nida\/pubfinder\/css\/pubfinder.top_nodes.css":1,"sites\/all\/modules\/tabular-data\/css\/tabular_data.css":1,"modules\/user\/user.css":1,"sites\/all\/modules\/workflow\/workflow_admin_ui\/workflow_admin_ui.css":1,"sites\/all\/modules\/views\/css\/views.css":1,"sites\/all\/modules\/ckeditor\/css\/ckeditor.css":1,"sites\/all\/libraries\/colorbox\/example3\/colorbox.css":1,"sites\/all\/modules\/ctools\/css\/ctools.css":1,"sites\/all\/modules\/funding_widget\/css\/funding_widget_mobile.css":1,"sites\/all\/modules\/funding_widget\/css\/funding_widget.css":1,"sites\/all\/modules\/govextlink\/govextlink.css":1,"sites\/all\/modules\/lexicon\/css\/lexicon.css":1,"sites\/all\/libraries\/chosen\/chosen.css":1,"sites\/all\/themes\/nida_vic_adaptive\/js\/flexslider.css":1,"sites\/all\/themes\/nida_vic_adaptive\/css\/font-awesome\/css\/font-awesome.min.css":1,"sites\/all\/themes\/nida_vic_adaptive\/css\/print.css":1,"sites\/all\/themes\/omega\/alpha\/css\/alpha-reset.css":1,"sites\/all\/themes\/omega\/alpha\/css\/alpha-mobile.css":1,"sites\/all\/themes\/omega\/alpha\/css\/alpha-alpha.css":1,"sites\/all\/themes\/omega\/omega\/css\/formalize.css":1,"sites\/all\/themes\/omega\/omega\/css\/omega-branding.css":1,"sites\/all\/themes\/omega\/omega\/css\/omega-menu.css":1,"sites\/all\/themes\/omega\/omega\/css\/omega-forms.css":1,"sites\/all\/themes\/omega\/omega\/css\/omega-visuals.css":1,"sites\/all\/themes\/nida_vic_adaptive\/css\/nida_vic_adaptive.css":1,"sites\/all\/themes\/nida_vic_adaptive\/css\/nida-vic-adaptive-alpha-fluid-grid-24.css":1,"sites\/all\/themes\/nida_vic_adaptive\/css\/sass.css":1,"ie::state03::sites\/all\/themes\/nida_vic_adaptive\/css\/nida-vic-adaptive-alpha-fluid-state03.css":1,"ie::state03::sites\/all\/themes\/nida_vic_adaptive\/css\/grid\/alpha_fluid\/state03\/alpha-fluid-state03-24.css":1,"state00::sites\/all\/themes\/nida_vic_adaptive\/css\/nida-vic-adaptive-alpha-fluid-state00.css":1,"sites\/all\/themes\/nida_vic_adaptive\/css\/grid\/alpha_fluid\/state00\/alpha-fluid-state00-24.css":1,"state01::sites\/all\/themes\/nida_vic_adaptive\/css\/nida-vic-adaptive-alpha-fluid-state01.css":1,"sites\/all\/themes\/nida_vic_adaptive\/css\/grid\/alpha_fluid\/state01\/alpha-fluid-state01-24.css":1,"state02::sites\/all\/themes\/nida_vic_adaptive\/css\/nida-vic-adaptive-alpha-fluid-state02.css":1,"sites\/all\/themes\/nida_vic_adaptive\/css\/grid\/alpha_fluid\/state02\/alpha-fluid-state02-24.css":1,"state03::sites\/all\/themes\/nida_vic_adaptive\/css\/nida-vic-adaptive-alpha-fluid-state03.css":1,"sites\/all\/themes\/nida_vic_adaptive\/css\/grid\/alpha_fluid\/state03\/alpha-fluid-state03-24.css":1}},"colorbox":{"opacity":"0.85","current":"{current} of {total}","previous":"\u00ab Prev","next":"Next \u00bb","close":"Close","maxWidth":"98%","maxHeight":"98%","fixed":true,"mobiledetect":true,"mobiledevicewidth":"480px"},"govextlink":{"extTarget":"_blank","extClass":"ext","extSubdomains":1,"extExclude":"","extInclude":"","extAlert":0,"extAlertText":"This link will take you to an external web site. We are not responsible for their content.","mailtoClass":"mailto"},"nida":{"logged_in":0},"omega":{"layouts":{"primary":"state03","order":["state00","state01","state02","state03"],"queries":{"state00":"all and (min-width: 1px) and (min-device-width: 1px), all and (max-device-width: 600px) and (min-width: 1px) and (orientation:portrait)","state01":"all and (min-width: 601px) and (min-device-width: 601px), all and (max-device-width: 768px) and (min-width: 601px) and (orientation:portrait)","state02":"all and (min-width: 769px) and (min-device-width: 769px), all and (max-device-width: 959px) and (min-width: 769px) and (orientation:landscape)","state03":"all and (min-width: 960px)"}}}});
//--><!]]>
</script>
<script type="application/ld+json">
          { "@context" : "http://schema.org",
            "@type" : "Organization",
            "name" : "National Institute on Drug Abuse",
            "logo": "https://www.drugabuse.gov/sites/all/themes/nida_vic_adaptive/images/nih-nida-logo.gif",
            "url" : "https://www.drugabuse.gov",
            "description" : "NIDA's mission is to lead the Nation in bringing the power of science to bear on drug abuse and addiction.",
            "sameAs" : [ "https://www.facebook.com/NIDANIH",
              "https://twitter.com/NIDAnews",
              "https://www.youtube.com/user/NIDANIH",
              "https://www.flickr.com/photos/nida-nih/collections/",
              "https://www.linkedin.com/company/the-national-institute-on-drug-abuse-nida"] 
          }
          </script>


<!-- Go to www.addthis.com/dashboard to customize your tools -->
<script type="text/javascript" src="//s7.addthis.com/js/300/addthis_widget.js#pubid=ra-4d6e5b9f65355e5e" async="async"></script>
  <script type="text/javascript">
    setTimeout(function(){var a=document.createElement("script");
    var b=document.getElementsByTagName("script")[0];
    a.src=document.location.protocol+"//dnn506yrbagrg.cloudfront.net/pages/scripts/0012/1010.js?"+Math.floor(new Date().getTime()/3600000);
    a.async=true;a.type="text/javascript";b.parentNode.insertBefore(a,b)}, 1);
  </script>
</body>
</html>

"""
soup = BeautifulSoup(html_doc, "lxml")
# print '---------------------------------'

try:
    title = soup.find('div', id = 'zone-pre-content').find('h1')
    if title:
        print '-------------------'
        all_p = title.get_text().strip()
        print all_p

    author = soup.find('div', id = 'zone-content-wrapper').find('div', class_='field field-name-abstract-f-and-l-name field-type-ds field-label-hidden')
    if author:
        print '-------------------'
        all_p = author.get_text().strip()
        print all_p
    
    content = soup.find('div', id = 'zone-content-wrapper').find('div', class_='field field-name-body field-type-text-with-summary field-label-hidden')
    if content:
        print '-------------------'
        all_p = content.get_text().strip()
        print all_p
    
    year = soup.find('div', id = 'zone-content-wrapper').find('div', class_='field field-name-field-abstract-year field-type-number-integer field-label-inline clearfix').find('div',class_='field-items')
    if year:
        print '-------------------'
        all_p = year.get_text().strip() + '-06-01 00:00:00'
        print all_p
    
    all = title + "\n" + author + "\n" + content
    
    # all_p = all_p.encode('GBK', 'ignore')
    # all_p = re.sub(r'\n', "", all_p)
    # all_p = re.sub(r'\t', "", all_p)
    # content = all_p
    # print all_p
except:
    print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'

# print '---------------------------------'  
