import re

pattern = r"\d+"
text = "There are 123 apples"
match = re.findall(pattern, text)
print(match)  # ['123']
