def select_supporting_images(
    image_paths,
    confidence_scores
):

    selected = []

    for image, score in zip(
        image_paths,
        confidence_scores
    ):

        if score >= 0.70:

            selected.append(image)

    return selected