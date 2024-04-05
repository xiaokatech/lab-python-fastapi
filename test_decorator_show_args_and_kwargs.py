def printer(func):
    def wrapper(*args, **kwargs):
        try:
            call_message_template = "Calling function {function_name} with arguments: {arguments_list} and keyword arguments: {keyword_arguments_dict}."
            success_message_template = "Result: {result}"
            exception_message_template = "An exception was raised: {exception_type}"
            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            print(
                call_message_template.format(
                    function_name=func.__name__,
                    arguments_list=args_repr,
                    keyword_arguments_dict=kwargs_repr,
                )
            )
            result = func(*args, **kwargs)
            print(success_message_template.format(result=result))

            return result
        except Exception as e:
            print(exception_message_template.format(exception_type=type(e).__name__))
            return None

    return wrapper


if __name__ == "__main__":
    convert_string_to_int("1")
