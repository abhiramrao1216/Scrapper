
import scrapy
import random

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = [
        'https://www.linkedin.com/company/usebraintrust?trk=public_jobs_jserp-result_job-search-card-subtitle',
        'https://www.linkedin.com/company/centraprise?trk=public_jobs_jserp-result_job-search-card-subtitle'
    ]


    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse_response, headers={'User-Agent': random.choice(self.user_agents)})

    def parse_response(self, response):
        # company_item = {}

        # company_item['name'] = response.css('.top-card-layout__entity-info h1::text').get(default='not-found').strip()
        # company_item['summary'] = response.css('.top-card-layout__entity-info h4 span::text').get(default='not-found').strip()

        try:
            # company_details = response.css('.core-section-container__content .mb-2')
            # company_industry_line = company_details[1].css('.text-md::text').getall()
            # company_item['industry'] = company_industry_line[1].strip()
            # company_size_line = company_details[2].css('.text-md::text').getall()
            # company_item['size'] = company_size_line[1].strip()
            # company_size_line = company_details[5].css('.text-md::text').getall()
            # company_item['founded'] = company_size_line[1].strip()


            
            div_element = response.css('.core-section-container__content')[2]
            # ul_selector = div_element.css('.ul::text').getall()
            #print(div_element)
            links = div_element.css('a')
            for link in links:
                href = link.attrib['href'] 
                # Printing employees profile links
                print(href)
                yield scrapy.Request(href, callback=self.parse_response2, headers={'User-Agent': random.choice(self.user_agents)})
                #yield response.follow(href, callback=self.parse_link)



            
            # people_profiles = {}
            # people_profiles_info = response.css('.details mx-details-container-padding')
            # last_section = people_profiles_info.css('section:last-child')
            # inner_div_content = last_section.css('div')
            # ul_selector = inner_div_content.css('ul')
            # li_elements = ul_selector.css('li::text').getall()
        except IndexError:
            self.logger.error("error")


    def parse_response2(self, response):
        try:
            item = {}
            item['profile'] = response.css('title::text').get()
            item['description'] = response.css('meta[name="og:description"]::attr(content)').get()
            # description_content = response.css('meta[name="description"]::attr(content)').get()

            print("Title:", item['profile'])
            #print("DESCRIPTION:", item['description'])

            # h2_content = response.css('section > h2::text').get()
            # print(h2_content)
            # p_content = response.css('section > div.core-section-container p::text').get()
            # print(p_content)

            h2_in_section = response.css('section.core-section-container')[0]
            inner_div_content = h2_in_section.css('div')
            i_elements = inner_div_content.css('p::text').getall()  
            print("DESCRIPTION:",i_elements)
            # first_div_with_class = response.css('section.core-section-container > div.core-section-container:first-child')

            # p_elements = first_div_with_class.css('p::text').getall()

            # print("DESCRIPTION:", p_elements)


            print('***********************************************')
            # summary_box = response.css("section.top-card-layout")
            # description = summary_box.css("h2::text").get().strip()
            # #print(description)
            # title = response.css('title::text').get()
            # print("Title:", title)

            # divs_with_class_x = response.css('.details mx-details-container-padding')


        except IndexError:
            self.logger.error("error")
                     
        
