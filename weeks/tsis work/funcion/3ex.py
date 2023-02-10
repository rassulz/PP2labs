def solve (nh, nl):
    y=((4*nh-nl)/2)
    x=nh-y;
    print("rabbits ", x, " chikens ", y)
    
number_heads=int(input())
number_legs=int(input())
solve(number_heads, number_legs)
