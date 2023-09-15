def main():
    s=input()
    print(convert(s))

def convert(s):
    c=s.replace(":)","🙂").replace(":(","🙁")
    return c

main()