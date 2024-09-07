from schemas import Agent, Confession, Message
from inference import infer, get_prompt_for_game_generation, get_prompt_for_game_response, get_prompt_for_chat_suggestion
from typing import List, Dict
import re


def generate_confession_event(agent: Agent, relation: str):
    content = f"""
    年龄：{agent.age}
    性别：{agent.gender}
    职业：{agent.vocation}
    兴趣爱好：{agent.interest}
    性格：{agent.personality}
    关系：{relation}
    """
    messages = [{"role": "user", "content": content}]
    messages.insert(0, {"role": "system", "content": get_prompt_for_game_generation()})
    results = infer(messages)

    return results
    

def generate_respose_in_confession(confession: Confession, conversation: List[Message]):
    messages = [{"role": "user" if message.sender == "user" else "assistant", 
                "content": message.text} for message in conversation]
    
    messages.insert(0, {"role": "system", "content": get_prompt_for_game_response(confession.agent, confession.description)})
    results = infer(messages)
    text = results.split('\n')[0]
    grade = int(re.findall(r'[+-]?\d', results)[-1])
    conf_value = confession.current_grade + grade
    game_end = conf_value == 0 or conf_value == 100
    return text, grade, conf_value, game_end


def generate_respose_in_chat(agent_ques: Agent, agent_ans: Agent, history_messages: str):
    text = "test: generate response in chatting"
    return text
