# Spec: HeadInfo (头信息组件)

[Metadata]
- **Component**: `d-headinfo`
- **Template Source**: `spec/4.template/headinfo-tem.html`
- **Benchmark Source**: `HistoryRender/component/headinfo/benchmark.html`

## 2. Content Presentation (内容呈现)
描述头信息（HeadInfo）组件如何组装 HTML 结构并展示：

### 2.1 Shell Container
- Structure:
  ```html
  <div class="devui-headinfo-container">
      {{backButton}}
      {{logo}}
      {{mainContent}}
  </div>
  ```
- **Component Height**: 固定为 `48px`。
- **Layout**: Flexbox，横向排列。

### 2.2 Back Button & Logo
- **Back Button**: 
  - `24x24px` 居中容器。
  - 内置一个 `20x20px` 图标（使用 CSS `-webkit-mask-image` 配合 `back.svg` 加载，跟随 `var(--devui-text)` 变色）。
- **Logo**: 
  - `48x48px` 容器，`8px` 圆角。
  - 带有一层极浅的内发光阴影以区分白色背景：`box-shadow: inset 0 0 0 1px #FEE1E7`。
  - 容器内部容纳 `<img>` 或内联 SVG 的无缝撑放。
  - **🚨 规则增强：** 如果从设计稿提取内容获取到图像/矢量信息，**必须**完整映射对应的 `data:image/svg+xml` 或者真实 `src` 值。如果没有真实 Logo，使用预设的项目占位图进行兜底，如 `icon/miniDev-icon/project-initial/P-48x48.svg`。**绝对禁止自行编写使用 `<text>` 标签组成的假 SVG Logo 进行糊弄。**

### 2.3 Main Content (Texts and Badges)
文本主内容在垂直方向被切分为上下两行，共同占据 `48px` 高度：
- **Row 1 (Title Group & Badges)**: 
  - 行高限制为 `28px`，`flex` 居中对齐。
  - `Brand` 前缀品牌名：字号 `20px`，字重 `400`，颜色 `var(--devui-text-weak)`。
  - `Slash` 分隔斜杠：字形 `20px / 300`，左右存在 `4px` 边距。
  - `Name` 核心名字：字号 `20px`，字重 `700` (Bold)，颜色 `var(--devui-text)`。
  - `Caret` 下拉倒三角：与文字同行，位于名字右侧，`14x14px` 尺寸（`chevron-down.svg` mask呈现）。
  - `Badges` 徽章盒子：与标题组间距 `14px`，容器内标签遵循 `8px` 间距。支持复合代码健康度 Badge，或浅色的普通 Tag。

- **Row 2 (Metadata)**: 
  - 行高限制为 `20px`，一般用于放置 Repository ID 等次要元数据。
  - `MetaText` 元数据说明：字号 `14px`，颜色 `var(--devui-placeholder)`。

## 5. Dynamic Response (动态响应)
- **Text Overflow (文本防崩塌打点截断)**:
  - 为了应对极端的长文本溢出场景，`.devui-headinfo-main` 及其子级的 Flex 容器（`.devui-headinfo-row1`, `.devui-headinfo-row2`, `.devui-headinfo-title-group`）必须设置 `min-width: 0;`。
  - 需要被截断打点的各个文本元器件包含 `.devui-text-brand`, `.devui-text-name`, `.devui-text-meta`，均必须声明完整的 CSS 截断样式：
    ```css
    overflow: hidden; 
    text-overflow: ellipsis;
    white-space: nowrap;
    ```
  - 当整行空间被大幅度挤压时，具有 `min-width: 0` 的外部容器会强制允许这些文字内部进行 `...` 省略处理，同时需要注意不要挤压最右侧固定尺寸的 `.devui-headinfo-caret` 和后面的徽标数组（对于徽章区域需要设定 `flex-shrink: 0` 保护）。
- **Empty Constraints (空状态占位)**:
  - 当 `Badges` 为空的时候，包含它的 `.devui-headinfo-badges` 元素应直接去除占位或为空即可，剩余元素将自动补充空白区间。

## 6. Template Injection (模版注入)
用于生成 `.html` 时所需注入的参数集合：
- **{{logoSrc}}**: Logo 的完整图片或内联 SVG 内容地址。
- **{{brand}}**: 第一行斜线前所修饰的归属者品牌名称（如示例中的 "huawei"）。
- **{{name}}**: 第一行斜线后代表主体的粗体库/项目名称（如示例中的 "Sample"）。
- **{{badges}}**: （可选）完整的标签 HTML 字符串组装内容。
- **{{meta}}**: （可选）第二行的深色副标题文字细节（如 "Repository ID: 123456"）。
