def movie_Ticket():

    movieChoice = input("Available movies today:\nA)12 Strong:   1)2:30  2)4:40 3)7:50 4)10:50\nB)Coco:        1)12:40 2)3:45\nC)The Post:    1)12:45 2)3:35 3)7:05 4)9:55\nMovie choice: ").upper()

    # Validate user selected movie.
    if movieChoice != 'A' and movieChoice != 'B' and movieChoice != 'C':
        print("Invalid option; please restart app...")
        return

    timeChoice = int(input("Showtime: "))

    # Validate user selected time.
    if timeChoice < 1:
        print("Invalid option; please restart app...")
        return
    elif movieChoice == "A":
        if timeChoice > 4:
            print("Invalid option; please restart app...")
            return
    elif movieChoice == "B":
        if timeChoice > 2:
            print("Invalid option; please restart app...")
            return
    else:
        if timeChoice > 4:
            print("Invalid option; please restart app...")
            return

    ticketAmountAdult = int(input("Adult tickets: "))

    # Validate user selected ticket amount (Adult)
    if ticketAmountAdult > 30:
        print("Invalid option; please restart app...")
        return

    ticketAmountKid = int(input("Kid tickets: "))

    # Validate user selected ticket amount (Kid)
    if ticketAmountAdult + ticketAmountKid > 30:
        print("Invalid option; please restart app...")
        return

    if (movieChoice == "B" or movieChoice == "C") and timeChoice == 1:
        adultTicketPrice = 11.17
        kidTicketPrice = 8.00
    else:
        adultTicketPrice = 12.45
        kidTicketPrice = 9.68

    #Calculate Total
    totalCost = format(ticketAmountAdult * adultTicketPrice +
                       ticketAmountKid * kidTicketPrice, '.2f')

    print("Total cost: $", totalCost, sep='')


movie_Ticket()
