import requests
response = requests.get("https://api.github.com/users/this_user_does_not_exist_123456789")
print("Status Code:",response.status_code)
if response.status_code==200:
    print("Success")
else:
    print("Something went wrong")