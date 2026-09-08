import random
def win_lose(usr):
    if usr == '1':
        return 'Head'
    elif usr == '2':
        return 'Tail'
    else:
        return 'Please provide valid input'
def fight(cpu_health, usr_health):
    if player_ans == ans and npc_ans == ans:
        cpu_health = cpu_health - player_damage
        usr_health = usr_health - npc_damage
        message = f'Both of you guessed correctly!\nYou dealt {player_damage} damage and the npc has {cpu_health} health\nThe npc dealt {npc_damage} damage and you have {usr_health} health'
    elif player_ans == ans and npc_ans != ans:
        cpu_health = cpu_health - player_damage
        message = f'You guessed correctly!\nYou dealt {player_damage} damage and the npc has {cpu_health} health'
    elif npc_ans == ans and player_ans != ans:
        usr_health = usr_health - npc_damage
        message = f'The npc guessed correctly!\nThe npc dealt {npc_damage} damage and you have {usr_health} health'
    else:
        message = f'Neither of you guessed correctly!\nNobody dealt damage.'
    return cpu_health, usr_health, message
# player health
player_health = 100
# npc health
npc_health = 100
# choice of head or tails
list_game = ['Head','Tail']
while player_health > 0 and npc_health > 0:
    ans = random.choice(list_game)
    print(ans)
    # usr input
    player_ans = input('Enter your choice\nHead rnter a [1]\nTail enter a [2]\n: ' )
    player_ans = win_lose(player_ans)
    print(f'You chose: {win_lose(player_ans)}')
    # DAMAGE
    player_damage = random.randint(10, 50)
    npc_damage = random.randint(10, 50)
    # actual answer
    print(f'The actual coin says: {ans}')
    # npc answer
    npc_ans = random.choice(list_game)
    print(f'The npc said: {npc_ans}')
    npc_health, player_health, message = fight(npc_health,player_health)
    print(message)
print('\nThe fight is over!')
if player_health <= 0:
    print('The NPC won!')
elif npc_health <= 0:
    print('You won!')

