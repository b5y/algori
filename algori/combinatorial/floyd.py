from itertools import islice, chain, izip, repeat


def floyd(seq=None):
    try:
        tortoise = iter(seq)
        tortoise_val = next(tortoise)
        hare = islice(iter(seq), None, None, 2)
        hare_val = next(hare)
        for tortoise_val, hare_val in izip(tortoise, hare):
            if tortoise_val == hare_val:
                break
        hare = tortoise
        hare_val = tortoise_val
        tortoise = iter(seq)
        tortoise_val = next(tortoise)
        mu = 0
        for tortoise_val, hare_val in chain(repeat((tortoise_val, hare_val), 1), izip(tortoise, hare)):
            if tortoise_val != hare_val:
                mu += 1
        lam = 0
        hare = tortoise
        for hare_val in hare:
            lam += 1
            if hare_val == tortoise_val:
                break
        return lam, mu
    except TypeError, te:
        print seq, 'is not iterable', te
