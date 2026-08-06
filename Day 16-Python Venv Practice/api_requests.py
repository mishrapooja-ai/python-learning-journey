import requests
response=requests.get("https://api.github.com/users/octocat")

data=response.json()
print("Username:",data["login"])
print("Followers:",data["followers"])
print("Following:",data["following"])
print("Public Repositories:",data["public_repos"])
print("Location:",data["location"])

