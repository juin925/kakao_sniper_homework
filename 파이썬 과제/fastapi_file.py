import os
from typing import List
from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.responses import FileResponse, StreamingResponse
import uvicorn

app = FastAPI()

@app.post('/upload-file/')
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

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)