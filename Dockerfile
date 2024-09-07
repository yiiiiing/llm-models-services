# 使用官方 Python 基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 安装 FFmpeg
# RUN apt-get update \
#     && apt-get install -y ffmpeg \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*

# 复制依赖文件并安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制 src 文件夹的内容到容器的 /app 目录
COPY ./src /app

# 指定要运行的命令
CMD ["python", "./main.py", "--host", "0.0.0.0", "--port", "80"]
