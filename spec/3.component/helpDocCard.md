# Spec: HelpDocCard

[Metadata]
- **Component**: `d-helpDocCard`
- **Template Source**: `spec/4.template/helpDocCard-tem.html`

## 2. Content Presentation (内容呈现)
描述不同类型的数据应如何组装 HTML：

### 2.1 Help Document Navigation Grid
-   Scenario: Used for portal dashboards to provide quick jump links to various documentation centers, tutorials, or frequently used resources.
-   Structure:
    ```html
    <div class="devui-helpDocCard">
        <div class="devui-helpDoc-header">
            <div class="devui-helpDoc-title">{{cardTitle}}</div>
            <a href="{{allDocsUrl}}" class="devui-helpDoc-all-link">
                <span class="devui-helpDoc-all-text">所有文档</span>
                <span class="devui-helpDoc-all-icon"></span>
            </a>
        </div>
        <div class="devui-helpDoc-grid">
            <!-- 循环下方的单独单元格 -->
            <a href="{{docUrl}}" class="devui-helpDoc-item">
                <span class="devui-helpDoc-item-icon {{iconClass}}"></span>
                <span class="devui-helpDoc-item-label">{{docTitle}}</span>
            </a>
        </div>
    </div>
    ```

## 5. Dynamic Response (动态响应)
-   **Grid Layout**:
    -   Container (`.devui-helpDocCard`) 高度为自适应 (`hugs content`)，无需固定 `height`，依靠内部栅格内容自然撑开。
    -   子项网格 (`.devui-helpDoc-grid`) 使用 Flex `flex-wrap` 进行排版，且单个图文块宽度固定为 `86px`（对应设计稿 384 外宽下平铺显示 4 列）。超出 4 个会自动下放至第二行展示。
-   **Truncation Constraints**:
    -   图文块的主文本 (`.devui-helpDoc-item-label`) 由于外层仅分配了 `86px` 宽度的极小响应区，超出时不做断行 (`white-space: nowrap;`)，由外层容器对超出部分予以隐式裁切。

## 3. Visual Spec (视觉规范)

### 3.1 Interaction & Styling Rules (交互状态与样式强规)

### 3.2 Icon Rendering Rules (⚠️ 关键：图标调用规范)
为了确保图标系统与文本色彩联动 (依靠 `mask-image`) 和支持动态换色，所有的单元格中心 Icon 必须满足"单色防污染"规则：
1.  **禁忌 `fill` 实底色块**：严禁选取含有内置 `<rect fill="...">` 衬底、或是采用填充绘制（如 `service-2d/release.svg` 或由于带底色而致使全部染黑导致无法通过 `mask` 映射出镂空轮廓的 `action/description.svg`）的素材图标。
2.  **强制选取线性素材**：必须统一要求提供来自于 `/icon/miniDev-icon/action/` 或同类单色线性镂空图标，依靠外层给予的 `var(--devui-text)` 进行渲染。

-   **Hitbox & Cursors**:
    -   右上角 "所有文档" 包含其箭头区域是完整的 `<a>` 跳转热区，整体响应 `cursor: pointer`。
    -   每个 `86*76` 的图标图文小块均是独立的 `<a>` 可点击响应区块。

## 6. Template Injection (模版注入)
-   **{{cardTitle}}**: 卡片左上角的主标题（例如 "帮助文档"）。
-   **{{allDocsUrl}}**: 右上角 "所有文档" 的跳转 URL。
-   **{{docUrl}}**: 每个具体文档类目的子项跳转 URL。
-   **{{iconClass}}**: 为该分类绑定的具体单色 SVG icon 的 `mask` 映射类名（如预置的 `.devui-helpDoc-icon--product-intro`）。
-   **{{docTitle}}**: 每个子图文块下方的两字/四字短标题（如 "产品介绍"）。
