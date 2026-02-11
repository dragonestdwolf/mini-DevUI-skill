---
description: 全流程：Figma -> Template -> Spec -> Render -> Design Review
---

# Component Generation and Review Workflow (组件生成与审查工作流)

## 前置条件 (Prerequisites)
- 用户提供 `ComponentName` (E.g., `Button`)
- 用户提供 `FigmaNodeId` (E.g., `123:456`)

## Step 1: 生成 HTML 模版 (Template Generation)
1.  **读取规则**: `.agent/rules/template_maker.md`
2.  **执行角色**: Template Architect
3.  **输入**: `FigmaNodeId`, `ComponentName`
4.  **动作**: 使用 `figma-dev-mode-mcp-server` 获取设计数据，并生成模版文件。
5.  **产出**: `spec/4.template/[ComponentName]-tem.html`

## Step 2: 生成 Spec 文档 (Spec Generation)
1.  **读取规则**: `.agent/rules/spec_maker.md`
2.  **执行角色**: Spec Architect
3.  **输入**: `ComponentName`
4.  **动作**: 定义组件的交互规范（Interaction Spec）和模版契约，关注视觉呈现而非业务逻辑。
5.  **产出**: `spec/3.component/[ComponentName].md`

## Step 3: 组件渲染验证 (Component Rendering)
1.  **读取规则**: `.agent/rules/componentrender.md`
2.  **执行角色**: Angular + DevUI Component Validation Expert
3.  **输入**: `ComponentName`
4.  **动作**: 生成测试 HTML 文件，包含多种状态和边界情况。
5.  **产出**: 
    - `HistoryRender/component/[ComponentName]/v[n].html`
    - 更新 `HistoryRender/component/componentlog.md`

## Step 4: 设计审查 (Design Review)
1.  **读取规则**: `.agent/rules/design_review.md`
2.  **执行角色**: Design Reviewer
3.  **输入**: 
    - `Target HTML File`: 上一步生成的 `v[n].html`
    - `Figma Node ID`: 初始提供的 `FigmaNodeId`
4.  **动作**: 调用 `mcp_figma_get_design_context` 获取真值，对比 HTML 实现，输出差异报告。
5.  **产出**: `HistoryRender/component/[ComponentName]/v[n]+list.md`
