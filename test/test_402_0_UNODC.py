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
<html xmlns="http://www.w3.org/1999/xhtml"><head><title>Search</title><script src="//www.unodc.org/cdn/js/jquery/jquery-1.8.2.min.js" type="text/javascript"></script><script type="text/javascript" src="/javascript/flash-mp3-player.js"></script><meta http-equiv="content-language" content="en"/>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<meta name="author" content="agt"/>
<meta name="description" content="United Nations Office on Drugs and Crime Web Site"/>
<meta name="keywords" content="un UN united UNITED nations NATIONS office on drugs and crime OFFICE ON DRUGS AND CRIME"/>
<meta name="document-type" content="webpage"/>
<meta name="document-language-name" content="English"/>
<meta name="creation-date" content="2007-11-07T13:53:19Z"/>
<meta name="posting-date" content="2007-11-07T13:53:46Z"/>
<link type="text/css" rel="stylesheet" href="/misc/unodc.css"/>
<link type="text/css" rel="stylesheet" href="/misc/xmenu.css"/>
<script language="JavaScript" type="text/javascript" src="/misc/xmenu.js"></script>

<style type="text/css">
@import url('/misc/goosearch.css');
@import url('/misc/gooadvsearch.css');
</style></head><body id="unodcBody"><div id="mainWrapper"><div id="mainThemeHolder"><div id="unodcHeader"><h1 id="headerTitle"><a title="United Nations Office on Drugs and Crime Home Page" href="/unodc/index.html"><span class="invisible">United Nations Office on Drugs and Crime</span></a></h1><div class="" id="searchForm">
	
	<form id="search" action="/unodc/search.html" name="search"><input class="searchField" name="q" type="text"/><button type="submit" class="searchButton">Search</button></form><div class="clearance"></div></div></div><div id="unodcTopNav"><ul id="nav">
  <li>
    <strong>
    <a title="Home" href="/unodc/index.html?ref=menutop">Home</a></strong>
  </li>
  <li>
  <strong>
  <a title="About UNODC" href="/unodc/en/about-unodc/index.html?ref=menutop">About UNODC</a></strong> 
  <ul>
    <li>
      <a href="/unodc/en/about-unodc/annual-appeal.html">Annual Appeal</a>
    </li>
    <li>
      <a href="/unodc/en/about-unodc/annual-report.html?ref=menutop">Annual Report</a>
    </li>
    <li>
      <a href="/unodc/en/about-unodc/employment.html?ref=menutop">Employment opportunities</a>
    </li>
    <li>
      <a href="/unodc/en/evaluation/index.html?ref=menutop">Evaluation</a>
    </li>
    <li>
      <a href="/unodc/en/donors/index.html?ref=menutop">Funding and partnerships</a>
    </li>
    <li>
      <a href="/unodc/en/about-unodc/unodc-goodwil-ambassadors.html">Goodwill Ambassadors</a>
    </li>
    <li>
      <a href="/unodc/en/about-unodc/campaigns.html?ref=menutop">International days and campaigns</a>
    </li>
    <li>
      <a href="http://www.unodc.org/unodc/en/eds-corner/biography.html">Leadership</a>
    </li>
    <li>
      <a href="http://www.unvienna.org/unov/en/library.html">Library</a>
    </li>
    <li>
      <a href="http://www.unvienna.org/unov/en/management_proc.html">Procurement</a>
    </li>
    <li>
      <a href="/unodc/en/publications.html?ref=menutop">Publications</a>
    </li>
    <li>
      <a href="/unodc/en/about-unodc/post-2015-development-agenda.html">Sustainable Development Goals</a>
    </li>
    <li>
      <a href="/unodc/en/about-unodc/unodc-strategy.html?ref=menutop">UNODC Strategy</a>
    </li>
    <li>
      <a href="/unodc/en/about-unodc/contact-us.html?ref=menutop">Contact UNODC</a>
    </li>
  </ul></li>
  <li>
  <strong>
  <a title="Quick Links" href="/unodc/en/quick-Links.html?ref=menutop">Quick Links</a></strong> 
  <ul>
    <li>
      <a href="/unodc/human-trafficking-fund.html" target="_blank">United Nations Trust Fund for Victims of Human Trafficking</a>
    </li>
    <li>
      <a href="/unodc/en/treaties/CTOC/CTOC-COP.html">Conference of the Parties to the United Nations Convention against Transnational Organized Crime and its Protocols (CTOP/COP)
      <br /></a>
    </li>
    <li>
      <a href="/unodc/en/commissions/CCPCJ/index.html?ref=menutop">Commission on Crime Prevention and Criminal Justice (CCPCJ)</a>
    </li>
    <li>
      <a href="/unodc/en/commissions/CND/index.html?ref=menutop">Commission on Narcotic Drugs (CND)</a>
    </li>
    <li>
      <a href="/unodc/en/prevention/youth-initiative.html">UNODC Youth Initiative</a>
    </li>
    <li>
      <a href="http://www.imolin.org">IMOLIN - the international money laundering information network</a>
    </li>
    <li>
      <a href="/drugs/">International Day against Drug Abuse and Illicit Trafficking (26 June)</a>
    </li>
    <li>
      <a href="http://www.anticorruptionday.org/actagainstcorruption/en/index.html" target="_blank">International Anti-Corruption Day (9 December)</a>
    </li>
    <li>
      <a href="http://www.incb.org/incb/index.html?ref=menutop">International Narcotics Control Board (INCB)</a>
    </li>
    <li>
      <a href="/treatment/index.html?ref=menutop">Treatnet</a>
    </li>
    <li>
      <a href="/wdr2016/" target="_blank">World Drug Report</a>
    </li>
    <li>
      <a href="/unodc/en/treaties/index.html?ref=menutop">United Nations drug, crime and terrorism treaties</a>
    </li>
    <li>
      <a href="http://www.unsystem.org/">United Nations system website locator</a>
    </li>
    <li>
      <a href="/unodc/en/drug-trafficking/paris-pact-initiative.html">Paris Pact Initiative</a>
    </li>
  </ul></li>
  <li>
  <strong>
  <a title="Field Offices" href="/unodc/en/field-offices.html?ref=menutop">Field Offices</a></strong> 
  <ul>
    <li>
    <a href="/unodc/en/regional/central-asia.html?ref=menutop">Europe and West/Central Asia</a> 
    <ul>
      <li>
        <a href="/afg/index.html?ref=menutop">Afghanistan</a>
      </li>
      <li>
        <a href="/balticstates/en/index.html?ref=menutop">Baltic States</a>
      </li>
      <li>
        <a href="/uzbekistan/index.html?ref=menutop">Central Asia</a>
      </li>
      <li>
        <a href="/islamicrepublicofiran/">Iran, Islamic Republic of</a>
      </li>
      <li>
        <a href="/russia/index.html">Russian Federation</a>
      </li>
      <li>
        <a href="/southeasterneurope">South Eastern Europe</a>
      </li>
    </ul></li>
    <li>
      <a href="#">Africa and Middle East</a>
      <br />
      <ul>
        <li>
          <a href="/easternafrica/index.html?ref=menutop">Eastern Africa</a>
        </li>
        <li>
          <a href="/middleeastandnorthafrica/index.html">Middle East and North Africa</a>
        </li>
        <li>
          <a href="/nigeria/index.html?ref=menutop">Nigeria</a>
        </li>
        <li>
          <a href="/southernafrica/index.html?ref=menutop">Southern Africa</a>
        </li>
        <li>
          <a href="/westandcentralafrica/en/index.html">West and Central Africa</a>
        </li>
      </ul>
    </li>
    <li>
    <a href="#">Latin America and the Caribbean</a> 
    <ul>
      <li>
        <a href="/bolivia/es/index.html?ref=menutop">Bolivia</a>
      </li>
      <li>
        <a href="/brazil?ref=menutop">Brasil and Southern Cone</a>
      </li>
      <li>
        <a href="/ropan/en/index.html" target="_blank">Central America and the Caribbean</a>
      </li>
      <li>
        <a href="/colombia/es/index.html?ref=menutop">Colombia</a>
      </li>
      <li>
        <a href="/mexicoandcentralamerica/es/index.html?ref=menutop">Mexico</a>
      </li>
      <li>
        <a href="/peruandecuador/es/index.html?ref=menutop">Peru and Ecuador</a>
      </li>
    </ul></li>
    <li>
    <a href="/southeastasiaandpacific">Southeast Asia and the Pacific</a> 
    <ul>
      <li>
        <a href="/eastasiaandpacific/en/cambodia/index.html">Cambodia</a>
      </li>
      <li>
        <a href="/indonesia">Indonesia</a>
      </li>
      <li>
        <a href="/laopdr/index.html?ref=menutop">Lao PDR</a>
      </li>
      <li>
        <a href="/myanmar/index.html?ref=menutop">Myanmar</a>
      </li>
      <li>
        <a href="/southeastasiaandpacific">Regional Office - Thailand</a>
      </li>
      <li>
        <a href="/vietnam/index.html?ref=menutop">Viet Nam</a>
      </li>
    </ul></li>
    <li>
    <a href="/southasia/">South Asia</a> 
    <ul>
      <li>
        <a href="/southasia/index.html?ref=menutop">Regional Office for South Asia</a>
      </li>
      <li>
        <a href="/pakistan-new/index.html?ref=menutop">Pakistan</a>
      </li>
    </ul></li>
    <li>
      <a href="http://www.unodc.org/brussels">Liaison Office - Brussels</a>
    </li>
    <li>
      <a href="/newyork/index.html?ref=menutop">Liaison Office - New York</a>
    </li>
    <li>
      <a href="/unodc/en/field-offices.html?ref=menutop">Map of Field Offices</a>
    </li>
  </ul></li>
  <li>
    <strong>
    <a title="Site Map" href="/unodc/en/site-map.html?ref=menutop">Site Map</a></strong>
  </li>
</ul>
</div><div id="contentBody"><div style="display:none;" id="unodcEverywhereContainerWrapper"><div id="unodcEverywhereContainer"><div class="unodcEverywhereToggle"><a onclick="return false;" href="">UNODC Everywhere </a></div><ul class="unodcEverywhere"><li><a target="_blank" href="http://www.facebook.com/unodc"><img alt="Facebook" src="/images/frontpage/icons/facebook_colour.jpg"/>Facebook</a></li><li><a target="_blank" href="http://twitter.com/unodc"><img height="16" width="16" alt="Twitter" src="/images/frontpage/icons/twitter_color.jpg"/>Twitter</a></li><li><a target="_blank" href="http://www.flickr.com/photos/unodc/"><img alt="Flickr" src="/images/frontpage/icons/flickr.jpg"/>Flickr</a></li><li><a target="_blank" href="http://www.youtube.com/unodchq"><img alt="YouTube" src="/images/frontpage/icons/youtube_colour.jpg"/>YouTube</a></li></ul></div></div><script type="text/javascript">
        $(document).ready(function () {
        $("#columnLeft").before($("#unodcEverywhereContainerWrapper").html());
        $("#unodcEverywhereContainerWrapper").remove();
        $(".unodcEverywhere").hide();
	$(".unodcEverywhereToggle").click(
		function (){
                    $(".unodcEverywhere").toggle('3000');
                });
        });

    </script><div id="columnLeft"><div id="leftNav"><ul class="M0"><li class="L0"><a href="/unodc/en/topics.html?ref=menuside"><span>Topics</span></a><ul class="M1"><li class="L1"><a href="/unodc/en/alternative-development/index.html?ref=menuside">Alternative development</a></li><li class="L1"><a href="/unodc/en/corruption/index.html?ref=menuside">Corruption</a></li><li class="L1"><a href="/unodc/en/justice-and-prison-reform/index.html?ref=menuside">Crime prevention and criminal justice</a></li><li class="L1"><a href="/unodc/en/drug-prevention-and-treatment/index.html">Drug prevention, treatment and care</a></li><li class="L1"><a href="/unodc/en/drug-trafficking/index.html">Drug trafficking</a></li><li class="L1"><a href="/unodc/en/firearms-protocol/introduction.html">Firearms</a></li><li class="L1"><a href="/unodc/en/fraudulentmedicines/introduction.html">Fraudulent medicines</a></li><li class="L1"><a href="/unodc/en/hiv-aids/new/index.html">HIV and AIDS</a></li><li class="L1"><a href="/unodc/en/human-trafficking/index.html?ref=menuside">Human trafficking and migrant smuggling</a></li><li class="L1"><a href="/unodc/en/money-laundering/index.html?ref=menuside">Money-laundering</a></li><li class="L1"><a href="/unodc/en/organized-crime/index.html">Organized crime</a></li><li class="L1"><a href="/unodc/en/piracy/index.html?ref=menuside">Maritime crime and piracy</a></li><li class="L1"><a href="/unodc/en/terrorism/index.html">Terrorism prevention</a></li><li class="L1"><a href="/unodc/en/wildlife-and-forest-crime/index.html">Wildlife and forest crime</a></li></ul></li><li class="L0"><a href="/unodc/en/resources.html?ref=menuside"><span>Resources</span></a><ul class="M1"><li class="L1"><a href="/unodc/en/about-unodc/campaigns.html?ref=menuside">Campaigns</a></li><li class="L1"><a href="/unodc/en/commissions/index.html?ref=menuside">Commissions</a></li><li class="L1"><a href="/congress/">Crime Congress</a></li><li class="L1"><a href="/unodc/en/data-and-analysis/index.html?ref=menuside">Research</a></li><li class="L1"><a href="https://data.unodc.org?lf=1&lng=en">Data & indicators</a></li><li class="L1"><a href="/elearning/frontpage.jsp">eLearning</a></li><li class="L1"><a href="/unodc/en/evaluation/index.html">Evaluation</a></li><li class="L1"><a href="/unodc/en/scientists/index.html">Laboratory and forensic science services</a></li><li class="L1"><a href="/unodc/en/legal-tools/index.html?ref=menuside">Legal tools</a></li><li class="L1"><a href="/unodc/en/treaties/index.html?ref=menuside">Treaties</a></li></ul></li><li class="L0"><a href="/unodc/en/information-for.html?ref=menuside"><span>Information For ...</span></a><ul class="M1"><li class="L1"><a href="/unodc/en/donors/index.html?ref=menuside">Donors</a></li><li class="L1"><a href="/unodc/en/member-states/index.html?ref=menuside">Member States</a></li><li class="L1"><a href="/unodc/en/ngos/DCN0-NGOs-and-civil-society.html">NGOs and civil society</a></li></ul></li></ul></div></div><div id="contentWrapper"><h1>Search</h1>
<div id="gooAdvSearchAnchor"><a href="/unodc/search.html?site=unodc&amp;proxyreload=1&amp;q=Cross-border&amp;sort=date:D:L:d1&amp;entqr=0&amp;entqrm=0&amp;ud=1&amp;proxycustom=<ADVANCED/&gt;">Advanced Search</a></div>
<!--trl2-->
<div id="gooSearchBox">
   <form name="gs" method="GET" action="/unodc/search.html">
      <div id="gooSearchInput"><input type="text" name="q" id="gooInputField" maxlength="256" value="Cross-border">
         <div id="gooCollections"><select name="site" id="gooCollectionsSelect">
               <option value="unodc" selected>All UNODC web sites</option>
               <option value="india">Regional Office for South Asia</option>
               <option value="brazil">Brasil e Cone Sul Escritório Regional</option>
               <option value="colombia">La Oficina de las Naciones Unidas contra la Droga y el Delito</option></select></div>
      </div>
      <div id="gooSearchButtonBox"><input type="submit" name="btnG" value="Search" id="gooSearchButton"></div>
      <input type="hidden" name="site" value="unodc">
      <input type="hidden" name="proxyreload" value="1">
      <input type="hidden" name="sort" value="date:D:L:d1">
      <input type="hidden" name="entqr" value="0">
      <input type="hidden" name="entqrm" value="0">
      <input type="hidden" name="ud" value="1">
      
   </form>
</div>
<div id="gooSearchedFor">Searched for '<span>Cross-border</span>'
</div>
<div id="gooTopSepBar">
   <div id="googooResultStats">Results <b>1</b> - <b>10</b> of about <b>3640</b>.
      
   </div>
   <div id="gooSearchTime">Search took <b>0.1</b> seconds.
   </div>
</div>
<div id="gooSortBy"><a href="/unodc/search.html?site=unodc&amp;proxyreload=1&amp;q=Cross-border&amp;entqr=0&amp;entqrm=0&amp;ud=1&amp;sort=date%3AD%3AS%3Ad1">Sort by date</a><span> / Sort by relevance</span></div>
<!--tro2-->
<div><div class="gooResult">
   <div class="gooDocType"></div> 
   <div class="gooResultURL"><a href="http://www.unodc.org/unodc/en/frontpage/2011/June/organized-crime-organized-responses-countering-cross-border-criminality.html">Organized crime, organized responses: countering <b>cross</b> <b>...</b></a></div>
   <div class="gooResSnippet"><b>...</b> Organized crime, organized responses - countering <b>cross</b>-<b>border</b> crime.<br> 9 June 2011 - As a major
      threat to human security <b>...</b>  
   </div>
   <div class="gooResultURLText">www.unodc.org/unodc/en/frontpage/2011/June/organized-crime-organized-responses-countering-cross-border-criminality.html</div>
   <div class="gooResMisc"> - 8k</div></div><div class="gooResult Lev02">
   <div class="gooDocType"></div> 
   <div class="gooResultURL"><a href="http://www.unodc.org/unodc/en/frontpage/2014/March/cross-border-cooperation-key-in-addressing-central-and-west-asias-drug-trafficking-problem.html"><b>Cross</b>-<b>border</b> cooperation key in addressing Central and West <b>...</b></a></div>
   <div class="gooResSnippet"><b>...</b> <b>Cross</b>-<b>border</b> cooperation key in addressing Central and West Asia&#39;s drug<br> trafficking problem.
      17 March 2014 - The trafficking <b>...</b>  
   </div>
   <div class="gooResultURLText">www.unodc.org/unodc/en/frontpage/2014/March/cross-border-cooperation-key-in-addressing-central-and-west-asias-drug-trafficking-problem.html</div>
   <div class="gooResMisc"> - 6k - 2014-03-19</div>
   <div class="gooMoreSiteLink">
      [
      <a class="f" href="/unodc/search.html?as_sitesearch=www.unodc.org/unodc/en/frontpage&amp;site=unodc&amp;proxyreload=1&amp;q=Cross-border&amp;sort=date:D:L:d1&amp;entqr=0&amp;entqrm=0&amp;ud=1">More results from www.unodc.org/unodc/en/frontpage</a>
      ]
      
   </div></div><div class="gooResult">
   <div class="gooDocType"></div> 
   <div class="gooResultURL"><a href="http://www.unodc.org/southeastasiaandpacific/en/what-we-do/criminal-justice/cross-border.html"><b>Cross</b>-<b>border</b> criminal justice cooperation</a></div>
   <div class="gooResSnippet"><b>...</b> What we do: UNODC assists Member States to be able to more effectively<br> cooperate on <b>cross</b>-<b>border</b>
      criminal justice issues, working with regional <b>...</b>  
   </div>
   <div class="gooResultURLText">www.unodc.org/southeastasiaandpacific/en/what-we-do/criminal-justice/cross-border.html</div>
   <div class="gooResMisc"> - 4k - 2015-10-09</div></div><div class="gooResult">
   <div class="gooDocType"></div> 
   <div class="gooResultURL"><a href="http://www.unodc.org/southasia/en/frontpage/2015/June/india-bhutan-crossborder-cooperation-to-prevent-human-trafficking-and-smuggling-of-migrants.html">India – Bhutan: <b>Cross</b>-<b>border</b> cooperation to prevent human <b>...</b></a></div>
   <div class="gooResSnippet"><b>...</b> India - Bhutan: <b>Cross</b>-<b>border</b> cooperation to prevent human trafficking and<br> smuggling of migrants.
      India and Bhutan share open borders. <b>...</b>  
   </div>
   <div class="gooResultURLText">www.unodc.org/southasia/en/frontpage/2015/June/india-bhutan-crossborder-cooperation-to-prevent-human-trafficking-and-smuggling-of-migrants.html</div>
   <div class="gooResMisc"> - 5k</div></div><div class="gooResult">
   <div class="gooDocType"></div> 
   <div class="gooResultURL"><a href="http://www.unodc.org/centralasia/en/news/enhancing-cross-border-cooperation.html">Enhancing <b>Cross</b>-<b>Border</b> Cooperation</a></div>
   <div class="gooResSnippet"><b>...</b> Contact Us; Regional database; Drug Statistics. Enhancing <b>Cross</b>-<b>Border</b><br> Cooperation. First technical
      workshop on the <b>cross</b> <b>...</b>  
   </div>
   <div class="gooResultURLText">www.unodc.org/centralasia/en/news/enhancing-cross-border-cooperation.html</div>
   <div class="gooResMisc"> - 4k</div></div><div class="gooResult">
   <div class="gooDocType"></div> 
   <div class="gooResultURL"><a href="http://www.unodc.org/southeastasiaandpacific/en/vietnam/2012/11/patrol/story.html">Using theory and practice to fight <b>cross</b>-<b>border</b> crimes</a></div>
   <div class="gooResSnippet"><b>...</b> Using theory and practice to fight <b>cross</b>-<b>border</b> crimes. Ho Chi Minh City (Viet<br> Nam), 15 November
      2012 - It would be as easy as usual, he thought. <b>...</b>  
   </div>
   <div class="gooResultURLText">www.unodc.org/southeastasiaandpacific/en/vietnam/2012/11/patrol/story.html</div>
   <div class="gooResMisc"> - 5k - 2013-04-02</div></div><div class="gooResult">
   <div class="gooDocType"></div> 
   <div class="gooResultURL"><a href="http://www.unodc.org/southeastasiaandpacific/en/2010/11/patrol-cambodia/story.html">Commitment on <b>cross</b>-<b>border</b> cooperation grows fast in <b>...</b></a></div>
   <div class="gooResSnippet"><b>...</b> Commitment on <b>cross</b>-<b>border</b> cooperation grows fast in Cambodia.<br> Phnom Penh (Cambodia), 8 November
      2010 - In May <b>...</b>  
   </div>
   <div class="gooResultURLText">www.unodc.org/southeastasiaandpacific/en/2010/11/patrol-cambodia/story.html</div>
   <div class="gooResMisc"> - 4k - 2013-04-02</div></div><div class="gooResult Lev02">
   <div class="gooDocType"></div> 
   <div class="gooResultURL"><a href="http://www.unodc.org/southeastasiaandpacific/en/2010/08/cbt-blo-cambodia-laos/story.html">Cambodia and the Lao People&#39;s Democratic Republic <b>...</b></a></div>
   <div class="gooResSnippet"><b>...</b> Cambodia and the Lao People&#39;s Democratic Republic increase<br> <b>cross</b>-<b>border</b> cooperation. Preah
      Vihear (Cambodia)/Ban <b>...</b>  
   </div>
   <div class="gooResultURLText">www.unodc.org/southeastasiaandpacific/en/2010/08/cbt-blo-cambodia-laos/story.html</div>
   <div class="gooResMisc"> - 4k - 2013-04-02</div>
   <div class="gooMoreSiteLink">
      [
      <a class="f" href="/unodc/search.html?as_sitesearch=www.unodc.org/southeastasiaandpacific/en/2010&amp;site=unodc&amp;proxyreload=1&amp;q=Cross-border&amp;sort=date:D:L:d1&amp;entqr=0&amp;entqrm=0&amp;ud=1">More results from www.unodc.org/southeastasiaandpacific/en/2010</a>
      ]
      
   </div></div><div class="gooResult">
   <div class="gooDocType"></div> 
   <div class="gooResultURL"><a href="http://www.unodc.org/unodc/en/human-trafficking/regional-workshop-western-balkans.html">Regional Workshop Western Balkans</a></div>
   <div class="gooResSnippet"><b>...</b> Western Balkans: <b>Cross Border</b> Cooperation on the Migrant Crisis. In<br> February 2016, according to Der
      Standard, a Serbian <b>...</b>  
   </div>
   <div class="gooResultURLText">www.unodc.org/unodc/en/human-trafficking/regional-workshop-western-balkans.html</div>
   <div class="gooResMisc"> - 6k - 2016-04-13</div></div><div class="gooResult">
   <div class="gooDocType"></div> 
   <div class="gooResultURL"><a href="http://www.unodc.org/southeastasiaandpacific/en/myanmar/2016/08/blo-data-training/story.html">Myanmar frontline officers strengthen capacities to track <b>cross</b> <b>...</b></a></div>
   <div class="gooResSnippet"><b>...</b> See also: More about Border management. Myanmar frontline officers<br> strengthen capacities to track <b>cross</b>-<b>border</b>
      criminals. <b>...</b>  
   </div>
   <div class="gooResultURLText">www.unodc.org/southeastasiaandpacific/en/myanmar/2016/08/blo-data-training/story.html</div>
   <div class="gooResMisc"> - 4k - 2016-08-19</div></div>
</div><div id="gooNavTablecenter">
Result Page&nbsp;<span>&nbsp;<span class="i">1</span>&nbsp;</span><span>&nbsp;<a href="/unodc/search.html?site=unodc&amp;proxyreload=1&amp;q=Cross-border&amp;sort=date:D:L:d1&amp;entqr=0&amp;entqrm=0&amp;ud=1&amp;start=10">2</a>&nbsp;</span><span>&nbsp;<a href="/unodc/search.html?site=unodc&amp;proxyreload=1&amp;q=Cross-border&amp;sort=date:D:L:d1&amp;entqr=0&amp;entqrm=0&amp;ud=1&amp;start=20">3</a>&nbsp;</span><span>&nbsp;<a href="/unodc/search.html?site=unodc&amp;proxyreload=1&amp;q=Cross-border&amp;sort=date:D:L:d1&amp;entqr=0&amp;entqrm=0&amp;ud=1&amp;start=30">4</a>&nbsp;</span><span>&nbsp;<a href="/unodc/search.html?site=unodc&amp;proxyreload=1&amp;q=Cross-border&amp;sort=date:D:L:d1&amp;entqr=0&amp;entqrm=0&amp;ud=1&amp;start=40">5</a>&nbsp;</span><span>&nbsp;<a href="/unodc/search.html?site=unodc&amp;proxyreload=1&amp;q=Cross-border&amp;sort=date:D:L:d1&amp;entqr=0&amp;entqrm=0&amp;ud=1&amp;start=50">6</a>&nbsp;</span><span>&nbsp;<a href="/unodc/search.html?site=unodc&amp;proxyreload=1&amp;q=Cross-border&amp;sort=date:D:L:d1&amp;entqr=0&amp;entqrm=0&amp;ud=1&amp;start=60">7</a>&nbsp;</span><span>&nbsp;<a href="/unodc/search.html?site=unodc&amp;proxyreload=1&amp;q=Cross-border&amp;sort=date:D:L:d1&amp;entqr=0&amp;entqrm=0&amp;ud=1&amp;start=70">8</a>&nbsp;</span><span>&nbsp;<a href="/unodc/search.html?site=unodc&amp;proxyreload=1&amp;q=Cross-border&amp;sort=date:D:L:d1&amp;entqr=0&amp;entqrm=0&amp;ud=1&amp;start=80">9</a>&nbsp;</span><span>&nbsp;<a href="/unodc/search.html?site=unodc&amp;proxyreload=1&amp;q=Cross-border&amp;sort=date:D:L:d1&amp;entqr=0&amp;entqrm=0&amp;ud=1&amp;start=90">10</a>&nbsp;</span><span class="gooNavItem">&nbsp;<span class="b"><a href="/unodc/search.html?site=unodc&amp;proxyreload=1&amp;q=Cross-border&amp;sort=date:D:L:d1&amp;entqr=0&amp;entqrm=0&amp;ud=1&amp;start=10">Next</a></span></span></div>
<div id="gooSearchBox">
   <form name="gs1" method="GET" action="/unodc/search.html">
      <div id="gooSearchInput"><input type="text" name="q" id="gooInputField" maxlength="256" value="Cross-border">
         <div id="gooCollections"><select name="site" id="gooCollectionsSelect">
               <option value="unodc" selected>All UNODC web sites</option>
               <option value="india">Regional Office for South Asia</option>
               <option value="brazil">Brasil e Cone Sul Escritório Regional</option>
               <option value="colombia">La Oficina de las Naciones Unidas contra la Droga y el Delito</option></select></div>
      </div>
      <div id="gooSearchButtonBox"><input type="submit" name="btnG" value="Search" id="gooSearchButton"></div>
      <input type="hidden" name="site" value="unodc">
      <input type="hidden" name="proxyreload" value="1">
      <input type="hidden" name="sort" value="date:D:L:d1">
      <input type="hidden" name="entqr" value="0">
      <input type="hidden" name="entqrm" value="0">
      <input type="hidden" name="ud" value="1">
      
   </form>
</div><span class="p"></span></div></div></div><div id="footer"><ul class="toolbarlist"><li><a href="/unodc/en/index.html">Home</a></li><li><a href="/unodc/en/site-map.html">Sitemap</a></li><li><a href="/unodc/en/contact-us.html">Contact Us</a></li><li><a href="/unodc/en/fraud-alert.html">Fraud Alert</a></li><li><a href="https://www.unodc.org/frontdoor/">Login</a></li><li><a target="_new" href="http://www.un.org">www.un.org</a></li></ul><p>Copyright<span>&copy;</span>2016<span>&nbsp;</span>UNODC, All Rights Reserved, <a href="/unodc/en/legal.html" class="legalnotice">Legal Notice</a></p></div></div><script type="text/javascript">
var _gaq = _gaq || [];_gaq.push(['_setAccount', 'UA-9293036-1']);_gaq.push(['_trackPageview']);
(function() {
var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
})();
</script></body></html>

"""


soup = BeautifulSoup(html_doc, "lxml")

print '---------------------------------'
# 解析得到网页链接

founds = soup.find('div', id='contentWrapper').find_all('div', class_='gooResult')
print len(founds)

item_list = []
print '------------url---------------'
id = 0
for found in founds:
    id += 1
    print id
    # item = items.PostItem()
    title = found.find('div', class_='gooResultURL').get_text().strip()
    url = found.find('div', class_='gooResultURL').find('a').get('href')
    print title
    print url
    m = md5.new() 
    m.update(url)
    md_str = m.hexdigest()
    print md_str

    post_time = found.find('div', class_='gooResMisc').get_text().strip()
    # post_time1 = ' - 4k - 2015-10-09'
    # post_time2 = ' - 8k'
    post_time = post_time.split('- ')
    # print len(post_time)
    # l = len(post_time)
    if len(post_time) == 3:
        post_time = post_time[2] + " 00:00:00"
        print post_time
    else:
        post_time = '2013-06-01 00:00:00'
        print post_time
    # print post_time

print '-------------------------------'
#得到下一页链接，寻找最后一个span标签

next_pages = soup.find('div', id='gooNavTablecenter').find('span', class_='gooNavItem')
try:
    next_page = next_pages.find('span', class_='b').a['href']
    next_page = 'https://www.unodc.org' + next_page
    print next_page
except:
    print 'last page-----'
