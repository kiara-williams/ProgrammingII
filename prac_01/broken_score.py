"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))
while score < 0 or score > 100:
  score = float(input("Enter a valid score: ""))
if score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")
