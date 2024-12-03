*** Settings ***
Library    SeleniumLibrary
Library    RPA.Desktop
*** Variables ***
*** Test Cases ***
Browser DropBox and Radio Buttons
    Open Browser    https://webdriveruniversity.com/index.html    chrome
    Maximize Browser Window
    Scroll Element Into View    //h1[contains(text(),'AJAX LOADER')]
    Sleep    3s
    Click Button    //h4[contains(text(),'The choice is yours!')]
    Sleep    2s
    Click Button    //select[@id='dropdowm-menu-1']

*** Keywords ***