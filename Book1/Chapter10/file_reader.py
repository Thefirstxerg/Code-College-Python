from pathlib import Path

path = Path("data.txt")
contents = path.read_text()

new_path = Path("data2.txt")

# Open the file 'data2.txt' in append mode using 'a' and assign it to the variable 'file'
with new_path.open('a') as file:
    # Loop 9 times (from 1 to 9)
    for i in range(1, 10):
        # Write the contents of 'data.txt' followed by a newline character to 'data2.txt'
        file.write("A very infromative string" + '\n')

# Open the file 'data2.txt' in append mode using 'a' and assign it to the variable 'file'
with path.open('a') as file:
    # Loop 9 times (from 1 to 9)
    for i in range(1, 10):
        # Write the contents of 'data.txt' followed by a newline character to 'data2.txt'
        file.write("A very infromative string" + '\n')
        file.clear()
