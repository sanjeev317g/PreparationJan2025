*** Settings ***
*** Variables ***
${start}    20
${end}    25
*** Test Cases ***
Passing Parameters to a Keywords
    calculate    ${start}    ${end}
*** Keywords ***
calculate
    [Arguments]    ${a}    ${b}
     FOR    ${counter}    IN RANGE    ${a}   ${b}
         Log    ${counter}
     END
    



