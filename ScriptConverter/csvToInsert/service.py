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
    print("-----------------------------------------------------\n",csv_data)
    print(type(csv_data))
    insert_str = "INSERT into "+table+" VALUES ( "
    index = 1 if include_header else 0
    print("index--------------------------------------------------",index)
    if column_header and replace_with:
        position = csv_data[0].index(column_header)
        return create_statement_with_replace(csv_data, index, insert_str, replace_with, position)
    return create_statement(csv_data, index, insert_str)


def create_statement(csv_data: list, index: int, insert_str: str):
    final = []
    for row in csv_data[index:]:
        row=row.split(",")
        final.append(insert_str+', '.join(map(str, row))+" );")
        print(insert_str+', '.join(map(str, row))+" );")
    return final


def create_statement_with_replace(csv_data: list, index: int, insert_str: str, replace_with: any, position: int):
    final = []
    for row in csv_data[index:]:
        row[position] = replace_with
        final.append(insert_str+', '.join(map(str, row))+" );")
    return final


def write_scripts(content: str, file_path: str):
    with open(file_path, "w") as f:
        for row in content:
            f.write(row)


def process_file(request):
    try:
        isheaders=False
        isreplace=False
        if request.POST.get("isheaders")=='on':
            isheaders=True
        if request.POST.get("replaceheaders")=='on':
            isreplace=True
        print("BOOLS",isheaders,isreplace)
        csv_file = request.FILES.get('csvfile')
        file_data = csv_file.read().decode("utf-8").split("\n")
        print("--------------------------------",file_data)
        if isheaders and isreplace:
            data = create_insert_script(file_data, request.POST.get("table"), isheaders, request.POST.get("replacecolumn"), request.POST.get("repacecolumnwith"))  

        if not request.POST.get("replaceheaders"):
            data = create_insert_script(file_data, request.POST.get("table"), isheaders)
            print(data)
        return data
    except Exception as e:
        print(e)
        return str(e)
