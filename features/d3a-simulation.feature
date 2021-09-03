Feature: Simulation
  Scenario: Create a Simulation for a new project
    Given the user logs in
	And the user creates a project
    When the user selects on the project
    And the user clicks on new simulation button
    And the user enters simulation name "sampleSimulationName" and description "sampleSimulationDescription"
    And the user clicks on Next button
    Then a new simulation is created
    And is visible on projects page under the project