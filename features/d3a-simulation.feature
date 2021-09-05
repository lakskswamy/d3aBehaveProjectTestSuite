Feature: Simulation

  Background: common steps
    Given the user logs in with username "laks.kswamy@gmail.com" and password "11-Feb-1995"

  Scenario: Create a Simulation for a new project
	Given the user creates a project with Project Name as "simname" and description as "simdescription"
    And the user selects on the project
    When the user clicks on new simulation button
    And the user enters simulation name "sampleSimulationName" and description "sampleSimulationDescription"
    And the user clicks on Next button
    Then a new simulation is visible on projects page under the project

  Scenario: Create a Simulation for an existing project
    Given the user selects an existing project
    When the user clicks on new simulation button
    And the user enters simulation name "SimulationNameExistingProj" and description "SimulationDescriptionExistingProj"
    And the user clicks on Next button
    Then a new simulation is visible on projects page under the existing project