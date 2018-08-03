import requests
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import os
import json
import os.path
from selenium.common.exceptions import NoSuchElementException

with open("config.json") as file:
    config = json.load(file)
    file.close()


email = config['email']
password = config['password']
firstname = config['firstN']
lastname = config['lastN']
dob = config['dob']
amount = config['amount']


desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
ext = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# amount
num = amount

def main():
    count = 0

    # number of instances
    for i in range(int(num)):

        # task number
        count = count+1

        chrome_options = webdriver.ChromeOptions()

		# window size
        chrome_options.add_argument("window-size=1100,900")

		# proxy setting
        chrome_options.add_extension(ext+"\SMS\extension_2_0_0_0.crx");

        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path = desktop+'/chromedriver.exe')


        print('Tasks '+'{}: Getting url...').format(count)

        # open url
        driver.get('https://www.nike.com/us/en_us/')

        # click join
        driver.find_element_by_xpath('/html/body/div[7]/nav/div[1]/ul[2]/li[2]/button/span').click()
        time.sleep(0.5)

        # click sign up
        driver.find_element_by_link_text('Join now.').click()
        html_source = driver.page_source

        # determining if it has reached correct page
        if "By creating an account" in html_source:
            print('Tasks '+'{}: Creating Account...').format(count)
        else:
            print('Tasks '+'{}: Failed to Create Account').format(count)

        # send info
        print('Tasks '+'{}: Sending info..').format(count)
        driver.find_element_by_name('emailAddress').send_keys(email)
        driver.find_element_by_name('password').send_keys(password)
        driver.find_element_by_name('firstName').send_keys(firstname)
        driver.find_element_by_name('lastName').send_keys(lastname)
        driver.find_element_by_name('dateOfBirth').send_keys('')
        driver.find_element_by_xpath("//span[text()='Male']").click()
        driver.find_element_by_class_name('checkbox').click()
        driver.find_element_by_xpath("//*[@value='CREATE ACCOUNT']").click()
        driver.close()

# call the function
main()
