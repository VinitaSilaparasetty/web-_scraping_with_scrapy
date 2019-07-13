{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf500
{\fonttbl\f0\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red255\green255\blue255;\red114\green137\blue4;
\red113\green130\blue132;\red164\green118\blue5;\red38\green146\blue134;\red33\green120\blue201;\red71\green91\blue98;
}
{\*\expandedcolortbl;;\cssrgb\c0\c1\c1;\cssrgb\c100000\c100000\c99985;\cssrgb\c51734\c59494\c0;
\cssrgb\c51517\c58196\c58851;\cssrgb\c70483\c53115\c0;\cssrgb\c16584\c63320\c59740;\cssrgb\c15379\c55095\c82900;\cssrgb\c34646\c43291\c45950;
}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl360\partightenfactor0

\f0\fs32\fsmilli16200 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 import\cf2 \cb3 \strokec5  scrapy\
\
\
\cf2 \cb3 \strokec4 class\cf2 \cb3 \strokec5  \cf2 \cb3 \strokec6 AliexpressTabletsSpider\cf2 \cb3 \strokec5 (scrapy.Spider):\
    name = \cf2 \cb3 \strokec7 'aliexpress_tablets'\cf2 \cb3 \strokec5 \
    allowed_domains = [\cf2 \cb3 \strokec7 'aliexpress.com'\cf2 \cb3 \strokec5 ]\
    start_urls = [\cf2 \cb3 \strokec7 'https://www.aliexpress.com/category/200216607/tablets.html'\cf2 \cb3 \strokec5 ,\
                 \cf2 \cb3 \strokec7 'https://www.aliexpress.com/category/200216607/tablets/2.html?site=glo&g=y&tag='\cf2 \cb3 \strokec5 ]\
\
\
    \cf2 \cb3 \strokec4 def\cf2 \cb3 \strokec5  \cf2 \cb3 \strokec8 parse\cf2 \cb3 \strokec5 (self, response):\
\
        print(\cf2 \cb3 \strokec7 "procesing:"\cf2 \cb3 \strokec5 +response.url)\
        \cf2 \cb3 \strokec9 #Extract data using css selectors\cf2 \cb3 \strokec5 \
        product_name=response.css(\cf2 \cb3 \strokec7 '.product::text'\cf2 \cb3 \strokec5 ).extract()\
        price_range=response.css(\cf2 \cb3 \strokec7 '.value::text'\cf2 \cb3 \strokec5 ).extract()\
        \cf2 \cb3 \strokec9 #Extract data using xpath\cf2 \cb3 \strokec5 \
        orders=response.xpath(\cf2 \cb3 \strokec7 "//em[@title='Total Orders']/text()"\cf2 \cb3 \strokec5 ).extract()\
        company_name=response.xpath(\cf2 \cb3 \strokec7 "//a[@class='store $p4pLog']/text()"\cf2 \cb3 \strokec5 ).extract()\
\
        row_data=zip(product_name,price_range,orders,company_name)\
\
        \cf2 \cb3 \strokec9 #Making extracted data row wise\cf2 \cb3 \strokec5 \
        \cf2 \cb3 \strokec4 for\cf2 \cb3 \strokec5  item \cf2 \cb3 \strokec4 in\cf2 \cb3 \strokec5  row_data:\
            \cf2 \cb3 \strokec9 #create a dictionary to store the scraped info\cf2 \cb3 \strokec5 \
            scraped_info = \{\
                \cf2 \cb3 \strokec9 #key:value\cf2 \cb3 \strokec5 \
                \cf2 \cb3 \strokec7 'page'\cf2 \cb3 \strokec5 :response.url,\
                \cf2 \cb3 \strokec7 'product_name'\cf2 \cb3 \strokec5  : item[\cf2 \cb3 \strokec7 0\cf2 \cb3 \strokec5 ], \cf2 \cb3 \strokec9 #item[0] means product in the list and so on, index tells what value to assign\cf2 \cb3 \strokec5 \
                \cf2 \cb3 \strokec7 'price_range'\cf2 \cb3 \strokec5  : item[\cf2 \cb3 \strokec7 1\cf2 \cb3 \strokec5 ],\
                \cf2 \cb3 \strokec7 'orders'\cf2 \cb3 \strokec5  : item[\cf2 \cb3 \strokec7 2\cf2 \cb3 \strokec5 ],\
                \cf2 \cb3 \strokec7 'company_name'\cf2 \cb3 \strokec5  : item[\cf2 \cb3 \strokec7 3\cf2 \cb3 \strokec5 ],\
            \}\
\
            \cf2 \cb3 \strokec9 #yield or give the scraped info to scrapy\cf2 \cb3 \strokec5 \
            \cf2 \cb3 \strokec4 yield\cf2 \cb3 \strokec5  scraped_info}