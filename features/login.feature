Feature: Login capability
  #smoke test este un sanity check - se ruleaza un login si daca merge, putem sa incepem suita mai mare de teste

  Background:
    Given home: I am an user on the home page

  @smoke
  Scenario Outline: I login with invalid credentials
    When login: I login with user "<user>" and pass "<pasw>"
    Then login: I validate that error message is displayed or not

    Examples:
      | user                 | pasw                |
      | itfta32ups@gmail.com | Testareautomata123  |
      | itffta32ups@gmail.co | TestareAutomata123! |

    #cream un Scenario Outline: pentru a fi mai eficienti in testare, pentru a face cat mai putine scenarii

  @smoke
  Scenario: I login with valid credentials
    When login: I login with user "itfta32usp@gmail.com" and pass "Testareautomata123!"
    Then login: I am on the household page

  @smoke
  Scenario Outline: I want to add a new person
    When login: I am on the household page
    When household: I click on the add button
    When household: I add a new person <first_name> <last_name>
    Then household: I validate that the person was added

    Examples:
      | first_name | last_name |
      | Silviu     | Petre     |
# pentru a rula aceste teste, folosim comanda behave -f html -o test_raport.html --tags=smoke
#  In cazul in care vrem sa rulam doar un Scenariu, putem redenumi sccenariul respectiv si inlocuim tagul smoke cu numele testului dorit
#  Deschidem test_raport.html cu browserul pentru a putea trage concluzii asupra testului rulat, daca a functionat