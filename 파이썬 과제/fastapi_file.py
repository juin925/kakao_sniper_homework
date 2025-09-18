import os
import zipfile
from typing import List
from fastapi import FastAPI, HTTPException, File, UploadFile, Query
from fastapi.responses import FileResponse, StreamingResponse
import uvicorn

app = FastAPI()

@app.post('/upload-file/') # 파일 업로드
async def upload_file(file: List[UploadFile] = File(...)):
    results = []

    for i in range(len(file)):
        print(f'recieved file: {file[i].filename}')
        
        allowed_types = ['image/jpeg', 'image/png', 'image/gif']
        
        content = await file[i].read()
        file_size = len(content)

        if file_size > 5 * 1024 * 1024:
            raise HTTPException(
                status_code=400,
                detail='파일 크기가 5MB를 초과합니다'
            )

        upload_dir = 'uploads'
        os.makedirs(upload_dir, exist_ok=True)

        file_path = os.path.join(upload_dir, file[i].filename)

        with open(file_path, 'wb') as buffer:
            buffer.write(content)

        results.append({
            'filename': file[i].filename,
            'content_type': file[i].content_type,
            'size': file_size,
            'message': '파일이 성공적으로 업로드 되었습니다'
        })
    
    return results

@app.get('/search-file/') # 확장자 비교하여 파일 검색
async def search_file(ext:str=""):
    folder = "uploads"
    file_list = []
    for file in os.listdir(folder):
        if file.endswith(ext):
            file_list.append(file)
    
    return file_list

@app.get("/download-file/") # 파일 다운로드
async def download_file(file_name: List[str] = Query(...)):
    folder = "uploads"
    zip_path = "downloads.zip"

    with zipfile.ZipFile(zip_path, "w") as zipf: # zip파일로 다운
        for file in file_name:
            file_path = os.path.join(folder, file)
            if os.path.exists(file_path):
                zipf.write(file_path, arcname=file)
            else:
                raise HTTPException(status_code=404, detail=f"{file} 파일이 존재하지 않습니다.")

    return FileResponse(zip_path, media_type="application/zip", filename="downloads.zip")

@app.delete("/delete-file/") # 파일 삭제
async def delete_file(file_name:List[str]=Query(...)):
    folder = "uploads"
    for file in file_name:
        file_path = os.path.join(folder, file)
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            raise HTTPException(status_code=404, detail="삭제할 파일이 존재하지 않습니다")
        
    return {"message" : "성공적으로 삭제되었습니다."}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)