# Created by Sachin at 07-01-2023
Feature: Verify if Books are added and deleted using library API
  # Enter feature description here
  @library
  Scenario: Verify AddBook API functionality
    Given the Books details which needs to be added to Library
    When we execute the AddBook PostAPI method
    Then book is successfully added

  @library
  Scenario Outline: Verify AddBook API functionality
    Given the Books details with <isbn> and <aisle>
    When we execute the AddBook PostAPI method
    Then book is successfully added
    Examples:
      |isbn  | aisle |
      | poer  |  56  |
      | yutu  |  85  |



