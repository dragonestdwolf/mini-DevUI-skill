# Spec: ActivityCard

[Metadata]
- **Component**: `d-activityCard`
- **Template Source**: `spec/4.template/activityCard-tem.html`

## 1. Content Presentation (内容呈现格式)
描述不同类型的数据应如何组装 HTML：

### 1.1 Activity Promotion Card
-   Scenario: Used for highlighting events, promotions, or primary call-to-actions within a dashboard or portal interface. Contains rich graphical backgrounds and custom typography.
-   Structure:
    ```html
    <div class="devui-activityCard">
        <div class="devui-activity-title">{{cardTitle}}</div>
        <div class="devui-activity-banner">
            <img class="devui-activity-bg-img" src="{{imageSrc}}" alt="" />
            <span class="devui-activity-badge">{{badgeText}}</span>
            <span class="devui-activity-highlight">{{highlightText}}</span>
            <div class="devui-activity-desc">{{description}}</div>
            <span class="devui-activity-arrow"></span>
        </div>
    </div>
    ```

## 2. Dynamic Response (动态响应)
-   **Text Overflow Constraints within the Banner**:
    -   `Badge Text` ("频繁"): 由于处在绝对定位中，内容不支持换行 (`white-space: nowrap`)。
    -   `Highlight Text` ("重新登录?"): 使用了 `background-clip: text` 实现渐变文字，同样不支持换行 (`white-space: nowrap`) 以防止视觉错位。
    -   `Description`: 文本区域始终不变（固定 `width: 124px`, `height: 44px`），当内容超过两行时使用带省略号的截断效果 (`-webkit-line-clamp: 2` 与 `overflow: hidden`) 进行处理，避免文字向下侵入甚至改变布局。
-   **Graphic Asset Handling**: 右侧的插图背景 `.devui-activity-bg-img` 宽度固定 (`220px`) 进行剪裁 (`object-fit: cover`)，且禁止响应任何鼠标事件 (`pointer-events: none`)以免干扰可能存在于该区域上方的点击交互。

## 3. Interaction States (交互状态描述)
-   **Banner Hitbox**: 整个 `.devui-activity-banner` 作为主要交互区域，应当具有 `cursor: pointer` 暗示其可被点击。
-   **Icons**: 右下角指示交互的指向右侧箭头，由 `arrow-left.svg` 图标经过 `rotate(180deg)` 变换而来，维持 `mask` 根据字体色随动。

## 4. Template injection (模版注入)
-   **{{cardTitle}}**: 外部卡片标题 (e.g. "活动").
-   **{{imageSrc}}**: 横幅右侧内部的 3D 悬空图片插图地址 (默认资源路径：`icon/activity-card.png`)。
-   **{{badgeText}}**: 左侧副标题前半段常规文字部分.
-   **{{highlightText}}**: 右侧紧接着的主副标题渐变色文字强调重点部分.
-   **{{description}}**: 下方用于进阶操作指引的双行描述文本.
