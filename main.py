import os

url = os.getenv("URL")
os.system("ktoolbox sync-creator " + url)
