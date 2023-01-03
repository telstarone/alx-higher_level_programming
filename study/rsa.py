def factorize(n):
    p = 2
    q = 2
    while (p * q <=n):
        while( p * q <= n):
            if (q * p == n):
                print("{} = {} * {}".format(n, q, p))
                return
            q += 1
        q = 2
        p += 1
factorize(15)
