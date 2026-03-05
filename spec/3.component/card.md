# Spec: Card (项目卡片)

[Metadata]
- **Component Name**: Card (pj-card)
- **Figma Node**: 3501-10161
- **DevUI Component**: `d-card` / `pj-card`
- **Template Source**: `spec/4.template/card-tem.html`
- **Version**: v1.0

## 1. Property Spec (属性规范)

| Prop Name | Type | Description | Default |
| :--- | :--- | :--- | :--- |
| `appIcon` | `string (path)` | 应用图标路径，引用 `engineering-initial/[X]-32x33.svg` | 必填 |
| `title` | `string` | 卡片标题文本 | 必填 |
| `tags` | `Array<{text, variant}>` | 标签列表，variant: `'success'` / `'general'` | `[]` |
| `creator` | `string` | 创建者名称 | `'-'` |
| `projectId` | `string` | 项目ID（显示截断+复制按钮） | `'-'` |
| `starred` | `boolean` | 是否已收藏 | `false` |

## 2. Content Presentation (内容呈现)

### 2.1 Header (头部区域)
- **Layout**: `display: flex; align-items: center; gap: 12px;`
- **Structure**:
    ```html
    <div class="devui-pjcard-header">
        <div class="devui-pjcard-app-icon">
            <img src="{{appIcon}}" alt="{{title}}">
        </div>
        <span class="devui-pjcard-title">{{title}}</span>
        <div class="devui-pjcard-actions">
            <button class="devui-pjcard-action-btn {{starredClass}}">☆</button>
            <button class="devui-pjcard-action-btn">•••</button>
        </div>
    </div>
    ```

#### App Icon (应用图标)
- **Size**: 40 × 40px，固定不变
- **Border Radius**: `var(--devui-border-radius-md, 8px)`
- **Source**: `icon/miniDev-icon/engineering-initial/[A-Z0-9]-32x33.svg`
- **Implementation**: 使用 `<img>` 标签，`object-fit: cover`
- **Note**: 禁止使用 CSS Mask（SVG 包含多色渐变）

#### Title (标题)
- **Font**: `var(--devui-font-size-lg, 16px)`, Weight `700`
- **Color**: `var(--devui-text, #252B3A)`
- **Line Height**: `24px`
- **Overflow**: 单行 ellipsis (`white-space: nowrap; overflow: hidden; text-overflow: ellipsis`)
- **Flex**: `flex: 1` 占据剩余空间

#### Action Buttons (操作按钮)
- 包含 **收藏** (Star) 和 **更多** (More •••) 两个按钮
- **Size**: 24 × 24px
- **Icon Size**: 16 × 16px (SVG inline)
- **Color**: `var(--devui-text-weak, #5E6678)`
- **Hover**: `background: var(--devui-pjcard-tag-general-bg, #F2F5FC); color: var(--devui-brand, #5E7CE0)`
- **Starred Active**: `color: #FAC20A` (金色填充), class `.is-starred`

### 2.2 Tags Section (标签区域)
- **Layout**: `display: flex; gap: 8px; flex-wrap: wrap;`
- **Min Height**: `22px` (即使无标签也保持占位)
- **Structure**:
    ```html
    <div class="devui-pjcard-tags">
        <span class="devui-pjcard-tag devui-pjcard-tag--{{variant}}">{{text}}</span>
        ...
    </div>
    ```

#### Tag Variants

| Variant | Background | Text Color | Use Case |
| :--- | :--- | :--- | :--- |
| `success` (绿色) | `var(--devui-pjcard-tag-success-bg, #E6F6F0)` | `var(--devui-pjcard-tag-success-text, #00A870)` | 正式/有效标签 |
| `general` (灰色) | `var(--devui-pjcard-tag-general-bg, #F2F5FC)` | `var(--devui-pjcard-tag-general-text, #252B3A)` | 通用/默认标签 |

#### Tag Common Style
- **Height**: `22px`
- **Padding**: `0 8px`
- **Border Radius**: `var(--devui-border-radius-sm, 4px)`
- **Font Size**: `var(--devui-font-size-sm, 12px)`, Weight `400`

### 2.3 Meta Section (底部信息区)
- **Layout**: `display: flex; align-items: center;`
- **Structure**:
    ```html
    <div class="devui-pjcard-meta">
        <div class="devui-pjcard-meta-item">
            <span class="devui-pjcard-meta-label">创建者：</span>
            <span class="devui-pjcard-meta-value">{{creator}}</span>
        </div>
        <div class="devui-pjcard-meta-divider"></div>
        <div class="devui-pjcard-meta-item">
            <span class="devui-pjcard-meta-label">项目ID：</span>
            <span class="devui-pjcard-meta-value devui-pjcard-meta-value--truncated">{{projectId}}</span>
            <button class="devui-pjcard-copy-btn">📋</button>
        </div>
    </div>
    ```

#### Meta Style
- **Font Size**: `var(--devui-font-size-sm, 12px)`
- **Label Color**: `var(--devui-text-weak, #5E6678)`
- **Value Color**: `var(--devui-text, #252B3A)`
- **Divider**: `1px × 12px`, Color `var(--devui-line, #DFE1E6)`, Margin `0 12px`
- **Value Overflow**: `max-width: 160px; text-overflow: ellipsis`
- **ProjectId Truncated**: `max-width: 80px`

## 3. Visual Spec (视觉规范)

### Card Container (卡片容器)

| Component Part | CSS Property | Token / Value | Fallback (Hex) |
| :--- | :--- | :--- | :--- |
| **Container** | `width` | `380px` (Fixed) | - |
| **Container** | `height` | Hug Contents | - |
| **Container** | `background-color` | `var(--devui-base-bg)` | `#FFFFFF` |
| **Container** | `border` | `1px solid var(--devui-line)` | `#DFE1E6` |
| **Container** | `border-radius` | `var(--devui-border-radius-lg)` | `12px` |
| **Container** | `padding` | `20px 24px` | - |
| **Container** | `gap` | `16px` (vertical flex) | - |
| **Container** | `cursor` | `pointer` | - |
| **Hover** | `box-shadow` | `var(--devui-shadow-length-hover)` | `0 4px 16px rgba(37,43,58,0.16)` |
| **Hover** | `border-color` | - | `#C8CADE` |

### Vertical Spacing (内部垂直间距)
```
Header (Icon + Title + Actions)
    ↓ 16px (gap)
Tags (标签区域)
    ↓ 16px (gap)
Meta (创建者 + 项目ID)
```

## 5. Dynamic Response (动态响应)

### Text Overflow
- **Title**: 单行 ellipsis，`flex: 1` 自适应宽度
- **Creator Value**: `max-width: 160px`, ellipsis
- **ProjectId Value**: `max-width: 80px`, ellipsis + "..." 显示

### Empty State
- **Tags Empty**: `.devui-pjcard-tags` 保留 `min-height: 22px`，不显示任何内容
- **No Icon**: 不应发生，appIcon 为必填字段

## 4. Icon Spec (图标规范)

### 4.1 图标来源
- **工程头像**: `icon/miniDev-icon/engineering-initial/`
- **操作图标**: 内联 SVG（收藏星标、更多菜单、复制）

### 4.2 渲染方式
| 类型 | 渲染方式 | 说明 |
|:---|:---|:---|
| 工程首字母头像 | `<img>` + `object-fit: cover` | 多色渐变，严禁 CSS Mask |
| 操作图标（Star/More/Copy） | 内联 SVG + `currentColor` | 需跟随文本/状态色变化 |

### 4.3 图标映射表

| 用途 | 图标文件 | 尺寸 | 渲染方式 | 备注 |
|:---|:---|:---|:---|:---|
| App 头像 | `engineering-initial/[A-Z0-9]-32x33.svg` | 32×33 | `<img>` | 首字母/首数字 + 尺寸后缀 |
| 收藏星标 | 内联 SVG (stroke) | 16×16 | inline SVG | `currentColor`；Active: `fill: #FAC20A` |
| 更多操作 | 内联 SVG (3圆点) | 16×16 | inline SVG | `currentColor` |
| 复制按钮 | 内联 SVG | 14×14 | inline SVG | `currentColor`，继承 `--devui-text-weak` |

### 4.4 Anti-Pattern
- ❌ **严禁** CSS Mask 渲染工程首字母头像（会破坏多色渐变）
- ❌ 禁止使用 `<img>` 加载操作类图标（无法跟随状态色变化）
- ❌ 禁止硬编码星标颜色（Active 态必须使用 `#FAC20A`）

## 8. Audit Checklist (自检清单)
- [ ] 是否使用了 `--devui-` Token 变量？
- [ ] App Icon 是否通过 `<img>` 引用 engineering-initial 图标？
- [ ] 标签是否支持 `success` / `general` 两种 variant？
- [ ] 容器 padding 是否为 `20px 24px`？
- [ ] Hover 是否有 shadow 和 border-color 变化？
- [ ] 底部 Meta 是否包含竖线分隔符（`1px × 12px`）？
