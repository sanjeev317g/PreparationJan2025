*** Settings ***
Library    Custom.py
Library    RPA.JavaAccessBridge
*** Variables ***

*** Test Cases ***
Calling Python file to Robot file
    ${add}=    Addition    100    100
    Log    ${add}
    

*** Keywords ***