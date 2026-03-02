# Layout Skill (布局规范)

该文档定义了页面布局的标准规范，所有Agent在生成或修改页面布局时必须严格遵循本规范。

## 1. 布局核心结构与关系

页面布局由四个部分组成，其空间位置关系如下：

- **Header (顶部栏)**：位于页面最顶端，贯穿整个页面宽度。
- **Sidebar (侧边栏)**：位于页面左侧，处于 Header 下方，占据剩余高度。
- **SubHeader (次级顶部栏)**：位于 Sidebar 右侧，紧接 Header 下方。
- **Content (内容区域)**：位于 SubHeader 下方，Sidebar 右侧，占据剩余空间。

```
+---------------------------------------------------------------+
|                            Header                             |
|                  (Height: 40px, Width: Fill)                  |
+--------------------------+------------------------------------+
|                          |             SubHeader              |
|         Sidebar          |     (Height: 80px, Width: Fill)    |
|      (Width: 280px,      +------------------------------------+
|       Height: Fill)      |                                    |
|                          |              Content               |
|                          |          (Width: Fill,             |
|                          |           Height: Fill)            |
|                          |                                    |
+--------------------------+------------------------------------+
```

## 2. 详细尺寸规范

| 组件名称 | 宽度 (Width) | 高度 (Height) | 备注 |
| :--- | :--- | :--- | :--- |
| **Header** | **响应式 (Fill)** | 固定 **40px** | 顶部通栏 |
| **Sidebar** | 固定 **280px** | **响应式 (Fill)** | 左侧，Header下方 |
| **SubHeader**| **响应式 (Fill)** | 固定 **80px** | 内容区顶部 |
| **Content** | **响应式 (Fill)** | **响应式 (Fill)** | 剩余空间 |

## 3. 实现建议 (Reference)

HTML/CSS 结构建议采用 Flexbox 布局：

1.  **外层容器**：`flex-direction: column; height: 100vh;`
    *   **Header**: `height: 40px;` （必须严格采取高优先级的 `header` 组件模板及样式架构）
    *   **Main Body (Wrapper)**: `flex: 1; display: flex; flex-direction: row;`
        *   **Sidebar**: `width: 280px;` （必须严格采取高优先级的 `sidebar` 组件模板及深层联通交互架构）
        *   **Right Column**: `flex: 1; display: flex; flex-direction: column;`
            *   **SubHeader**: `height: 80px;`
            *   **Content**: `flex: 1;`

【🚨 高优先级结构要求】：
任何有关 Header 和 Sidebar 的装配操作属于最高优先级，**必须每次渲染整页时**，严格调用读取其专门沉淀的模板代码（`header/sidebar-tem.html`）或协议文件（`header.md`/`sidebar.md`），保证这类外围框架型组件全局极度一致，不可在页面生成中自由发挥删减其架构细节。

请确保所有页面生成任务均符合此布局结构标准及依赖。

## 4. 卡片工作台布局架构 (Card Workbench Layout)

该布局专为工作台卡片页面设计，打破了传统标准的上下/左右弹性布局结构，采用固定画布（宽 1920px、最小高 1080px）上的绝对定位（`position: absolute`）策略，呈现丰富的多列浮动层级视觉体系。

### 4.1 核心结构与关系

布局由五个主要绝对定位部分组成：

- **Outer Wrapper (`.workbench-layout`)**: `width: 1920px; min-height: 1080px; position: relative; overflow: hidden;`，并通常承载 3D 渲染背景装饰图（`.bg-decoration`，如 `left: 939px; top: 20px;`）。
- **Header (`.devui-header`)**: 宽 `100%`，高 `48px`，顶部对齐 `top: 0; left: 0; z-index: 1000;`。
- **Left Sidebar (`.left-sidebar`)**: 宽 `248px`，距离左侧与顶部有明确悬浮间距：`left: 15px; top: 80px;`。
- **Main Content (`.main-content`)**: 宽 `1175px`，占据主要视觉中心：`left: 287px; top: 40px;`。
- **Right Sidebar (`.right-sidebar`)**: 宽 `384px`，右侧悬浮面板区：`left: 1487px; top: 76px;`。

```text
+------------------------------------------------------------------------------------------------+
|                                    Header (Height: 48px, Top: 0)                               |
+------------------------------------------------------------------------------------------------+
|                      |                                                  |                      |
|  Left Sidebar        |                  Main Content                    |  Right Sidebar       |
|  (Width: 248px,      |                  (Width: 1175px,                 |  (Width: 384px,      |
|   Left: 15px,        |                   Left: 287px,                   |   Left: 1487px,      |
|   Top: 80px)         |                   Top: 40px)                     |   Top: 76px)         |
|                      |                                                  |                      |
|                      |                                                  |                      |
+----------------------+--------------------------------------------------+----------------------+
```

### 4.2 区域组件构成建议

1. **Main Content (`.main-content`)**: 
   - 包含主旨横幅区（`.welcome-banner-area`，内部如 `.recent-visits-row` 提供胶囊卡片）。
   - 包含核心功能网格区（`.projects-section`，内部包括多形态视图切换、筛选标签组以及 `.project-grid` 三列瀑布流卡片阵列）。
2. **Right Sidebar (`.right-sidebar`)**: 
   - 内部按垂直流（`flex-direction: column; gap: 16px;`）挂载多个业务面板卡片，如带有明确统一样式定义的 `.devui-announcementCard`, `.devui-activityCard`, `.devui-helpDocCard` 等。
3. **视觉层面特征**: 卡片式页面通常采用较大的模块圆角（如 `8px`/`16px`），统一且层次分明的轻薄阴影（如 `0 1px 6px 0 rgba(0, 0, 0, 0.08)`），以及明显的模块间白底悬浮感。
