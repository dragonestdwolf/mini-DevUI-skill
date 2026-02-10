# Skill: Tag (标签)

[Metadata]
- **Component Name**: Tag
- **Figma Node**: 39:96
- **DevUI Component**: `d-tag`
- **Version**: v1.0

## Property Skill
定义组件的 API 接口，确保与 DevUI 标准对齐。

| Prop Name | Type | Description | Default |
| :--- | :--- | :--- | :--- |
| `type` | `'general' \| 'auxiliary' \| 'solid' \| 'outline'` | 标签类型：常规/辅助/纯色/线性 | `'general'` |
| `color` | `'blue-w98' \| 'green-w98' \| 'orange-w98' \| 'red-w98' ...` | 颜色主题 (对应 Token 变量名后缀) | - |
| `size` | `'md' \| 'lg'` | 尺寸大小 | `'md'` |
| `deletable` | `boolean` | 是否可删除 (显示关闭图标) | `false` |
| `onDelete` | `() => void` | 删除回调 | - |

## Visual Skill
定义视觉还原的严格规范，强制使用 Token 和 Flex 布局。

### 1. Layout Logic (布局逻辑)
- **Container (`.devui-tag`)**:
    - `display: inline-flex`
    - `align-items: center`
    - `justify-content: center`
    - `border-radius`: `4px` (Unified)
    - `white-space`: `nowrap`
    - `gap`: `4px` (Icon 与 Text 间距)
    - `padding`: `0 8px` (Unified for all types)
    - `cursor`: `default` (Deletable: `pointer` on close icon)

- **Size Rules**:
    - **md** (Default): Height `20px`, Font Size `12px`, Line Height `20px`.
    - **lg**: Height `24px`, Font Size `14px`, Line Height `22px`.

### 2. Styling Rules (样式映射)

#### Type: General (常规标签 - Default)
用于中性展示，通常是灰底黑字。

| Component Part | CSS Property | Token / Value | Fallback (Hex) |
| :--- | :--- | :--- | :--- |
| **Container** | `background-color` | `var(--devui-list-item-hover-bg)` (Figma match: #F2F5FC) | `#F2F5FC` |
| **Container** | `border` | `none` | - |
| **Text** | `color` | `var(--devui-text)` | `#252B3A` |
| **Text** | `font-weight` | `400` (Regular) | - |

#### Type: Auxiliary (辅助标签)
用于表达语义状态（成功、警告等），浅色背景+深色文字。

| Component Part | CSS Property | Token / Value | Fallback (Hex) |
| :--- | :--- | :--- | :--- |
| **Container** | `background-color` | `var(--devui-[state]-bg)` (e.g., success-bg #EDFFF9) | `#EDFFF9` |
| **Container** | `border` | `none` | - |
| **Text** | `color` | `var(--devui-[state])` (e.g., success #50D4AB) | `#50D4AB` |
| **Text** | `font-weight` | `400` (Regular) | - |

#### Type: Solid (纯色背景标签)
用于强强调，深色背景+白色文字。

| Component Part | CSS Property | Token / Value | Fallback (Hex) |
| :--- | :--- | :--- | :--- |
| **Container** | `background-color` | `var(--devui-[state])` (e.g., success #50D4AB) | `#50D4AB` |
| **Container** | `border` | `none` | - |
| **Text** | `color` | `var(--devui-light-text)` (White) | `#FFFFFF` |
| **Text** | `font-weight` | `500` (Medium) | - |

#### Type: Outline (线性标签)
用于弱强调或描边风格。

| Component Part | CSS Property | Token / Value | Fallback (Hex) |
| :--- | :--- | :--- | :--- |
| **Container** | `background-color` | `var(--devui-base-bg)` (White) | `#FFFFFF` |
| **Container** | `border` | `1px solid var(--devui-[state])` | `#50D4AB` |
| **Text** | `color` | `var(--devui-[state])` | `#50D4AB` |
| **Text** | `font-weight` | `400` (Regular) | - |

## Icon Skill (图标规范)
- **Delete Icon**: 使用 `icon/close.svg`。
- **Size**: 12px (md) / 14px (lg) —— 图标尺寸通常跟随文字尺寸或稍小 (Figma source shows 16px wrapper with centered icon, visual weight is key).
- **Color**:
    - Solid: `var(--devui-light-text)`
    - Others: `currentColor` (Inherits text color).

## Anti-Patterns (负面示例)
1.  **❌ 禁止 Solid 类型使用 Regular 字体**
    - Solid 类型必须使用 Medium (500) 字重以保证在深色背景下的易读性。
2.  **❌ 禁止 Outline 类型无边框**
    - Linear/Outline 必须有 `1px solid` 边框。
3.  **❌ 禁止自定义 Height**
    - 严格遵循 `20px` (md) 和 `24px` (lg)。

## Audit Checklist (自检清单)
- [ ] Solid 标签文字是否为白色且加粗 (Medium)？
- [ ] 常规标签背景是否为只读态灰 (`#F2F5FC`)？
- [ ] 线性标签是否有边框？
- [ ] 圆角是否统一为 4px？
