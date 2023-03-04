#Frog jog with minimum steps
# X - start, Y - End, D - Speed
#A small frog wants to get to the other side of the road. The frog is currently located at position X and
#wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

def solution(X,Y,D):
    distance = Y - X
    num_jump_float = float (distance / D)
    num_jump_int = int (distance / D)
    num_jump_need = num_jump_int
    if (num_jump_float > num_jump_int):
        num_jump_need += 1
    print (num_jump_need)
    return (num_jump_need)
    pass


solution (0,80,40)