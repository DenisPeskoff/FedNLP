label_to_score = {
    "dovish": -1, 
    "mostly dovish":-0.5, 
    "neutral": 0, 
    "mostly hawkish": 0.5, 
    "hawkish": 1,
}

def extract_score(label: str) -> float:
    label = label.lower()
    if label not in label_to_score:
        return None
    return label_to_score[label]