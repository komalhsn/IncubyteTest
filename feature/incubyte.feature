Feature: Functionality to Gmail compose and send email

  Scenario: Verify Gmail login functionality
    Given the user is on the Gmail login page
    When the user enters a valid username and password
    And the user clicks on the "Next" button
    Then the user should be logged into Gmail


  Scenario: Verify Compose button functionality
    Given the user is logged into Gmail
    When the user clicks on the "Compose" button
    Then a new email compose window should open

  Scenario: Verify email is sent with specified subject and body
    Given the user is logged into Gmail and the compose window is open
    When the user enters the recipient's email address
    And the user enters "Incubyte" in the subject field
    And the user enters "Automation QA test for Incubyte" in the email body
    And the user clicks on the "Send" button
    Then the email should be sent successfully
    And a confirmation message should appear

  Scenario: Verify email appears in Sent Mail
    Given the email is sent successfully
    When the user clicks on the "Sent" folder
    Then the sent email should appear in the Sent Mail folder

  Scenario: Verify error message for invalid email address
    Given the user is logged into Gmail and the compose window is open
    When the user enters an invalid email address
    And the user enters any subject and body
    And the user clicks on the "Send" button
    Then an error message indicating an invalid email address should appear