def lcs_algo_aux ( S1 , S2 , m , n ) :
    L = [ [ 0 for x in range ( n + 1 ) ] for x in range ( m + 1 ) ]
    
    # Building the mtrix in bottom-up way
    for i in range ( m + 1 ) :
        for j in range ( n + 1 ) :
            if i == 0 or j == 0 :
                L [ i ] [ j ] = 0
            elif S1 [ i - 1 ] == S2 [ j - 1 ] :
                L [ i ] [ j ] = L [ i - 1 ] [ j - 1 ] + 1
            else :
                L [ i ] [ j ] = max ( L [ i - 1 ] [ j ] , L [ i ] [ j - 1 ] )
    
    index = L [ m ] [ n ]
    
    lcs_algo = [ ]
    
    i = m
    j = n
    while i > 0 and j > 0 :
        
        if S1 [ i - 1 ] == S2 [ j - 1 ] :
            lcs_algo.insert ( 0 , S1 [ i - 1 ] )
            i -= 1
            j -= 1
            index -= 1
        
        elif L [ i - 1 ] [ j ] > L [ i ] [ j - 1 ] :
            i -= 1
        else :
            j -= 1
    
    for i in range ( 0 , len ( lcs_algo ) ) :
        
        actualStr = str ( lcs_algo [ :len ( lcs_algo ) - i ] ).strip ( "[]" )
        
        if actualStr in str ( S1 ) and actualStr in str ( S2 ) :
            return actualStr
    
    return ""

def lcs_algo ( S1 , S2 , m , n ) :
    l = [ ]
    r = [ ]
    for i in range ( 0 , len ( S2 ) ) :
        l.append ( lcs_algo_aux ( S1 , S2 [ i : ] , len ( S1 ) , len ( S2 [ i : ] ) ) )
    l = list ( dict.fromkeys ( l ) )
    for i in l :
        for j in l :
            if i != j :
                if i in j :
                    r.append ( i )
    for r1 in r :
        if r1 in l :
            l.remove ( r1 )
    
    return l
