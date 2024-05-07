import scrapy
from fashion_scrap.items import AsosFashionItems
import json

class AsosSpiderSpider(scrapy.Spider):
    name = "asos_spider"
    start_urls = ['https://www2.hm.com/en_us/men/new-arrivals/view-all.html']
    headers={
        'Cookie':'preshoppingUser=false; HMCORP_locale=en_US; HMCOUNTRY_name=United States; HMCORP_locale_autoassigned=false; OptanonAlertBoxClosed=2024-04-17T19:59:21.253Z; utag_main_vapi_domain=hm.com; _scid=1d7ec461-0bb4-4270-94e9-1229482139ad; hmid=F3A98C4D-54D5-44CD-BA7E-A594F308C723; _ga=GA1.2.1699250401.1713383962; _gcl_au=1.1.1793225122.1713383962; s_ecid=MCMID%7C27763651983216717411052356172931740590; _fbp=fb.1.1713383962794.950574006; _tt_enable_cookie=1; _ttp=AzXToLTfjE1Rlt-YMBHxoZn_DSy; _pin_unauth=dWlkPU1EZG1ZakF3TURBdE9HSTRaQzAwWVRjd0xUZ3dZbU10T1Rkak5tTTJNR1JsWVdSaw; __attentive_id=daca92c6e9824fd29de8dd99b3b7da74; _attn_=eyJ1Ijoie1wiY29cIjoxNzEzMzgzOTY2MzU5LFwidW9cIjoxNzEzMzgzOTY2MzU5LFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcImRhY2E5MmM2ZTk4MjRmZDI5ZGU4ZGQ5OWIzYjdkYTc0XCJ9In0=; __attentive_cco=1713383966366; optimizelyEndUserId=oeu1713383976001r0.545857588310283; agCookie=0e9ad7e5-c5f6-4997-8537-025f916b9f70; _cs_c=0; hm-us-cart=ae7bb7fb-4cc4-4d31-a227-e2f43c4eec0c; peseg=pseg%3D16995268; ogseg=ogsegs%3D16995268; bazsegs=baz%3D16995268; dedsegs=ded%3D16995268; aemsegs=aem%3D16995268%3B6494087%3B26147686; aamoptsegs=aam%3D16995268%2Caam%3D6494087%2Caam%3D25168856%2Caam%3D13197145%2Caam%3D26147686; _gid=GA1.2.1828031684.1714030786; _sctr=1%7C1713985200000; hm-us-favourites=""; aamgasegs=segid%3D16792613%3B16792620%3B16792636%3B16792625%3B16995268%3B16995331%3B20439960%3B6494087%3B21544055%3B21544058%3B13197145%3B26147686; akainst=AM; AKA_A2=A; _abck=5939EA0CE1E44A14DDB2E77434E60A57~0~YAAQxKwwF7u0XOaOAQAA7AOAGwsH7Nl3B9OhQYE3Lc8kyScwzK+Ou51U88vcFxk0NVQRiB6S5kSKCdoC+moHVNFMxrwYmXkMePXk+xgzrgvweUyMQ4waViXtfS6aQJtUFpl83PYokbNMXyj13TdxwH7lBma6Ack1qF/CRIk6DecM2l6VXMir2uvlpCPUCXt3Z9dbFJ24M79fBuKsxY1kkwMo2s3Jg+MjfcWHnRRA2+bBldXlSa/mcBHEP4k9ifXa8eCeb0egfAhvZVgV3F9HQLK2O03fKBqh2c5ZFJ1WxL7vYLCEUoAGNjTSffclToj2TthdyKCCUubcRj8RY0rVDXqnt1sGBzJDhuplEfEkPUYO2EvVQ82wotCgg3l0dlkm6vJfFNk6TfQggw/Gh8Xt185LAe+O~-1~-1~1714156925; INGRESSCOOKIE=1714153327.07.477.164047|ce11af63eaca573be5110d180bb330ca; JSESSIONID=414127DE7331F27DED33DD02FDF84BF1E0E64DEB1EE0B6C7B5D7F56CDE325428CA1C306C4CC637DF303AC170A94157612F3B85CB7A2C0A035DA4B3F01085C552.hybris-ecm-web-6bc645c756-p2grf; userCookie=##eyJjYXJ0Q291bnQiOjB9##; ak_bmsc=70729AAA23FD72BF3BD70711D9CC7451~000000000000000000000000000000~YAAQxKwwF8y0XOaOAQAA2BWAGxdfJDgDHGnXsRn/JJGi923kF1hJWCId+CGhbuxhFS0p9qMGYDtUb5AH4GmvQ7Xurlf7cOAxJXfCziN0dZlb1SjeDwaYKfP9rXhrLZQnZ/HywChAcgOtAp6Ve17sw3twZ+EOaWoOgT8Jwf9CVWlRA6cimyHNfOEqKFzlxEjrMP+5oB+/iD3xcaL2JdpAZQr55+cDQR5UTTTOIiFC1zVvmSl+Sm4iOQYbzakkDJCQbLvcrU9RpBiOL45RI82SnSCPRoPvMi6gL64MaXcO91B8NWpP3i/l3SMwUZhPXaKvV9j3k6vRIw7iLSg4uRj5OaKRFzXijDitR9MlrTwwtS6RJvJ9M/QJPk1p2ZXjTBWEe4XiDpQhvj8ZB+fuKobkd8LImCSe+qZGYD3q+HK7ZZqKG+hRLIKOowur2kBkwYVryd4b5D5D6kI=; utag_main__sn=14; utag_main_ses_id=1714153331142%3Bexp-session; dep_sid=s_1646890567983699.1714153331160; utag_main_segment=dep-test-data%3Bexp-session; utag_main_cart_active=No%3Bexp-session; _cs_mk_ga=0.6371892908749957_1714153336705; utag_main__ss=0%3Bexp-session; AMCVS_32B2238B555215F50A4C98A4%40AdobeOrg=1; AMCV_32B2238B555215F50A4C98A4%40AdobeOrg=179643557%7CMCIDTS%7C19840%7CMCMID%7C27763651983216717411052356172931740590%7CMCAAMLH-1714758137%7C3%7CMCAAMB-1714758137%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1714160537s%7CNONE%7CMCAID%7CNONE%7CMCCIDH%7C1824003287%7CMCSYNCSOP%7C411-19845%7CvVersion%7C5.5.0; __attentive_ss_referrer=ORGANIC; __attentive_dv=1; _uetsid=fdcdad8002d611ef9dd7edf95881532a; _uetvid=fbcedcf0fcf411eeb05f6f8f57513f19; _cs_id=5a8a59cb-0e73-a407-b7b6-32b599b590f5.1713716131.9.1714153380.1714153337.1671006191.1747880131433.1; _cs_s=2.5.0.1714155180149; _scid_r=1d7ec461-0bb4-4270-94e9-1229482139ad; __attentive_pv=2; _gat_GA_GLOBAL=1; bm_sz=13C54E4C0C92F4D1FB15BFF7B97EC2BE~YAAQxKwwF1m2XOaOAQAA2KKCGxfJQDR187SwsD1efO1lxxU24Qqt+XUXeEg6eKvN8uBg7qSTQzH3RsG5TV3ig/MGwm3z50XwTuUWfItSQH1TJGkbWDnpSvODuUnTH2z/oJstyZbj/0Uxd13lZoG0up97I/rCqGyWs11NJB5J+IEz1aREDJtV32YEBmBalVM90qlRHPWnmwfdHzZCojqwB3P3YjSDvHVCERstLcCVFl0o9hxOZSX3cyhL3g27h4LBTittP5k987NZv77Rv5ZY5UXi/ooINlhkoh9Cpm1yKDZQmnm4gwI+eFw2SFgcO2DReF7E0aBlUojWiV24h3Vv2wV0bQFwG6ql80guU7rSvRQOb2P/IPRchn7O+i1VjZ5qiINRfFrGUlef36y8z1xvC2x7Cu8/y62nxw==~3621700~4276531; RT="z=1&dm=hm.com&si=b16c9ffd-9083-4715-8fbb-52c6478b5962&ss=lvgyml5u&sl=2&tt=i6m&bcn=%2F%2F684d0d4c.akstat.io%2F"; utag_main__pn=3%3Bexp-session; utag_main__se=7%3Bexp-session; utag_main__st=1714155299876%3Bexp-session; dep_exp=Fri, 26 Apr 2024 18:14:59 GMT; _ga_Z1370GPB5L=GS1.2.1714153337.14.1.1714153501.56.0.0; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Apr+26+2024+22%3A45%3A02+GMT%2B0500+(Pakistan+Standard+Time)&version=202401.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=af48bb3b-bab8-47ef-ac46-cc0c528c4b39&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=PK%3BSD&AwaitingReconsent=false; akamref=en_us; akavpau_www2_en_us=1714153803~id=23628f9b9aab17d183953352973512b5; bm_sv=0426F6AECF32D848F03F31FD77A70B1C~YAAQxKwwF2a2XOaOAQAAe7mCGxe10dgz/GOyOW0vHj7WmON5mz4/8uUolbQwu4jqzoWqN8ea7TFlLlMTWe2NKq/qbjtH4T1TAVHcOGLeBwwGh0OFPGqzARjD8Gmg0tr0EA/BTJ4faIElyG3MqPkQkD8T4n1B8EEYSDUvH/1beOuW1/pb2mdsXshuybrxRdEB4ln3MdZACVWREyRtfwb49nqP68ekvMwZy2Ms01NG/eZOHKSPCAFjOutZigg=~1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
        'Accept':'application/json',
        'Content-Type':'application/json',
        ':authority': 'www2.hm.com',
        ':method': 'POST',
        ':path':'/en_us/pra/panel/product-detail-page',

    }



    def parse(self, response):
        products = response.xpath('//article[@class="f0cf84"]')
        for product in products:
            product_url = product.xpath('//a[@class="db7c79"]/@href').get()
            print(f'----------------------------->{product_url} <------------------------')
            yield scrapy.Request(url=product_url, callback=self.parse_details)
    def parse_details(self,response):
        print('-------------------------------------- DETAILS ------------------------------------')
        yield scrapy.Request(url='https://www2.hm.com/en_us/pra/panel/product-detail-page',headers=self.headers,callback=self.parse_json_data)
    def parse_json_data(self,response):
        data = json.loads(response.body)
        print(data)
        print('--------------------- Data was Yielded------------------------')



