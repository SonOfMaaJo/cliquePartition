def powerset(N):
    """
    Returns the powerset of a set N.
    """
    if len(N) == 0:
        return [set()]
    else:
        P = powerset(N[1:])
        return P + [subset | {N[0]} for subset in P]