def get_headers(csv_file:str) -> list:
    lines = csv_file.split("\n")
    #print(lines)
    headers=lines[0].split(',')
    return headers