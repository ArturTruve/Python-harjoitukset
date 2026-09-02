# mod06/tehtävä02
numbers = []

while True:
    input_number = input("Anna luku: ")
    if input_number == "":
        # lopeta kysely
        break
    # lisätään syötetty luku listalle
    numbers.append(int(input_number))
numbers.sort(reverse=True)

# quick"n"dirty
#print(numbers[0:5])

# for-lauseella viisi enimmäistä alkiota
for num in range(5):
    print(numbers[num])