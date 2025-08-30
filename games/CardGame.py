import random
class CardGame:
    """
    Class CardGame

    A fun class that represents a card game.

    Attributes:
        suits: The suit of the card.
        ranks: The rank of the card.
        deck: The deck of the card.

    Methods:
        print_deck(): Prints the card deck.
        _create_deck(): Creates a new deck. (private)
        pick_card(): Picks a card from the deck. (public)

    """

    def __init__(self):
        """
        Constructor.
        """

        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Ace', 'Jack', 'Queen', 'King']
        self.deck = self._create_deck()

    def _create_deck(self):
        """
        Returns a deck of cards.
        :return: Returns a deck of cards.
        """
        suit_symbols = {
            "Hearts": "\u2665",
            "Diamonds": "\u2666",
            "Clubs": "\u2663",
            "Spades": "\u2660"
        }

        return {
            suit : [f"{rank} {suit_symbols[suit]}" for rank in self.ranks] for suit in self.suits
        }

    def pick_card(self):
        """
        Picks a ramdom card from the deck.
        :return: Random card from the deck.
        """
        suit = random.choice(self.suits)
        chosen_card = random.choice(self.deck[suit])
        return chosen_card

    def print_deck(self):
        """
        Prints the deck.
        :return:
        """
        return self.deck