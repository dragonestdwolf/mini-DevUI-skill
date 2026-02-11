# Skill: Form (表单)

[Metadata]
- **Component Name**: Form
- **Figma Node**: 379:1093, 345:1340
- **DevUI Component**: `d-form`, `d-form-item`, `d-form-label`, `d-form-control`
- **Version**: v1.0

## Layout Skill
定义表单的整体布局结构，重点在于 Label 与 Control 的相对位置。

### 1. Structure Logic (结构逻辑)
表单由多个 `FormItem` 组成，每个 `FormItem` 包含 `Label` (标签) 和 `Control` (控件区域)。

- **Form Container (`.devui-form`)**:
    - `display: flex`
    - `flex-direction`: `column` (通常表单项是垂直堆叠的)
    - `gap`: `16px` (FormItem 之间的垂直间距)

- **Form Item (`.devui-form-item`)**:
    - **Horizontal Layout (水平排列)**:
        - `display: flex`
        - `align-items: flex-start` (Label 与 Control 顶部对齐)
        - `gap`: `8px` 或 `16px` (Label 与 Control 的间距)
    - **Vertical Layout (垂直排列)**:
        - `display: flex`
        - `flex-direction`: `column`
        - `gap`: `4px` (Label 与 Control 的间距)

### 2. Form Control Integration (控件集成)
`Form Control` 区域是一个容器，内部可以承载多种输入组件。
- **Core Rule**: 必须使用独立的 Input/Select/Checkbox Skill 组件，**禁止**在 Form Skill 中重新定义输入框样式。
- **Slot Usage**:
    - `<d-input>`
    - `<d-select>`
    - `<d-textarea>`
    - `<d-checkbox-group>`
    - `<d-radio-group>`

## Visual Skill
定义 Label 和辅助信息的样式。

### 1. Label Styling (标签样式)
| Component Part | CSS Property | Token / Value | Fallback (Hex) |
| :--- | :--- | :--- | :--- |
| **Label Text** | `font-size` | `14px` | - |
| **Label Text** | `color` | `var(--devui-text)` | `#252B3A` |
| **Label Text** | `line-height` | `32px` (Vertical-center with Input md) | `32px` |
| **Required (*)**| `color` | `var(--devui-danger)` | `#F66F6A` |
| **Required (*)**| `margin-right` | `4px` | - |
| **Optional Info**| `color` | `var(--devui-aide-text)` | `#8A8E99` |

### 2. Validation Message (校验信息)
当表单校验失败时显示的错误提示。
- **Container**: 位于 Control 下方。
- **Text Style**:
    - `font-size`: `12px`
    - `line-height`: `1.5`
    - `color`: `var(--devui-danger)` (#F66F6A)
    - `margin-top`: `4px`

## Anti-Patterns (负面示例)
1.  **❌ 禁止在 Form 中硬编码 Input 样式**
    - 表单只负责布局（Layout），控件样式（Visual）由 Input Skill 负责。
2.  **❌ 禁止非 Token 的 Label 颜色**
    - Label 颜色必须严格跟随 `devui-text`。
3.  **❌ 禁止混用布局模式**
    - 同一个表单内，建议统一使用 Horizontal 或 Vertical 布局，避免视觉混乱。

## Audit Checklist (自检清单)
- [ ] Label 是否垂直居中对齐 Input (Horizontal Mode)？
- [ ] 必填星号 (*) 是否为红色？
- [ ] FormItem 之间是否有统一间距 (16px)？
- [ ] 内部控件是否调用了标准的 Input/Select 组件？
