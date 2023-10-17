import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd


url = 'https://svensksolenergi.se/sok-medlemsforetag/#!'
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument('--headless')
chrome_options.binary_location = r'C:\chrome-win64\chrome.exe'
driver = webdriver.Chrome(service=Service(ChromeDriverManager(driver_version='116').install()), options=chrome_options)
driver.get(url)
driver.maximize_window()
time.sleep(3)
try: driver.find_element(By.XPATH, '//a[@class="modal-cacsp-btn modal-cacsp-btn-accept"]').click()
except: pass
time.sleep(2)


company_name = []
elec_name = []
website = []
contact_email = []
local_address = []
post_code = []
linkedin = []
city = []
elec_reg = []
inst_reg = []
plat_reg = []

a1489 = []
a2619 = []
a2504 = []
a2585 = []
a2597 = []
a5308 = []
a2618 = []
a2507 = []
a2505 = []
a2506 = []
a2586 = []
a2508 = []
a2704 = []
a2509 = []
a2511 = []
a2503 = []
a2617 = []
a2512 = []
a2661 = []

b2539 = []
b2540 = []
b2541 = []
b2542 = []
b2543 = []
b2544 = []
b2545 = []
b2546 = []
b2547 = []
b2548 = []
b2549 = []
b2550 = []
b2551 = []
b2552 = []
b2553 = []
b2554 = []
b2555 = []
b2556 = []
b2557 = []
b2558 = []
b2560 = []
URL = []


count = 0
cat_rows = driver.find_elements(By.XPATH, '//h4[text()="Verksamhet" or text()="Län"]//following-sibling::ul/li')
for cat_row in cat_rows:
    category = cat_row.find_element(By.XPATH, './input[@type="checkbox"]')
    category.click()
    time.sleep(3)
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

    while True:
        try:
            count2 = 0
            rows = driver.find_elements(By.XPATH, '//li[contains(@class,"mira-list-item")]')
            for row in rows:
                company_name.append(row.find_element(By.XPATH, './/h3//span[@x-text="item.name"]').text)
                try: elec_name.append(row.find_element(By.XPATH, './/div[@class="mira-list-item-content-meta"]//span[@x-text="item.contact"]').text)
                except: elec_name.append(None)
                try: website.append(row.find_element(By.XPATH, './/div[@class="mira-list-item-content-meta"]//a[@x-text="item.url"]').text)
                except: website.append(None)
                try: contact_email.append(row.find_element(By.XPATH, './/div[@class="mira-list-item-content-meta"]//a[@x-text="item.email"]').text)
                except: contact_email.append(None)
                try: local_address.append(row.find_element(By.XPATH, './/div[@class="mira-list-item-content-info"]//span[@x-text="item.address"]').text)
                except: local_address.append(None)
                try: post_code.append(row.find_element(By.XPATH, './/div[@class="mira-list-item-content-info"]//span[@x-text="item.zip"]').text)
                except: post_code.append(None)
                try: linkedin.append(row.find_element(By.XPATH, './/div[@class="mira-list-item-content-info"]//span[@x-show="item.linkedin"]/a').get_attribute('href'))
                except: linkedin.append(None)
                try: city.append(row.find_element(By.XPATH, './/div[@class="mira-list-item-content-info"]//span[@x-text="item.city"]').text)
                except: city.append(None)
                try:
                    electricity = row.find_element(By.XPATH, './/div[@class="mira-list-item-content-cta"]//div[@class="mira-filter-certified mira-list-item-content-certified" and @style="display: none;"]')
                    elec_reg.append('No')
                except: elec_reg.append('Yes')
                try:
                    installers = row.find_element(By.XPATH, './/div[@class="mira-list-item-content-cta"]//div[@class="mira-filter-certified2 mira-list-item-content-certified2" and @style="display: none;"]')
                    inst_reg.append('No')
                except: inst_reg.append('Yes')
                try:
                    platinum = row.find_element(By.XPATH, './/span[contains(@x-show,"premium") and @style="display: none;"]')
                    plat_reg.append('No')
                except: plat_reg.append('Yes')

                a1489.append(1) if '1489' in driver.current_url else a1489.append(0)
                a2619.append(1) if '2619' in driver.current_url else a2619.append(0)
                a2504.append(1) if '2504' in driver.current_url else a2504.append(0)
                a2585.append(1) if '2585' in driver.current_url else a2585.append(0)
                a2597.append(1) if '2597' in driver.current_url else a2597.append(0)
                a5308.append(1) if '5308' in driver.current_url else a5308.append(0)
                a2618.append(1) if '2618' in driver.current_url else a2618.append(0)
                a2507.append(1) if '2507' in driver.current_url else a2507.append(0)
                a2505.append(1) if '2505' in driver.current_url else a2505.append(0)
                a2506.append(1) if '2506' in driver.current_url else a2506.append(0)
                a2586.append(1) if '2586' in driver.current_url else a2586.append(0)
                a2508.append(1) if '2508' in driver.current_url else a2508.append(0)
                a2704.append(1) if '2704' in driver.current_url else a2704.append(0)
                a2509.append(1) if '2509' in driver.current_url else a2509.append(0)
                a2511.append(1) if '2511' in driver.current_url else a2511.append(0)
                a2503.append(1) if '2503' in driver.current_url else a2503.append(0)
                a2617.append(1) if '2617' in driver.current_url else a2617.append(0)
                a2512.append(1) if '2512' in driver.current_url else a2512.append(0)
                a2661.append(1) if '2661' in driver.current_url else a2661.append(0)

                b2539.append(1) if '2539' in driver.current_url else b2539.append(0)
                b2540.append(1) if '2540' in driver.current_url else b2540.append(0)
                b2541.append(1) if '2541' in driver.current_url else b2541.append(0)
                b2542.append(1) if '2542' in driver.current_url else b2542.append(0)
                b2543.append(1) if '2543' in driver.current_url else b2543.append(0)
                b2544.append(1) if '2544' in driver.current_url else b2544.append(0)
                b2545.append(1) if '2545' in driver.current_url else b2545.append(0)
                b2546.append(1) if '2546' in driver.current_url else b2546.append(0)
                b2547.append(1) if '2547' in driver.current_url else b2547.append(0)
                b2548.append(1) if '2548' in driver.current_url else b2548.append(0)
                b2549.append(1) if '2549' in driver.current_url else b2549.append(0)
                b2550.append(1) if '2550' in driver.current_url else b2550.append(0)
                b2551.append(1) if '2551' in driver.current_url else b2551.append(0)
                b2552.append(1) if '2552' in driver.current_url else b2552.append(0)
                b2553.append(1) if '2553' in driver.current_url else b2553.append(0)
                b2554.append(1) if '2554' in driver.current_url else b2554.append(0)
                b2555.append(1) if '2555' in driver.current_url else b2555.append(0)
                b2556.append(1) if '2556' in driver.current_url else b2556.append(0)
                b2557.append(1) if '2557' in driver.current_url else b2557.append(0)
                b2558.append(1) if '2558' in driver.current_url else b2558.append(0)
                b2560.append(1) if '2560' in driver.current_url else b2560.append(0)

                URL.append(driver.current_url)


                # Extras
                print(f'\n\n{count2} row done... [{len(company_name)}, {len(elec_name)}, {len(website)}, {len(contact_email)}, {len(local_address)}, {len(post_code)}, {len(linkedin)}, {len(city)}, {len(elec_reg)}, {len(inst_reg)}, {len(plat_reg)}, {len(a1489)}, {len(a2619)}, {len(a2504)}, {len(a2585)}, {len(a2597)}, {len(a5308)}, {len(a2618)}, {len(a2507)}, {len(a2505)}, {len(a2506)}, {len(a2586)}, {len(a2508)}, {len(a2704)}, {len(a2509)}, {len(a2511)}, {len(a2503)}, {len(a2617)}, {len(a2512)}, {len(a2661)}, {len(b2539)}, {len(b2540)}, {len(b2541)}, {len(b2542)}, {len(b2543)}, {len(b2544)}, {len(b2545)}, {len(b2546)}, {len(b2547)}, {len(b2548)}, {len(b2549)}, {len(b2550)}, {len(b2551)}, {len(b2552)}, {len(b2553)}, {len(b2554)}, {len(b2555)}, {len(b2556)}, {len(b2557)}, {len(b2558)}, {len(b2560)}, {len(URL)}]')
                count2 += 1

            # Pagination
            try:
                next_page = driver.find_element(By.XPATH, '(//li[@class="pagination-item pagination-item-next"]//i)[1]')
                next_page.click()
                time.sleep(3)
                driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                print('Next page')
            except:
                break

        except:
            break

    category2 = driver.find_element(By.XPATH, '//input[@checked="checked"]')
    category2.click()
    time.sleep(3)
    print(f'{count} CATEGORY DONE...')
    count += 1


data_dict = {
    'Sr #': [i+1 for i in range(len(company_name))],
    'Company name': company_name,
    'Electrician name': elec_name,
    'Website': website,
    'Contact email': contact_email,
    'Local address': local_address,
    'Post Code': post_code,
    'LinkedIn': linkedin,
    'City': city,
    'Registered for electrical safety': elec_reg,
    'Has certified installers': inst_reg,
    'Platinum/Gold Status?': plat_reg,

    'Besiktningsföretag': a1489,
    'Byggföretag': a2619,
    'Elhandelsföretag': a2504,
    'Elnätsföretag': a2585,
    'Fastighetsföretag': a2597,
    'Finansiering av solprojekt': a5308,
    'Forskning': a2618,
    'Grossist': a2507,
    'Innovationsföretag': a2505,
    'Installationsföretag': a2506,
    'Juridiskt konsultföretag': a2586,
    'Kringtjänster': a2508,
    'Medlemsorganisation': a2704,
    'Projektutvecklare, t ex solparker': a2509,
    'Tekniskt konsultföretag': a2511,
    'Tillverkare': a2503,
    'Universitet och högskola': a2617,
    'Utbildningsföretag': a2512,
    'YH-utbildare': a2661,

    'Blekinge': b2539,
    'Dalarna': b2540,
    'Gotland': b2541,
    'Gävleborg': b2542,
    'Halland': b2543,
    'Jämtland': b2544,
    'Jönköping': b2545,
    'Kalmar': b2546,
    'Kronoberg': b2547,
    'Norrbotten': b2548,
    'Skåne': b2549,
    'Stockholm': b2550,
    'Södermanland': b2551,
    'Uppsala': b2552,
    'Värmland': b2553,
    'Västerbotten': b2554,
    'Västernorrland': b2555,
    'Västmanland': b2556,
    'Västra Götaland': b2557,
    'Örebro': b2558,
    'Östergötland': b2560,

    'URL': URL,
}
df = pd.DataFrame(data_dict)
df.to_excel('snevs_data2.xlsx', index=False)
