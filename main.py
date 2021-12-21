names = []
with open("Input/Names/invited_names.txt") as file:
    names = file.read().split('\n')

letter_template = ''
with open("Input/Letters/starting_letter.txt") as template:
    letter_template = template.read()

for name in names:
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as output:
        output_letter = letter_template.replace("[name]", name)
        output.write(output_letter)
