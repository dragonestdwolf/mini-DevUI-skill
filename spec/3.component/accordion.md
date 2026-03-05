# Spec: Accordion

[Metadata]
- **Component**: `d-accordion`
- **Template Source**: `spec/4.template/accordion-tem.html`
- **Figma Node**: `2920:9654` (侧边导航-手风琴)

## 2. Content Presentation (内容呈现)

### 2.1 一级菜单项 (Primary Item)
- **Structure**:
  ```html
  <div class="devui-accordion-item {{state}}">
      <span class="devui-accordion-item-text">{{label}}</span>
      <div class="devui-accordion-item-icon"></div>
  </div>
  ```
- **Style**:
  - `padding`: `9px 12px`
  - `justify-content`: `space-between`
  - `align-items`: `center`
  - Icon using `mask-image` with `chevron-down.svg`, reversed by `transform: rotate(-90deg)` in default state to face right.

### 2.2 二级菜单项 (Secondary Subitem)
- **Structure**:
  ```html
  <div class="devui-accordion-subitem {{state}}">
      <span class="devui-accordion-subitem-text">{{label}}</span>
  </div>
  ```
- **Style**:
  - `padding`: `9px 12px 9px 32px` (左侧 32px 缩进形成视觉层级)
  - `justify-content`: `space-between`

### 2.3 侧边栏组装体 (Sidebar Menu Assembly)
- **Structure**:
  ```html
  <div class="devui-accordion-menu">
      <div class="devui-accordion-menu-header">
          <h3 class="devui-accordion-menu-title">{{title}}</h3>
          <div class="devui-accordion-menu-icon" title="收起列表"></div>
      </div>
      <div class="devui-accordion-menu-list">
          <div class="devui-accordion-group is-expanded">
              <!-- 一级菜单 -->
              <!-- 二级菜单列表 -->
          </div>
      </div>
  </div>
  ```

## 4. Icon Spec (图标规范)

### 4.1 图标来源
- **目录**: `icon/miniDev-icon/action/`

### 4.2 渲染方式
展开/收起箭头为**单色线性图标**，必须使用 **CSS Mask** + `currentColor`。

### 4.3 图标映射表

| 用途 | 图标文件 | 尺寸 | 渲染方式 | 备注 |
|:---|:---|:---|:---|:---|
| 展开/收起指示箭头 | `chevron-down.svg` | 16×16 | mask | 收起态 `rotate(-90deg)`；展开态 `rotate(0deg)` |

### 4.4 Anti-Pattern
- ❌ 禁止用 ">" 或 "▶" 文本替代 SVG 箭头图标
- ❌ 禁止 `<img>` 加载箭头（需跟随文本色变化：Active 态为品牌蓝）

---

## 5. Dynamic Response (动态响应)

### 5.1 Text Overflow (文本溢出截断)
- **Problem**: Long strings without spaces or long text input break the rigid `248px` box layout.
- **Solution**: The text elements (`.devui-accordion-item-text`, `.devui-accordion-subitem-text`, `.devui-accordion-menu-title`) limit width using Flexbox:
  - Text node style: `overflow: hidden; text-overflow: ellipsis; white-space: nowrap; flex: 1; min-width: 0;`
  - Fixed-width elements (Icons) style: `flex-shrink: 0;`

## 3. Visual Spec (视觉规范)

### 3.1 Hover (悬浮态)
- **Trigger**: Mouse hover over item or subitem, or `.hover` class.
- **Visuals**:
  - `background-color`: `var(--devui-list-item-hover-bg)` (e.g., `#f5f5f6`)

### 3.2 Active (激活/选中态)
- **Trigger**: Selected active routing, or `.active` class.
- **Visuals**:
  - Text color: `var(--devui-brand)` (e.g., `#5e7ce0`)
  - `font-weight`: `700` (Bold)
  - Base Icon (if active context required): `background-color: var(--devui-icon-fill-active)`

### 3.3 Expand (展开态 - 仅适用于一级菜单)
- **Trigger**: Click to expand group, or `.expand` class.
- **Visuals**:
  - Icon rotation: `transform: rotate(0deg)` (箭头恢复向下)

## 6. Template Injection (模版注入)

- `{{title}}`: 侧边栏组装体的头部标题文本，例如 "设置"。
- `{{label}}`: 一级或二级菜单文本内容。
- `{{state}}`: 对应元素的状态修饰，如 `active`, `hover`, `expand` (可组合，以空格分隔)。
- `{{items}}`: 整个菜单列表区域插入 HTML 组合切片片段的地方，内部按 `.devui-accordion-group` 分级封装。
