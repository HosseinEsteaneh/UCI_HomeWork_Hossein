# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd 
import pymongo
import requests

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars = {}

    # Mars Article
    # define news url
    mars_news_url = "https://mars.nasa.gov/news/"
    browser.visit(mars_news_url)
    # create beautiful soup object
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve the latest news title and paragraph
    article = soup.find("div", class_='list_text')
    news_title = article.find("div", class_="content_title").text
    news_p = article.find("div", class_ ="article_teaser_body").text

    # Mars Image
    # define mars images url
    mars_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(mars_image_url)
    # create beautiful soup object
    html = browser.html
    images_soup = BeautifulSoup(html, 'html.parser')
    # retrieve featured image link
    main_url = "https://www.jpl.nasa.gov"
    relative_image_path = images_soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]
    featured_image_url = main_url + relative_image_path

    # Mars Facts
    # define mars facts url
    mars_facts_url = "https://space-facts.com/mars/"
    browser.visit(mars_facts_url)
    # Use Pandas to scrape the table containing facts about Mars
    tables = pd.read_html(mars_facts_url)
    mars_facts = tables[0]
    # Rename the columns
    mars_facts.columns= ['Description', 'Value']
    # Reset the index
    mars_facts = mars_facts.to_html(index=False, header=False, border=0, classes="table table-sm table-striped font-weight-light")

    # Mars Hemispheres
    # define mars hemispheres url
    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres_url)
    # create beautiful soup object
    html = browser.html
    hemisphere_soup = BeautifulSoup(html, 'html.parser')
    # Create a list of dictionaries to store titles & links to images
    hemisphere_image_urls = []

    # Retrieve all elements that contain image information
    results = hemisphere_soup.find("div", class_ = "result-list" )
    hemispheres = results.find_all("div", class_="item")

    # Iterate through each image
    for hemisphere in hemispheres:
        title = hemisphere.find("h3").text
        title = title.replace("Enhanced", "")
        end_link = hemisphere.find("a")["href"]
        image_link = "https://astrogeology.usgs.gov/" + end_link    
        browser.visit(image_link)
        html = browser.html
        soup = BeautifulSoup(html, "html.parser")
        downloads = soup.find("div", class_="downloads")
        image_url = downloads.find("a")["href"]
        hemisphere_image_urls.append({"title": title, "img_url": image_url})

    # Mars
    mars = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_facts": mars_facts,
        "hemisphere_image_urls": hemisphere_image_urls
    }

    browser.quit()

    return mars