
PLACEHOLDER = "[name]"

with open('Input/Names/invited_names.txt') as f:
	names = f.readlines()

print(names)

with open('Input/letters/starting_letter.txt') as letter_file:
	letter_contents = letter_file.read()
	for name in names:
		stripped_name = name.strip()
		new_letter = letter_contents.replace(PLACEHOLDER,stripped_name)
		with open(f'output/ReadyToSend/letter_for_{stripped_name}.txt',"w") as completed:
			completed.write(new_letter)