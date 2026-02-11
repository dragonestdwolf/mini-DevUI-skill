# AI-MiniDevUI (AI 驱动的 DevUI 设计系统交付)

本项目旨在探索 **AI 驱动的设计系统交付（AI-Driven Design Delivery）** 新范式。通过标准化工作流，辅助 AI 生成符合 **DevUI Design System** 规范的高保真界面。

## 🎯 核心目标 (Goal)
探究如何通过结构化的 **Prompt Engineering** 与 **Figma MCP** 工具链，让 AI Agent 能够精确理解并还原设计系统，实现从设计稿到代码的闭环交付与自动化审查。

## 🔄 核心工作流 (Workflow)

整个流程模拟了从设计到代码再到验收的自动化链路：

1.  **输入 (Input)**:
    -   连接 **Figma Dev Mode** (通过 MCP Server)。
    -   获取组件的 Design Tokens、Auto-layout 属性与 Variants 定义。

2.  **定义 (Definition)**:
    -   **Template Maker**: 将 Figma 视觉样式“编译”为锁定的 HTML/CSS 模版 (`skill/4.template/*-tem.html`)。
    -   **Skill Maker**: 提取组件的交互逻辑与 API 定义，生成 Markdown 文档 (`skill/3.component/*.md`)。

3.  **生成 (Generation)**:
    -   AI Agent 基于 Skill 文档理解组件用法。
    -   AI Agent 调用 Template 模版注入动态数据，生成最终页面。

4.  **渲染与审查 (Render & Review)**:
    -   生成的 HTML 页面保存至 `HistoryRender/` 目录进行渲染测试。
    -   运行 **Design Review** 规则，自动对比 Figma 真值与 HTML 实现，输出差异报告 (`*+list.md`)，指导样式修正。

## 📂 目录结构 (Directory Structure)

-   **`.agent/`**: Agent 规则库。
    -   `rules/`: 包含 `skillMakerv2.md`, `template_maker.md`, `componentrender.md`, `design_review.md` 等核心 Prompt。
    -   `workflows/`: 自动化工作流定义 (e.g. Component Generation Workflow)。
-   **`skill/`**: 组件知识库。
    -   `3.component/`: 组件逻辑定义 (Markdown)。
    -   `4.template/`: 组件视觉模版 (HTML)。
-   **`HistoryRender/`**: 渲染产物归档。
    -   包含生成的 `v*.html` 测试页。
    -   包含 `*+list.md` 设计审查报告。

## ✨ 特性 (Features)

-   **Pixel-Perfect**: 通过 Template 锁定 CSS，确保 1:1 还原 Figma。
-   **Logic/View Separation**: 逻辑与视图分离，AI 专注于业务逻辑，模版负责视觉呈现。
-   **Automated Review**: 内置设计审查 Agent，自动发现间距、颜色、排版差异。

---
*Project initialized for AI-Assisted DevUI Research*
