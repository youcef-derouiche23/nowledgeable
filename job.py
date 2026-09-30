import os

secret = os.environ.get("SECRET_API_TOKEN")

print("Le secret est accessible :", secret)