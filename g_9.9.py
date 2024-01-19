# Эта программа применяет словарь в качестве колоды карт.

def main():
    # Создать колоду карт.
    deck = create_deck()

    # game's keep going until there are cards in a deck.
    count = 1
    while len(deck) > 0:
        print(f"Game {count}")
        pl_1_sc, pl_2_sc = deal_cards(deck)
        get_winner(pl_1_sc, pl_2_sc)
        count += 1


def get_winner(sc1:int, sc2:int):
    '''
    evaluate who is winner on scores
    '''
    print(f'Player 1 scores: {sc1}, player 2 scores: {sc2}', end='\n\t')
    if sc1 > 21 and sc2 >21:
        print("Noone winned")
    elif sc1 <= 21 and sc2 <= 21:
        if sc1 == sc2:
            print("Players got equal scores. No winner")
        elif sc1 < sc2:
            print("Player 1 winned")
        else:
            print("Player 2 winned")
    elif sc1 < 21 and sc2 > 21:
        print("Player 1 winned")
    else:
        print("Player 2 winned")

# Функция create_deck возвращает словарь,
# представляющий колоду карт.
def create_deck():
    # Создать словарь, в котором каждая карта и ее значение
    # хранится в виде пар ключ/значение.
    deck = {'Туз пик':1, '2 пик':2, '3 пик':3,
            '4 пик':4, '5 пик':5, '6 пик':6,
            '7 пик':7, '8 пик':8, '9 пик':9,
            '10 пик':10, 'Валет пик':10,
            'Дама пик':10, 'Король пик': 10,

            'Туз червей':1, '2 червей':2, '3 червей':3,
            '4 червей':4, '5 червей':5, '6 червей':6,
            '7 червей':7, '8 червей':8, '9 червей':9,
            '10 червей':10, 'Валет червей':10,
            'Дама червей':10, 'Король червей': 10,

            'Туз треф':1, '2 треф':2, '3 треф':3,
            '4 треф':4, '5 треф':5, '6 треф':6,
            '7 треф':7, '8 треф':8, '9 треф':9,
            '10 треф':10, 'Валет треф':10,
            'Дама треф':10, 'Король треф': 10,

            'Туз бубей':1, '2 бубей':2, '3 бубей':3,
            '4 бубей':4, '5 бубей':5, '6 бубей':6,
            '7 бубей':7, '8 бубей':8, '9 бубей':9,
            '10 бубей':10, 'Валет бубей':10,
            'Дама бубей':10, 'Король бубей': 10}

    # Вернуть колоду.
    return deck

# Функция deal_cards раздает заданное количество карт
# из колоды.
def player_move(deck: dict, player_value: int):
    '''
    Deals cards to player cards until score is equal or more than 21
    and return value of scores
    Ace is scored as 11, if players score is < 20 and 1 if => 20
    '''
    while player_value < 21:
        card, value = deck.popitem()
        if card.find('Туз'):
            player_value += value
        else:
            if player_value <= 10:
                player_value += 11
            else:
                player_value += 1


    return player_value
def deal_cards(deck): #   return tuple(scores of 1st and 2nd user)
    '''
    deals cards to 2 user with decreased numbers in deck
    '''
    player1_value = player2_value = 0
    scores_1 = player_move(deck, player1_value)
    scores_2 = player_move(deck, player2_value)
    return scores_1, scores_2

# Вызвать главную функцию.
main()