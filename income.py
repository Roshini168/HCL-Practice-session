income=int(input())
credit=int(input())
debt=int(input())
if (income>=50000 and credit>=700 and debt<=20000):
    print("Eligible")
elif (income>=20000 and credit>=600 and debt<=10000):
    print("Review")
else:
    print("Reject")
