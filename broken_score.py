import random
def eval(score):
    if score < 0 or score > 100:
        return ("Invalid score")
    elif score >= 90:
        return ("Excellent")
    elif score >= 50:
        return ("Passable")
    else:
        return ("Bad")
def main():
    score = float(input("Enter score: "))
    print(eval(score))
    s=random.randint(0,100)
    print(s)
    print(eval(s))
main()