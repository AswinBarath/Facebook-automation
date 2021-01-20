from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="path_to_chrome_driver")
driver.get("https://www.facebook.com/campaign/landing.php?campaign_id=1653993517&extra_1=s%7Cc%7C318504236042%7Ce"
           "%7Cfacebook%7C&placement=&creative=318504236042&keyword=facebook&partner_id=googlesem&extra_2=campaignid"
           "%3D1653993517%26adgroupid%3D63066387003%26matchtype%3De%26network%3Dg%26source%3Dnotmobile"
           "%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D%26target%3D%26targetid%3Dkwd"
           "-541132862%26loc_physical_ms%3D9040218%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid"
           "=EAIaIQobChMIwr_Jieep7QIVKZVLBR1nkQAXEAAYASAAEgLxaPD_BwE")

driver.find_element_by_name("firstname").send_keys("John")
driver.find_element_by_name("lastname").send_keys("Doe")
driver.find_element_by_name("reg_email__").send_keys("example@xyzcompany.com")
driver.find_element_by_name("reg_email_confirmation__").send_keys("example@xyzcompany.com")
driver.find_element_by_id("password_step_input").send_keys("password")

dropdown = Select(driver.find_element_by_id("day"))
dropdown.select_by_visible_text("15")

dropdown = Select(driver.find_element_by_id("month"))
dropdown.select_by_visible_text("Aug")

dropdown = Select(driver.find_element_by_id("year"))
dropdown.select_by_visible_text("2000")

driver.find_element_by_class_name("_58mt").click()
driver.find_element_by_name("websubmit").click()

get_url = driver.current_url
print(get_url)

# driver.refresh()
# driver.back()
# driver.forward()
# driver.execute_script("window.open('https://www.google.com');")
