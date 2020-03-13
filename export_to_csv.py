import pandas


def export(data, file_name):
    df = pandas.DataFrame(data=data)
    df.to_csv(file_name)
