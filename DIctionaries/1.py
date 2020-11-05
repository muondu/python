def tryal():
    database = {}
    schema = dict(Fname = "firstName")
    for key,value in schema.items():
        database[key] = input('Please enter your {}: '.format(value))
        print(database)
        asking = input("Do you want to add another entry yes(Y) or no(N):  ")
        if asking == "Y":
            tryal()
        else:
            print("Goodbye.")
tryal()