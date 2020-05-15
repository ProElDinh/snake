snake_size = 20
food_size = 20



def brain(head_pos,food_pos,Traectory,body_pos):
    Trac= None

    wall_pos=[40,580,780,0]
    if snakebody(head_pos,body_pos,Traectory)!=None:
        Trac= snakebody(head_pos, body_pos,Traectory)

    elif (head_pos[0] in wall_pos and head_pos[1]!=food_pos[1]) or (head_pos[1] in wall_pos and head_pos[0]!=food_pos[0]):
        Trac = corners(head_pos,Traectory,food_pos)
    else:
        Trac = run_to_food(head_pos,food_pos,Traectory,body_pos)
    return Trac
#Snake go to food if not corners
def run_to_food(head_pos,food_pos,Traectory,body_pos):
    Trac=None
    x = [i[0] for i in body_pos]
    y = [i[1] for i in body_pos]
    if (head_pos[0]+ snake_size in x[1::] and food_pos[0] in x[1::]) or (head_pos[1]+ snake_size in y[1::] and food_pos[1] in y[1::]):
        Trac = None
    else:
        if head_pos[0] == food_pos[0] and head_pos[1]<food_pos[1] and Traectory!='UP':
            Trac = 'DOWN'
        elif head_pos[0] == food_pos[0] and head_pos[1]>food_pos[1] and Traectory!='DOWN':
            Trac = 'UP'
        elif head_pos[1] == food_pos[1] and head_pos[0]<food_pos[0] and Traectory!='LEFT':
            Trac = 'RIGHT'
        elif head_pos[1] == food_pos[1] and head_pos[0]>food_pos[0] and Traectory!='RIGHT':
            Trac = 'LEFT'

    return Trac
#If snake meet a corners
def corners(head_pos,Traectory,food_pos):
    wall_pos=[[0,40],[0,580],[780,40],[780,580]]

    head_pos1=head_pos[:]
    head_pos1.append(Traectory)
    Tract={
        (0,40,'UP'):'RIGHT',
        (0,40,'LEFT'):'DOWN',
        (0,580,'DOWN'):'RIGHT',
        (0, 580, 'LEFT'): 'UP',
        (780,40, 'RIGHT'): 'DOWN',
        (780, 40, 'UP'): 'LEFT',
        (780,580, 'DOWN'):'LEFT',
        (780, 580, 'RIGHT'): 'UP'
    }

    if head_pos in wall_pos:
        return Tract[tuple(head_pos1)]
    else:
        if (head_pos[0] == 0 or head_pos[0] == 780):
            if head_pos[1]- food_pos[1]>=0 and Traectory!='DOWN':
                return 'UP'
            elif head_pos[1]- food_pos[1]<0 and Traectory!='UP':
                return 'DOWN'
        elif (head_pos[1] == 40 or head_pos[1] == 580):
            if head_pos[0]- food_pos[0]>=0 and Traectory!='RIGHT':
                return 'LEFT'
            elif head_pos[0]- food_pos[0]<0 and Traectory!='LEFT':
                return 'RIGHT'
#Snake is not going to food if see his body
def snakebody(head_pos, body_pos,Traectory):
    x = [i[0] for i in body_pos]
    y = [i[1] for i in body_pos]
    if ([head_pos[0], head_pos[1] + snake_size] in body_pos and Traectory == 'DOWN'):
        return 'LEFT' if head_pos[0] - x[x.index(head_pos[0])]<0 else 'RIGHT'
    elif ([head_pos[0],head_pos[1] - snake_size] in body_pos and Traectory=='UP'):
        return 'LEFT' if head_pos[0] - x[x.index(head_pos[0])] <0 else 'RIGHT'
    elif ([head_pos[0]+snake_size,head_pos[1]] in body_pos and Traectory == 'RIGHT'):
        return 'UP' if head_pos[1] - y[y.index(head_pos[1])] < 0 else 'DOWN'
    elif ([head_pos[0]-snake_size,head_pos[1]] in body_pos and Traectory== 'LEFT'):
        return 'UP' if head_pos[1] - y[y.index(head_pos[1])] < 0 else 'DOWN'

#def bodyline():
    #if [head_pos[0]+ snake_size ,head_pos[1]] in body_pos and (Traectory == 'DOWN' or Traectory == 'UP') and food_size[0] in head_pos[0]:
        