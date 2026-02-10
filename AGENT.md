# AGENT.md

## 项目简介

这是一个代码学习过程中的可视化/可交互演示动画合集。每个演示都是独立的 HTML 文件，通过动画和交互帮助理解底层原理。项目托管在 Cloudflare Pages 上作为静态站点。

## 技术约定

- 每个演示为独立的 `.html` 文件
- 使用 Tailwind CSS + 原生 JavaScript 实现，不引入框架
- 文件可以放在根目录，也可以按主题使用子目录组织
- 所有页面使用中文

## 导航首页

项目使用 Python 脚本 `generate_index.py` 自动生成 `index.html` 作为导航页。

工作流程：
1. 新增或修改演示文件
2. 运行 `python generate_index.py` 重新生成 `index.html`
3. 提交所有变更（包括生成的 `index.html`）

注意：`index.html` 是自动生成的，不要手动编辑。

## 部署

静态资源托管在 Cloudflare Pages，推送到主分支后自动部署。

## 现有演示

- `inline-hook.html` — Inline Hook 执行流演示，展示 Hook 劫持、代理函数、跳板机制的完整调用链
