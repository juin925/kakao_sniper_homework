import csv

class EmptyFileError(Exception): ## 사용자 정의 예외(파일 안에 내용이 비었을 떄)
    def __init__(self, message = None):
        self.message = message or "파일이 비어있습니다."

    def __str__(self):
        return self.message

def read_txt(path): ## .txt 파일 읽기
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = f.read()
            if data == "": ## 파일이 비어있다면
                raise EmptyFileError("파일이 비었습니다")
            return data
    except FileNotFoundError as e:
        print(e)
        print("읽을 파일 이름을 찾을 수가 없습니다")
    except OSError as e:
        print(e)
        print("파일 위치를 경로로 입력해야합니다.")
    

def write_txt(path, content): ## .txt 파일에 content 쓰기
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
    except FileNotFoundError as e:
        print(e)
        print("내용을 추가할 파일이름을 찾을 수가 없습니다")
    except OSError as e:
        print(e)
        print("파일 위치를 경로로 입력해야합니다.")    


def read_binary(path): ## binary 형식으로 읽기
    try:
        with open(path, "rb") as f:
            data = f.read()
            if data == "": ## 파일이 비어있다면
                raise EmptyFileError("파일이 비었습니다")
            return data
    except FileNotFoundError as e:
        print(e)
        print("읽을 파일 이름을 찾을 수가 없습니다")
    except OSError as e:
        print(e)
        print("파일 위치를 경로로 입력해야합니다.")
    
    
def write_binary(path, content): ## 바이너리
    try:
        with open(path, "wb") as f:
            f.write(content)
    except FileNotFoundError as e:
        print(e)
        print("읽을 파일 이름을 찾을 수가 없습니다")
    except OSError as e:
        print(e)
        print("파일 위치를 경로로 입력해야합니다.")


def read_csv(path): ## csv 파일 읽기
    try:
        with open(path, "r", encoding="utf-8") as f:
            csv_reader = csv.reader(f)
            list_csv_reader = list(csv_reader) ## csv 데이터를 리스트로 변환
            if len(list_csv_reader) == 0: ## 리스트 길이가 0이라면(파일이 비어있다는 뜻)
                raise EmptyFileError("파일이 비었습니다")
            header = list_csv_reader[0] ## 헤더는 리스트의 첫번째
            print(f"컬럼: {header}")

            for row in list_csv_reader[1:]: ## 리스트의 두번째 이후 모두를 순환
                print(f"데이터: {row}")
    except FileNotFoundError as e:
        print(e)
        print("읽을 파일 이름을 찾을 수가 없습니다")
    except OSError as e:
        print(e)
        print("파일 위치를 경로로 입력해야합니다.")

def write_csv(path, header, data): ## csv 파일 쓰기
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