from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#FUNCTIONS---

#Below are the variable explanations for this particular function

#Function to build url and get HTML element ID's based on LMS choice. This will also grab HTML element ID's that change
#url: url that points to the LMS login page
#loginID: the HTML object ID for the field where the user will input their usernames
#passwordID: this is the HTML object ID for the field where the user will input their passwords
#catalogURL: this is the url that points to the catalog search page on whichever LMS the user is on
#courseNumName: this is the HTML object NAME for the field where the user will input their course number
#selectName: this is the HTML object NAME for the select object that needs to be changed to 'Course Number'
#optionValue: this is the HTML object value for the course number option. Might use this or might go by the actual text which would be 'COURSE NUMBER'. Depends on how the automation loop goes.

def buildCatURL(LMS):
    if LMS == 'gmt':
        url = 'https://www.centerlearning.com/HomePage/Portal.asp'
        loginID = 'sSSN'
        passwordID = 'sPassword'
        catalogURL = 'https://www.centerlearning.com/catalog/index.asp?iQueryID1=40&sFieldName1=sFilterType&iDataTypeID1=2&iFilterID1=1&sCriteria1=1&iResultSet1=1&iSectionID1=1&iPageID1=19&sPageName1=../catalog/index.asp&iRecordCount=1'
        courseNumName = 'sCriterial'
        selectName = 'sFieldName1'
        optionValue = 'tCourse.sCourseNumber'
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
        loginID = 'sUserID'
        passwordID = 'sPassword'
    elif LMS == 'ad':
        url = 'https://training.alldata.com/HomePage/LoginPage.aspx?iCompanyID=1'
        loginID = 'sUserID'
        passwordID = 'sPassword'
    return(url,loginID,passwordID,catalogURL,courseNumName,selectName,optionValue)

#The function below will be the actual selenium browser automation. There will be more values passed when the function above is finished.
#The added 'courseNum' stipulation will be the actual course number being searched for by the user. 'username' and 'password' are the users actual information'

def automation(courseNum,username,password,url,loginID,passwordID,catalogURL,courseNumName,selectName,optionValue):
    browser = webdriver.Firefox()
    browser.get(url)
    username_field = browser.find_element_by_id(loginID)
    username_field.send_keys(username)
    username_field.send_keys(Keys.TAB)
    password_field = browser.find_element_by_id(passwordID)
    password_field.send_keys(password)
    password_field.send_keys(Keys.ENTER)
    browser.get(catalogURL)
    select = browser.find_element_by_name(selectName)

#Below is all test code

LMS = 'gmt'
username = '1487191'
password = 'password'
courseNum = '18420'
url,loginID,passwordID,catalogURL,courseNumName,selectName,optionValue = buildCatURL(LMS)
print(url,loginID,passwordID,catalogURL,courseNumName,selectName,optionValue)
automation(courseNum,username,password,url,loginID,passwordID,catalogURL,courseNumName,selectName,optionValue)





