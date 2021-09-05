Feature: Project

  Background: common steps
    Given the user logs in with username "laks.kswamy@gmail.com" and password "11-Feb-1995"

  Scenario: Create a Project with valid elements using project icon
    When the user navigates to https://www.d3a.io/projects
    And the user clicks on second icon from top on the left hand side
    And the user clicks on new project icon
    And the user enters name "sampleName" and description "sampleDescription"
    And the user clicks on Add button
    Then a new project is created
    And is visible on projects page

  Scenario: Create a Project with valid elements using project url
    When the user navigates to https://www.d3a.io/projects
    And the user clicks on new project icon
    And the user enters name "sampleName" and description "sampleDescription"
    And the user clicks on Add button
    Then a new project is created
    And is visible on projects page

  Scenario: Create a Project with only project name
    When the user navigates to https://www.d3a.io/projects
    And the user clicks on new project icon
    And the user enters name "sampleName" and description " "
    And the user clicks on Add button
    Then a new project is created
    And is visible on projects page

  Scenario: Create a Project with no name and description
    When the user navigates to https://www.d3a.io/projects
    And the user clicks on new project icon
    Then Add button for creation of project is not clickable

  Scenario: Create a Project with a name of an existing project
    When the user navigates to https://www.d3a.io/projects
    And the user clicks on new project icon
    And the user enters name "sampleName1" and description " "
    And the user clicks on Add button
    Then a new project is not created
