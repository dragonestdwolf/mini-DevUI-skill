import json
import os

# Configuration
INPUT_FILE = '/Users/renyuqing/Desktop/2026/miniDevUI/AI-MiniDevUI/skill/2.theme/devui-light-theme.tokens.json'
OUTPUT_FILE = '/Users/renyuqing/Desktop/2026/miniDevUI/AI-MiniDevUI/skill/2.theme/theme.md'

def main():
    with open(INPUT_FILE, 'r') as f:
        data = json.load(f)

    # Categories to sort tokens into
    categories = {
        'Brand': [],
        'Background': [],
        'Text': [],
        'Status': [],
        'Border/Line': [],
        'Shadow': [],
        'Other': []
    }

    # Filter out metadata keys like $extensions
    tokens = {k: v for k, v in data.items() if not k.startswith('$')}

    for name, token in tokens.items():
        # Ensure it has a value and hex
        if '$value' not in token or 'hex' not in token['$value']:
            continue
        
        hex_val = token['$value']['hex']
        
        # Categorization logic based on name
        if 'brand' in name:
            categories['Brand'].append((name, hex_val))
        elif 'bg' in name or 'area' in name or 'block' in name:
            categories['Background'].append((name, hex_val))
        elif 'text' in name or 'link' in name or 'placeholder' in name:
            categories['Text'].append((name, hex_val))
        elif any(x in name for x in ['danger', 'warning', 'success', 'info', 'waiting']):
            categories['Status'].append((name, hex_val))
        elif 'line' in name or 'border' in name:
            categories['Border/Line'].append((name, hex_val))
        elif 'shadow' in name:
            categories['Shadow'].append((name, hex_val))
        else:
            categories['Other'].append((name, hex_val))

    # Generate Markdown content
    content = []
    content.append("# Theme Skill (主题规范)\n")
    content.append("该文档定义了 DevUI 主题颜色 Token。Agent 在生成代码时，**必须**使用 Token 名称而非硬编码的 Hex 值，以确保主题一致性和可维护性。\n")
    
    for category, items in categories.items():
        if not items:
            continue
        
        content.append(f"## {category} Colors\n")
        content.append("| Token Name | Hex Value | Sample |")
        content.append("| :--- | :--- | :--- |")
        
        for name, hex_val in items:
            # Add a small color box using HTML if supported, or just the code
            # Using inline code for clarity
            content.append(f"| `{name}` | `{hex_val}` | <div style='background-color:{hex_val}; width: 20px; height: 20px; border: 1px solid #ddd;'></div> |")
        
        content.append("\n")

    # Write to file
    with open(OUTPUT_FILE, 'w') as f:
        f.write("\n".join(content))
    
    print(f"Successfully generated {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
