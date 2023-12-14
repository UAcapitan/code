
from inspect import signature


def tag(name, *content, cls=None, **attrs):
    if cls:
        attrs["class"] = cls

    if attrs:
        attr_str = ''.join(f' {attr}="{value}"' for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    
    if content:
        return "\n".join(f"<{name}{attr_str}>{c}</{name}>" for c in content)
    else:
        return f"<{name}{attr_str}/>"


if __name__ == "__main__":
    print(tag('img', cls="test"))
    print(tag('div', tag("p", "Hello, world"), cls="test"))
    print(tag('img', data="test"))

    sig = signature(tag)

    for name, param in sig.parameters.items():
        print(param.kind, ":", name, "=", param.default)

    args = {'name': 'img', 'data': 'test', 'cls': 'data'}
    
    bound_args = sig.bind(**args)

    for name, value in bound_args.arguments.items():
        print(name, "=", value)
