#!/usr/bin/env python3
import http.server
import socketserver
import os
import webbrowser
import threading
import time

PORT = 8000

# 获取当前脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))

# 更改工作目录到脚本所在目录
os.chdir(script_dir)

Handler = http.server.SimpleHTTPRequestHandler

# 使用with语句确保服务器在结束时关闭
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"服务器启动在 http://localhost:{PORT}")
    print(f"编辑器地址: http://localhost:{PORT}/code-editor.html")
    print("按 Ctrl+C 关闭服务器")
    
    # 在新线程中打开浏览器
    def open_browser():
        time.sleep(1)  # 等待服务器启动
        webbrowser.open(f"http://localhost:{PORT}/code-editor.html")
    
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    try:
        # 运行服务器
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器关闭")