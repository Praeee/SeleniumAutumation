import requests

# Get user profile success
url = "https://reqres.in/api/users/12"
response = requests.get('https://reqres.in/api/users/12')
if response.status_code == 200:
    print(url, ' : 200')
elif response.status_code == 404:
    print(url, ' : 404')


# Get user profile but user not found
url = "https://reqres.in/api/users/1234"
response = requests.get('https://reqres.in/api/users/1234')
if response.status_code == 200:
    print(url, ' : 200')
elif response.status_code == 404:
    print(url, ' : 404')




