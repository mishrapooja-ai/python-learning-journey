import requests
url = "https://jsonplaceholder.typicode.com/posts"
data={
    "title":"my first post",
    "user id":"1",
    "body":"Learning Python APIs"
}
response=requests.post(url,json=data)
