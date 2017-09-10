from xml.dom import minidom
import re

doc = minidom.parse("xml")
root = doc.documentElement
print(root.nodeName)
personElements = root.getElementsByTagName("person")
print(personElements)
for person in personElements:
    print(person.childNodes[0].nodeValue)

pattern1 = r"\d{3}-\d{3,8}"

pattern2 = r"\d{3}"

pattern3 = r"(\d*)-(\d*)-(\D*)"

matcherObject = re.match(pattern3, "028-332333-xxxxx")
print(matcherObject)

# matcherGroups = matcherObject.groups()
# print(matcherGroups)
# print(matcherGroups[0])
# print(matcherGroups[1])
# print(matcherGroups[2])
# print(matcherGroups[3])

clockM = "59"

patternM = r"[0-9]"

matchM = re.match(patternM, "99")
