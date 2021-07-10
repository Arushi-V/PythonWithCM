''' 
Q. What is JSON?
Ans. JSON (JavaScript Object Notation) is a lightweight data-interchange format.
	It is easy for humans to read and write. It is easy for machines to parse and generate.

	JSON is built on two structures:

	1. A collection of name/value pairs. In various languages, this is realized as an object, record, struct, dictionary, 
		hash table, keyed list, or associative array.
	2. An ordered list of values. In most languages, this is realized as an array, vectors, list or sequence. 
'''

import json 


aruJson = '''{
  "login": "Arushi-V",
  "id": 83902402,
  "node_id": "MDQ6VXNlcjgzOTAyNDAy",
  "avatar_url": "https://avatars.githubusercontent.com/u/83902402?v=4",
  "gravatar_id": "",
  "url": "https://api.github.com/users/Arushi-V",
  "html_url": "https://github.com/Arushi-V",
  "followers_url": "https://api.github.com/users/Arushi-V/followers",
  "following_url": "https://api.github.com/users/Arushi-V/following{/other_user}",
  "gists_url": "https://api.github.com/users/Arushi-V/gists{/gist_id}",
  "starred_url": "https://api.github.com/users/Arushi-V/starred{/owner}{/repo}",
  "subscriptions_url": "https://api.github.com/users/Arushi-V/subscriptions",
  "organizations_url": "https://api.github.com/users/Arushi-V/orgs",
  "repos_url": "https://api.github.com/users/Arushi-V/repos",
  "events_url": "https://api.github.com/users/Arushi-V/events{/privacy}",
  "received_events_url": "https://api.github.com/users/Arushi-V/received_events",
  "type": "User",
  "site_admin": false,
  "name": null,
  "company": null,
  "blog": "",
  "location": null,
  "email": null,
  "hireable": null,
  "bio": null,
  "twitter_username": null,
  "public_repos": 1,
  "public_gists": 0,
  "followers": 0,
  "following": 0,
  "created_at": "2021-05-09T08:27:15Z",
  "updated_at": "2021-07-10T07:35:50Z"
}'''

parsedData = json.loads(aruJson)

print(parsedData["login"])
print(type(parsedData))

# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

convertData = json.dumps(aruJson)

print(convertData)


''' You can convert Python objects of the following types, into JSON strings:

dict
list
tuple
string
int
float
True
False
None '''

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))