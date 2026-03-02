# Spec: Select 选择框

[Metadata]
- **Component**: `d-select`
- **Template Source**: `spec/4.template/select-tem.html`
- **Figma Source**: Node `431:4454` (选择框 Select), `578:4417` (表单项-下拉选择框)

## 1. Content Presentation (内容呈现格式)
描述 Select 选择框及其下拉面板的不同呈现状态和内部元素组装方式。

### 1.1 Standard Select Input (标准选择框输入区)
-   **Scenario**: 默认状态下展示占位符或已选值的输入框区域，右侧常驻下拉箭头。
-   **Structure**:
    ```html
    <div class="devui-select-input">
        <div class="devui-select-placeholder">{{placeholder | value}}</div>
        <div class="devui-select-arrow"></div>
    </div>
    ```

### 1.2 Dropdown Panel (下拉面板容器)
-   **Scenario**: 激活状态下展开的浮层，包含选项列表。
-   **Structure**:
    ```html
    <div class="devui-select-dropdown">
        <!-- Options injected here -->
    </div>
    ```
-   **Style**: 需要具备标准的 `0px 4px 12px 0px rgba(0,0,0,0.16)` 浅色容器阴影。

### 1.3 Single-Select Option (单选选项文本)
-   **Scenario**: 列表内最基础的纯文本单选项。
-   **Structure**:
    ```html
    <div class="devui-select-option {{selected class}}">
        <span class="devui-select-option-text">{{text}}</span>
    </div>
    ```

### 1.4 Multi-Select Option with Checkbox (多选带复选框选项)
-   **Scenario**: 用于多选模式，左侧带有一个勾选框。
-   **Structure**:
    ```html
    <div class="devui-select-option {{selected class}}">
        <div class="devui-select-checkbox"></div>
        <span class="devui-select-option-text">{{text}}</span>
    </div>
    ```
-   **Interaction Details**: 选中状态下，复选框变为 `var(--devui-constant-blue)` 底色并浮现对号。

## 2. Interaction States (交互状态描述)

### 2.1 Select Input States
-   **Hover**: 边框色变深，对应 `var(--devui-form-control-line-hover)`。
-   **Active / Focus**: 边框变为主题蓝 `var(--devui-constant-blue)`，外延附加 4px 的半透明光效晕染层阴影 `box-shadow: 0 0 0 4px var(--devui-form-control-line-rippling)`，且右侧 Chevron 箭头**旋转 180 度**。
-   **Disabled**: 置灰处理。背景变为 `var(--devui-disabled-fill-bg)`，边框变为 `var(--devui-disabled-line)`，光标设为 `not-allowed`。占位文本变浅色。

### 2.2 Dropdown Option States
-   **Hover**: 选项背景色变为 `var(--devui-list-item-hover-bg)`。
-   **Selected**: 单选状态下文本可突显为主题色；多选状态下复选框点亮。
-   **Disabled**: 选项本身可独立置灰，文本呈现为 `var(--devui-placeholder)`，复选框填充失效底色。

## 3. Dynamic Response (动态响应)
-   **Text Overflow (选值溢出)**: 当用户选择的文本过长时，必须在 `.devui-select-placeholder`（或 `.devui-select-value`）及 `.devui-select-option-text` 中执行 `overflow: hidden; text-overflow: ellipsis; white-space: nowrap;` 防抖截断截断。
-   **Panel Positioning**: 下拉面板应默认附着于输入框底部并预留 4px 的 `margin-top`。

## 4. Template Injection (模版注入契约)
-   **{{placeholder}}**: "请选择" 或已选择的文本文案。
-   **{{status}}**: 'default' | 'hover' | 'focus' | 'disabled' (控制输入框状态)。
-   **{{dropdown_visible}}**: 'hidden' | '' 控制下拉面板是否出现。
-   **{{dropdown_content}}**: 注入 1.3/1.4 章节描述的列表项结构。
