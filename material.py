

def header_end():

    f = open("header" + ".txt", "r")

    end = '''\end{questions}
           \end{document}'''

    header = f.read()

    f.close()

    return (header, end)

# %%


def body_of_text(format_filled):
    f = open(format_filled + ".txt", "rb")

    body = f.read().decode()

    f.close()

    return (body)

# %%


def answers_right(path_answers_right):

    f = open(path_answers_right + ".txt", "r")

    answer = f.read()
    answer = answer.upper().split(",")

    f.close()

    return (answer)
