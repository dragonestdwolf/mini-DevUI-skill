# AI-MiniDevUI (Agentic UI Engineering)

本项目旨在通过标准化工作流，辅助 AI Agent 生成符合 **DevUI Design System** 规范的高保真设计界面，致力于探究从设计稿到代码的闭环交付。

## 🎯 核心目标 (Goal)
探究如何通过结构化的 **Prompt Engineering** 与 **Figma MCP** 工具链，让 AI Agent 能够精确理解并还原复杂设计系统。不仅实现单体组件的一对一重构，还探寻在宏观复杂工作台上实现真正的 Code-to-Design 还原（Pixel-Perfect）及自动化审美审查。

## 🔄 核心工作流 (Workflow)

整个流程模拟了从设计到代码再到验收的 Agentic 自动化链路，划分为三大核心执行阶段：

1. **结构化定义 (1.make)**:
   - **Spec Maker**: 连接 Figma MCP，获取组件的 Design Tokens、Auto-layout 等属性，将其“编译”为组件级 API 约束与 Markdown 行为文稿 (`spec/3.component/*.md`)。
   - **Template Maker**: 提取组件的视觉表达，输出纯原生的 HTML 封装模版代码 (`spec/4.template/*-tem.html`) 以切断 AI 自由发挥的样式偏移。
2. **沉浸式生成 (2.render)**:
   - **HTML Render**: AI Agent 基于 Spec 约束与 Template 模板字典，结合目标设计稿截图或节点数据，进行组装。通过变量注入等手段，自动化生成高保真组合页面或基准测试页 (`HistoryRender/page/*.html`)。
3. **视觉设计审查 (3.review)**:
   - **Design Reviewer**: 运行审查规则协议，对生成的独立组件 DOM 或复合排版直接与 Figma 原真值进行比对差异，输出审查修复分析。

## 📂 目录结构体系 (Architecture)

### 🤖 核心驱动 (`.agent/`)
Agent 的核心大脑与 Prompt 仓库。
- `rules/` 体系：
  - `1.make/`: 包含 `spec_maker.md`, `template_maker.md`，主导核心规格提炼与结构固化。
  - `2.render/`: 包含 `htmlrender.md`，主导复合页面高保真渲染生成逻辑。
  - `3.review/`: 包含 `design_review.md`，执行视觉与间距层面的审计。
  - `workspace-global.md`: 工作区全局基础约定及 AI 基础响应控制。

### 📚 组件知识库 (`spec/`)
脱胎于原 `skill`，聚合了所有界面的原子与区块定义。
- `0.role/`: 图标角色等特定规范定义。
- `1.layout/`: 复杂应用级页面骨架与布局规范。
- `2.theme/`: 统一的主题色彩与 Token 字典字典。
- `3.component/`: 组件使用标准、交互状态及结构说明文档 (Markdown)。
- `4.template/`: 标准组件的模板基座 (HTML/CSS)，杜绝外部污染。
- `5.block/`: 复合业务级通用区块标准与模版。

### 📊 仿真及测试 (`HistoryRender/`)
渲染的产物沙盒。
- `page/`: 归档包含了所有 AI 在不同迭代轮次生成的 `v*.html` 测试页以及对应的 `Pagelog.md` 世代日志。也存放业务级标杆界面 (如 `bench-card.html`, `bench-form.html` 等 Benchmark)。

### 🖼️ 静态资产 (`icon/` & `icon-feed-mcp/`)
存放包括原生多彩图形、单色线性切图、3D装饰素材和首字母头像在内的标准物料库。

---
*Project systematically refactored for AI-Assisted Front-End Component Spec & Render Verification.*