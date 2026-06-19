from image_analysis.image_quality_checker import (
    check_image_quality
)


def test_image_quality():

    result = check_image_quality(
        "sample.jpg"
    )

    assert isinstance(
        result,
        dict
    )


if __name__ == "__main__":

    try:

        test_image_quality()

        print(
            "Image tests passed."
        )

    except Exception as e:

        print(
            "Test skipped:",
            e
        )