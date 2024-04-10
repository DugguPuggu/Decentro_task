*** Settings ***
Library    RequestsLibrary
Library    Collections


*** Variables ***
${base_url}=    https://jsonplaceholder.typicode.com
${title}=       Robot post request
${body}=       send
${userid}=      1

*** Test Cases ***
test_post_res

    create session    mysession     ${base_url}
    ${body}=    create dictionary       title=${title}     body=${body}      userId=${userid}
    ${header}=  create dictionary    Content-Type=application/json

    ${response}=    post on session    mysession   /posts   ${body}   ${header}

    log to console    ${response.status_code}
    log to console    ${response.text}


    #Validations

    ${status_code}=     convert to string    ${response.status_code}
    should be equal    ${status_code}   201

    ${response}=    convert to string    ${response.content}
    should contain    ${response}       ${title}