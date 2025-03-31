from flask import Flask, request, jsonify
import sqlite3
import yaml

app = Flask(__name__)

# 加载配置文件
with open("config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)

# 初始化数据库
def init_db():
    conn = sqlite3.connect(config["database"]["path"])
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            assignee TEXT NOT NULL,
            status TEXT DEFAULT 'pending'
        )
    """)
    conn.commit()
    conn.close()

# 创建任务
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    title = data.get('title')
    assignee = data.get('assignee')
    if not title or not assignee:
        return jsonify({"error": "Title and assignee are required"}), 400
    
    conn = sqlite3.connect(config["database"]["path"])
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, assignee) VALUES (?, ?)", (title, assignee))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    
    return jsonify({"message": "Task created", "task": {"id": task_id, "title": title, "assignee": assignee, "status": "pending"}}), 201

# 查询所有任务
@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = sqlite3.connect(config["database"]["path"])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = [{"id": row[0], "title": row[1], "assignee": row[2], "status": row[3]} for row in cursor.fetchall()]
    conn.close()
    return jsonify(tasks), 200

if __name__ == "__main__":
    init_db()
    app.run(host=config["server"]["host"], port=config["server"]["port"])
