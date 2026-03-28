# utils.py

def calculate_sum(numbers):
    """Returns the sum of a list of numbers."""
    return sum(numbers)

def split_words(text, delimiter=" "):
    """Splits a string into a list of words based on a delimiter."""
    return text.split(delimiter)

def sort_numbers(numbers, descending=False):
    """Sorts a list of numbers in ascending or descending order."""
    return sorted(numbers, reverse=descending)

# Quick test to see them in action
if __name__ == "__main__":
    nums = [10, 5, 8, 20]
    sentence = "Python is pretty versatile"
    
    print(f"Sum: {calculate_sum(nums)}")
    print(f"Words: {split_words(sentence)}")
    print(f"Sorted: {sort_numbers(nums)}")

    