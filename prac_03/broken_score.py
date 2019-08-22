"""
CP1404/CP5632 - Practical
Program to determine score status
"""

def main():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        score = float(input("Enter a valid score: "))
    status = get_score_status(score)
    print(status)


def get_score_status(score):
    """Select status using score"""
    if score >= 90:
        status = "Excellent"
    elif score >= 50:
        status = "Passable"
    else:
        status = "Bad"
    return status


main()