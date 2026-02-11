# Role: Icon Usage (图标使用规范)

[Metadata]
- **Role Name**: Icon Role
- **Root Directory**: `icon/miniDev-icon/`
- **Primary Source**: `icon/miniDev-icon/action/` (Operation Icons)
- **File Type**: SVG
- **Version**: v1.1

## Core Rule: Source of Truth
**所有 HTML 生成中的图标资源，必须严格从 `icon/miniDev-icon/` 及其子目录中选取。**

- **Primary Location**: 大多数功能性图标 (Search, Close, Delete, Settings etc.) 位于 `icon/miniDev-icon/action/`。
- **Naming Note**: 文件名多为中文或“中文(english)”格式。
    - Search -> `icon/miniDev-icon/action/搜索.svg`
    - Close -> `icon/miniDev-icon/action/close.svg` 或 `icon/miniDev-icon/action/清除.svg`
    - Settings -> `icon/miniDev-icon/action/设置.svg`
    - Check -> `icon/miniDev-icon/action/已选.svg`
- **Action**: 若不确定文件名，需先使用 `find` 或 `list_dir` 确认文件存在，禁止猜测路径。

## Core Rule: Dimension Control (尺寸严格定义)
**图标尺寸必须严格遵循用户需求或组件设计规范。**

1.  **User Defined**: 若用户在 Prompt 中指定尺寸 (e.g. "use 20px icons")，**必须**显式设置 CSS 宽高为 `20px`。
2.  **Component Skill**: 若用于特定组件，遵循组件文档 (e.g. Button sm=12px, md=16px)。
3.  **Strict Enforcement**: 
    - ❌ 禁止使用 `width: auto`。
    - ✅ 必须使用 `width: [size]px; height: [size]px;`。

## Usage Pattern (使用模式)

### 1. Img Tag (General Use)
```html
<!-- Example: Search Icon (Size: Strict 16px) -->
<!-- 注意：路径需根据实际文件结构调整 -->
<img src="icon/miniDev-icon/action/搜索.svg" class="devui-icon-search" alt="search" />

<style>
.devui-icon-search {
  width: 16px; /* User strict requirement */
  height: 16px;
  display: block;
}
</style>
```

### 2. Background Image (Inputs / Decor)
```css
.devui-input-icon {
  width: 16px;
  height: 16px;
  /*引用本地路径*/
  background-image: url('icon/miniDev-icon/action/搜索.svg');
  background-size: 100% 100%; /* Ensure strict fit */
  background-repeat: no-repeat;
}
```

## Audit Checklist (生成前自检)
1.  **Path Valid**: 路径是否真实存在？(e.g. 是 `搜索.svg` 还是 `search.svg`?)
2.  **Size Strict**: `width/height` 是否已显式写入 CSS？
3.  **Source Compliance**: 是否使用了 `icon/miniDev-icon` 下的资源？
