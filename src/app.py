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

    :param file_path:
    :return:
    """
    response: dict = {}
    with open(file_path) as file_reader:
        reader = file_reader.read()
        parameters = reader.split("\n")
        count_messages = len(parameters)
        count_error, count_success = 0, 0
        response["Total"] = count_messages

        data_comp = [item if "ERROR" in item else None for item in parameters]
        # print(data_comp)
        for item in parameters:
            if "ERROR" in item:
                count_error += 1
            if "SUCCESS" in item:
                count_success += 1

        response["ErrorCount"] = count_error
        response["SuccessCount"] = count_success
    return response


FILE_PATH = "resources/log.log"
data = statics_log(file_path=FILE_PATH)
print(data)
