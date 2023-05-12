#BRAYDEN ZIYANG SAGA S10258659C

see = input('Does the guard see the player (y/n)? ' ) #Get whether the guard see the player
if see == 'y':
    sees_player = True
elif see == 'n':
    sees_player = False

if sees_player == False:
    print('The guard waits.')
    
elif sees_player == True:
    dist_from_player = int(input('How far away is the player? ')) #Get the distance from the player
    if dist_from_player <= 1:
        print('The guard attacks!')
    elif 2 <= dist_from_player <= 4:
        print('The guard advances.')
    elif dist_from_player >= 5:
        print('The guard waits.')
