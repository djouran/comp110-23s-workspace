from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str,str]]:
    """Read csv file and return as a list of dicts with header keys"""
    result: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result

def column_values(table: list[dict[str,str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header."""
    result: list[str] = []
    for row in table:
        result.append(row[header])
    return result

def columnar(table: list[dict[str, str]]) -> dict[str,list[str]]:
    """Reformats data so that it's a dictionary with column headers as keys."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = table[0]
    for key in first_row:
        result[key] = column_values(table, key)
    return result

def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Visualizes Data."""
    result: dict[str, list[str]] = {}
    columns = list(table.keys())
    for column in columns:
        list1: list[str] = []
        for item in table[column][:rows]:
            list1.append(item)
        result[column] = list1
    return result

def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Select specific columns from a column-based table."""
    result: dict[str, list[str]] = {}
    for column in columns:
        result[column] = table[column]
    return result

def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    result = {}
    for col in table1:
        result[col] = table1[col]
    for col in table2:
        if col in result:
            result[col].extend(table2.get(col, []))
        else:
            result[col] = table2.get(col, [])
    return result


def count(values: list[str]) -> dict[str, int]:
    result = {}
    for value in values:
        if value in result:
            result[value] += 1
        else:
            result[value] = 1
    return result