from volcenginesdkarkruntime import Ark
from typing import List, Dict
from schemas import Agent

# CLIENT = Ark(api_key=os.environ.get("ARK_API_KEY"))
CLIENT = Ark(api_key = "4cdbe67c-0558-4902-9b4a-1306e504cba4")
MODEL_LITE_4K = "ep-20240907185934-l556z"
MODEL_PRO_4K = "ep-20240521201123-dscmt"
MODEL_LITE_32K = "ep-20240908055735-dkv94"
MODEL_PRO_32K = "ep-20240908055911-k9dkc"


def format_list(ls: List):
    return ",".format(ls)


def get_agent_prompt(agent: Agent):
    prompt = f"""
    你的性别是{agent.gender}，你今年{agent.age}岁了，你的工作是{agent.vocation}，你喜欢
    {format_list(agent.interest)}, 你的性格特点是{format_list(agent.personality)}
    """
    return prompt


def get_prompt_for_game_generation() -> str:
    prompt = """
    ### Goal
    你很擅长对别人表白,根据user提供的被表白者信息, 分析被表白者的喜好, 生成一段表白场景的描述, 包括表白的背景，地点和时间
    
    ### Rule
    user提供的表白对象的信息包括: 年龄, 性别,兴趣爱好, 职业, 性格特点, user和表白对象的关系.
    根据user提供的表白对象的信息, 为user生成合理的表白场景, 表白场景描述尽量简洁，且不包括你想说的话
    
    ### output format
    你们是{二人关系的描述}，有一天{时间}在{表白地点}你想向对方表白{表白背景}。
    """
    return prompt


def get_prompt_for_game_response(agent: Agent, game_description: str) -> str:
    prompt = f"""
    ### Goal
    user正在向你表白, 但是你很难接受别人的表白，请合理根据表白场景的描述, 你的个人信息, user的回复, 生成回复
    
    ### 表白场景
    {game_description}
    
    ### 个人信息
    {get_agent_prompt(agent)}
    
    ### Rule
    * 根据表白场景, 个人信息, 和用户的消息, 尽量简单生成你的回复, 回复包括你的心情, 你的消息, 对user的心动等级
    * 请从-10到10分为5个心动等级:
    -10为特别不心动
    -5为不心动
    0为正常
    +5为心动
    +10为非常心动

    ### Output format
    (你的心情)你的消息
    得分:(+-心动等级)
    """
    return prompt


def get_prompt_for_chat_suggestion():
    prompt = ""
    return prompt


def infer_test():
    print("----- multiple rounds request -----")
    completion = CLIENT.chat.completions.create(
        model=MODEL_LITE_4K,
        messages = [
            {"role": "system", "content": "你是豆包，是由字节跳动开发的 AI 人工智能助手"},
            {"role": "user", "content": "花椰菜是什么？"},
            {"role": "assistant", "content": "花椰菜又称菜花、花菜，是一种常见的蔬菜。"},
            {"role": "user", "content": "再详细点"},
        ],
    )
    print(completion.choices[0].message.content)


def infer(messages) -> str:

    completion = CLIENT.chat.completions.create(model = MODEL_PRO_32K, messages = messages)
    
    return completion.choices[0].message.content


if __name__ == "__main__":
    infer_test()


