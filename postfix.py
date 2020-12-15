#!/usr/bin/env python3

def eval_expr0(text):
    s=list()
    t=text.split()
    for item in t:
       #for item in text:
        if item.isdigit():
            s.append(int(item))
        else:
            b = s.pop()
            a = s.pop() 
            if item == "+":
                w = a + b
                s.append(w)
            elif item == "-":
                w = a - b
                s.append(w)
            elif item == "*":
                w = a * b
                s.append(w)
            elif item == "/":
                w = int(a / b)
                s.append(w)
    return s.pop()

def eval_expr(text,d={}):
    s=list()
    t=text.split()
    nt=list()
    for i in t:
        if i in d.keys():
            nt.append(str(d[i]))
        else:
            nt.append(i)
    for item in nt:
        if item.isdigit():
            s.append(int(item))
        else:
            b = s.pop()
            a = s.pop()
            if item == "+":
                w = a + b
                s.append(w)
            elif item == "-":
                w = a - b
                s.append(w)
            elif item == "*":
                w = a * b
                s.append(w)
            elif item == "/":
                w = int(a / b)
                s.append(w)
    return s.pop()

def to_infix(text):
    t=text.split()
    l=list()
    for id in range(len(t)):
        if t[id].isalnum():
            l.append(t[id])
        else:
            a = l.pop()
            b = l.pop()
            l.append("(" + b + t[id] + a + ")")
    return l.pop()

def to_postfix(text):
    t=text.split()
    l=list()
    for s in t:
        if s== ")":
            b=l.pop()
            op=l.pop()
            a=l.pop()
            l.pop() #otvaracia zatvorka
            l.append(a + " " + b + " " + op + " ")
        else:
            l.append(s)
    return l.pop()
