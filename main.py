#helloword fastapi
from fastapi import FastAPI

# 1. Khởi tạo ứng dụng
app = FastAPI()

# 2. Định nghĩa một đường dẫn (route)
@app.get("/")
def read_root():
    return {"message": "Hello World"}

# 3. Thêm một đường dẫn có tham số
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}
