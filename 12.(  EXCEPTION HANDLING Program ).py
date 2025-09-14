try:
 number = int(input("Enter a number: "))
 print(1/number)

except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Enter only numeric value!")
except Exception:
    print("something went wrong!")
finally:
    print("Goodbye!")
