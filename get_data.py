import sys
from datetime import date

print("Hello world")

if __name__=="__main__":
    if len(sys.argv) > 1:
        try:
            year,month, day = [int(v) for v in sys.argv[1].split("-")]
            date = date(year, month, day)
        except ValueError:
            print("ce n'est pas une date")
    else:
        print("il manque un argument")