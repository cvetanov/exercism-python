def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    top = []
    i = 0
    iterations = min([len(scores), 3])
    while (i < iterations):
        top_current = max(scores)
        top.append(top_current)
        scores.remove(top_current)
        i += 1
    return top
