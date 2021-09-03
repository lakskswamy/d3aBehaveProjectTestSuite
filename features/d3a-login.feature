Feature: D3O Login

  Scenario: Login to D3O with valid parameters
    Given the user launches Chrome Browser
    When the user opens D3a login page
    And the user enters username "laks.kswamy@gmail.com" and password "11-Feb-1995"
    And the user clicks the Login Button
    Then the home page opens