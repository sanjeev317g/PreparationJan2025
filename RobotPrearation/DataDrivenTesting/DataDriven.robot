*** Settings ***
*** Variables ***
*** Test Cases ***
DataDriver testing
    [Template]    TestDataDrivern
    int(10)    int(20)
    30    40
    50    60
    70    80
    90    100

*** Keywords ***
TestDataDrivern
    [Arguments]    ${var1}    ${var2}
    Log    ${var1}+${var2}