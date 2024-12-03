*** Settings ***
Library    SeleniumLibrary
Library    String
# Library    DatabaseLibrary
# Library    RequestLibrary

*** Test Cases ***
Evaluating a test Cases
    ${c}    Evaluate    10*10
    Log    ${c}
    Should Be Equal As Numbers    ${c}    100
    ${randomString}    Generate Random String    10
    Log    ${randomString}

*** Keywords ***


