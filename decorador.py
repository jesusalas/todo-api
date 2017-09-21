import inspect


def filter(func):
    def wrapper(*args, **kwargs):
        bound_args = inspect.signature(func).bind(*args, **kwargs)
        bound_args.apply_defaults()
        params = dict(bound_args.arguments)

        if type(params["name"]) != str:
            params["name"] = "Nan"

        if type(params["age"]) == str or (params["age"] == int and params["age"] < 18):
            params["age"] = "Nan"

        params_t = (params["name"], params["age"])
        return func(*params_t)
    return wrapper


@filter
def welcome_message(name, age):
    print("Mi Nombre es: {0} y tengo {1}".format(name, age))


welcome_message("Jose", 19)
