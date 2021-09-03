Feature: Project
  Scenario: Create a Project with valid elements
    Given the user logs in
    When the user clicks on second icon from top on the left hand side
    And the user clicks on new project icon
    And the user enters name "sampleName" and description "sampleDescription"
    And the user clicks on Add button
    Then a project is created
    And is visible on projects page