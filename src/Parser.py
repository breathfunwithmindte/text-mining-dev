import re

class Parser:


  def parse (self):
    #
    # simulateAI: [{ name: "happy", keywords: [] }] -> number of meets 2 | 3 | 10
    # [{ rule: "=", matchWord: "username" }]
    # return { simulateAI: [{ name:"happy",  }] }
    #
    #
    print("parsing")


  def findKeywords (self, keywords, category):
    array_for_return = [];
    string_regex = ""
    for i in keywords:
      if(string_regex == ""):
        string_regex = i
      else: string_regex = string_regex + "|" + i
    for x in re.findall(string_regex, self.text):
      array_for_return.append(x)
    return { "category": category, "found_keywords": array_for_return }

  def ruleParseBetween (self, rule, text):
    if(rule == None): return -1
    params = rule.split("...")
    if(len(params) < 1): return -1
    a, b = text.find(params[0]), text.find(params[1])
    if(a == -1): return -1
    if(b == -1): return -1
    a_count = a + len(params[0])
    b_count = b + len(params[1]) - 1
    #print(a_count, b_count)

    return text[a_count:b_count]

  def ruleParseStartingWith (self, keyword, symbol_to, text):
    return re.findall(f"(?<={keyword}) ?{symbol_to} ?(\S*)", text)

  def costumRegex (self, regex, text):
    return re.findall(regex, text)

