# Spec: Accordion

[Metadata]
- **Component**: `d-accordion`
- **Template Source**: `spec/4.template/accordion-tem.html`
- **Figma Node**: `2920:9654` (侧边导航-手风琴)

## 1. Content Presentation (内容呈现格式)

### 1.1 一级菜单项 (Primary Item)
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

### 1.2 二级菜单项 (Secondary Subitem)
- **Structure**:
  ```html
  <div class="devui-accordion-subitem {{state}}">
      <span class="devui-accordion-subitem-text">{{label}}</span>
  </div>
  ```
- **Style**:
  - `padding`: `9px 12px 9px 32px` (左侧 32px 缩进形成视觉层级)
  - `justify-content`: `space-between`

### 1.3 侧边栏组装体 (Sidebar Menu Assembly)
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

## 2. Dynamic Response (动态响应)

### 2.1 Text Overflow (文本溢出截断)
- **Problem**: Long strings without spaces or long text input break the rigid `248px` box layout.
- **Solution**: The text elements (`.devui-accordion-item-text`, `.devui-accordion-subitem-text`, `.devui-accordion-menu-title`) limit width using Flexbox:
  - Text node style: `overflow: hidden; text-overflow: ellipsis; white-space: nowrap; flex: 1; min-width: 0;`
  - Fixed-width elements (Icons) style: `flex-shrink: 0;`

## 3. Interaction States (交互状态)

### 2.1 Hover (悬浮态)
- **Trigger**: Mouse hover over item or subitem, or `.hover` class.
- **Visuals**:
  - `background-color`: `var(--devui-list-item-hover-bg)` (e.g., `#f5f5f6`)

### 2.2 Active (激活/选中态)
- **Trigger**: Selected active routing, or `.active` class.
- **Visuals**:
  - Text color: `var(--devui-brand)` (e.g., `#5e7ce0`)
  - `font-weight`: `700` (Bold)
  - Base Icon (if active context required): `background-color: var(--devui-icon-fill-active)`

### 2.3 Expand (展开态 - 仅适用于一级菜单)
- **Trigger**: Click to expand group, or `.expand` class.
- **Visuals**:
  - Icon rotation: `transform: rotate(0deg)` (箭头恢复向下)

## 4. Template Injection (模版注入)

- `{{title}}`: 侧边栏组装体的头部标题文本，例如 "设置"。
- `{{label}}`: 一级或二级菜单文本内容。
- `{{state}}`: 对应元素的状态修饰，如 `active`, `hover`, `expand` (可组合，以空格分隔)。
- `{{items}}`: 整个菜单列表区域插入 HTML 组合切片片段的地方，内部按 `.devui-accordion-group` 分级封装。
