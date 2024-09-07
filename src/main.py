from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from utils import generate_confession_event, generate_respose_in_chat, generate_respose_in_confession
from schemas import GenConfEventRequest, GenConfResRequest, GenChatResRequest

app = FastAPI()

# 生成表白场景描述
@app.post("/confevent")
async def confession_event(request: GenConfEventRequest):
    try:
        result = generate_confession_event(request.agent, request.relation)
        success = 1
    except Exception as e:
        result = ""
        success = 0
    
    content = jsonable_encoder({"description": result, "success": success})
    response = JSONResponse(content=content)
    
    return response

# 在表白场景中，生成被表白者的回复
@app.post("/conf")
async def confession_event(request: GenConfResRequest):
    try:
        result, grade, conf_value, game_end = generate_respose_in_confession(request.conf_event, request.conversation)
        success = 1
    except Exception as e:
        result = ""
        success = 0
    
    content = jsonable_encoder({"reponse": result, "grade": grade, "value": conf_value, "end": game_end, "success": success})
    response = JSONResponse(content=content)
    
    return response


# 在对话场景中，生成回复灵感
@app.post("/chat")
async def confession_event(request: GenChatResRequest):
    try:
        result = generate_respose_in_chat(request.agent_ques, request.agent_ans,request.histories)
        success = 1
    except Exception as e:
        result = ""
        success = 0
    
    content = jsonable_encoder({"description": result, "success": success})
    response = JSONResponse(content=content)
    
    return response


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
