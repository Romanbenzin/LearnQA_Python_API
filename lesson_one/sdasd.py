import requests

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
text_response = requests.get(url)
print(text_response.text, "\n")