Feature: Books CRUD operations
  This feature tests create, update, delete and get books functionality

  Scenario: Create a new book
    Given user sends "POST" request to endpoint "Books"
    Then response code "200" is received

  Scenario: Get all books
    When user sends "POST" request to endpoint "Books"
    Then response code "200" is received

