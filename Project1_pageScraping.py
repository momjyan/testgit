
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import sys
import datetime






#############
driver = webdriver.Chrome()
driver.get("file:///C:/Users/hakobm/Documents/MyPython/Selenium/Upwork/Project1_Scraping09102018/10000_-----Ticketmaster%20Delivery.htm#order")


#print ("Python version: " + sys.version)


## Section

file = open("Data.txt","w+")
file.write("* * * * *  Python Version * * * * * " + "\n"+ 
	         sys.version + "\n" + "\n" +
	         "* * * * * Data * * * * *" + "\n")


	## define labels
labelLeft1 = driver.find_element_by_xpath("//div[@id='ticketFrame']/div[1]/div[2]/div[1]/h3[1]")
labelLeft2 = driver.find_element_by_xpath("//div[@id='ticketFrame']/div[1]/div[2]/div[1]/h3[2]")
labelLeft3 = driver.find_element_by_xpath("//div[@id='ticketFrame']/div[1]/div[2]/div[1]/h3[3]")
labelLeft4 = driver.find_element_by_xpath("//div[@id='ticketFrame']/div[1]/div[5]/h3")

time = driver.find_element_by_xpath("//div[@id='countdown_clock']/div[2]") 
## Values for Labels
valueRight1 = driver.find_element_by_xpath("//div[@id='ticketFrame']/div[1]/div[2]/div[1]/div[1]")
valueRight2 = driver.find_element_by_xpath("//div[@id='ticketFrame']/div[1]/div[2]/div[1]/div[2]")
valueRight3 = driver.find_element_by_xpath("//div[@id='ticketFrame']/div[1]/div[2]/div[1]/div[3]")
valueRight4 = driver.find_element_by_xpath("//div[@id='ticketFrame']/div[1]/div[5]/div[1]")

if ((labelLeft1.text == "Section")  and (labelLeft2.text == "Row") and (labelLeft3.text == "Seats") and (labelLeft4.text == "SUBTOTAL*")):
	#print ("Section " + valueRight1.text + "\n" + "Row " + valueRight2.text + "\n" +"Seats " + valueRight3.text + "\n" +"SUBTOTAL " + valueRight4.text)
	file.write( "Section " + valueRight1.text + "\n" + 
		"Row " + valueRight2.text + "\n" + 
		"Seats " + valueRight3.text + "\n" + 
		"SUBTOTAL " + valueRight4.text+"\n\n")




#print (time.text+"\n\n\n")
file.write(time.text+"\n\n\n")
file.write("- - - - - - - - - - - - - - -" + "\n")
file.write(datetime.datetime.now().ctime())
file.close()


#re.search(r'<div.*?>(*?)</div>',name.get_attribute('innerHTML')).group(1)

