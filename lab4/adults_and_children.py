def get_adults(people):
    adults = []
    for person in people:
        if person["age"] >= 18:
            adults.append(person)

    return adults


def remove_children(people):
    people[:] = [p for p in people if p["age"] >= 18]
