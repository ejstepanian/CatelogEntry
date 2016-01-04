from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#FUNCTIONS---

#Function to build url and get HTML element ID's based on LMS choice.
def buildCatURL(LMS):
    if LMS == 'gmt':
        url = 'https://www.centerlearning.com/HomePage/Portal.asp'
        loginID = 'sSSN'
        passwordID = 'sPassword'
    elif LMS == 'gmio':
        url = 'https://www.gmiotraining.com/HomePage/LoginPage.aspx?iCompanyID=9'
        loginID = 'sUserID'
        passwordID = 'sPassword'
    elif LMS == 'urbsci':
        url = 'https://www.urbanscienceuniversity.com/HomePage/LoginPage.aspx'
        loginID = 'sUserID'
        passwordID = 'sPassword'
    elif LMS == 'delco':
        url = 'https://www.acdelcotraining.com/HomePage/LoginPage.asp?iCompanyID=10'
        loginID = 'sUserID'
        passwordID = 'sPassword'
    elif LMS == 'sch':
        url ='https://www.schwabadvisoruniversity.com/homepage/loginpage.aspx?schwab1030=1'
    elif LMS == 'ad':
        url = 'https://training.alldata.com/HomePage/LoginPage.aspx?iCompanyID=1'
    return(url)

browser = webdriver.Firefox()
browser.get('https://www.centerlearning.com/HomePage/Portal.asp')
login = browser.find_element_by_id('sSSN')
login.send_keys('swag')

