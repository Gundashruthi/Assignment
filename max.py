# 1.Create a user-defined function max_value() that returns the maximum value from a list. If the list contains both numbers and strings, handle them properly so the function still works without error.


def max_value(lst):
    numbers = [x for x in lst if isinstance(x, (int, float))]
    strings = [x for x in lst if isinstance(x, str)]

    max_num = max(numbers) if numbers else None
    max_str = max(strings) if strings else None

    if max_num is not None and max_str is not None:
        return f"Max number: {max_num}, Max string: '{max_str}'"
    elif max_num is not None:
        return f"Max number: {max_num}"
    elif max_str is not None:
        return f"Max string: '{max_str}'"
    else:
        return "List is empty or has unsupported data types."


data = [10, 'apple', 25, 'banana', 3.5, 'zebra']
print(max_value(data))


# 2. Create a user-defined function title_case() that converts the first letter of each word in a string to uppercase (like the built-in title() function).



def title_case(text):
    words = text.split()
    result = " ".join(word[0].upper() + word[1:].lower() if word else "" for word in words)
    return result


text = "hello world this is python"
print(title_case(text))