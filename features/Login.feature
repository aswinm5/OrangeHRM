Feature: To test the login page
  Background:
    Given i launch the browser
    When i open the URL
    Then i should see the Login Page
  @elements
  Scenario: To verify the displayed elements
    Then i should see the orange HRM Logo displayed
    And i should see the default Username : Admin and password : admin123 displayed
    Then i should see the Login Button

 @validlogin
  Scenario: Login with Valid Credentials
    Then i enter the Username "Admin" and Password "admin123"
    And i click on login button
    Then i should be logged in successfully to the dashboard

 @invalidlogin
  Scenario Outline: Login with invalid credentials
    Then i enter the Username "<Username>" and Password "<Password>"
    And i click on login button
    Then i should see the Invalid Credentials message

    Examples:
    |Username|Password|
    |Sahil   |Sahil123|
    |test    |test123 |
