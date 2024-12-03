*** Settings ***
Library    SeleniumLibrary

*** Variables ***
*** Test Cases ***
Launch the Browser Input Password
    Open Browser    https://ultimateqa.com/complicated-page    chrome
    Maximize Browser Window
    Scroll Element Into View    //Input[@id="user_login_674308deb37d5"]
    Input Text    //Input[@id="user_login_674308deb37d5"]    "Carrier"
    Input Text    //Input[@id="user_pass_674308deb37d5"]    "CarrierPassword"

Launch Another Website for DropDown CheckBoxes And Radio Buttons


*** Keywords ***