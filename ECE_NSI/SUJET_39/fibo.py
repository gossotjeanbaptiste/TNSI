def fibonnaci(n):
    if n <= 2:
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)