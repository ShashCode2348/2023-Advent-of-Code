def hand_type(hand, unique_chars, j_count):
    if len(unique_chars) in (0, 1):
        return '6'
    elif len(unique_chars) == 2:
        if hand.count(unique_chars[0]) in (1, 4 - j_count):
            return '5'
        else:
            return '4'
    elif len(unique_chars) == 3:
        if 3 - j_count in map(lambda x:hand.count(x), unique_chars):
            return '3'
        else:
            return '2'
    elif len(unique_chars) == 4:
        return '1'
    else:
        return ''

file = open('Camel Cards.in')
hands_1 = {}
hands_2 = {}
card_strength_1 = {'2':'0', '3':'1', '4':'2', '5':'3', '6':'4', '7':'5', '8':'6', '9':'7',
                 'T':'8', 'J':'9', 'Q':'A', 'K':'B', 'A':'C'}
card_strength_2 = {'J':'0', '2':'1', '3':'2', '4':'3', '5':'4', '6':'5', '7':'6', '8':'7', '9':'8',
                 'T':'9', 'Q':'A', 'K':'B', 'A':'C'}
p1 = p2 = 0

for line in file:
    hand, bid = line.split()
    mod_hand = hand.replace('J', '')
    hand_score_1 = hand_type(hand, list(set(hand)), 0)
    hand_score_2 = hand_type(mod_hand, list(set(mod_hand)), len(hand) - len(mod_hand))
    for card in hand:
        hand_score_1 += card_strength_1[card]
        hand_score_2 += card_strength_2[card]
    hands_1[int(hand_score_1, 13)] = int(bid)
    hands_2[int(hand_score_2, 13)] = int(bid)

for rank, score in enumerate(sorted(hands_1), 1):
    p1 += hands_1[score] * rank
for rank, score in enumerate(sorted(hands_2), 1):
    p2 += hands_2[score] * rank
print('Part 1:', p1, '\nPart 2:', p2)
