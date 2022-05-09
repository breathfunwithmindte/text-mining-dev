# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from src.Textmining import TextMining

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    f = open("sample.txt", "r")

    schema = {
        "name": "some proccess name",
        "keywords_categories": [
            { "category": "open source", "keywords": ["open", "public", "open url"] },
            { "category": "private project","keywords": ["private", "401 not autheticated", "require login"] }
        ],
        "rulesBetween": [ "{...}", "[...]", "start...end"],
        "rulesStart": [{"keyword": "username", "symbol_to": "="}, {"keyword": "this", "symbol_to": ":"}],
        "rulesAdvanced": ["(?<=He)..", "(?<= )[0-9]{11}(?=\s)"]
    }

    textmining = TextMining(f.read(), schema)
    textmining.execute()

    print(textmining.rulesBetweenResult)
    print("~~~~~ RULE BETWEEN RESULT ~~~~~")
    for x in textmining.rulesBetweenResult:
        print("RESULT => " + x["found"])
    print("\n\n")
    print("~~~~~ RULE START RESULT ~~~~~")
    print(textmining.rulesStartResult)
    for x in textmining.rulesStartResult:
        print("RESULT => ", x["found"])
    print("\n\n")
    print("~~~~~ RULE START RESULT ~~~~~")
    print(textmining.rulesAdvancedResult)
    for x in textmining.rulesAdvancedResult:
        print("RESULT => ", x["found"])
    print("\n\n")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
