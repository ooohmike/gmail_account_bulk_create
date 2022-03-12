# IMPORTS

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import configs as conf
import buysim
import chrome_driver_configs as chronfigs
from proxy_auth import manifest_json, background_js, plugin_file
import os
import zipfile
from random import choice

class Proxies:
    proxy_list = []

    @staticmethod
    def load_proxies(file_path: str):
        """
        Reads a text file with proxies
        :param file_path: Path to proxy file with proxies in <user>:<pas>@<ip>:<port> format each on one line
        """
        lst = []
        if file_path:
            if os.path.exists(file_path):
                with open(file_path, 'r') as file:
                    lst = [x for x in file.read().split('\n') if x.strip()]
            else:
                print('File: {}. Does not exist.'.format(file_path))
        Proxies.proxy_list = lst

    @staticmethod
    def get_random_proxy():
        """ Returns a random proxy """
        return choice(Proxies.proxy_list)

class GmailBulk :
    
    
        def __init__(self, base_url, driver):
            
            self.base_url = base_url
            self.driver = driver
            
        
    
        def open_gmail_signup(self):
            
            # Open Gmail Signup Page 
            self.driver.get(conf.BASE_URL)
            time.sleep(2)
            
            
        
        def signup_page_1(self, mailno):
            str_mailno = str(mailno)
            
            lang_select = self.driver.find_element(By.CSS_SELECTOR, '#lang-chooser > div:nth-child(1) > div.ry3kXd.Ulgu9 > div.MocG8c.B9IrJb.LMgvRb.KKjvXb')
            lang_select.click()
            time.sleep(3)
            lang_select_option = self.driver.find_element(By.CSS_SELECTOR, 'div[data-value="en"][role="option"]')
            lang_select_option.click()
            time.sleep(2)
            first_name = self.driver.find_element(By.XPATH, '//*[@id="firstName"]')
            first_name.send_keys(conf.FIRST_NAME)
            
            last_name = self.driver.find_element(By.XPATH, '//*[@id="lastName"]')
            last_name.send_keys(conf.LAST_NAME)
            
            gmail_id = self.driver.find_element(By.XPATH, '//*[@id="username"]')
            gmail_id.send_keys(conf.USER_ID + str_mailno.zfill(3))
            
            password = self.driver.find_element(By.XPATH, '//*[@id="passwd"]/div[1]/div/div[1]/input')
            password.send_keys(conf.PASSWORD)
            
            confirm_password = self.driver.find_element(By.XPATH, '//*[@id="confirm-passwd"]/div[1]/div/div[1]/input')
            confirm_password.send_keys(conf.PASSWORD)
            
            time.sleep(2)
            
            next_button = self.driver.find_element(By.XPATH, '//*[@id="accountDetailsNext"]//span')
            next_button.click()
    

        def signup_page_2(self):
            # time.sleep(5)
            while True:
                phone_number = WebDriverWait(self.driver, 500).until(EC.presence_of_element_located((By.XPATH, '//input[@id="phoneNumberId"]')))
                time.sleep(10)
                str_phone = ""
                str_id = 0
                str_code = ""
                while True:
                    print("waiting for new order.....")
                    while True:
                        ret = buysim.buy_google_number()
                        # print(ret)
                        try:
                            if ('phone' in ret):
                                str_phone = ret["phone"]
                                str_id = ret["id"]
                                break
                        except Exception as e:
                            pass
                        time.sleep(5)
                    time.sleep(1)
                    # phone_number = self.driver.find_element(By.XPATH, '//input[@id="phoneNumberId"]')
                    while True:
                        time.sleep(1)
                        try:
                            phone_number.send_keys(Keys.CONTROL + "a")
                            phone_number.send_keys(str_phone)
                            break
                        except Exception as e:
                            pass

                    next_button_2 = self.driver.find_element(By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')
                    next_button_2.click()
                    time.sleep(1)
                    error_msgs = self.driver.find_elements(By.CSS_SELECTOR, "div[aria-live = 'assertive'] font")
                    error_msgs_1 = self.driver.find_elements(By.CSS_SELECTOR, "div[aria-live = 'assertive'] span")
                    # print("error", error_msgs)
                    if(len(error_msgs) < 3 and len(error_msgs_1) == 0):
                        print("success")
                        break
                    else:
                        print("banning order.....")
                        buysim.ban_order(str_id)
                    time.sleep(1)
                for i in range(10):
                    print("getting sms.....")
                    ret = buysim.get_sms(str_id)
                    if('sms' in ret and len(ret['sms']) > 0):
                        str_code = ret['sms'][0]['code']
                        buysim.finish_order(str_id)
                        break
                    time.sleep(15)
                # print(i)
                if(str_code == ""):
                    print("canceling order.....")
                    buysim.cancel_order(str_id)
                    back_button = self.driver.find_element(By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div[1]/div/div/button')
                    back_button.click()
                    time.sleep(5)
                else: 
                    break
            
            # phone_code = input("Enter Verification Code : ")
            phone_verify = self.driver.find_element(By.XPATH, '//*[@id="code"]')
            phone_verify.send_keys(str_code)
            phone_verify.send_keys(Keys.ENTER)
            # time.sleep(1000)
            time.sleep(2)
            
            
            
        def signup_page_3(self):
            
    
            time.sleep(2)
            month = self.driver.find_element(By.XPATH, '//*[@id="month"]')
            month.send_keys("j")
            
            day = self.driver.find_element(By.XPATH, '//*[@id="day"]')
            day.send_keys("1")
            
            year = self.driver.find_element(By.XPATH, '//*[@id="year"]')
            year.send_keys("1995")
            
        
            gender = self.driver.find_element(By.XPATH, '//*[@id="gender"]/option[3]')
            gender.click()

            time.sleep(2)
            
            next_button_4 = self.driver.find_element(By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')
            next_button_4.click()
            
            
            
            time.sleep(3)
            
           
            skip_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div/button')
            skip_button.click()
            
            time.sleep(5)
        
            
            agree_button = self.driver.find_element(By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')
            time.sleep(1)
            agree_button.click()
            f = open('result.txt', 'a')
            f.write("address: " + conf.USER_ID + str_mailno.zfill(3) + "\t" + "password: " + conf.PASSWORD + "\n")
            f.close()
            time.sleep(2)

        def less_secure_app(self):
            time.sleep(2)
            self.driver.get(conf.LESS_SECURE_URL)
            security_menu = self.driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/c-wiz/div/div[4]/div/div/div/ul/li/div[1]/div[2]/div/button/div[2]/div/div[2]')
            # security_menu.click()
            self.driver.execute_script("arguments[0].click();", security_menu)
            time.sleep(2)

        def run(self, addrno):
            self.open_gmail_signup()
            self.signup_page_1(addrno+1)
            self.signup_page_2()
            self.signup_page_3()
            self.less_secure_app()
            time.sleep(2)
            self.driver.quit()
                
                                                
if __name__ == "__main__":
    
    print("Initialising")
    
    Proxies.load_proxies('proxies.txt')
    options = chronfigs.get_chromdriver_options()
    chronfigs.set_ignore_certificate_error(options)
    # chronfigs.set_incognito_mode(options)

    # chrome_options = webdriver.ChromeOptions()
    
    random_proxy = Proxies.get_random_proxy()
    # Parse Proxy
    auth, ip_port = random_proxy.split('@')
    user, pwd = auth.split(':')
    ip, port = ip_port.split(':')

    with zipfile.ZipFile(plugin_file, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js % (ip, port, user, pwd))
    options.add_extension(plugin_file)

    # return webdriver.Chrome(chrome_options=chrome_options)

    for i in range(2, 5):
        driver = chronfigs.get_chrome_driver(options)
        gmail_bulk = GmailBulk(conf.BASE_URL, driver)
        gmail_bulk.run(i)
        str_mailno = str(i+1)
        
    print("Done")