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

- **Outer Wrapper (`.workbench-layout`)**: `width: 1920px; min-height: 1080px; position: relative; overflow: hidden;`，通常内部承载绝对定位的缩略背景图以增强视觉层次（`z-index: 0`, `pointer-events: none`），包含：
  - 顶部右侧渐变光晕/3D装饰 (`.bg-layer-top-right`): 引用 `icon/card-bg-1.png`，样式设置为 `top: 48px; left: 0; right: 0; height: 400px; background: url('...') no-repeat center top / cover;`。
  - 左下角光晕/装饰元素 (`.bg-layer-left-bottom`): 引用 `icon/card-bg-2.png`，样式设置为 `bottom: 0; left: 0; width: 256px; height: 364px; background: url('...') no-repeat left bottom / contain;`。
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
   - ⚠️ **HTML 结构完整性强约束**: 顶部的工具条控制列（带有 Search、Filters 和 Tabs）通常采用 `display: flex; align-items: center;` 进行横向包裹。**必须绝对确保该横向排版容器标签得到完整闭合 `</div>`**。严禁发生遗漏导致下方的 `.project-grid`（多列瀑布流大模块）被意外吸入并吞并进此横向 Flex 容器内，否则将引发全局横向极致挤压、文字被迫竖排断裂等毁灭级错位失控！
2. **Right Sidebar (`.right-sidebar`)**: 
   - 内部按垂直流（`flex-direction: column; gap: 16px;`）挂载多个业务面板卡片，如带有明确统一样式定义的 `.devui-announcementCard`, `.devui-activityCard`, `.devui-helpDocCard` 等。
3. **视觉层面特征**: 卡片式页面通常采用较大的模块圆角（如 `8px`/`16px`），统一且层次分明的轻薄阴影（如 `0 1px 6px 0 rgba(0, 0, 0, 0.08)`），以及明显的模块间白底悬浮感。

## 5. 表单页布局架构 (Form Page Layout, bench-form-v3)

该布局用于“表单页”类页面，基于 `bench-form-v3.html` 提炼，采用 1920 基准画布 + 顶栏 + 左工具链导航 + 主工作区分栏结构。

### 5.1 核心结构与关系

- **Canvas (`.page`)**: `width: 1920px; height: 1080px; overflow: hidden;`
- **Header (`.devui-header`)**: 顶部通栏，`height: 40px`，需保留 `devui-header-left / devui-header-nav / devui-header-right` 语义结构。
- **Shell (`.shell`)**: `display: flex; height: calc(100% - 40px);`
- **Toolchain Sidebar (`.toolchain-sidebar`)**: 左侧工具链导航，`width: 230px; height: 1040px;`
- **Workspace (`.workspace`)**: 右侧主工作区，`width: 1690px; height: 1040px;`，再拆分为：
  - **Top (`.workspace-top`)**: 仓库信息头 + 页签区，`height: 136px`
  - **Bottom (`.workspace-bottom`)**: 设置区主体，`height: 905px`
    - **Settings Sidebar (`.settings-sidebar`)**: `width: 288px`
    - **Main Form (`.repo-settings-main`)**: `width: 1360px`

```text
+------------------------------------------------------------------------------------------------+
|                                Header (40px, full width)                                      |
+--------------+---------------------------------------------------------------------------------+
| Toolchain    | Workspace Top (136px): breadcrumb + page header + tabs                         |
| Sidebar      +--------------------------------------+------------------------------------------+
| (230px)      | Settings Sidebar (288px)             | Repo Settings Main (1360px)             |
|              | menu groups / sub-menu / active      | 3 cards: 154px / 108px / 448px          |
+--------------+--------------------------------------+------------------------------------------+
```

### 5.2 关键尺寸基线（必须对齐）

| 区域 | 尺寸 |
| :--- | :--- |
| 画布 | `1920 x 1080` |
| Header | 高 `40px` |
| 左工具链导航 | 宽 `230px` |
| Workspace | 宽 `1690px` |
| Workspace Top | 高 `136px` |
| Bottom 主体 | 高 `905px` |
| 设置侧栏 | 宽 `288px`（内部内容列 `248px`） |
| 表单主列 | 宽 `1360px` |
| 三张表单卡片 | 高 `154px / 108px / 448px` |

### 5.3 布局实现骨架（推荐）

1. 外层使用固定画布容器，避免响应式拉伸破坏像素对齐。
2. `header` 与 `shell` 采用纵向分层，`shell` 内采用横向双栏（`230 + 1690`）。
3. `workspace` 内采用上下两段（`136 + 905`），底部再采用左右两栏（`288 + 20 gap + 1360`）。
4. 表单区卡片按纵向流堆叠，卡片间距固定（`12px`），统一白底 + `8px` 圆角 + 轻阴影。

### 5.4 强约束与依赖

- Header 与 Sidebar 为高优先级框架组件，渲染时必须读取并遵循 `spec/3.component/header.md` 与 `spec/3.component/sidebar.md` 的语义结构，不可随意删减。
- 当组件 spec 与设计稿尺寸冲突时，尺寸数值以页面设计真值为准，语义结构以 spec 为准。
- 建议统一使用 `--devui-*` 变量管理颜色、边框、阴影与禁用态，避免硬编码样式扩散。
