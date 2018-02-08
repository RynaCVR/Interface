

def args_to_dict(args):
    args_dict = dict(args)
    args_keys = args.keys()
    new_args_dict = dict()

    for key in args_keys:
        new_args_dict[key] = args_dict[key][0]
    return new_args_dict
