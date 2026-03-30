# Study Pattern Analyzer (using ML)

from sklearn.tree import DecisionTreeClassifier

print("Study Pattern Analyzer\n")

# sample data (made manually)
# [study hours, sleep, distractions]
X = [
    [6, 7, 2],
    [5, 6, 3],
    [2, 5, 6],
    [7, 8, 1],
    [3, 5, 5],
    [4, 6, 4],
    [1, 4, 7],
    [8, 7, 2]
]

# output labels
# 2 = good, 1 = avg, 0 = poor
y = [2, 2, 0, 2, 1, 1, 0, 2]

# making model
model = DecisionTreeClassifier()

# training step
model.fit(X, y)

print("Model ready (trained on small data)\n")

name = input("Enter your name: ")

# taking input
h = int(input("Study hours: "))
s = int(input("Sleep hours: "))
d = int(input("Distractions: "))

print("\nChecking result...\n")

# prediction
res = model.predict([[h, s, d]])

# storing value
out = res[0]

print("\n--- Result ---")
print("Name:", name)

if out == 2:
    print("Looks like you will do good.")
elif out == 1:
    print("Maybe average performance.")
else:
    print("Performance might be low.")

# small suggestion part (kept simple)
print("\nSuggestions:")

if h < 4:
    print("- increase study time")

if s < 6:
    print("- sleep a bit more")

if d > 5:
    print("- try to reduce distractions")
