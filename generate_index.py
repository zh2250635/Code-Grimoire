"""
扫描项目中的演示 HTML 文件，自动生成 index.html 导航页。

用法: python generate_index.py
"""

import os
import re
from pathlib import Path

IGNORE = {"index.html"}


def extract_title(filepath: Path) -> str:
    """从 HTML 文件的 <title> 标签提取标题，提取不到则用文件名。"""
    try:
        text = filepath.read_text(encoding="utf-8")
        m = re.search(r"<title>(.*?)</title>", text, re.IGNORECASE | re.DOTALL)
        if m:
            return m.group(1).strip()
    except Exception:
        pass
    return filepath.stem


def collect_demos(root: Path) -> list[dict]:
    """递归收集所有 .html 演示文件，返回 [{path, title}]。"""
    demos = []
    for html_file in sorted(root.rglob("*.html")):
        rel = html_file.relative_to(root).as_posix()
        if rel in IGNORE or html_file.name.startswith("."):
            continue
        demos.append({"path": rel, "title": extract_title(html_file)})
    return demos


def render(demos: list[dict]) -> str:
    """生成 index.html 内容。"""
    items = ""
    for d in demos:
        items += (
            f'        <a href="{d["path"]}" class="block px-5 py-4 rounded-lg'
            f" bg-gray-800 hover:bg-gray-700 transition-colors"
            f' border border-gray-700 hover:border-gray-500">\n'
            f'          <span class="text-gray-100">{d["title"]}</span>\n'
            f'          <span class="block mt-1 text-sm text-gray-500">{d["path"]}</span>\n'
            f"        </a>\n"
        )

    return f"""\
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>演示动画合集</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-900 text-gray-100 min-h-screen flex items-start justify-center p-8">
  <main class="w-full max-w-2xl">
    <h1 class="text-3xl font-bold mb-2">演示动画合集</h1>
    <p class="text-gray-400 mb-8">共 {len(demos)} 个演示</p>
    <div class="flex flex-col gap-3">
{items}\
    </div>
  </main>
</body>
</html>
"""


def main():
    root = Path(__file__).resolve().parent
    demos = collect_demos(root)
    out = root / "index.html"
    out.write_text(render(demos), encoding="utf-8")
    print(f"已生成 {out.name}，包含 {len(demos)} 个演示。")


if __name__ == "__main__":
    main()
