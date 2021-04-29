from itertools import chain


def fractal_series(n: int) -> tuple:
    """Produces the fractal series for my non-recursive Hanoi tower implementation"""
    series = [1]
    for i in range(2, n+1):
        series = [series[:], [i], series[:]]
        series = list(chain.from_iterable(series))
    return tuple(series)


def hanoi(number_of_discs: int):
    """
    <summary>
    Iterative implementation of recursive version of hanoi tower.
    For decisions uses fractal series of given number of disks.
    Example of fractal series of 4 : 1,2,1,3,1,2,1,4,1,2,1,3,1,2,1
    When there are two possibilities of move then number of fractal series at some index dictate which to choose.
    </summary>

    :param number_of_discs:
    :return solved polls:
    """
    # Fractal series
    fractal_tup = fractal_series(number_of_discs)

    # The polls
    A = []
    B = []
    C = []

    # First move
    n = number_of_discs % 2

    # Accessing elements of python dictionary takes O(1) time
    polls = [A, B, C]

    for i in range(1, number_of_discs+1):
        A.append(i)

    # previous move
    p = A[0]

    A.append(2*number_of_discs)
    B.append(2*number_of_discs)
    C.append(2*number_of_discs)

    step = 0
    if n == 1:
        C.insert(0, A.pop(0))
        p = C[0]
        step += 1
    elif n == 0:
        B.insert(0, A.pop(0))
        p = B[0]
        step += 1

    for poll in polls:
        print(poll[:-1])
    print('\n')

    while step < pow(2, number_of_discs)-1:

        for i, poll in enumerate(polls):
            if poll[0] == p:
                pass
            elif poll[0] < polls[(i+1) % 3][0] and poll[0] < polls[(i+2) % 3][0]:
                if fractal_tup[step]-n % 2:
                    polls[(i+1) % 3].insert(0, poll.pop(0))
                    p = polls[(i+1) % 3][0]
                    break
                elif not fractal_tup[step]-n % 2:
                    polls[(i + 2) % 3].insert(0, poll.pop(0))
                    p = polls[(i + 2) % 3][0]
                    break

            elif poll[0] < polls[(i+1) % 3][0]:
                polls[(i + 1) % 3].insert(0, poll.pop(0))
                p = polls[(i + 1) % 3][0]
                break
            elif poll[0] < polls[(i+2) % 3][0]:
                polls[(i + 2) % 3].insert(0, poll.pop(0))
                p = polls[(i + 2) % 3][0]
                break

        for poll in polls:
            print(poll[:-1])
        print('\n')
        step += 1

    return polls


if __name__ == "__main__":
    hanoi(14)

