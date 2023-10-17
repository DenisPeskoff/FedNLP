"""
This file contains a function for extracting scores from labels based on pre-defined mappings from label to score. 

Author: Sander Schulhoff
Contact: sschulho@umd.edu
"""

label_to_score = {
    "dovish": -1, 
    "mostly dovish": -0.5, 
    "neutral": 0, 
    "mostly hawkish": 0.5, 
    "hawkish": 1,
}

def extract_score(label: str) -> float:
    """
    Extracts the numerical score corresponding to a given label.

    Args:
    label (str): The label for which the score needs to be extracted.

    Returns:
    float: The numerical score associated with the given label, or None if the label is not found in the mapping.
    """
    label = label.lower()
    if label not in label_to_score:
        return None
    return label_to_score[label]
