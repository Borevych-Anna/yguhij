def capitalize_decorator(func):


    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if isinstance(result, str):
            return result.capitalize()

        return result

    return wrapper