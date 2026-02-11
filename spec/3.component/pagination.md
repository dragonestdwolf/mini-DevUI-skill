# Skill: Pagination (分页器)

[Metadata]
- **Component Name**: Pagination
- **Figma Node**: 233:431
- **DevUI Component**: `d-pagination`
- **Version**: v1.0

## Property Skill
定义组件的 API 接口，确保与 DevUI 标准对齐。

| Prop Name | Type | Description | Default |
| :--- | :--- | :--- | :--- |
| `total` | `number` | 总条目数 | `0` |
| `pageSize` | `number` | 每页条数 | `10` |
| `pageIndex` | `number` | 当前页码 | `1` |
| `showSizeChanger` | `boolean` | 是否显示页码切换器 (Select) | `false` |
| `showJump` | `boolean` | 是否显示跳转输入框 | `false` |
| `canViewTotal` | `boolean` | 是否显示总条数 | `false` |
| `onChange` | `(pageIndex: number, pageSize: number) => void` | 页码或每页条数改变回调 | - |

## Visual Skill
定义视觉还原的严格规范，强制使用 Token 和 Flex 布局。

### 1. Layout Logic (布局逻辑)
- **Container (`.devui-pagination`)**:
    - `display: flex`
    - `align-items: center`
    - `user-select`: `none`
    - `gap`: `8px` (Items 之间间距)
    - `font-size`: `12px` (Context text like "Total")
    - `color`: `var(--devui-text)`

- **Items Alignment**:
    - **Total Text**: Leftmost (if visible).
    - **Size Changer (Select)**: Left/Middle.
    - **Page List (UL)**: Center/Right.
    - **Jump (Go To)**: Rightmost.

- **Page Item (Button)**:
    - `width`: `28px` (Fixed square)
    - `height`: `28px`
    - `border-radius`: `4px`
    - `display`: `flex`
    - `align-items`: `center`
    - `justify-content`: `center`
    - `cursor`: `pointer`
    - `transition`: `all .2s`

### 2. Styling Rules (样式映射)

#### Page Number (页码按钮)

| State | CSS Property | Token / Value | Fallback (Hex) |
| :--- | :--- | :--- | :--- |
| **Default** | `color` | `var(--devui-text)` (#252B3A) | `#252B3A` |
| **Default** | `background-color` | `transparent` | - |
| **Hover** | `background-color` | `var(--devui-list-item-hover-bg)` (#F2F5FC) | `#F2F5FC` |
| **Hover** | `color` | `var(--devui-brand)` (#5E7CE0) | `#5E7CE0` |
| **Active (Selected)** | `background-color` | `var(--devui-list-item-hover-bg)` (#F2F5FC) | `#F2F5FC` |
| **Active (Selected)** | `color` | `var(--devui-brand)` (#5E7CE0) | `#5E7CE0` |
| **Disabled** | `color` | `var(--devui-disabled-text)` (#ADB0B8) | `#ADB0B8` |
| **Disabled** | `cursor` | `not-allowed` | - |

#### Prev/Next Button (翻页按钮)
- **Icon**: Chevron Left / Chevron Right (`icon/miniDev-icon/action/向左(chevron-left).svg`, `icon/miniDev-icon/action/向右(chevron-right).svg`).
- **Style**: Same hover/active rules as Page Number.
- **Disabled**: Opacity 0.5 or specific disabled token if at start/end.

#### Size Changer (Select - 下拉框)
- **Component**: 使用 `d-select` 组件。
- **Size**: `sm` (Height 28px match page items).
- **Width**: `80px` (Approx).

#### Jump to (跳转)
- **Text**: "前往" / "Go to" (`var(--devui-text)`).
- **Input**: 使用 `d-input` (`size="sm"`, width `48px` approx).
- **Unit**: "页" / "Page".

## Anti-Patterns (负面示例)
1.  **❌ 禁止页码使用 Circle 圆角**
    - 必须遵循 `border-radius: 4px`。
2.  **❌ 禁止自定义 Select 样式**
    - 必须复用 `d-select` 组件实现“10条/页”切换。
3.  **❌ 禁止硬编码文本颜色**
    - 使用 `var(--devui-text)` 和 `var(--devui-brand)` 响应主题。

## Audit Checklist (自检清单)
- [ ] 页码尺寸是否为 28x28px？
- [ ] 选中状态是否为淡蓝背景+品牌色文字？
- [ ] 切换条数部分是否使用了 Select 组件？
- [ ] 整体布局是否水平对齐居中？
