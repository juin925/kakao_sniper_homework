import csv

class EmptyFileError(Exception):
    def __init__(self, message = None):
        self.message = message or "파일이 비어있습니다."

def read_txt(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = f.read()
            if data == "":
                raise EmptyFileError("파일이 비었습니다")
            return data
    except FileNotFoundError as e:
        print(e)
        print("읽을 파일 이름을 찾을 수가 없습니다")
    except OSError as e:
        print(e)
        print("파일 위치를 경로로 입력해야합니다.")
    

def write_txt(path, content):
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
    except FileNotFoundError as e:
        print(e)
        print("내용을 추가할 파일이름을 찾을 수가 없습니다")
    except OSError as e:
        print(e)
        print("파일 위치를 경로로 입력해야합니다.")    


def read_binary(path):
    try:
        with open(path, "rb") as f:
            data = f.read()
            if data == "":
                raise EmptyFileError("파일이 비었습니다")
            return data
    except FileNotFoundError as e:
        print(e)
        print("읽을 파일 이름을 찾을 수가 없습니다")
    except OSError as e:
        print(e)
        print("파일 위치를 경로로 입력해야합니다.")
    
    
def write_binary(path, content):
    try:
        with open(path, "wb") as f:
            f.write(content)
    except FileNotFoundError as e:
        print(e)
        print("읽을 파일 이름을 찾을 수가 없습니다")
    except OSError as e:
        print(e)
        print("파일 위치를 경로로 입력해야합니다.")


def read_csv(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            csv_reader = csv.reader(f)
            list_csv_reader = list(csv_reader)
            if len(list_csv_reader) == 0:
                raise EmptyFileError("파일이 비었습니다")
            header = list_csv_reader[0]
            print(f"컬럼: {header}")

            for row in list_csv_reader[1:]:
                print(f"데이터: {row}")
    except FileNotFoundError as e:
        print(e)
        print("읽을 파일 이름을 찾을 수가 없습니다")
    except OSError as e:
        print(e)
        print("파일 위치를 경로로 입력해야합니다.")

def write_csv(path, header, data):
    try:
        with open(path, "w", newline="", encoding="utf-8") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(header)
            csv_writer.writerows(data)
    except FileNotFoundError as e:
        print(e)
        print("읽을 파일 이름을 찾을 수가 없습니다")
    except OSError as e:
        print(e)
        print("파일 위치를 경로로 입력해야합니다.")