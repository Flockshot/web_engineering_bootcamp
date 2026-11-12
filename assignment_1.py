# Question 1
def grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"

print("Q1:", grade(85), grade(65), grade(45), grade(30))


# Question 2
def analyze(numbers):
    smallest = min(numbers)
    largest = max(numbers)
    average = sum(numbers) / len(numbers)
    evens = [num for num in numbers if num % 2 == 0]
    return smallest, largest, average, evens

lo, hi, avg, ev = analyze([4, 9, 1, 7, 10])
print(f"Q2: lo={lo}, hi={hi}, avg={avg}, ev={ev}")


# Question 3
def word_count(text):
    counts = {}
    words = text.lower().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

print("Q3:", word_count("Python is great and python is fun"))


# Question 4
def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result

print("Q4:", fizzbuzz(15))