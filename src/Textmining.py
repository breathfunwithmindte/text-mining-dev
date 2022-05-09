from src.Parser import Parser
import re

class TextMining(Parser):
  pass

  def __init__(self, text, schema):
    self.name = schema["name"]
    self.text = text
    self.keywords_categories = schema["keywords_categories"]
    # @doc textCategory is final category of the text
    # @doc keywords_categories_result is the list of all proccess runned to search the number of keywords.
    self.textCategory = ""
    self.keywords_categories_result = []
    self.rulesBetween = schema["rulesBetween"]
    self.rulesBetweenResult = []
    self.rulesStart = schema["rulesStart"]
    self.rulesStartResult = []
    self.rulesAdvanced = schema["rulesAdvanced"];
    self.rulesAdvancedResult = []

  def execute (self):
    self.setCategories()
    # print(self.keywords_categories_result)
    self.searchBetween()
    # print(self.rulesBetweenResult)
    self.searchByStart()
    # print(self.rulesStartResult)
    self.searchAdvanced()


  def searchAdvanced (self):
    for x in self.rulesAdvanced:
      self.rulesAdvancedResult.append({
          "rule": x, "found": self.costumRegex(x, self.text)
      })

  def setCategories (self):
    for x in self.keywords_categories:
      current_category = x["category"]
      current_keywords = x["keywords"]
      self.keywords_categories_result.append(self.findKeywords(current_keywords, current_category))

  def searchBetween (self):
      for x in self.rulesBetween:
        current = self.ruleParseBetween(x, self.text)
        if current != -1:
          self.rulesBetweenResult.append({"rule": x, "found": current})

  def searchByStart (self):
      for x in self.rulesStart:
        self.rulesStartResult.append({
          "rule": x,
          "found": self.ruleParseStartingWith(x["keyword"], x["symbol_to"], self.text)
        })