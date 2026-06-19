def calculate_score(num_images, duplicate_found):

    score = 10

    if num_images < 2:
        score += 30

    if duplicate_found:
        score += 40

    return min(score, 100)