# Skill: Checkbox (复选框)

[Metadata]
- **Component Name**: Checkbox
- **Figma Node**: 180:337
- **DevUI Component**: `d-checkbox`
- **Version**: v1.0

## Property Skill
定义组件的 API 接口，确保与 DevUI 标准对齐。

| Prop Name | Type | Description | Default |
| :--- | :--- | :--- | :--- |
| `checked` | `boolean` | 是否选中 | `false` |
| `halfChecked` | `boolean` | 是否半选（不确定状态） | `false` |
| `disabled` | `boolean` | 是否禁用 | `false` |
| `label` | `ReactNode` | 显示标签 | - |
| `onChange` | `(checked: boolean) => void` | 状态改变回调 | - |

## Visual Skill
定义视觉还原的严格规范，强制使用 Token 和 Flex 布局。

### 1. Layout Logic (布局逻辑)
- **Container (`.devui-checkbox-wrapper`)**:
    - `display: inline-flex`
    - `align-items: center`
    - `cursor`: `pointer` (Disabled: `not-allowed`)
    - `gap`: `8px` (Checkbox 与 Label 间距)

- **Checkbox Box (`.devui-checkbox`)**:
    - `width`: `16px`
    - `height`: `16px`
    - `border-radius`: `2px` (Fixed)
    - `display`: `flex`
    - `justify-content`: `center`
    - `align-items`: `center`
    - `transition`: `all .2s`
    - `position`: `relative`

### 2. Styling Rules (样式映射)

#### Base Style (Unchecked - Default)
| Component Part | CSS Property | Token / Value | Fallback (Hex) |
| :--- | :--- | :--- | :--- |
| **Box** | `background-color` | `var(--devui-base-bg)` | `#FFFFFF` |
| **Box** | `border` | `1px solid var(--devui-form-control-line)` | `#ADB0B8` |

#### Comparison: States (状态交互)

| State | CSS Property | Token / Value | Fallback (Hex) |
| :--- | :--- | :--- | :--- |
| **Hover** | `border-color` | `var(--devui-brand)` (Figma: #5E7CE0) | `#5E7CE0` |
| **Hover (Ripple)** | `box-shadow` | `0 0 0 8px var(--devui-form-control-line-rippling)` | `rgba(94,124,224,0.08)` |
| **Checked/Half** | `background-color` | `var(--devui-brand)` (Figma: #5E7CE0) | `#5E7CE0` |
| **Checked/Half** | `border-color` | `var(--devui-brand)` | `#5E7CE0` |
| **Checked Icon** | `color` | `var(--devui-light-text)` (White) | `#FFFFFF` |
| **HalfCheck Marker**| `background-color` | `var(--devui-light-text)` | `#FFFFFF` |
| **Disabled (Unchecked)**| `background-color` | `var(--devui-disabled-bg)` (Figma: #F3F3F3) | `#F3F3F3` |
| **Disabled (Unchecked)**| `border-color` | `var(--devui-disabled-line)` (Figma: #DFE1E6) | `#DFE1E6` |
| **Disabled (Checked)** | `background-color` | `var(--devui-disabled-bg-active)` (Figma: #BECCFA) | `#BECCFA` |
| **Disabled (Checked)** | `border-color` | `var(--devui-disabled-bg-active)` | `#BECCFA` |

#### Inner Content (内部图标/标记)
- **Checked**: 显示对勾图标 (SVG Path)。
    - Path Color: `var(--devui-light-text)`
- **HalfChecked**: 显示矩形标记。
    - Size: `6px x 6px`? (Figma shows `size-[6px]` rounded-[1px])
    - Color: `var(--devui-light-text)`
    - Position: Center.

#### Label Style
| Part | CSS Property | Token / Value | Fallback (Hex) |
| :--- | :--- | :--- | :--- |
| **Text** | `font-size` | `14px` | - |
| **Text** | `color` | `var(--devui-text)` | `#252B3A` |
| **Text (Disabled)**| `color` | `var(--devui-disabled-text)` | `#ADB0B8` |

## Anti-Patterns (负面示例)
1.  **❌ 禁止 Input[type="checkbox"] 裸用**
    - 必须隐藏原生 Input，使用 `div/span` 模拟样式的 Checkbox，以支持自定义样式和动画。
2.  **❌ 禁止硬编码 Gap**
    - 使用 `gap: 8px` 而不是 `margin-right`。
3.  **❌ 禁止 HalfChecked 与 Checked 混淆**
    - HalfChecked 为实心方块 (`rect`)，Checked 为对勾。

## Audit Checklist (自检清单)
- [ ] Checkbox 尺寸是否为 16px？
- [ ] 圆角是否为 2px？
- [ ] Disabled 状态下的选中色是否正确 (`#BECCFA`)？
- [ ] Unchecked Hover 是否变色？
