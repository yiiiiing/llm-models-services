# LLM microservice

## Create env
```bash
python3 -m venv llm-service
source llm-service/bin/activate
pip install -r requirements.txt
```


## Run locally

```bash
python ./src/main.py
```

## Run with docker
- Create image
```bash
docker build -t llm-models-service .
```
- Run
```bash
docker run -p 3001:8000  llm-models-service
```
Access by http://localhost:3001/confevent

- Save docker image
```bash
docker save -o llm-models-service.tar llm-models-service
```

## API

### 生成表白场景的一段描述
- POST /confevent
```json
{
    "agent" : 
        {
            "nickname": "就这样吧",
            "gender": "男",
            "age": 30,
            "vocation": "老师",
            "interest": ["游戏", "历史", "哲学"],
            "personality": ["学渣", "直爽"]
        },
    "relation": "同学"
}
```
- Response
```json
{
  "description": "表白场景的描述",
  "success": 1
}
```

### 在表白游戏中，生成AI的回复，得分和当前得分以及是否游戏结束
- POST /conf
```json
{
    "conf_event":
        {
            "agent" : 
            {
                "nickname": "就这样吧",
                "gender": "男",
                "age": 30,
                "vocation": "老师",
                "interest": ["游戏", "历史", "哲学"],
                "personality": ["学渣", "直爽"]
            },
            "current_grade": 50,
            "description": "你们是同学，有一天下午在图书馆你想向对方表白，你知道他喜欢哲学，所以你准备在图书馆找一本关于哲学的书，在书中夹上你想对他说的话。"
        },
    "conversation":
        [
            {
                "sender": "user", 
                "text": "我喜欢你"
            }, 
            {
                "sender": "ai", 
                "text": "（有些惊讶）我还没想好呢"
            }, 
            {
                "sender": "user", 
                "text": "我真的喜欢你"
            }
        ]
}
```
- Response
  
  `grade`为得分的增减数值
  `value`为当前得分
  初始分值为50分，当前得分为0或100，游戏结束，得分为0，表白失败，得分为100则表白成功
```json
{
  "reponse": "（有些不好意思）谢谢你的喜欢，但是我现在还没有这方面的想法。",
  "grade": -5,
  "value": 50,
  "end": false,
  "success": 1
}
```

