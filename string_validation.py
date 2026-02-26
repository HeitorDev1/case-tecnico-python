def starts_with_b_and_ends_with_a(string):
    parsed_string = string.lower().strip()
    if parsed_string.startswith('b') and parsed_string.endswith('a'):
        return True


