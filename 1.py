def ob(V0,V1,t):
    def distance(acceleration):
        def wrap():
            a = acceleration(V0,V1,t)
            S = V0*t+(a*(t**2)/2)
            print(S)
        return wrap
    return distance
@ob(10,20,30)
def acceleration(V0,V1,t):
    return (V1-V0)/t

acceleration()


