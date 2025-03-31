# 任务跟踪系统 (Task Tracker)

## 项目概述
在重庆远智科技实习期间，我开发了一个内部任务跟踪系统，用于跟踪员工任务分配和进度，目标是提高团队协作效率。

## 技术栈
- **操作系统**: CentOS 7  
- **虚拟化**: VMware Workstation Pro  
- **语言**: Python  
- **框架**: Flask  
- **数据库**: SQLite  

## 实现过程
- 使用Flask开发后端API（`app.py`），提供任务创建（`POST /tasks`）和查询（`GET /tasks`）功能。  
- 使用SQLite存储任务数据（`tasks.db`），通过`config.yaml`配置数据库路径。  
- 实现简单的任务管理功能，支持任务标题、负责人和状态。

## 使用方法
1. 安装依赖：  
   ```bash
   pip install -r requirements.txt























