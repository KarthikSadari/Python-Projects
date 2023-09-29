#Silent Auction
import os
def find_winner(bidder_details):
  highest_bidding = 0
  winner = ""
  for bidder in bidder_details:
    bidding_price = bidder_details[bidder]
    if bidding_price > highest_bidding:
      highest_bidding = bidding_price
      winner = bidder
  print(f"The Winner is {winner} with a bid price of {highest_bidding}")



bidder_data = {}
end_of_bidding =False
while not end_of_bidding:
  name = input("What is your Name ?: ")
  price = int(input("Enter Your Bid price: "))
  bidder_data[name]=price
  more_bidders = input("Are ther more bidders? Type 'yes' or 'no' :").lower()
  if more_bidders == 'no':
    end_of_bidding = True
    find_winner(bidder_data)
  elif more_bidders == 'yes':
    os.system('cls')
