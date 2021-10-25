## Regular Expressions
# import re

# pattern = r"eggs"
# if re.match(pattern, "baconeggseggseggsbacon"):
#     print("Match Found")
# else:
#     print("No match found")

## Search and Find all
# pattern = r"eggs"

# if re.search(pattern, "baconeggseggseggsbacon"):
#     print("Match Found")
# else:
#     print("No match found")

# if re.findall(pattern, "baconeggseggseggsbacon"):
#     print("Match Found")
# else:
#     print("No match found")

# print(re.findall(pattern, "baconeggseggseggsbacon"))

## Find and Replace
# import re
# string = "My name is John . Hiee I am John"
# pattern = r"John"
# print(re.sub(pattern,"Rob",string))

## Dot Metacharacter
# import re

# pattern = r"gr.y"
# if re.match(pattern, "grey"):
#     print("Match Found")

## Caret Dollar Metacharacter
# import re

# pattern =r"^gr.y$"
# if re.match(pattern, "grey"):
#     print("Match Found")

## Character Classes
# import re

# pattern = r"[A-Z][A-Z][0-9]"

# if re.search(pattern, "AA1"):
#     print("Match Found")

## Star Metacharacter
# import re

# pattern = "eggs(bacon)*"
# if re.match(pattern, "eggsbacon"):
#     print("Match Found")

## Groups
# import re
# pattern=r"bread(eggs)*bread"

# if re.match(pattern,"breadeggseggsbread"):
#     print("Match Found")