with open('input') as infile:
    firstctr = 0
    secondctr = 0
    for line in infile.readlines():
        amountspec, letter, password = line.strip().split()
        mina, maxa = amountspec.split('-')
        mina, maxa = int(mina), int(maxa)
        letter = letter[0]
        if mina <= password.count(letter) <= maxa:
            firstctr += 1
        if (password[mina - 1] == letter) != (password[maxa - 1] == letter):
            secondctr += 1
    print(firstctr)
    print(secondctr)