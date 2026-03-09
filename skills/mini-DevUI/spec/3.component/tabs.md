# Spec: Tabs (页签)

[Metadata]
- **Component Name**: Tabs
- **Figma Node**: 98-263
- **CSS Class Prefix**: `devui-tabs`
- **Version**: v1.0

## 1. Property Spec (属性规范)
定义组件的 API 接口，确保与 DevUI 标准对齐。

| Prop Name | Type | Description | Default |
| :--- | :--- | :--- | :--- |
| `activeTab` | `string \| number` | 当前激活的 Tab ID | - |
| `data` | `Array<{ id: string\|number, title: string, disabled?: boolean }>` | 页签数据源 | `[]` |
| `type` | `'pills' \| 'tabs' \| 'wrapped' \| 'icon' \| 'text'` | 页签样式类型：胶囊(Pills)/标准(Tabs)/包裹(Wrapped)/纯图标(Icon)/文本带图标(Text) | `'pills'` |

## 3. Visual Spec (视觉规范)
定义视觉还原的严格规范，强制使用 Token 和 Flex 布局。

### 3.1 Layout Logic (布局逻辑)
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
    - `gap: 4px` (如内部包含前缀图标或后缀 Badge，以此参数保障原生间距)

### 3.2 Styling Rules (样式映射)

#### Type: Pills (胶囊型 - Figma Definition)
*Note: Figma 中名为 Pills，但视觉表现为文字下划线样式 (Line Style).*

| Component Part | CSS Property | Token / Value | Fallback (Hex) |
| :--- | :--- | :--- | :--- |
| **Container** | `border-bottom` | `none` (Figma: 无底边线) | - |
| **Container** | `gap` | `24px` | - |
| **Item (Normal)** | `padding` | `8px 0` (消除横向padding, 使下划线与文字同宽) | - |
| **Item (Normal)** | `color` / `font-weight` | `var(--devui-aide-text)`, `font-weight: 400` | `#8A8E99` |
| **Item (Hover/Active)** | `color` / `font-weight` | `var(--devui-text)`, `font-weight: 500` | `#252B3A` |
| **Item (Active)** | `border-bottom` | `2px solid var(--devui-text)` (高对比黑条) | `#252B3A` |

#### Type: Tabs (标准型)
*Note: 视觉上与 Pills 类似，但增加了容器底部的灰色分割线。*

| Component Part | CSS Property | Token / Value | Fallback (Hex) |
| :--- | :--- | :--- | :--- |
| **Container** | `border-bottom` | `1px solid var(--devui-line)` (灰色底线) | `#DFE1E6` |
| **Container** | `gap` | `24px` | - |
| **Item (Normal)** | `padding` | `8px 0` (消除横向padding, 使下划线与文字同宽) | - |
| **Item (Normal)** | `color` / `font-weight` | `var(--devui-aide-text)`, `font-weight: 400` | `#8A8E99` |
| **Item (Hover/Active)** | `color` / `font-weight` | `var(--devui-text)`, `font-weight: 500` | `#252B3A` |
| **Item (Active)** | `border-bottom` | `2px solid var(--devui-text)` (高对比黑条) | `#252B3A` |

#### Type: Wrapped (包裹型 - Figma Definition)
*Note: Figma 中名为 Wrapped，但视觉表现为灰色块状样式 (Solid/Gray Style).*

| Component Part | CSS Property | Token / Value | Fallback (Hex) |
| :--- | :--- | :--- | :--- |
| **Container** | `border-bottom` | `1px solid var(--devui-global-bg)` / `gap: 0px` | `#F3F5F8` |
| **Item (Normal/Hover)** | `background-color` | `transparent` (悬浮时背景仍保持透明) | - |
| **Item (Normal)** | `color` / `font-weight` | `var(--devui-text-weak)`, `font-weight: 400` | `#575D6C` |
| **Item (Hover)** | `color` | `var(--devui-text)` | `#252B3A` |
| **Item (Active)** | `background-color` | `var(--devui-global-bg)` (扁平，无任何外边框) | `#F3F5F8` |
| **Item (Active)** | `color` / `font-weight` | `var(--devui-text)`, `font-weight: 400` (依据Figma基准) | `#252B3A` |
| **Radius** | `border-radius` | `var(--devui-radius) var(--devui-radius) 0 0` | `4px` |
| **Badge (Normal)**| `background` / `color` | bg: `var(--devui-global-bg)`, text: `var(--devui-aide-text)`, `fw: 400` | - |
| **Badge (Active)**| `background` / `color` | bg: `var(--devui-global-bg)` (视觉隐身), text: `var(--devui-text)`, `fw: 700` | - |

> [!CAUTION]
> **Naming vs Visual**: Figma 中的命名与 DevUI 标准组件库有差异。请严格遵循上述 **Preview 视觉特征** 而非仅看名字。
> - `type="pills"` -> Output **Underline** style.
> - `type="wrapped"` -> Output **Solid Gray Block** style.
> - `type="icon" / "text"` -> Output **Segmented Block** style with shadows on active.

## 4. Icon Spec (图标规范)
- ⚠️ **强制约束**: 对于图标页签和文本页签中的图标调用，**必须且只能使用 `action` 目录下的底层图标素材** (即路径类似 `../../../icon/miniDev-icon/action/[name].svg`)。
- 图标渲染方式: 必须采用 `-webkit-mask-image` 配合 `background-color: currentColor`，以确保 Hover/Active 等交互状态下色值的自然继承。

#### Type: Icon / Text (图标/文本组页签)
*Note: 此类页签常用于工具栏内部或面板内的局部切换，外层为一个带2px Padding与浅灰色背景的集合容器，激活项具有白底加阴影呈现凸起效果。*

| Component Part | CSS Property | Token / Value | Fallback (Hex) |
| :--- | :--- | :--- | :--- |
| **Container (Group)** | `background-color` | `var(--devui-list-item-hover-bg)` | `#F2F5FC` |
| **Container (Group)** | `padding` / `border-radius` | `padding: 2px`, `border-radius: 4px` | - |
| **Icon Item (Size)** | `width` / `height` | `28px` | - |
| **Text Item (Padding)** | `padding` | `4px 8px` (外加 `gap: 4px`) | - |
| **Item (Normal Text)** | `color` / `font-weight` | Icon为 `var(--devui-text)`, Text为 `var(--devui-aide-text)`, `font-weight: 400` | Icon:`#25`, Text:`#8A` |
| **Item (Hover)** | `background-color` | Icon项为 `var(--devui-list-item-hover-bg)` | `#F2F5FC` |
| **Item (Active)** | `background-color` | `var(--devui-base-bg)` | `#FFFFFF` |
| **Item (Active)** | `box-shadow` | `0px 4px 12px 0px rgba(0, 0, 0, 0.16)` | - |
| **Item (Active Text)** | `color` / `font-weight` | 均激活为 `var(--devui-text)`, `font-weight: 500` | `#252B3A` |
| **Item (Disabled)** | `color` | `var(--devui-disabled-text)` | `#ADB0B8` |

## 7. Anti-Patterns (负面示例)
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

## 8. Audit Checklist (自检清单)
- [ ] 属性名是否包含 `activeTab`, `type`？
- [ ] 颜色引用是否全部为 `var(--devui-*)`？
- [ ] Pills 类型激活态是否为 Brand 背景？
- [ ] Wrapped 类型激活态是否与内容区连通（底边框处理）？
- [ ] Icon/Text 类型激活态是否正确包含 `0 4px 12px rgba(0,0,0,0.16)` 阴影与白色背景？
- [ ] 图标是否严格限定使用 `icon/miniDev-icon/action/` 目录？
- [ ] 布局是否使用了 Flex？
