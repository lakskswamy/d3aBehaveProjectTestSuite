
Feature: D3A Login

  Background: common steps
    Given the user launches Chrome Browser
    When the user opens D3a login page url "https://www.d3a.io/login"

  Scenario: Successful login to D3O with valid parameters
    When the user enters username "laks.kswamy@gmail.com" and password "11-Feb-1995"
    And the user clicks the Login Button
    Then the home page opens

  Scenario: Failure login to D3O with invalid password
    When the user enters username "laks.kswamy@gmail.com" and password "wrongPassword"
    And the user clicks the Login Button
    Then the home page does not open with invalid password

  Scenario: Failure login to D3O with invalid username
    When the user enters username "wrongemailid@gmail.com" and password "11-Feb-1995"
    And the user clicks the Login Button
    Then the home page does not open with invalid username
