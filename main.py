from selenium import webdriver
import time
from lxml import html
import requests
import json

ans = 'y'
while(ans):
    dl_no = input("Enter your DL Number : ")
    dob = input("Enter your DOB : ")
    web = webdriver.Chrome('./chromedriver.exe')
    web.get('https://parivahan.gov.in/rcdlstatus/?pur_cd=101')
    page = requests.get("https://parivahan.gov.in/rcdlstatus/?pur_cd=101")
    tree = html.fromstring(page.content)

    time.sleep(5)

    dl_path = web.find_element_by_xpath('//*[@id="form_rcdl:tf_dlNO"]')
    dob_path = web.find_element_by_xpath('//*[@id="form_rcdl:tf_dob_input"]')

    dl_path.send_keys(dl_no)
    dob_path.send_keys(dob)

    time.sleep(15)
    submit = web.find_element_by_xpath('//*[@id="form_rcdl:j_idt50"]')
    submit.click()

    time.sleep(5)

    current_status = tree.xpath('//*[@id="form_rcdl:j_idt71"]/table[1]/tbody/tr[1]/td[2]/span/text()')
    name = tree.xpath('//*[@id="form_rcdl:j_idt71"]/table[1]/tbody/tr[2]/td[2]/text()')
    date_of_issue = tree.xpath('//*[@id="form_rcdl:j_idt71"]/table[2]/tbody/tr[1]/td[2]/text()')
    issuing_office = tree.xpath('//*[@id="form_rcdl:j_idt71"]/table[2]/tbody/tr[2]/td[2]/text()')
    date_of_expiry = tree.xpath('//*[@id="form_rcdl:j_idt71"]/table[3]/tbody/tr[1]/td[3]/text()')
    class_of_vehicle = tree.xpath('//*[@id="form_rcdl:j_idt123_data"]/tr/td[2]/text()')

    result = {
        "Name of Holder : ": name,
        "Date of Birth : ": dob,
        "Driving Licence Number : ": dl_no,
        "Date of Issue : ": date_of_issue,
        "Date of Expiry : ": date_of_expiry,
        "Initial Issuing Office : ": issuing_office,
        "Current Status : ": current_status,
        "Class of Vehicle : ": class_of_vehicle
    }

    json_object = json.dumps(result,indent = 4)
    print(json_object)
    ans = input('Do you want to continue? [y/n]')
