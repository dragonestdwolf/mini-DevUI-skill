# Skill: Tabs (页签)

[Metadata]
- **Component Name**: Tabs
- **Figma Node**: 98-263
- **DevUI Component**: `d-tabs`
- **Version**: v1.0

## Property Skill
定义组件的 API 接口，确保与 DevUI 标准对齐。

| Prop Name | Type | Description | Default |
| :--- | :--- | :--- | :--- |
| `activeTab` | `string \| number` | 当前激活的 Tab ID | - |
| `data` | `Array<{ id: string\|number, title: string, disabled?: boolean }>` | 页签数据源 | `[]` |
| `type` | `'pills' \| 'tabs' \| 'wrapped'` | 页签样式类型：胶囊(Pills)/标准(Tabs)/包裹(Wrapped) | `'pills'` |
| `onChange` | `(id: string \| number) => void` | 切换页签时的回调 | - |

## Visual Skill
定义视觉还原的严格规范，强制使用 Token 和 Flex 布局。

### 1. Layout Logic (布局逻辑)
- **Container (`.devui-tabs`)**:
    - `display: flex`
    - `align-items: center`
    - `gap: 4px` (Token: 这里的间距根据具体类型会有微调，下划线型（Pills） 为24px，包裹型（Wrapped）为0px)
    - `border-bottom`: Wrapped 类型通常需要底部边框。

- **Tab Item (`.devui-tab-item`)**:
    - `display: flex`
    - `align-items: center`
    - `justify-content: center`
    - `padding`: 必须使用 Token `var(--devui-padding-base)` 或具体像素值 (e.g. `8px 16px`)。
    - `cursor: pointer`

### 2. Styling Rules (样式映射)

#### Type: Pills (胶囊型 - Figma Definition)
*Note: Figma 中名为 Pills，但视觉表现为文字下划线样式 (Line Style).*

| Component Part | CSS Property | Token / Value | Fallback (Hex) |
| :--- | :--- | :--- | :--- |
| **Container** | `border-bottom` | `none` (Figma: 无底边线) | - |
| **Item (Normal)** | `color` | `var(--devui-text-weak)` | `#575D6C` |
| **Item (Active)** | `color` | `var(--devui-text)` | `#252B3A` |
| **Item (Active)** | `border-bottom` | `2px solid var(--devui-text)` (高对比黑条) | `#252B3A` |
| **Padding** | `padding` | `var(--devui-padding-base)` (e.g. 8px 0px) | - |

#### Type: Tabs (标准型)
*Note: 视觉上与 Pills 类似，但增加了容器底部的灰色分割线。*

| Component Part | CSS Property | Token / Value | Fallback (Hex) |
| :--- | :--- | :--- | :--- |
| **Container** | `border-bottom` | `1px solid var(--devui-line)` (灰色底线) | `#DFE1E6` |
| **Item (Normal)** | `color` | `var(--devui-text-weak)` | `#575D6C` |
| **Item (Active)** | `color` | `var(--devui-text)` | `#252B3A` |
| **Item (Active)** | `border-bottom` | `2px solid var(--devui-text)` (高对比黑条) | `#252B3A` |
| **Padding** | `padding` | `var(--devui-padding-base)` | - |

#### Type: Wrapped (包裹型 - Figma Definition)
*Note: Figma 中名为 Wrapped，但视觉表现为灰色块状样式 (Solid/Gray Style).*

| Component Part | CSS Property | Token / Value | Fallback (Hex) |
| :--- | :--- | :--- | :--- |
| **Container** | `background-color` | `transparent` | - |
| **Item (Normal)** | `background-color` | `transparent` | - |
| **Item (Normal)** | `color` | `var(--devui-text-weak)` | `#575D6C` |
| **Item (Active)** | `background-color` | `var(--devui-global-bg)` (浅灰背景) | `#F5F5F5` |
| **Item (Active)** | `color` | `var(--devui-text)` | `#252B3A` |
| **Radius** | `border-radius` | `var(--devui-radius) var(--devui-radius) 0 0` (通常上方圆角) | `4px` |

> [!CAUTION]
> **Naming vs Visual**: Figma 中的命名与 DevUI 标准组件库有差异。请严格遵循上述 **Preview 视觉特征** 而非仅看名字。
> - `type="pills"` -> Output **Underline** style.
> - `type="wrapped"` -> Output **Solid Gray Block** style.

## Anti-Patterns (负面示例)
禁止在生成代码时出现以下模式：

1.  **❌ 禁止硬编码颜色**
    ```css
    /* Bad */
    background-color: #5E7CE0;
    /* Good */
    background-color: var(--devui-brand);
    ```

2.  **❌ 禁止使用 Float 布局**
    - 必须使用 `display: flex`。

3.  **❌ 禁止混用 Type 样式**
    - Pills 类型不应有边框，Wrapped 类型不应全是圆角。

## Audit Checklist (自检清单)
- [ ] 属性名是否包含 `activeTab`, `type`？
- [ ] 颜色引用是否全部为 `var(--devui-*)`？
- [ ] Pills 类型激活态是否为 Brand 背景？
- [ ] Wrapped 类型激活态是否与内容区连通（底边框处理）？
- [ ] 布局是否使用了 Flex？
