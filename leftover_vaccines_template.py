
# AUTOMATED SIGNUP PROCESS FOR LEFTOVER VACCINES IN REGION NORDJYLLAND

# The script checks if the user's chosen location(s) offer(s) vaccinations today
# and signs up the user for leftover vaccines at the relevant location(s)

# REQUIREMENTS:
# - Selenium
# - ChromeDriver

# INSTRUCTIONS:
# - Type in your path to ChromeDriver
# - Uncomment your invitation status and comment the rest
# - Type in your details as strings
# - Add your location(s) to list
# - Run script

########################################################################################################

# EDIT THIS PART

# Type in your path to ChromeDriver
chrome_driver_path = r"\path\to\driver"

# Choose your invitation status
invitation_status = '//*[@id="ch_1601148219-1601148221"]'     #  Invitation received
#invitation_status = '//*[@id="ch_1601148219-1601148222"]'    #  No invitation received
#invitation_status = '//*[@id="ch_1601148219-1601148223"]'    #  Don't know

# Add your details
full_name = "firstname lastname"
age = "0"
phone_number = "12345678"

# Possible location(s)
location1 = "MESSEVEJ 1, 9600 AARS"
location2 = "HÅNDVÆRKERVEJ 24C, 9000 AALBORG"
location3 = "HARALD NIELSENS PLADS 9, 9900 FREDERIKSHAVN"
location4 = "AMERIKAVEJ 22, 9500 HOBRO"
location5 = "FUGLSIGVEJ 23, 9800 HJØRRING"
location6 = "MUNKEVEJ 9E, 7700 THISTED"

# Add your location(s) to the list selected_locations (separated by commas if more than one)
selected_locations = [location1, location2]

########################################################################################################

# DON'T EDIT THIS PART

import sys
from datetime import date
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# XPaths of location checkboxes
location_checkboxes = {
    "MESSEVEJ 1, 9600 AARS": '//*[@id="ch_337561929-337561931"]',
    "HÅNDVÆRKERVEJ 24C, 9000 AALBORG": '//*[@id="ch_337561929-337561936"]',
    "HARALD NIELSENS PLADS 9, 9900 FREDERIKSHAVN": '//*[@id="ch_337561929-1601148227"]',
    "AMERIKAVEJ 22, 9500 HOBRO": '//*[@id="ch_337561929-1601148225"]',
    "FUGLSIGVEJ 23, 9800 HJØRRING": '//*[@id="ch_337561929-1601148226"]',
    "MUNKEVEJ 9E, 7700 THISTED": '//*[@id="ch_337561929-337561938"]'
}

# XPaths of vaccination locations for each day
day1 = '//*[@id="outercontent_0_zone1_0_ctl08_repModules_ctl00_AccordionModule1_AccordionListRepeater_AccordionGrid1_3_ctl00_3_repModules_3_ctl01_3_MultiModule1_3_MultiModuleGrid_3_MultiModuleGridContent_3"]'
day2 = '//*[@id="outercontent_0_zone1_0_ctl08_repModules_ctl00_AccordionModule1_AccordionListRepeater_AccordionGrid1_3_ctl00_3_repModules_3_ctl02_3_MultiModule1_3_MultiModuleGrid_3_MultiModuleGridContent_3"]'
day3 = '//*[@id="outercontent_0_zone1_0_ctl08_repModules_ctl00_AccordionModule1_AccordionListRepeater_AccordionGrid1_3_ctl00_3_repModules_3_ctl03_3_MultiModule1_3_MultiModuleGrid_3_MultiModuleGridContent_3"]'
day4 = '//*[@id="outercontent_0_zone1_0_ctl08_repModules_ctl00_AccordionModule1_AccordionListRepeater_AccordionGrid1_3_ctl00_3_repModules_3_ctl04_3_MultiModule1_3_MultiModuleGrid_3_MultiModuleGridContent_3"]'
day5 = '//*[@id="outercontent_0_zone1_0_ctl08_repModules_ctl00_AccordionModule1_AccordionListRepeater_AccordionGrid1_3_ctl00_3_repModules_3_ctl05_3_MultiModule1_3_MultiModuleGrid_3_MultiModuleGridContent_3"]'
day6 = '//*[@id="outercontent_0_zone1_0_ctl08_repModules_ctl00_AccordionModule1_AccordionListRepeater_AccordionGrid1_3_ctl00_3_repModules_3_ctl06_3_MultiModule1_3_MultiModuleGrid_3_MultiModuleGridContent_3"]'
day7 = '//*[@id="outercontent_0_zone1_0_ctl08_repModules_ctl00_AccordionModule1_AccordionListRepeater_AccordionGrid1_3_ctl00_3_repModules_3_ctl07_3_MultiModule1_3_MultiModuleGrid_3_MultiModuleGridContent_3"]'

weekday_xpaths = [day1, day2, day3, day4, day5, day6, day7]

# Get week day and week number
weekday = date.today().weekday()
weeknum = date.today().isocalendar()[1]

# Launch browser without creating a visual browser window
# and go to page with vaccination locations
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(chrome_driver_path, options=options)
driver.implicitly_wait(2)  # wait 2 sec if element cannot be found
locations_url = "https://rn.dk/restvacciner?accordion-expand=Vaccinations-steder-og-datoer_uge-" + str(weeknum) + "_KLON"
driver.get(locations_url)

# Find vaccination locations of today
locations = driver.find_element_by_xpath(weekday_xpaths[weekday]).text.upper()

# Remove locations that do not offer vaccinations today from user's list
[selected_locations.remove(location) for location in selected_locations if location not in locations]

# Close program if none of the selected locations offer vaccinations today
if len(selected_locations) == 0:
    print("Der vaccineres ikke på din(e) valgte lokation(er) i dag.")
    sys.exit()

# Go to signup page
signup_url = "https://eur03.safelinks.protection.outlook.com/?url=https%3A%2F%2Fskema.rn.dk%2FLinkCollector%3Fkey%3DNNX2AGF6JK35&data=04%7C01%7C%7C4f69357da2b0446a6a4208d8e47b04ee%7C5968b90c51a64f088b4750ffffbe2e4f%7C0%7C0%7C637510564294119451%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C1000&sdata=qFv1iD2etsU16A2e9FMiH%2FPXkJ2Qh4OTyaslgRDAP%2Fg%3D&reserved=0"
driver.get(signup_url)

# Find text fields and clickable elements
invitation_radio = driver.find_element_by_xpath(invitation_status)
name_field = driver.find_element_by_xpath('//*[@id="t337561910"]')
age_field = driver.find_element_by_xpath('//*[@id="n337561915"]')
phone_field = driver.find_element_by_xpath('//*[@id="t337561922"]')
submit = driver.find_element_by_xpath('/html/body/div/form/div[2]/div[3]/input')

# Fill out form
driver.execute_script("arguments[0].click()", invitation_radio)
name_field.send_keys(full_name)
age_field.send_keys(age)
phone_field.send_keys(phone_number)

for location in selected_locations:
    location_checkbox = driver.find_element_by_xpath(location_checkboxes[location])
    driver.execute_script("arguments[0].click()", location_checkbox)

# Submit form
submit.click()

# Confirm submission
confirmation_text = driver.find_element_by_css_selector(".text-element").text
print(confirmation_text)

# Close
driver.quit()