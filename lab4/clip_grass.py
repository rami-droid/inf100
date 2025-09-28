def clip_grass(heights, max_height):
    for i in range(len(heights)):
        if heights[i] > max_height:
            heights[i] = max_height
    return


def get_adults(people):
    adults = []
    for person in people:
        if person["age"] >= 18:
            adults.append(person)

    return adults
