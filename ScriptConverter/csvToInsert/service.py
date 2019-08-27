def get_headers(csv_file: str) -> list:
    lines = csv_file.split("\n")
    # print(lines)
    headers = lines[0].split(',')
    return headers


def replace_column(scripts: list, headers: list, column_header: str, replace_with: any) -> list:
    position = headers.index(column_header)
    for row in scripts:
        row[position] = replace_with


def create_insert_script(csv_data: list, table, include_header: bool, column_header=None, replace_with=None):
    insert_str = "INSERT into "+table+" VALUES ( "
    index = 0 if include_header else 1
    if index and column_header and replace_with:
        position = csv_data[0].index(column_header)
        return create_statement_with_replace(csv_data, index, insert_str, replace_with, position)
    return create_statement(csv_data, index, insert_str)


def create_statement(csv_data: list, index: int, insert_str: str):
    final = []
    for row in csv_data[index:]:
        final.append(insert_str+', '.join(map(str, row))+" );\n")
    return final


def create_statement_with_replace(csv_data: list, index: int, insert_str: str, replace_with: any, position: int):
    final = []
    for row in csv_data[index:]:
        row[position] = replace_with
        final.append(insert_str+', '.join(map(str, row))+" );\n")
    return final


def write_scripts(content: str, file_path: str):
    with open(file_path, "w") as f:
        for row in content:
            f.write(row)


def process_file(request):
    try:
        csv_file = request.FILES.get('csvfile')
        file_data = csv_file.read().decode("utf-8").split("\n")
        if request.POST.get("isheaders") and request.POST.get("replaceheaders"):
            data = create_insert_script(file_data, request.POST.get("table"), request.POST.get(
                "isheaders"), request.POST.get("replacecolumn"), request.POST.get("repacecolumnwith"))  

        if not request.POST.get("replaceheaders"):
            data = create_insert_script(file_data, request.POST.get("table"), request.POST.get(
                "isheaders"))

        return "\n".join(data)
    except Exception as e:
        print(e)
        return str(e)
