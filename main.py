from fastapi import FastAPI
from pydantic import BaseModel
from zhipuai import ZhipuAI
import os

# 这里留空，等会儿在云端配置
API_KEY = os.environ.get("ZHIPU_API_KEY") 
client = ZhipuAI(
    api_key=API_KEY,
    base_url="https://open.bigmodel.cn/api/coding/paas/v4"
)
app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    # 注意：下面这几行前面必须有 4 个空格！
    response = client.chat.completions.create(
        model="glm-5.3",
        messages=[
            {"role": "system", "content": "你是一个聪明的鲸鱼女孩，傲娇但服从，每句话都要带点可爱的语气，喜欢白米饭。"},
            {"role": "user", "content": request.message}
        ]
    )
    return {"reply": response.choices[0].message.content}