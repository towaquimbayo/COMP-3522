"""
Implements the observer pattern and simulates a simple auction.
"""
import random


class Auctioneer:
    """
    The auctioneer acts as the "core". This class is responsible for
    tracking the highest bid and notifying the bidders if it changes.
    """

    def __init__(self):
        self.bidders = []
        self._highest_bid = 0
        self._highest_bidder = None

    def register_bidder(self, bidder):
        """
        Adds a bidder to the list of tracked bidders.
        :param bidder: object with __call__(auctioneer) interface.
        """
        self.bidders.append(bidder)

    def reset_auctioneer(self):
        """
        Resets the auctioneer. Removes all the bidders and resets the
        highest bid to 0.
        """
        self.bidders = []
        self._highest_bid = 0
        self._highest_bidder = None

    def _notify_bidders(self):
        """
        Executes all the bidder callbacks. Should only be called if the
        highest bid has changed.
        """
        [bidder(self) for bidder in self.bidders if bidder is not self._highest_bidder]

    def accept_bid(self, bid, bidder):
        """
        Accepts a new bid and updates the highest bid. This notifies all
        the bidders via their callbacks.
        :param bid: a float.
        :precondition bid: should be higher than the existing bid.
        :param bidder: The object with __call__(auctioneer) that placed
        the bid.
        """
        if bid > self._highest_bid:
            self._highest_bid = bid
            self._highest_bidder = bidder
            self._notify_bidders()


class Bidder:
    def __init__(self, name, budget=100, bid_probability=0.35, bid_increase_perc=1.1):
        self.name = name
        self.bid_probability = bid_probability
        self.budget = budget
        self.bid_increase_perc = bid_increase_perc
        self.highest_bid = 0

    def __call__(self, auctioneer):
        if (
            random.random() < self.bid_probability
            and auctioneer._highest_bid * self.bid_increase_perc <= self.budget
        ):
            self.highest_bid = auctioneer._highest_bid * self.bid_increase_perc
            print(
                f"{self.name} bidded ${self.highest_bid} in response to {auctioneer._highest_bidder}'s bid of ${auctioneer._highest_bid}!"
            )
            auctioneer.accept_bid(self.highest_bid, self)

    def __str__(self):
        return self.name


class Auction:
    """
    Simulates an auction. Is responsible for driving the auctioneer and
    the bidders.
    """

    def __init__(self, bidders):
        """
        Initialize an auction. Requires a list of bidders that are
        attending the auction and can bid.
        :param bidders: sequence type of objects of type Bidder
        """
        self.bidders = bidders
        self.auctioneer = Auctioneer()
        [self.auctioneer.register_bidder(bidder) for bidder in self.bidders]

    def simulate_auction(self, item, start_price):
        """
        Starts the auction for the given item at the given starting
        price. Drives the auction till completion and prints the results.
        :param item: string, name of item.
        :param start_price: float
        """
        print(f"Auctioning {item} starting at ${start_price}")
        self.auctioneer.accept_bid(start_price, "Starting Bid")
        print(
            f"The winner of the auction is: {self.auctioneer._highest_bidder} at ${self.auctioneer._highest_bid}"
        )
        [
            print(f"Bidder: {bidder.name} Highest Bid: {bidder.highest_bid}")
            for bidder in self.bidders
        ]


def main():
    bidders = [
        Bidder("Jojo", 3000, random.random(), 1.2),
        Bidder("Melissa", 7000, random.random(), 1.5),
        Bidder("Priya", 15000, random.random(), 1.1),
        Bidder("Kewei", 800, random.random(), 1.9),
        Bidder("Scott", 4000, random.random(), 2),
    ]

    print("\n\nStarting Auction!!")
    print("------------------")
    my_auction = Auction(bidders)
    my_auction.simulate_auction("Antique Vase", 100)


if __name__ == "__main__":
    main()
