import re

test_string = """
Hello world
My name is bob how's going
Python_testing1010@gmail.com
testing120@main.ru
mYemain-test@email.cz
newemain345333@org.org
2000-12-12
23.04.2021
https://www.google.com
http://my_website.org
"""

pattern_url = re.compile(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))")
pattern_email = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
pattern_date = re.compile(r"\d{1,4}.\d{2}.\d{1,4}")

# most common methods: match(), search(), findall(), finditer()
matches_urls = pattern_url.finditer(test_string)
matches_emails = pattern_email.finditer(test_string)
matches_dates = pattern_date.finditer(test_string)


# group(), start(), end(), span()
for match_url in matches_urls:
    print(match_url)

for match_email in matches_emails:
    print(match_email)

for match_date in matches_dates:
    print(match_date)
