import csv


def read_file(file_path, mode):
    with open(file_path, mode) as f:
        return list(csv.reader(f))


def get_headers(csv_data: list):
    headers = ', '.join(map(str, csv_data[0]))
    return headers


def create_script(csv_data: list, table, include_header: bool):
    insert_str = "INSERT into "+table+" VALUES ( "
    final = []
    index = 0 if include_header else 1
    for row in csv_data[index:]:
        statement = insert_str+', '.join(map(str, row))+" );\n"
        final.append(statement)
    return final


def write_scripts(content: str, file_path: str):
    with open(file_path, "w") as f:
        for row in content:
            f.write(row)


data = create_script(read_file("resources/data.csv", "rt"), "abc", False)
get_headers(read_file("resources/data.csv", "rt"))
print(data)
write_scripts(data, "resources/data.sql")

