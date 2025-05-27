def pack_it_tup(*args):
    print(args)
    print(type(args))


def unpack_it_tup(first_name, sur_name, family_name):
    print(f"{first_name} {sur_name} {family_name}")


def pack_it_dict(**kwargs):
    print(kwargs)
    print(kwargs["f_name"])
    print(type(kwargs))


def unpack_it_dict(f_name, s_name, fa_name):
    print(f"{f_name} {s_name} {fa_name}")


# full_name = ["Iavor", "Georgiev", "Stoimenov"]

# pack_it_tup(*full_name)
# unpack_it_tup(*full_name)
full_name_dict = {
    "f_name": "Iavor",
    "s_name": "Georgiev",
    "fa_name": "Stoimenov",
}

pack_it_dict(f_name="Yavor", sur_name="Georgiev", family_name="Stoimenov")
pack_it_dict(**full_name_dict)
# unpack_it_dict(**full_name_dict)
