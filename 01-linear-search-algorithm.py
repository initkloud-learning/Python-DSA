# Linear Search Algorithm

def locate_card(cards, query):
    position = 0

    while True:
        if cards[position] == query:
            return position
        position += 1

        if position == len(cards):
            return -1


def locate_card02(cards, query):
    position = 0

    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1

        if position == len(cards):
            return -1

# Complexity and identify inefficiencies
