# Skill: Input (输入框)

[Metadata]
- **Component Name**: Input
- **Figma Node**: 250:436 (Text), 379:671 (Number)
- **DevUI Component**: `d-input`, `d-input-number`
- **Version**: v1.1

## Property Skill
定义组件的 API 接口，确保与 DevUI 标准对齐。

| Prop Name | Type | Description | Default |
| :--- | :--- | :--- | :--- |
| `type` | `'text' \| 'password' \| 'number'` | 输入框类型 | `'text'` |
| `value` | `string \| number` | 输入值 | - |
| `placeholder` | `string` | 占位文本 | `请输入` |
| `disabled` | `boolean` | 是否禁用 | `false` |
| `status` | `'error' \| 'success'` | 校验状态 | - |
| `size` | `'sm' \| 'md' \| 'lg'` | 尺寸大小 | `'md'` |
| `step` | `number` | 步长 (仅 Number 类型) | `1` |
| `max` | `number` | 最大值 (仅 Number 类型) | - |
| `min` | `number` | 最小值 (仅 Number 类型) | - |
| `onChange` | `(val: string \| number) => void` | 输入回调 | - |

## Visual Skill
定义视觉还原的严格规范，强制使用 Token 和 Flex 布局。

### 1. Layout Logic (布局逻辑)
- **Wrapper (`.devui-input-wrapper`)**:
    - `display: flex`
    - `align-items: center`
    - `width`: `100%` (fill container)
    - `height`: `32px` (md size)
    - `border-radius`: `4px`
    - `padding`: `0 12px`
    - `transition`: `all .2s`
    - `position`: `relative` (for Shadow positioning if needed)
    - `background-color`: `var(--devui-base-bg)` (#FFFFFF)
    - `border`: `1px solid var(--devui-form-control-line)` (#C9C9C9)

- **Input Element (`input`)**:
    - `flex`: `1`
    - `width`: `100%`
    - `border`: `none`
    - `outline`: `none`
    - `background`: `transparent`
    - `padding`: `0`
    - `font-size`: `14px`
    - `color`: `var(--devui-text)` (#252B3A)
    - `line-height`: `22px`
    - **Number Type**: `text-align: left` (Default)

- **Number Input Stepper (操作按钮)**:
    - **Layout**: 位于 Input 右侧内部，垂直排列或水平内嵌（Figma Design shows vertical buttons on the right inside the border, or hover-trigger? **Check Design**: Typically `devui-input-number` has `inc` and `dec` buttons).
    - **Container**: `display: flex; flex-direction: column; width: 22px; border-left: 1px solid var(--devui-dividing-line);`
    - **Buttons**:
        - `flex: 1`
        - `display: flex; align-items: center; justify-content: center`
        - `cursor`: `pointer`
        - `hover`: `bg-color: var(--devui-list-item-hover-bg)`

### 2. Styling Rules (样式映射)

#### Base Style (Default)
| Component Part | CSS Property | Token / Value | Fallback (Hex) |
| :--- | :--- | :--- | :--- |
| **Wrapper** | `background-color` | `var(--devui-base-bg)` | `#FFFFFF` |
| **Wrapper** | `border-color` | `var(--devui-form-control-line)` | `#C9C9C9` |
| **Placeholder**| `color` | `var(--devui-placeholder)` | `#8A8E99` |

#### States (状态交互) - **Strict Box-Shadow Implementation**

| State | CSS Property | Token / Value | Fallback (Hex) |
| :--- | :--- | :--- | :--- |
| **Hover** | `border-color` | `var(--devui-form-control-line-hover)` | `#575D6C` |
| **Hover** | `box-shadow` | `0 0 0 4px var(--devui-form-control-line-rippling)` | `rgba(94,124,224,0.08)` |
| **Active/Focus** | `border-color` | `var(--devui-form-control-line-active)` | `#5E7CE0` |
| **Active/Focus** | `box-shadow` | `0 0 0 4px var(--devui-form-control-line-rippling)` | `rgba(94,124,224,0.08)` |
| **Error** | `border-color` | `var(--devui-danger)` | `#F66F6A` |
| **Error** | `background-color` | `var(--devui-danger-bg)` | `#FFEED` |
| **Success** | `border-color` | `var(--devui-success)` | `#50D4AB` |
| **Disabled** | `background-color` | `var(--devui-disabled-bg)` | `#F3F3F3` |
| **Disabled** | `border-color` | `var(--devui-disabled-line)` | `#DFE1E6` |
| **Disabled** | `color` | `var(--devui-disabled-text)` | `#ADB0B8` |

#### Number Input Specifics
- **Stepper Border**: `1px solid var(--devui-dividing-line)` (#E3E5E9).
- **Icon**: Up/Down arrows (`chevron-up`, `chevron-down` from Icon Role).

## Anti-Patterns (负面示例)
1.  **❌ 禁止 Input 原生边框**
    - Input 标签必须无边框，所有视觉边框由父级 Wrapper 承担。
2.  **❌ 禁止 Focus 轮廓**
    - `input:focus` 必须设置 `outline: none`，Focus 样式通过 Wrapper 的 `border` 和 `box-shadow` 体现。
3.  **❌ 禁止使用 `type="number"` 的原生箭头**
    - 必须隐藏浏览器的默认 Spin Button (`::-webkit-inner-spin-button`)，使用自定义 DOM 模拟 Stepper 以保证跨浏览器一致性和样式还原。

## Audit Checklist (自检清单)
- [ ] Hover/Focus 状态是否有 `4px` 的淡蓝色 Ripple 阴影 (Box-Shadow)？
- [ ] Number Input 是否隐藏了原生 Spin Button？
- [ ] Number Input 右侧是否有自定义的加减按钮？
- [ ] 圆角是否统一为 4px？
