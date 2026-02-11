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
    *   **Header**: `height: 40px;`
    *   **Main Body (Wrapper)**: `flex: 1; display: flex; flex-direction: row;`
        *   **Sidebar**: `width: 280px;`
        *   **Right Column**: `flex: 1; display: flex; flex-direction: column;`
            *   **SubHeader**: `height: 80px;`
            *   **Content**: `flex: 1;`

请确保所有页面生成任务均符合此布局结构。
