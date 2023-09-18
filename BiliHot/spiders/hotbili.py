import scrapy
from selenium import webdriver
from BiliHot.items import BilihotItem
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
options.add_argument('headless')

class HotbiliSpider(scrapy.Spider):
    name = 'hotbili'
    week_urls = []
    count = 0
    video_urls = []

    # start_urls = ['https://www.bilibili.com/v/popular/weekly?num=145']
    def __init__(self):
        self.bro = webdriver.Chrome(executable_path="D:\Python_Project\BiliSpider\BiliHot\chromedriver.exe",
                                    chrome_options=options)

    def start_requests(self):
        for week in range(94, 146):
            self.week_urls.append("https://www.bilibili.com/v/popular/weekly?num={0}".format(week))

        for url in self.week_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        week_videos = response.xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[@class="video-card"]')
        week_info = response.xpath('//*[@id="app"]//div[@class="select-item item-active"]/p[@class="item-info"]/text()') \
            .extract_first().strip().replace('\n', '')
        week_num = select(week_info, '第', '期')
        week_time = week_info.split('期 ', 2)[1]
        item = BilihotItem()
        item['week'] = week_num
        item['week_time'] = week_time
        for week_video in week_videos:
            video_url = "https:" + week_video.xpath('./div[@class="video-card__content"]/a/@href').extract_first()
            self.video_urls.append(video_url)

        for v in self.video_urls:
            yield scrapy.Request(url=v, callback=self.parse_video, meta={'item': item})
            # yield item

    def parse_video(self, response):
        if response.text != "":
            item = response.meta['item']
            video_wrap = response.xpath('//*[@id="app"]/div[@class="v-wrap"]')
            video_url = response.xpath('/html/head/meta[@itemprop="url"]/@content').get()
            upname = response.xpath('/html/head/meta[@name="author"]/@content').get()
            title = response.xpath('/html/head/meta[@name="title"]/@content').get()
            play_count = response.xpath('//*[@id="viewbox_report"]/div/span[1]/@title').get()
            dm_count = response.xpath('//*[@id="viewbox_report"]/div/span[2]/@title').get()
            video_time = response.xpath('//*[@id="viewbox_report"]/div/span[3]/text()').get()
            like_count = response.xpath('//*[@id="arc_toolbar_report"]/div[1]/span[1]/@title').get()
            coin_count = response.xpath('//*[@id="arc_toolbar_report"]/div[1]/span[2]/text()') \
                .extract_first().strip().replace('\n', '')
            collect_count = response.xpath('//*[@id="arc_toolbar_report"]/div[1]/span[3]/text()') \
                .extract_first().strip().replace('\n', '')
            share_count = response.xpath('//*[@id="arc_toolbar_report"]/div[1]/span[4]/text()') \
                .extract_first().strip().replace('\n', '')
            v_tags = video_wrap.xpath('//*[@id="v_tag"]/ul/li/a/span/text()').getall()

            item['bvid'] = video_url.split('video/')[1].split('/')[0]
            item['upname'] = upname
            item['title'] = title.replace('_哔哩哔哩_bilibili', '')
            item['play_count'] = play_count
            item['dm_count'] = dm_count
            item['video_time'] = video_time

            item['like_count'] = like_count
            item['coin_count'] = coin_count
            item['collect_count'] = collect_count
            item['share_count'] = share_count
            item['v_tags'] = '·'.join(v_tags)

            yield item


    def close_bro(self, spider):
        print('爬虫结束！')
        self.bro.quit()


def select(str, l_tag, r_tag):
    return str.split(l_tag)[1].split(r_tag)[0]


