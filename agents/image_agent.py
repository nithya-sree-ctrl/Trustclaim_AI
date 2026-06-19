from image_analysis.damage_detector import detect_damage
from image_analysis.duplicate_detector import detect_duplicate

def analyze_images(images):

    damage = detect_damage(images)

    duplicate = detect_duplicate(images)

    return {
        "damage": damage,
        "duplicate": duplicate
    }