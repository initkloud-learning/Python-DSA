# Binary Search in Python

cards = [9, 7, 6, 4, 3, 2, 1]


def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = cards[mid]

        if mid_number == query:
            return mid
        elif mid_number < query:
            hi = mid - 1
        elif mid_number > query:
            lo = mid + 1
    return -1


print("Position:", locate_card(cards=cards, query=3))
