# Theme Skill (主题规范)

该文档定义了 DevUI 主题颜色 Token。Agent 在生成代码时，**必须**使用 Token 名称而非硬编码的 Hex 值，以确保主题一致性和可维护性。

## Brand Colors

| Token Name | Hex Value | Sample |
| :--- | :--- | :--- |
| `devui-brand` | `#5E7CE0` | <div style='background-color:#5E7CE0; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-brand-foil` | `#859BFF` | <div style='background-color:#859BFF; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-brand-hover` | `#7693F5` | <div style='background-color:#7693F5; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-brand-active` | `#526ECC` | <div style='background-color:#526ECC; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-brand-active-focus` | `#344899` | <div style='background-color:#344899; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |


## Background Colors

| Token Name | Hex Value | Sample |
| :--- | :--- | :--- |
| `devui-global-bg` | `#F5F5F5` | <div style='background-color:#F5F5F5; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-glass-morphism-bg` | `#F5F6F8` | <div style='background-color:#F5F6F8; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-global-bg-normal` | `#FFFFFF` | <div style='background-color:#FFFFFF; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-base-bg` | `#FFFFFF` | <div style='background-color:#FFFFFF; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-base-bg-dark` | `#333854` | <div style='background-color:#333854; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-block` | `#FFFFFF` | <div style='background-color:#FFFFFF; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-area` | `#F8F8F8` | <div style='background-color:#F8F8F8; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-icon-bg` | `#FFFFFF` | <div style='background-color:#FFFFFF; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-form-control-bg` | `#FFFFFF` | <div style='background-color:#FFFFFF; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-list-item-active-bg` | `#5E7CE0` | <div style='background-color:#5E7CE0; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-list-item-active-hover-bg` | `#526ECC` | <div style='background-color:#526ECC; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-list-item-hover-bg` | `#F2F5FC` | <div style='background-color:#F2F5FC; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-list-item-selected-bg` | `#E9EDFA` | <div style='background-color:#E9EDFA; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-list-item-strip-bg` | `#F2F5FC` | <div style='background-color:#F2F5FC; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-disabled-bg` | `#F5F5F6` | <div style='background-color:#F5F5F6; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-label-bg` | `#EEF0F5` | <div style='background-color:#EEF0F5; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-connected-overlay-bg` | `#FFFFFF` | <div style='background-color:#FFFFFF; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-fullscreen-overlay-bg` | `#FFFFFF` | <div style='background-color:#FFFFFF; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-feedback-overlay-bg` | `#464D6E` | <div style='background-color:#464D6E; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-gray-form-control-bg` | `#F5F5F5` | <div style='background-color:#F5F5F5; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-gray-form-control-hover-bg` | `#EBEBEB` | <div style='background-color:#EBEBEB; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-nav-expand-bg` | `#FBFBFC` | <div style='background-color:#FBFBFC; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-embed-search-bg` | `#F2F5FC` | <div style='background-color:#F2F5FC; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-embed-search-bg-hover` | `#EEF0F5` | <div style='background-color:#EEF0F5; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-float-block-shadow` | `#5E7CE0` | <div style='background-color:#5E7CE0; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-range-item-hover-bg` | `#E9EDFA` | <div style='background-color:#E9EDFA; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-danger-bg` | `#FFEEED` | <div style='background-color:#FFEEED; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-warning-bg` | `#FFF3E8` | <div style='background-color:#FFF3E8; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-info-bg` | `#F2F5FC` | <div style='background-color:#F2F5FC; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-success-bg` | `#EDFFF9` | <div style='background-color:#EDFFF9; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-primary-bg` | `#F2F5FC` | <div style='background-color:#F2F5FC; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-default-bg` | `#F3F6F8` | <div style='background-color:#F3F6F8; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |


## Text Colors

| Token Name | Hex Value | Sample |
| :--- | :--- | :--- |
| `devui-text` | `#252B3A` | <div style='background-color:#252B3A; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-text-weak` | `#575D6C` | <div style='background-color:#575D6C; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-aide-text` | `#8A8E99` | <div style='background-color:#8A8E99; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-aide-text-hover` | `#252B3A` | <div style='background-color:#252B3A; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-aide-text-stress` | `#575D6C` | <div style='background-color:#575D6C; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-placeholder` | `#8A8E99` | <div style='background-color:#8A8E99; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-light-text` | `#FFFFFF` | <div style='background-color:#FFFFFF; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-dark-text` | `#252B3A` | <div style='background-color:#252B3A; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-link` | `#526ECC` | <div style='background-color:#526ECC; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-link-active` | `#344899` | <div style='background-color:#344899; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-link-light` | `#96ADFA` | <div style='background-color:#96ADFA; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-link-light-active` | `#BECCFA` | <div style='background-color:#BECCFA; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-icon-text` | `#252B3A` | <div style='background-color:#252B3A; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-list-item-active-text` | `#FFFFFF` | <div style='background-color:#FFFFFF; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-list-item-hover-text` | `#526ECC` | <div style='background-color:#526ECC; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-disabled-text` | `#ADB0B8` | <div style='background-color:#ADB0B8; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-feedback-overlay-text` | `#DFE1E6` | <div style='background-color:#DFE1E6; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |


## Status Colors

| Token Name | Hex Value | Sample |
| :--- | :--- | :--- |
| `devui-danger` | `#F66F6A` | <div style='background-color:#F66F6A; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-warning` | `#FAC20A` | <div style='background-color:#FAC20A; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-waiting` | `#9FAAD7` | <div style='background-color:#9FAAD7; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-success` | `#50D4AB` | <div style='background-color:#50D4AB; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-info` | `#5E7CE0` | <div style='background-color:#5E7CE0; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-danger-line` | `#F66F6A` | <div style='background-color:#F66F6A; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-warning-line` | `#FA9841` | <div style='background-color:#FA9841; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-info-line` | `#5E7CE0` | <div style='background-color:#5E7CE0; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-success-line` | `#50D4AB` | <div style='background-color:#50D4AB; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |


## Border/Line Colors

| Token Name | Hex Value | Sample |
| :--- | :--- | :--- |
| `devui-line` | `#ADB0B8` | <div style='background-color:#ADB0B8; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-dividing-line` | `#DFE1E6` | <div style='background-color:#DFE1E6; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-form-control-line` | `#ADB0B8` | <div style='background-color:#ADB0B8; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-form-control-line-hover` | `#575D6C` | <div style='background-color:#575D6C; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-form-control-line-active` | `#5E7CE0` | <div style='background-color:#5E7CE0; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-form-control-interactive-outline` | `#5E7CE0` | <div style='background-color:#5E7CE0; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-form-control-line-active-hover` | `#344899` | <div style='background-color:#344899; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-disabled-line` | `#DFE1E6` | <div style='background-color:#DFE1E6; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-connected-overlay-line` | `#526ECC` | <div style='background-color:#526ECC; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-primary-line` | `#5E7CE0` | <div style='background-color:#5E7CE0; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-default-line` | `#5E7CE0` | <div style='background-color:#5E7CE0; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |


## Shadow Colors

| Token Name | Hex Value | Sample |
| :--- | :--- | :--- |
| `devui-shadow` | `#000000` | <div style='background-color:#000000; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-light-shadow` | `#000000` | <div style='background-color:#000000; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-connected-overlay-shadow` | `#000000` | <div style='background-color:#000000; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-feedback-overlay-shadow` | `#000000` | <div style='background-color:#000000; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-hover-shadow` | `#000000` | <div style='background-color:#000000; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-table-column-shadow-color` | `#252B3A` | <div style='background-color:#252B3A; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |


## Other Colors

| Token Name | Hex Value | Sample |
| :--- | :--- | :--- |
| `devui-contrast` | `#C7000B` | <div style='background-color:#C7000B; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-initial` | `#E9EDFA` | <div style='background-color:#E9EDFA; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-unavailable` | `#F5F5F6` | <div style='background-color:#F5F5F6; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-feedback-overlay-backdrop` | `#000000` | <div style='background-color:#000000; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-icon-fill` | `#252B3A` | <div style='background-color:#252B3A; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-icon-fill-weak` | `#BABBC0` | <div style='background-color:#BABBC0; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-icon-fill-hover` | `#5E7CE0` | <div style='background-color:#5E7CE0; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-icon-fill-active` | `#5E7CE0` | <div style='background-color:#5E7CE0; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-icon-fill-active-hover` | `#526ECC` | <div style='background-color:#526ECC; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-shape-icon-fill` | `#D7D8DA` | <div style='background-color:#D7D8DA; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-shape-icon-fill-active` | `#BABBC0` | <div style='background-color:#BABBC0; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-shape-icon-fill-hover` | `#BABBC0` | <div style='background-color:#BABBC0; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-shape-icon-fill-disabled` | `#F5F5F5` | <div style='background-color:#F5F5F5; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-primary-disabled` | `#BECCFA` | <div style='background-color:#BECCFA; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-icon-fill-active-disabled` | `#BECCFA` | <div style='background-color:#BECCFA; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-highlight-overlay` | `#FFFFFF` | <div style='background-color:#FFFFFF; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-primary` | `#5E7CE0` | <div style='background-color:#5E7CE0; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-primary-hover` | `#7693F5` | <div style='background-color:#7693F5; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-primary-active` | `#344899` | <div style='background-color:#344899; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-contrast-hover` | `#D64A52` | <div style='background-color:#D64A52; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-contrast-active` | `#B12220` | <div style='background-color:#B12220; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |
| `devui-icon-active-color` | `#FFFFFF` | <div style='background-color:#FFFFFF; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |

