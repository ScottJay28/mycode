#!/usr/bin/env python3

loginfail = 0
posts = 0
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    for line in kfile:
        if "- - - - -] Authorization failed" in line:
            loginfail += 1
        elif "POST" in line:
            posts += 1

print("The number of failed log in attempts is", loginfail)

print("The number of successful POSTs is", posts)
print(line.split(" ")[-1])
