# Url Shortener

Url shortener written in Python with Flask. It has some useful skills

  - Adding shortened link
  - Remove shortened link
  - Secured with password
  - Saving visit counts
 
### Tech
* Python
* Sqlite3
* Flask


### Installation

I am suggesting you to create a virtual environmet.
This link can help you => https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04

Default password is 123. You can change that from app.py

```sh
$ cd python-url-shortener
$ pip install -r requirements.txt 
$ python3 app.py
```

### Routes

domain.com/add for creating short link
domain.com/remove for remove short link
domain.com/{SHORTENED_LINK}/stat for see visit count

### Todos

 - Build better UI
 - Think about removing password protection
