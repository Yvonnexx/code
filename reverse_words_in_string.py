#!/usr/bin/python

def reverse(s):
    string = s.split()
    return ' '.join(string[::-1])

if __name__ == "__main__":
    s = "the sky is blue "
    print reverse(s)
