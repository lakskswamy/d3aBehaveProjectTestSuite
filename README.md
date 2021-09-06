# d3a Automation Project

This is a Selenium automation project built using Python.

The project deals with test suites for the d3a.io website. It covers 3 Major features - Login, Project Creation and Simulation Creation where each feature has a set of test scenarios.

In this project, Behave - Gherkin layer is the top layer which is Behavioural Driven Development(Layer 1).

Then a Selenium Python underneath is defined to make those generic keywords(Layer 1) to code in the backend - thus making it Layer 2.
Project also uses allure for report creation.

The automation test report is available at: **allure-report-d3a.netlify.app**

**Login Feature Scenarios**

1. Successful login to D3O with valid parameters
 
2. Failure login to D3O with invalid password
 
3. Failure login to D3O with invalid username

**Project Feature Scenario**

1. Create a Project with valid elements using project icon
 
2. Create a Project with valid elements using project url

3. Create a Project with only project name

4. Create a Project with no name and description

5. Create a Project with a name of an existing project

**Simulation Feature Scenario**

1. Create a Simulation for a new project

2. Create a Simulation for an existing project

**To execute the project and generate json report run the below command**

behave -f allure_behave.formatter:AllureFormatter -o {path to create json reports}/ {path to feature file folder}/

 **To view HTML report of the execution, run the below command**
 
 allure generate {path to json report folder}/



