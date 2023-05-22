greeting = input("Greeting: ").strip().lower()

if greeting.startswith("h") and not greeting.startswith("hello"):
    print("$20")
elif greeting.startswith("hello"):
    print("$0")
else:
    print("$100")