# TODO: Provide a welcome message Y
# TODO: Display the entrance ticket prices Y
# TODO: Ask how many adult tickets are required Y
# TODO: Ask how many child tickets are required Y
# TODO: Ask how many senior citizen tickets are required Y
# TODO: Ask for the lead booker surname (for the ticket) Y
# TODO: Ask if they require a parking pass for the car park
# TODO: Add the total number of tickets to display the total cost
# TODO: Print a ticket (display lead booker surname, tickets purchased, today's date)
#       Print a car parking pass (if requested)
#       Use data validation techniques to avoid runtime errors through incorrect data entry
#       Thank the customer for their purchase

def printWelcomeMessage():
  print("""Welcome to Jumanji!\r
Home of ferocious beasts and mysterious artifacts\r
Whether you run through a maze or fight a jaguar, remember to have fun!\n""")

def printTicketPrices():
  print ("{:<20} {:>10}".format('Ticket','Price'))
  print("-------------------------------")
  print ("{:<20} {:>10}".format('Adult','£20'))
  print ("{:<20} {:>10}".format('Child','£12'))
  print ("{:<20} {:>10}".format('Senior Citizen','£11'))

def getTicket(prompt):
  try:
    tickets = int(input(prompt))
    if (tickets < 0):
      return Exception
  except:
    return Exception
  
  return tickets

printWelcomeMessage()
printTicketPrices()

transactionCompleted = False

while not(transactionCompleted):
  try:
    adultTickets = getTicket("How many adult tickets would you like? ")
    childTickets = getTicket("How many child tickets would you like? ")
    seniorTickets = getTicket("How many senior citizen tickets would you like? ")
  except(Exception):
    print("Please enter a non-negative integer")
    continue


