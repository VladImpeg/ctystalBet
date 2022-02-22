from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from flask import Flask, render_template, request

from bs4 import BeautifulSoup 
import urllib 
import requests
from time import sleep

options = webdriver.ChromeOptions()

options.add_argument("start-maximized")

options.add_argument('--profile-directory=Profile 1')
options.add_argument('--disable-web-security')
user_agent = '''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'''
options.add_argument('--no-sandbox')
options.add_argument("--disable-infobars")
options.add_argument("--enable-file-cookies")

options.add_argument('user-agent={0}'.format(user_agent))
#options.add_argument('--disable-dev-shm-usage')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)


driver = webdriver.Chrome(options=options, executable_path=r'/chromedriver')

driver.get("https://www.crystalbet.com/Pages/LiveBetting.aspx")
sleep(9)





x = 25
#25 just for fun
while x == 25:
	driver.get("https://www.crystalbet.com/Pages/LiveBetting.aspx")
	# waiting for the page to load - TODO: change
	wait = WebDriverWait(driver, 10)
	app=Flask(__name__, template_folder='templates')
	app.debug=True
	wait.until(EC.visibility_of_element_located((By.ID, "ctl00_ctl00_ContentPlaceHolder1_LiveStreamUserControl_PanelGameTracker")))
	
	data = driver.page_source
	
	soup = BeautifulSoup(data, "html.parser")
	area = soup.find("div", {"class": "tracker-iframe"})
	print(str(area))
	@app.route("/")
	def index():
		with app.app_context() :
			return render_template("file.html", block=area)
	    
	index()
	page = urllib.request.urlopen('https://www.crystalbet.com/Pages/LiveBetting.aspx').read()
	soup = BeautifulSoup(page)
	body = soup.find('body')
	the_contents_of_body_without_body_tags = body.findChildren(recursive=False)
	with open("/var/www/API/file.html", "w") as file:
		file.write('<body>' + str(the_contents_of_body_without_body_tags) + '</body>')
	break
