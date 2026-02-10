# Skill: Search (搜索框)

[Metadata]
- **Component Name**: Search
- **Figma Node**: 164:370
- **DevUI Component**: `d-search`
- **Version**: v1.0

## Property Skill
定义组件的 API 接口，确保与 DevUI 标准对齐。

| Prop Name | Type | Description | Default |
| :--- | :--- | :--- | :--- |
| `size` | `'sm' \| 'md' \| 'lg'` | 尺寸大小 | `'md'` |
| `placeholder` | `string` | 占位文本 | `'请输入搜索内容'` |
| `iconPosition` | `'left' \| 'right'` | 搜索图标位置 | `'right'` |
| `disabled` | `boolean` | 是否禁用 | `false` |
| `isKeyupSearch` | `boolean` | 是否在按下键盘时触发搜索 | `false` |
| `onSearch` | `(value: string) => void` | 搜索回调 | - |

## Visual Skill
定义视觉还原的严格规范，强制使用 Token 和 Flex 布局。

### 1. Layout Logic (布局逻辑)
- **Container (`.devui-search`)**:
    - `display: flex`
    - `align-items: center`
    - `width`: `100%` (或由父容器控制)
    - `border-radius`: `6px` (Fixed consistency)
    - `transition`: `all .3s`
    - **Positioning**:
        - 图标与输入框的相对位置通过 Flex 顺序控制，或 Icon 绝对定位（但在 Skill 中优先推荐 Flex 布局）。
        - **Left Icon**: Icon 在 Input 左侧。
        - **Right Icon**: Icon 在 Input 右侧。

- **Input Element (`input`)**:
    - `flex: 1` (撑满剩余空间)
    - `border`: `none`
    - `outline`: `none`
    - `background`: `transparent`
    - `padding`: `0` (Padding 由 Container 统一管理)

### 2. Styling Rules (样式映射)

#### Base Style (基础样式 - Size=md)
| Component Part | CSS Property | Token / Value | Fallback (Hex) |
| :--- | :--- | :--- | :--- |
| **Container** | `height` | `32px` (Size=md) | - |
| **Container** | `padding` | `0 8px` | - |
| **Container** | `background-color` | `var(--devui-base-bg)` | `#FFFFFF` |
| **Container** | `border` | `1px solid var(--devui-form-control-line)` | `#ADB0B8` |
| **Placeholder** | `color` | `var(--devui-placeholder)` | `#8A8E99` |
| **Text** | `color` | `var(--devui-text)` | `#252B3A` |

#### Comparison: Icon Position (图标位置)
| Feature | Implementation Hint |
| :--- | :--- |
| **Icon Left** | Flex Order: `Icon -> Input`. Gap: `4px` |
| **Icon Right** | Flex Order: `Input -> Icon`. Gap: `4px` (Clear Icon 也需考虑) |

#### States (状态交互)

| State | CSS Property | Token / Value | Fallback (Hex) |
| :--- | :--- | :--- | :--- |
| **Hover** | `border-color` | `var(--devui-form-control-line-)` | `#5E7CE0` |
| **Hover** | `box-shadow` | `box-shadow` | `0 0 0 4px var(--devui-form-control-line-rippling)` (Figma: rgba 94,124,224,0.08) | - |
| **Active/Focus** | `border-color` | `var(--devui-form-control-line-active)` | `#5E7CE0` |
| **Active/Focus** | `box-shadow` | `0 0 0 4px var(--devui-form-control-line-rippling)` (Figma: rgba 94,124,224,0.08) | - |
| **Disabled** | `background-color` | `var(--devui-disabled-bg)` (Figma: #F3F3F3) | `#F3F3F3` |
| **Disabled** | `border-color` | `var(--devui-disabled-line)` | `#DFE1E6` |
| **Disabled** | `color` | `var(--devui-disabled-text)` | `#ADB0B8` |
| **Disabled** | `cursor` | `not-allowed` | - |

## Icon Skill (图标规范)
图标资源位于项目根目录 `icon/` 文件夹下。
- **Search Icon**: 使用 `icon/search.svg` (需确认是否存在，或用默认图标)。
- **Clear Icon**: 使用 `icon/close.svg` (当有内容时显示)。
- **Color**:
    - Default: `var(--devui-placeholder)` 或 `var(--devui-text)` (视设计稿而定，Figma 中 Icon 为 `#252B3A` 或 `#8A8E99`)。
    - Active: `var(--devui-icon-fill-active)` (Figma: #5E7CE0) —— 当 `isKeyupSearch` 或特定交互时。

## Anti-Patterns (负面示例)
1.  **❌ 禁止 Input 自带 Border**
    - Input 标签应无边框，边框样式在父容器 Container 上实现。
2.  **❌ 禁止硬编码图标颜色**
    - 图标颜色应响应状态变化（如 Focus 时变色）。
3.  **❌ 禁止忽略 Hover 状态**
    - 鼠标悬停时边框颜色需加深。

## Audit Checklist (自检清单)
- [ ] 是否支持 `iconPosition` 左右切换？
- [ ] Focus 状态是否有 `rippling` 阴影效果？
- [ ] Disabled 状态背景色是否正确 (`#F3F3F3`)？
- [ ] Placeholder 颜色是否符合 Token (`devui-placeholder`)？
