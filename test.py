description1 = "Description1."
description2 = "Description2."
description3 = "Description3."


def description(pos):
    pos_int = int(pos)
    if pos_int == 1:
        return description1
    elif pos_int == 2:
        return description2
    else:
        return description3


def input_fields():
    return "<input type=\"text\" name=\"username\" id=\"username-field\" class=\"login-form-field\" " \
           "placeholder=\"Username\"><input type=\"password\" name=\"password\" id=\"password-field\" " \
           "class=\"login-form-field\" placeholder=\"Password\"> "
