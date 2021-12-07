log_data_a = {"timestamp": "20211102T00:00", "application": "app", "category": "SUCESS", "message": "No problem here"}
log_data_b = {"timestamp": "20211102T00:01", "application": "app", "category": "SUCESS", "message": "No problem here"}
log_data_c = {"timestamp": "20211102T00:02", "application": "app", "category": "SUCESS", "message": "No problem here"}
log_data_d = {"timestamp": "20211130T00:00", "application": "app", "category": "SUCESS",
              "message": "No problem here"}  # JSON

data = []
data.append(log_data_a)
data.append(log_data_b)
data.append(log_data_c)
# print(data)
data[0]

status = ("SUCCESS", "ERROR", "INFO")

# 1
# PEP-8
MAX_NUM = 100


def statics_log(file_path: str) -> dict:
    """
    # statics_log is a function ...
    Response
        ErrorCount : Cantidad de mensajes de error.
        SuccessCount : Cantidad de mensajes de éxito (successful).
        Total : Número total de mensajes.

    :rtype: object
    :param file_path:
    :return:
    """
    response: dict = {}
    with open(file_path) as file_reader:
        reader = file_reader.read()
        parameters = reader.split("\n")
        count_messages = len(parameters)
        response["Total"] = count_messages
        data_comp_error = [item for item in parameters if 'ERROR' in item]
        data_comp_success = [item for item in parameters if 'SUCCESS' in item]
        response["ErrorCount"] = len(data_comp_error)
        response["SuccessCount"] = len(data_comp_success)
    return response


def get_data_log(file_path: str):
    with open(file_path) as file_reader:
        reader = file_reader.read()
        parameters = reader.split("\n")
        return parameters


def filter_log(request: dict, path: str):
    """

    :return:
    """
    # category: app
    # timestamp: 1213123123.12
    result = []
    data = get_data_log(file_path=path)
    if data is not None:
        for item in data:
            category_value = request.get("category")
            if category_value:
                # filtra por category
                if "ERROR" in item:
                    result.append(item)
    return result
