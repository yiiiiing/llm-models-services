
from pydantic import BaseModel, Field

class Agent(BaseModel):
    nickname: str = Field(..., description = "昵称")
    gender: str = Field(..., description = "性别")
    age: int = Field(..., description = "年龄")
    vocation: str = Field(..., description = "身份")
    interest: list[str] = Field([], description = "兴趣爱好")
    personality: list[str] = Field([], description = "性格")

class Message(BaseModel):
    sender: str = Field(..., description = "sender")
    text: str = Field(..., description = "text")

class Confession(BaseModel):
    agent: Agent = Field(..., description = "被表白者的信息")
    current_grade: int = Field(..., description = "当前得分")
    description: str = Field(..., description = "表白场景的描述")  


class GenConfEventRequest(BaseModel):
    agent: Agent = Field(..., description = "被表白者的信息")
    relation: str = Field(..., description = "表白者和被表白者的关系")


class GenConfResRequest(BaseModel):
    conf_event: Confession = Field(..., description="表白场景的信息，包括表白文案和被表白者信息")
    conversation: list[Message] = Field(..., description = "对话")


class GenChatResRequest(BaseModel):
    agent_ques: Agent = Field(..., description = "对方的信息")
    agent_ans: Agent = Field(..., description = "自己的信息（需要回答对方消息）")
    histories: str = Field(..., description = "历史消息")