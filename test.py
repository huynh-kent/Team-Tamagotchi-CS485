import random

with open('my_body.txt', 'r') as form:
    all_form = form.read()

print(random.choice(all_form.splitlines()))