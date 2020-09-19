from config import keys
from selenium import webdriver
import time

#this bot is item type dependant (sort of). Some items do not have certain fields
#if you want a specific item lmk and ill make a bot tailored to that item. 


# function makes it easy to execute
def order(keys):
   
    driver.get(keys['products'])
    
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/form/fieldset[2]/input').click()

    time.sleep(1)
    
    try:
        driver.find_element_by_xpath('//*[@id="s"]/option[{}]'.format(keys['size'])).click()
    except:
        print('no size')
        
    driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()

    driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(keys["name"])

    driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(keys["email"])

    driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(keys["phone"])

    driver.find_element_by_xpath('//*[@id="bo"]').send_keys(keys["address"])

    driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(keys["zip"])

    driver.find_element_by_xpath('//*[@id="rnsnckrn"]').send_keys(keys["cardn"])

    driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(keys["ccv"])

	#state drop down
    driver.find_element_by_xpath('//*[@id="order_billing_state"]/option[45]').click()
    
	#terms/conditions
    driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p/label/div/ins').click()

    #//*[@id="cart-cc"]/fieldset/p/label/div/ins
    #//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins
    
	#expirations 
    driver.find_element_by_xpath('//*[@id="credit_card_month"]/option[{}]'.format(keys["month"])).click()
       
	#year cc
    driver.find_element_by_xpath('//*[@id="credit_card_year"]/option[{}]'.format(keys["year"])).click()

	#process payment    
    driver.find_element_by_xpath('//*[@id="pay"]/input').click()


if __name__ == '__main__':
    driver = webdriver.Chrome('./chromedriver')
    order(keys) 
