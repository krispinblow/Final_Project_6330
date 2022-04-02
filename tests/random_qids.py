import uuid


def random_suffix():
    return uuid.uuid4().hex[:1]


def random_ques(name=""):
    return f"ques-{name}-{random_suffix()}"


def random_questionqid(name=""):
    return f"question-{name}-{random_suffix()}"


def random_d_id(name=""):
    return f"order-{name}-{random_suffix()}"