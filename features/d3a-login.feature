Feature: D3O Login

  Scenario: Successful login to D3O with valid parameters
    Given the user launches Chrome Browser
    When the user opens D3a login page
    And the user enters username "laks.kswamy@gmail.com" and password "11-Feb-1995"
    And the user clicks the Login Button
    Then the home page opens

  Scenario: Failure login to D3O with ivalid password
    Given the user launches Chrome Browser
    When the user opens D3a login page
    And the user enters username "laks.kswamy@gmail.com" and password "wrongPassword"
    And the user clicks the Login Button
    Then the home page does not open

  Scenario: Failure login to D3O with ivalid password
    Given the user launches Chrome Browser
    When the user opens D3a login page
    And the user enters username "wrongemail@gmail.com" and password "11-Feb-1995"
    And the user clicks the Login Button
    Then the home page does not open
