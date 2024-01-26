# Print multiplication table from 1 to 10

# Pseudocode

# Outer loop to iterate over numbers from 1 to 10
for i in range(1, 11):
# Inner loop to iterate over numbers from 1 to 10 for each i
    for j in range(1, 11):
# Print the product of i and j with a space at the end
        print(i * j, end=" ")
# Print a newline character to move to the next row
    print("\t\t")