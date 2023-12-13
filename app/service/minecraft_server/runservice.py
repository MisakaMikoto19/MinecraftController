import subprocess

def RunService(params):
    # minecraft服务器套件路径
    path = params.get("path", "")
    core_name = params.get("core_name", "")
    # minecraft启动命令
    command = f"java -jar {path}/{core_name} -nogui"
    start_minecraft_server(command=command, path=path)
    return command
    
def start_minecraft_server(command, path):
    print("启动Minecraft服务器...")
    subprocess.Popen(command, shell=True, cwd=path)

def stop_minecraft_server(command):
    print("停止Minecraft服务器...")
    subprocess.run(["tmux", "send-keys", "-t", "minecraft_server_session_name", "stop", "C-m"], cwd=command)