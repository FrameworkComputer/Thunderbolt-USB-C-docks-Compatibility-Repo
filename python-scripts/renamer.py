import os
import random
import string

# Run as python3 renamer.py
# Function to generate a random string of specified length
def random_string(length=10):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

# Generate a new random file name with .md extension
new_file = random_string() + '.md'

# Create an empty .md file with the random name
with open(new_file, 'w') as f:
    f.write('# This is a random .md file\n')

# Print the new file name
print(f'File created: {new_file}')
