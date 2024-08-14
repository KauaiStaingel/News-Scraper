from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import config
import pandas as pd
import sys
import os

#---------------------------------------------------------------------------#

#All elements functions receives the time,text or wanted elements by parameter

def click_element_by_selector(element_selector,time):#Click on element by the elements selector
        element = WebDriverWait(browser,time).until(EC.visibility_of_element_located((By.CSS_SELECTOR,element_selector)))
        element.click()

def find_element_by_tag(element_tag,time,web_element):#Return an element found by its tag
        element = WebDriverWait(web_element,time).until(EC.visibility_of_element_located((By.TAG_NAME,element_tag)))
        return element

def find_element_by_class(element_class,time,web_element):#Return an element found by its class
        element = WebDriverWait(web_element,time).until(EC.visibility_of_element_located((By.CLASS_NAME,element_class)))
        return element

def find_all_element_by_tag(element_tag,time,web_element):#Return all elements found by its tag
        elements = WebDriverWait(web_element,time).until(EC.visibility_of_all_elements_located((By.TAG_NAME,element_tag)))
        return elements 

def write_element_by_selector(element_selector,time,text):#Write a text in an element by its selector
        element = WebDriverWait(browser,time).until(EC.visibility_of_element_located((By.CSS_SELECTOR,element_selector)))
        element.send_keys(text)

def scroll_element_selector(element_selector,time):#scroll the page to an element by its selector

    element = WebDriverWait(browser,time).until(EC.visibility_of_element_located((By.CSS_SELECTOR,element_selector)))
    action = ActionChains(browser)
    action.move_to_element(element).perform()

def press_enter():#Function used to simulate an ENTER press
    action = ActionChains(browser)
    action.send_keys(Keys.ENTER)
    action.perform()

#---------------------------------------------------------------------------#

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument('--log-level=3') # show only some error messages
    options.add_argument('--headless') # set the browser to run on background
    options.add_argument("window-size=1920x1080")
    try:#checks and remove if a file with other news exists
        os.remove('news.xlsx')
    except:
        pass
    try:
        search = str(input("Type the news you want to search:\n"))
        print("Searching...")
        browser = webdriver.Chrome(options=options)
        browser.get(config.url)
        try:#checks if the website asks for cookies
            click_element_by_selector('button[data-testid ="Accept all-btn"]',7)
        except:
            pass
        try:#search the news in the site
            click_element_by_selector('button[aria-controls="search-input"]',7)
            write_element_by_selector('input[data-testid="search-input"]',7,search)
            press_enter()
        except Exception as e:
            print('Searching error.')
            print(f'Error: {e}')
            browser.quit()
            sys.exit()

        while True:
            try:#loop responsible for gathering all news in the page
                scroll_element_selector('button[data-testid="search-show-more-button"]',7)
                click_element_by_selector('button[data-testid="search-show-more-button"]',7)
            except:
                break


        ol_on_page = find_element_by_tag('ol',7,browser)#accessing the ol with the news
        li_on_page = find_all_element_by_tag('li',7,ol_on_page)#gets all the news inside the ol

        titles = []
        descriptions = []
        news_dates = []
        images_links = []

        for li in li_on_page:
            try:#loop for each news and get its components
                title = find_element_by_tag('css-nsjm9t',2,li) 
                titles.append(title.text)
                news_date = find_element_by_class('css-17ubb9w',2,li) 
                news_dates.append(news_date.text)
                try:
                    description = find_element_by_class('css-16nhkrn',2,li) 
                    descriptions.append(description.text)
                except:
                    descriptions.append("News without description.")
                try:
                    image = find_element_by_class('css-rq4mmj',2,li) 
                    images_links.append(image.get_attribute("src"))
                except:
                    images_links.append("News without image.")
            except:
                    pass
        
        print('All news found.')
        #Creates the Dataframe with all the information got in the previous loop
        df = pd.DataFrame(titles, columns = ['Titles'])
        df['Descriptions'] = descriptions
        df['Dates'] = news_dates
        df['Image Links'] = images_links

        print('Creating excel file.')
        df.to_excel("news.xlsx", index=False)#Creates the excel file by the Dataframe, with its name in the parameters
        print('Excel file created.')
    except Exception as e:
        print('Searching error.')
        print(f'Error: {e}')
        browser.quit()
        sys.exit()