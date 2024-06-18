mail = ""
names =""

# TODO 1. First read the starting letter
with open("./Input/Letters/starting_letter.txt") as file:
    mail = file.read()

with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()


for _ in names:
    name_after_modify = _.strip()
    a_mail = mail.replace('[name]', name_after_modify)

    # TODO 2. Write the mails in the output files
    with open(f"./Output/ReadyToSend/letter_for_{name_after_modify}.txt", "w") as file:
        file.write(a_mail)







