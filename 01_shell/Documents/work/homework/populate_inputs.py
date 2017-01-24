#! /usr/env/python

with open('homework.tex','r') as f:
    for line in f:
        if line.startswith('\input'):
            print(line.strip()[7:-1])
