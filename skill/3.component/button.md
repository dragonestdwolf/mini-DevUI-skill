# Skill: Button (按钮)

[Metadata]
- **Component Name**: Button
- **Figma Node**: 23:100
- **DevUI Component**: `d-button`
- **Version**: v1.0

## Property Skill
定义组件的 API 接口，确保与 DevUI 标准对齐。

| Prop Name | Type | Description | Default |
| :--- | :--- | :--- | :--- |
| `variant` | `'primary' \| 'secondary' \| 'text'` | 按钮样式变体：主要/次要(通用)/文本 | `'secondary'` |
| `size` | `'sm' \| 'md' \| 'lg'` | 尺寸大小 | `'md'` |
| `icon` | `ReactNode` | 按钮图标（左侧） | - |
| `disabled` | `boolean` | 是否禁用 | `false` |
| `onClick` | `() => void` | 点击事件回调 | - |
| `children` | `ReactNode` | 按钮内容 | - |

## Icon Skill (图标规范)
图标资源位于项目根目录 `icon/` 文件夹下。

### 1. Usage Rules (使用规则)
- **Import**: 需从 `icon/` 目录导入 SVG 文件。
- **Prop**:
    - **Primary/Secondary**: 使用 `icon` 属性传递 Icon 组件。
    - **Text**: 可直接作为 `children` 的一部分，或使用 `icon` 属性。
- **Size**: 按钮内图标默认尺寸为 `16px x 16px`。图标与文字的间距为4px
- **Color**:
    - Icon 颜色应继承父级文字颜色 (`currentColor`) 或显式跟随 Variant 规则。
    - **Primary**: `var(--devui-light-text)` (White).
    - **Secondary/Text**: `var(--devui-text)` / Hover: `var(--devui-primary)`.

## Visual Skill
定义视觉还原的严格规范，强制使用 Token 和 Flex 布局。

### 1. Layout Logic (布局逻辑)
- **Container (`.devui-btn`)**:
    - `display: flex`
    - `align-items: center`
    - `justify-content: center`
    - `white-space: nowrap`
    - `gap: 4px` (Content 与 Icon 间距)
    - `border-radius`: `var(--devui-radius)` (通常 4px)
    - `cursor`: `pointer` (Disabled: `not-allowed`)
    - **Height/Padding Rules**:
        - **sm**: Height 28px, Padding `0 12px` (Primary: py=3px+border=0? / Secondary: py=2px+border=1?) -> 保持总高一致。
        - **md**: Height 32px, Padding `0 16px` (Design: Primary py=5px, Secondary py=4px+1px border).
        - **lg**: Height 40px, Padding `0 20px`.

### 2. Styling Rules (样式映射)

#### Variant: Primary (主要按钮)
高频操作或强调操作。

| Component Part | CSS Property | Token / Value | Fallback (Hex) |
| :--- | :--- | :--- | :--- |
| **Container** | `background-color` | `var(--devui-primary)` | `#5E7CE0` |
| **Container** | `border` | `none` (或 1px solid transparent) | - |
| **Text** | `color` | `var(--devui-light-text)` | `#FFFFFF` |
| **Hover** | `background-color` | `var(--devui-primary-hover)` (需推断或使用 Light/Dark 变体) | `#7693F5` |
| **Active** | `background-color` | `var(--devui-primary-active)` (Figma: #344899) | `#344899` |
| **Disabled** | `background-color` | `var(--devui-primary-disabled)` (Figma: #BECCFA) | `#BECCFA` |
| **Disabled** | `color` | `var(--devui-light-text)` (保持白色) | `#FFFFFF` |
| **Disabled** | `cursor` | `not-allowed` | - |

#### Variant: Secondary (次要/通用按钮)
常用于取消、重置或次要操作。

| Component Part | CSS Property | Token / Value | Fallback (Hex) |
| :--- | :--- | :--- | :--- |
| **Container** | `background-color` | `var(--devui-base-bg)` | `#FFFFFF` |
| **Container** | `border` | `1px solid var(--devui-form-control-line)` (或 `devui-line`) | `#ADB0B8` |
| **Text** | `color` | `var(--devui-text)` | `#252B3A` |
| **Hover** | `border-color` | `var(--devui-from-control-line-hover)` | `#575D6C` |
| **Active** | `border-color` | `var(--devui-form-control-line-active)` (Figma: #5E7CE0) | `#5E7CE0` |
| **Disabled** | `background-color` | `var(--devui-btn-common-bg-disabled)` (Figma: #F5F5F5) | `#F5F5F5` |
| **Disabled** | `border-color` | `var(--devui-disabled-line)` (Figma: #DFE1E6) | `#DFE1E6` |
| **Disabled** | `color` | `var(--devui-disabled-text)` (Figma: #ADB0B8) | `#ADB0B8` |

#### Variant: Text (文本按钮)
常用于无需强调的操作，或表格行内操作。

| Component Part | CSS Property | Token / Value | Fallback (Hex) |
| :--- | :--- | :--- | :--- |
| **Container** | `background-color` | `transparent` | - |
| **Container** | `border` | `none` | - |
| **Text** | `color` | `var(--devui-text)` | `#252B3A` |
| **Padding** | `padding` | `0 8px` (比实体按钮小) | - |
| **Hover** | `color` | `var(--devui-primary)` | `#5E7CE0` |
| **Active** | `color` | `var(--devui-primary-active)` (Figma: #5E7CE0) | `#344899` |
| **Disabled** | `color` | `var(--devui-disabled-text)` (Figma: #BABBC0/ADB0B8) | `#ADB0B8` |
| **Disabled** | `background-color` | `transparent` | - |

> [!NOTE]
> Text 按钮在 Figma 中有 `Icon` 变体 (`chevronDown`)，这应通过 `children` 或 `icon` 属性灵活实现，不强制绑定在样式中。

## Anti-Patterns (负面示例)
禁止在生成代码时出现以下模式：

1.  **❌ 禁止硬编码颜色**
    ```css
    /* Bad */
    background: #5E7CE0;
    /* Good */
    background: var(--devui-primary);
    ```

2.  **❌ 禁止使用 Fixed Width**
    - 按钮宽度应由内容 (`padding`) 撑开，除非有特殊全宽需求。

3.  **❌ 禁止混淆 Secondary 与 Text**
    - Secondary 必须有边框 (`1px solid`)，Text 必须无边框。

## Audit Checklist (自检清单)
- [ ] 是否支持 `variant` (primary, secondary, text)？
- [ ] Secondary 按钮是否有边框 (`devui-form-control-line`)？
- [ ] Primary 按钮文字是否为白色 (`devui-light-text`)？
- [ ] Padding 是否符合 Size=md (`0 16px`)？
- [ ] 布局是否使用了 Flex + Gap？
