"""
Student Name : Ertuğrul Demir
Student ID : 260201059
"""
def minNumOfTrials(H , N ):
    list_of_trials = []
    if N == 1 :
        return H
    if H == 0:
        return H
    if H == 1 :
        return H
    for i in range(1,H+1):
        first = 1 + minNumOfTrials(i-1,N-1)
        second = 1 + minNumOfTrials(H-i,N)
        if first > second:
            list_of_trials.append(first)
        else:
            list_of_trials.append(second)
    list_of_trials.sort()
    return list_of_trials[0]

def numOfWays(L):
    if L == 0:
        return 1
    elif L == 1 :
        lenght = L * 100
        count20 = 0
        count40 = 0
        while lenght !=0 :
            lenght -= 20
            count20 += 1
        way_count = 1
        count20 -= 2
        count40 += 1
        while not( count20 == 1 or count20 == 0 ):    
            if count20 > count40 :
                way_count += (count20 + 1 ) * count40
            elif count40 > count20 :
                way_count += (count40 + 1 ) * count20
            else:
                way_count += count40 * count20
            count20 -= 2
            count40 += 1
        if count20 == 1 :
            way_count += count20 * (count40+1)
        elif count20 == 0 :
            way_count += 1
        return way_count
    else:
        return 11*(numOfWays( L - 1 ))+numOfWays( L - 2 ) 
        """
        L=1 , 8 | L=2, 89 | L=3, 987 | L=4, 10946
        According to these datas , I created a formula, This formula is like fibonacci formula
        My formula is f(L) = 11*f(L-1)+f(L-2)
        Therefore , I need f(1) and f(0)
        I calculated f(1) up there
        And I suppose that f(0) = 1 , Because this formula work if f(0) = 1
        So, why f(0) is 1, Because there is an option which is doing nothing
        This formula is the most speedy way for this job
        """
def bfMinNumOfTrials(H,N):
    if H == 1:
        return 1
    else:
        return 1 + bfMinNumOfTrials(H-1,N)
def main(H,N,L):
    print(minNumOfTrials(H,N))
    print(numOfWays(L))
    print(bfMinNumOfTrials(H,N))


main(10,3,4)
main(7,5,3)
main(9,1,2)
main(12,2,5)
main(6,5,1)
#-----optional----- 
#H,N,L = map(int,input("Plese Enter H N L values there is a space between them:   ").split(" "))
#main(H,N,L)
