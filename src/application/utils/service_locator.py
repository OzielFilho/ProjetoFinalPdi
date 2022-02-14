import inspect

binds = []


def get_dependency(data):
    for bind in binds:
        if issubclass(type(bind), data):
            return bind


def parse_dependencies(data: list):
    if (len(data) == 1):
        return data[0]
    else:
        return data[0], parse_dependencies(data[1:])


def register_bind(bind):
    dependencies = []

    init_function = inspect.signature(bind.__init__)

    for key, value in init_function.parameters.items():
        if (key != 'self' and key != 'args' and key != 'kwargs'):
            dependency = get_dependency(value.annotation)
            dependencies.append(dependency)

    instance = None

    if (len(dependencies) == 0):
        instance = bind()
    else:
        instance = bind(parse_dependencies(dependencies))

    if instance not in binds:
        binds.append(instance)
