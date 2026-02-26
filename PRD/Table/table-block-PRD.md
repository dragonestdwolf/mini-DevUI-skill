# PRD: Table Block (表格区域)
**Version**: v1.0
**Source**: User Design Image (Step 192)

## 1. Table Block Overview (表格区域概述)
The Table Block is a core data management interface displaying a list of items (e.g., Stories, Bugs) with rich filtering, sorting, and operational capabilities. It features a toolbar for view management and creation, a data table with status indicators and tags, and a pagination control.

## 2. Layout Structure (布局结构)
The page follows a standard Vertical Stack layout:
1.  **Toolbar (Top)**: Controls for view switching, creation, and global search.
2.  **Table (Middle)**: Data grid displaying records.
3.  **Pagination (Bottom)**: Navigation for large datasets.

## 3. Component Specification (组件详情)

### 3.1 Toolbar Area (工具栏区域)
Located at the top of the page.
*   **Left Section**:
    *   **View Filter**: A dropdown or selector triggered by "全部" (All) with a down arrow icon.
        *   *Function*: Filters the scope of items displayed.
    *   **Tab Switcher**: Text-based tabs "Backlog" (Active/Underlined) and "缺陷" (Defects).
        *   *Component*: `d-tabs` (Type: `pills` or `underline`).
        *   *Active State*: Bold text with bottom border/indicator.
*   **Middle Section**:
    *   **Create Button**: Primary blue button "+ 新建" (New).
        *   *Component*: `d-button` (Type: `primary`, Icon: `add.svg`).
    *   **Quick Filter**: Dropdown "临时过滤" (Temporary Filter).
        *   *Component*: `d-dropdown` or `d-select` trigger.
*   **Right Section**:
    *   **Category Search**: A complex search bar.
        *   *Component*: `d-category-search`.
        *   *Content*:
            *   **Icon**: Search icon (Left).
            *   **Tags**: "类型: Story | Task | Bug" (Removable), "状态: 新建 | 进行中..." (Removable).
            *   **Input**: Placeholder "点击此处输入关键词或添加筛选条件".
            *   **Actions**: Clear (x), Save Filter, Directory/Folder icons.
    *   **Action Icons**:
        *   **Settings**: Table settings icon.
        *   **More**: Vertical/Horizontal dots for more options.
    *   **View Toggle**: Toggle between List View and Board View.
        *   *Component*: Radio group or Toggle button style.

### 3.2 Data Table (数据表格)
Main content area.
*   **Component**: `d-table`.
*   **Columns**:
    1.  **Checkbox**: Multi-select row.
    2.  **编号 (ID)**: Text + Sort Icon.
    3.  **标题 (Title)**:
        *   *Content*: Icon (Square/Tree toggle?) + Text + Sort Icon.
        *   *Note*: Shows hierarchy or type?
    4.  **结束时间 (End Date)**: Text ("--") + Sort Icon.
    5.  **状态 (Status)**: Text ("新建") + Filter Icon + Sort Icon.
    6.  **处理人 (Assignee)**: User/Avatar + Text + Filter Icon + Sort Icon.
    7.  **预计开始日期 (Est. Start)**: Text ("--") + Sort Icon.
    8.  **预计结束日期 (Est. End)**: Text ("--") + Sort Icon.
    9.  **优先级 (Priority)**:
        *   *Component*: Flag Icon (Orange/Red) + Text ("中", "高").
        *   *Icon*: `flag.svg` (Color-coded).
    10. **操作 (Actions)**:
        *   *Icons*: Star (Follow), Split View/Detail, More Actions.
        *   *Hover*: Tooltips on hover.

### 3.3 Pagination (分页)
Located at the bottom right.
*   **Component**: `d-pagination`.
*   **Elements**:
    *   **Size Changer**: Dropdown "15 条/页".
    *   **Total Count**: Text "条/页，总条数: 8".
    *   **Navigation**:
        *   **Prev**: `<` Button (Disabled).
        *   **Pages**: "1" (Active).
        *   **Next**: `>` Button (Disabled).
    *   **Jump**: "跳至" Input "页".

## 4. Visual Styles (视觉样式)
*   **Tags**:
    *   **Feature/Story**: Green background, White text.
    *   **Bug**: Orange background, White text.
*   **Colors**:
    *   **Primary**: Blue (`#5E7CE0`).
    *   **Text**: Dark Grey (`#252B3A`).
    *   **Border**: Light Grey (`#DFE1E6`).
*   **Icons**:
    *   All icons must use **Relative Paths** (`../../../icon/...`) as per `icon_role.md`.
    *   Size: Generally 16x16px.

## 5. Interaction Flows (交互流程)
*   **Hover**: Rows highlight on hover (`#F2F5FC`).
*   **Click**: Clicking a row (except checkbox/actions) might open a detail view.
*   **Sort/Filter**: Clicking header icons triggers sorting or opens a filter menu.
