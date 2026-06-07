import os

# 配置你的文章目录和博客根目录（根据实际情况修改）
ARTICLES_DIR = "./articles"  # 存放文章的文件夹
OUTPUT_FILE = "./_article_list.html"  # 生成的列表片段，之后复制到你的网页中

# 定义分类映射（根据文件路径或文件名关键词判断）
CATEGORY_MAP = {
    "articles-day": "生活",
    "Essay": "随笔",
    "ESP32": "ESP32入门",
    "PLC": "plc",
    "Analog Devices": "模电",   # 把 Analog Devices 文件夹下的文章归为“模电”
}

# 支持的扩展名
EXTENSIONS = (".html", ".htm", ".md")

# 扫描文章
articles = []
for root, dirs, files in os.walk(ARTICLES_DIR):
    for file in files:
        if file.endswith(EXTENSIONS):
            # 获取相对路径
            rel_path = os.path.relpath(os.path.join(root, file), ARTICLES_DIR)
            # 生成动态加载链接（关键修改）
            url_path = f"wenzhangmulu.html?p=/articles/{rel_path.replace('\\', '/')}"
            
            # 提取标题（去掉扩展名）
            title = os.path.splitext(file)[0]
            
            # 判断分类（根据路径中的关键词）
            category = "其它"  # 默认分类
            for key, cat in CATEGORY_MAP.items():
                if key in rel_path:
                    category = cat
                    break
            
            articles.append({
                "url": url_path,
                "title": title,
                "category": category,
                "file": file
            })

# 按文件名排序
articles.sort(key=lambda x: x["file"])

# 生成 HTML
html_items = []
for art in articles:
    html_items.append(f'              <li data-category="{art["category"]}"><a href="{art["url"]}">{art["title"]}</a></li>')

article_list_html = "\n".join(html_items)

# 输出到文件（或直接打印）
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(article_list_html)

print(f"已生成 {len(articles)} 篇文章的列表，保存到 {OUTPUT_FILE}")
print(article_list_html)  # 直接打印出来复制