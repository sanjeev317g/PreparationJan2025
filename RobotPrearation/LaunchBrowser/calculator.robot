*** Settings ***
*** Variables ***
*** Test Cases ***
calculator
    ${addition}    Evaluate    1+2
    ${subtration}    Evaluate    2-1
    ${multiplication}    Evaluate    2*2
    ${devision}    Evaluate    4/2
    Log    ${addition}
    Log    ${subtration}
    Log    ${multiplication}
    Log    ${devision}
*** Keywords ***
