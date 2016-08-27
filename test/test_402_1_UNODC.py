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

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"><head><title>Drug Trafficking</title><meta http-equiv="content-language" content="en"/>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<meta name="alt-language-name" content="Español"/>
<meta name="author" content="bo-shakira.harris"/>
<meta name="description" content="United Nations Office on Drugs and Crime Web Site"/>
<meta name="keywords" content="un UN united UNITED nations NATIONS office on drugs and crime OFFICE ON DRUGS AND CRIME"/>
<meta name="document-type" content="webpage"/>
<meta name="document-language-name" content="English"/>
<meta name="creation-date" content="2013-05-16T16:09:47Z"/>
<meta name="posting-date" content="2013-05-24T01:58:23Z"/>
<link type="text/css" rel="stylesheet" href="/misc/unodc.css"/>
<link type="text/css" rel="stylesheet" href="/misc/xmenu.css"/>
<script language="JavaScript" type="text/javascript" src="/misc/xmenu.js"></script>
</head><body id="unodcBody"><div id="mainWrapper"><div id="mainThemeHolder"><div id="unodcHeaderLocal"><div id="unodcHeaderWrapper"><h1 class="default-header" title="United Nations Office on Drugs and Crime" id="headerTitle"><a title="" href="/unodc/index.html"><span class="invisible">United Nations Office on Drugs and Crime</span></a></h1><h2 style="font-size:120%" title="UNODC ROPAN" id="headerSubTitleSmaller"><a title="UNODC ROPAN" href="/ropan/index.html">Central America and the Caribbean</a></h2><div class="langSwitcher" id="searchForm">
	<ul id="languageSwitch"><li><a href="/ropan/es/BorderControl/drug-trafficking.html">Español</a></li></ul>
	<form id="search" action="/unodc/search.html" name="search"><input class="searchField" name="q" type="text"/><button type="submit" class="searchButton">Search</button></form><div class="clearance"></div></div></div></div><div id="unodcTopNav"><span style="display:none">File is not found</span></div><div id="contentBody"><script src="/javascript/jquery-min.js" type="text/javascript"></script><div style="display:none;" id="unodcEverywhereContainerWrapper"><div id="unodcEverywhereContainer"><div class="unodcEverywhereToggle"><a onclick="return false;" href="">UNODC Everywhere </a></div><ul class="unodcEverywhere"><li><a target="_blank" href="http://www.facebook.com/unodc"><img alt="" src="/images/frontpage/icons/facebook_colour.jpg"/>Facebook</a></li><li><a target="_blank" href="http://twitter.com/unodc"><img height="16" width="16" alt="" src="/images/frontpage/icons/twitter_color.jpg"/>Twitter</a></li><li><a target="_blank" href="http://www.flickr.com/photos/unodc/"><img alt="" src="/images/frontpage/icons/flickr.jpg"/>Flickr</a></li><li><a target="_blank" href="http://www.youtube.com/unodchq"><img alt="" src="/images/frontpage/icons/youtube_colour.jpg"/>YouTube</a></li></ul></div></div><script type="text/javascript">
        $(document).ready(function () {
        $("#columnLeft").before($("#unodcEverywhereContainerWrapper").html());
        $("#unodcEverywhereContainerWrapper").remove();
        $(".unodcEverywhere").show();
	$(".unodcEverywhereToggle").click(
		function (){
                    $(".unodcEverywhere").toggle('3000');
                });
        });

    </script><div id="columnLeft"><div id="leftNav"><ul class="M0"><li class="L0"><a href="/ropan/en/index.html"><span>UNODC ROPAN</span></a><ul class="M1"><li class="L1"><a href="/ropan/en/Introduction/aboutunodcropan.html">About UNODC ROPAN</a></li></ul></li><li class="L0"><a href="/ropan/en/topics.html"><span>Areas of Work</span></a><ul class="M1"><li class="L1"><a href="/ropan/en/CitizensSecurity/ventana-de-paz.html">Citizen's Security</a></li><li class="L1"><a href="/ropan/en/AntiCorruptionARAC/unodc-and-corruption.html">Corruption</a></li><li class="L1"><a href="/ropan/en/PrisonReform/criminal-justice-and-crime-prevention.html">Criminal Justice and Crime Prevention</a></li><li class="L1"><a href="/ropan/en/DrugDemandReduction/drug-demand-reduction-introduction.html">Drug Demand Reduction</a></li><li class="L1"><a href="/ropan/en/BorderControl/drug-trafficking.html" class="selected">Drug Trafficking</a><ul class="M2"><li class="L2"><a href="/ropan/en/BorderControl/legal-framework.html">Legal Framework</a></li><li class="L2"><a href="/ropan/en/BorderControl/AIRCOP/aircop.html">Aircop</a></li><li class="L2"><a href="/ropan/en/BorderControl/container-control/ccp.html">UNODC-WCO Global Container Control Programme</a></li><li class="L2"><a href="/ropan/en/BorderControl/MediaCentre/media-centre.html">Media Centre</a></li></ul></li><li class="L1"><a href="/ropan/en/PrisonReform/hiv-aids-in-prison/hiv-aids-in-prison-in-lac.html">HIV and AIDS in Prisons</a></li><li class="L1"><a href="/ropan/en/HumanTrafficking/human-trafficking.html">Human Trafficking and Smuggling of Migrants</a></li><li class="L1"><a href="/ropan/en/organized-crime.html">Organized Crime</a></li><li class="L1"><a href="/ropan/en/ResearchandTrendAnalysis/SDPSUM/sdp_sum.html">Research and Trend Analysis</a></li><li class="L1"><a href="/ropan/en/SECOPA/secopa.html">SECOPA</a></li></ul></li><li class="L0"><a href="/ropan/en/resources.html"><span>Resources</span></a><ul class="M1"><li class="L1"><a href="/ropan/en/get-the-facts-about-drugs.html">Get the Facts about Drugs</a></li><li class="L1"><a href="/ropan/en/unodc-and-the-protection-of-human-rights.html">UNODC and the protection of Human Rights</a></li><li class="L1"><a href="/ropan/en/unodc-regional-programme-2014-2016-in-support-of-the-caricom-crime-and-security-strategy.html">UNODC Regional Programme 2014-2016 in Support of the CARICOM Crime and Security Strategy</a></li><li class="L1"><a href="/ropan/en/TCO/technical-consultative-opinions.html">Technical Consultative Opinions</a></li><li class="L1"><a href="/ropan/en/working-paper-series/working-paper-series.html">Working Paper Series</a></li><li class="L1"><a href="/ropan/en/Vacancies/vacancies.html">Work Opportunities</a></li><li class="L1"><a href="/ropan/en/Resources/media-centre.html">Media Centre</a></li><li class="L1"><a href="/ropan/en/Resources/publications.html">Publications</a></li><li class="L1"><a href="/ropan/en/Campaigns/campaigns.html">Campaigns</a></li></ul></li><li class="L0"><a href="/ropan/en/ContactUs/form.html"><span>Contact Us</span></a></li></ul></div></div><div id="contentWrapper"><h2 style="text-align: justify;">Drug Trafficking in Central America and the Caribbean</h2>
<p style="text-align: justify;">Violent crime and drug-related trafficking pose serious threats to rule of law and development in Central America and the Caribbean. Although cocaine trafficking has sown violence in Central America and the Caribbean, there is a need to promote good governance and strengthen institutions, which are exploited by powerful cross-border criminals. Even if the northbound cocaine flows dwindle, criminal groups involved in trafficking are likely to vie for profits from other highly lucrative illicit activities and continue to spread mayhem.</p>
<p style="text-align: justify;">According to the UNODC Executive Director, Mr. Yury Fedotov, "The relationship between development, the rule of law and security needs to be fully understood. Drugs and crime are also development issues, while stability can be promoted by embracing human rights and access to justice".</p>
<p style="text-align: justify;">Central America has some of the highest homicide rates in the world, with 39 murders per 100,000 citizens in Guatemala, 69 per 100,000 in El Salvador and 92 per 100,000 in Honduras in 2011. Wedged between the suppliers of coca in the South and the consumers of cocaine in the North the region has become a transit corridor. However, the high rates of violence are not always associated with drug trafficking. El Salvador, for example, has a relatively low cocaine flow of 4 to 5 tons per year but registers the highest sustained murder rate in the region (over 65 per 100,000 between 2000 and 2010). Rather, it seems that lower demand and increased law enforcement has sparked brutal turf wars between traffickers as they fight over a share in a reduced market. The implementation of Mexico's security strategy in 2006, which disrupted the northbound supply of cocaine, triggered conflict over new "plazas" at key border crossings, notably along the Guatemalan/Honduran border. Displacement of trafficking routes to the Caribbean also remains a threat. According to studies, contraband flows become concentrated in the countries with the most challenges in dealing with them. The challenge is to tackle impunity and corruption, it says, while building police and criminal justice capacity.</p>
</div></div></div><div id="footer"><ul class="toolbarlist"><li><a href="/ropan/en/index.html">Home</a></li><li><a href="/ropan/en/site-map.html">Sitemap</a></li><li><a href="/ropan/en/contact-us.html">Contact Us</a></li><li><a href="https://www.unodc.org/frontdoor/">Login</a></li></ul><p>Copyright<span>&copy;</span>2016<span>&nbsp;</span>UNODC, All Rights Reserved, <a href="/ropan/en/legal.html" class="legalnotice">Legal Notice</a></p></div></div></body></html>

"""
soup = BeautifulSoup(html_doc, "lxml")
# print '---------------------------------'

try:
    content = soup.find('div', id = 'contentWrapper')
    if content:
        print '-------------------'
        all_p = content.get_text().strip()
        print all_p
    
    title = soup.find('div', id = 'contentWrapper').find('h1')
    title2 = soup.find('div', id = 'contentWrapper').find('h2')
    if title:
        print '-------------------'
        all_p = title.get_text().strip()
        print all_p
    elif title2:
        print '-------------------'
        all_p = title2.get_text().strip()
        print all_p

    # all_p = all_p.encode('GBK', 'ignore')
    # all_p = re.sub(r'\n', "", all_p)
    # all_p = re.sub(r'\t', "", all_p)
    # content = all_p
    # print all_p
except:
    print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'

# print '---------------------------------'  
