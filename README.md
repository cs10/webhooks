webhooks
========

Automation + Github = &lt;3

---

This repo is a set of tools which help us update all of our various websites 
quickly and easily. The setup is starting off fairly basic, but may expand over
time. Right now, we only really care about pulling changes from Github, and
correctly updating our various sites. (In the future, we might expand the 
services used, but many others have already written fantastic scripts to do 
some of that.)

## How it Works

Our web server contains a simple PHP file, `gh.php`. When called, all this does
is log a couple basic tasks (just incase!) and then call `github.py`.

Certainly, we could have done more in PHP (or any other language), but many of 
us have pretty good familiarity with Python. :)

#### Directory:
Here's how the site is _currently_ setup:

```
/
- github/
    - github.py
    - php_log.txt
    - github_log_REPO.txt
- public_html/
    - gh.php
```
##### GitHub
Each repo needs a hook setup for `server.com/gh.php`. We don't use a secret and
all events can be sent, but right now we really only care about the `push` 
event. (Sometime, it will probably make sense to track issues or deploys for 
more complex projects.)

## Meat & Potatoes

The `github.py` takes in JSON data from the POST to `gh.php`. It then parses the
repository name from the data, and executes the functions associated with that
repo.

..... We may completely change this in the future, but right now we have 1 file
to update all the sites and servers. (1 file for multiple servers seems like 
a stupid idea long term, so we might create a file per server with a generic 
class for handling the configuration.)