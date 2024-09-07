from schemas import Agent, Confession
from utils import generate_confession_event, generate_respose_in_chat, generate_respose_in_confession
from typing import Dict


def get_character_prompt(character: Dict):
    pass


def init_conf_game(agent: Agent, relation):
    print("---------根据角色信息创建表白场景------------")
    game_description = generate_confession_event(agent, relation)
    return game_description


def confession_game(character: Dict):
    # 生成表白场景
    agent = Agent(**character["agent"])
    game_description = init_conf_game(agent, character["relation"])
    print(game_description)
    print("----------表白游戏--------------")
    conversation = []
    current_grade = 50
    conf_event = {
        "agent": agent,
        "current_grade": current_grade,
        "description": game_description
    }
    conf_event = Confession(**conf_event)
    
    while True:
        message = input("You: ")
        conversation.append({"sender": "user", "text": message})
        result, grade, conf_value, game_end = generate_respose_in_confession(conf_event, conversation)
        
        if game_end:
            print("游戏结束，最终得分：", conf_value)
            break
        
        conf_event.current_grade = conf_value
        conversation.append({"sender": "assistant", "text": result})
        
        if len(conversation) > 5:
            conversation = conversation[-5 : ]
            
        log = f"agent: {result} 得分：{grade}, 当前得分：{conf_event.current_grade }/100"
        print(log)


if __name__ == "__main__":
    character = {
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
    
    confession_game(character)