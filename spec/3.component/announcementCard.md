# Spec: AnnouncementCard

[Metadata]
- **Component**: `d-announcementCard`
- **Template Source**: `spec/4.template/announcementCard-tem.html`

## 2. Content Presentation (内容呈现)
描述不同类型的数据应如何组装 HTML：

### 2.1 Default Card Structure
-   Scenario: Used for displaying system announcements, news, or updates in a card format.
-   Structure:
    ```html
    <div class="devui-announcementCard">
        <div class="devui-announcement-content">
            <div class="devui-announcement-title">{{title}}</div>
            <div class="devui-announcement-info">
                <div class="devui-announcement-desc">{{description}}</div>
                <div class="devui-announcement-meta">{{time}}</div>
            </div>
        </div>
        <div class="devui-announcement-indicators">
            <!-- Indicator items -->
            <div class="devui-indicator active"></div>
            <div class="devui-indicator"></div>
            ...
        </div>
    </div>
    ```

## 5. Dynamic Response (动态响应)
-   **Text Overflow**:
    -   Title: 支持换行呈现。
    -   Description (`.devui-announcement-desc`): 超过 3 行的部分使用省略号截断（`-webkit-line-clamp: 3`），固定高度为 66px 保持卡片高度不受极少短文案影响塌陷。
    
## 3. Visual Spec (视觉规范)

### 3.1 Interaction States (交互状态)
-   **Indicators**: 顶部的分页/轮播指示器 `.devui-indicator` 默认状态呈点状（宽 4px，灰 `var(--devui-shape-icon-fill)`），激活状态（追加 `.active` 类）呈线状（宽 32px，深色 `var(--devui-icon-text)`）。

## 6. Template Injection (模版注入)
-   **{{title}}**: 公告的标题文本。
-   **{{description}}**: 公告的详情描述文字。
-   **{{time}}**: 公告发布的时间戳或提示元信息。
-   **{{indicators}}**: 分页/轮播指示器的 HTML 结构注入。
