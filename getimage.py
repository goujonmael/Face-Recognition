from icrawler.builtin import BingImageCrawler

classes=['visage'] 
number=250
for c in classes:
    bing_crawler=BingImageCrawler(storage={'root_dir':'images/n'})
    bing_crawler.crawl(keyword=c,filters=None,max_num=number,offset=0)