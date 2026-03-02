# -*- coding: utf-8 -*-
"""20 个图标的定义：元数据 + 本地 SVG 文件路径。"""

from __future__ import annotations

import os
import re

# 图标 SVG 文件所在目录（相对本文件所在目录）
ICONS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons")

# 仅元数据，SVG 从 file 指向的本地文件读取
ICONS = [
    {'id': 'bell', 'name': '通知/铃铛', 'name_en': 'Bell', 'category': 'nav', 'tags': ['通知', 'bell', '消息'], 'file': 'bell.svg', 'size': [24.0, 24.0]},
    {'id': 'arrow-left', 'name': '左箭头', 'name_en': 'Arrow Left', 'category': 'nav', 'tags': ['箭头', 'arrow', '返回', '左'], 'file': 'arrow-left.svg', 'size': [16.0, 16.0]},
    {'id': 'arrow-right', 'name': '右箭头', 'name_en': 'Arrow Right', 'category': 'nav', 'tags': ['箭头', 'arrow', '下一步', '右'], 'file': 'arrow-right.svg', 'size': [16.0, 16.0]},
    {'id': 'arrow-down', 'name': '下箭头', 'name_en': 'Arrow Down', 'category': 'nav', 'tags': ['箭头', '下拉', '展开'], 'file': 'arrow-down.svg', 'size': [12.0, 6.0]},
    {'id': 'check', 'name': '勾选/完成', 'name_en': 'Check', 'category': 'status', 'tags': ['完成', 'check', '勾选', '预警'], 'file': 'check.svg', 'size': [16.0, 16.0]},
    {'id': 'circle', 'name': '圆点/待处理', 'name_en': 'Circle', 'category': 'status', 'tags': ['待处理', '圆点', '状态'], 'file': 'circle.svg', 'size': [16.0, 16.0]},
    {'id': 'more', 'name': '更多/三点', 'name_en': 'More', 'category': 'action', 'tags': ['更多', '菜单', 'more', '三点'], 'file': 'more.svg', 'size': [16.0, 16.0]},
    {'id': 'user', 'name': '用户', 'name_en': 'User', 'category': 'nav', 'tags': ['用户', 'user', '头像'], 'file': 'user.svg', 'size': [20.0, 20.0]},
    {'id': 'calendar', 'name': '日历', 'name_en': 'Calendar', 'category': 'form', 'tags': ['日历', '日期', 'calendar'], 'file': 'calendar.svg', 'size': [1.5, 14.0]},
    {'id': 'edit', 'name': '编辑', 'name_en': 'Edit', 'category': 'action', 'tags': ['编辑', 'edit', '修改'], 'file': 'edit.svg', 'size': [20.0, 20.0]},
    {'id': 'trash', 'name': '删除', 'name_en': 'Trash', 'category': 'action', 'tags': ['删除', 'trash', '移除'], 'file': 'trash.svg', 'size': [20.0, 20.0]},
    {'id': 'download', 'name': '下载', 'name_en': 'Download', 'category': 'action', 'tags': ['下载', 'download'], 'file': 'download.svg', 'size': [20.0, 20.0]},
    {'id': 'upload', 'name': '上传', 'name_en': 'Upload', 'category': 'action', 'tags': ['上传', 'upload'], 'file': 'upload.svg', 'size': [20.0, 20.0]},
    {'id': 'settings', 'name': '设置', 'name_en': 'Settings', 'category': 'nav', 'tags': ['设置', 'settings', '配置'], 'file': 'settings.svg', 'size': [20.0, 20.0]},
    {'id': 'document', 'name': '文档', 'name_en': 'Document', 'category': 'content', 'tags': ['文档', 'document', '发票'], 'file': 'document.svg', 'size': [20.0, 20.0]},
    {'id': 'chart', 'name': '图表', 'name_en': 'Chart', 'category': 'content', 'tags': ['图表', 'chart', '统计'], 'file': 'chart.svg', 'size': [20.0, 20.0]},
    {'id': 'link', 'name': '链接', 'name_en': 'Link', 'category': 'action', 'tags': ['链接', 'link', '关联'], 'file': 'link.svg', 'size': [20.0, 20.0]},
    {'id': 'filter', 'name': '筛选', 'name_en': 'Filter', 'category': 'action', 'tags': ['筛选', '过滤', 'filter'], 'file': 'filter.svg', 'size': [80.0, 80.0]},
    {'id': 'location', 'name': '定位', 'name_en': 'Location', 'category': 'action', 'tags': ['定位', '坐标', 'location'], 'file': 'location.svg', 'size': [80.0, 80.0]},
    {'id': 'dropdown', 'name': '下拉', 'name_en': 'Dropdown', 'category': 'action', 'tags': ['下拉', '展开', 'more'], 'file': 'dropdown.svg', 'size': [51.0, 51.0]},
    {'id': 'huawei_mirrors', 'name': '华为开源镜像站', 'name_en': 'Huawei Open Source Mirror', 'category': 'brand', 'tags': ['华为', '镜像', 'huawei', 'mirror'], 'file': 'huawei-mirror.svg', 'size': [80.0, 80.0]},
    {'id': 'global_nav', 'name': '全局导航新', 'name_en': 'Global Navigation New', 'category': 'navigation', 'tags': ['导航', '菜单', 'navigation'], 'file': 'global-nav.svg', 'size': [80.0, 80.0]},
    {'id': 'menu', 'name': '菜单', 'name_en': 'Menu', 'category': 'navigation', 'tags': ['菜单', '列表', 'menu'], 'file': 'menu.svg', 'size': [80.0, 80.0]},
    {'id': 'minimize', 'name': '最小化', 'name_en': 'Minimize', 'category': 'action', 'tags': ['最小化', '收起', 'minimize'], 'file': 'minimize.svg', 'size': [80.0, 80.0]},
    {'id': 'home', 'name': '首页', 'name_en': 'Home', 'category': 'navigation', 'tags': ['首页', '主页', 'home'], 'file': 'home.svg', 'size': [80.0, 80.0]},
    {'id': 'workbench', 'name': '工作台', 'name_en': 'Workbench', 'category': 'navigation', 'tags': ['工作台', '控制台', 'workbench'], 'file': 'workspace.svg', 'size': [80.0, 80.0]},
    {'id': 'efficiency_insights', 'name': '效能洞察', 'name_en': 'Efficiency Insights', 'category': 'action', 'tags': ['效能', '洞察', '数据', 'insights'], 'file': 'efficiency-insight.svg', 'size': [80.0, 80.0]},
    {'id': 'deep_thinking', 'name': '深度思考', 'name_en': 'Deep Thinking', 'category': 'action', 'tags': ['深度思考', 'AI', 'thinking'], 'file': 'deep-thinking.svg', 'size': [80.0, 80.0]},
    {'id': 'created_by_me', 'name': '我创建的', 'name_en': 'Created by Me', 'category': 'action', 'tags': ['我的', '创建', 'user'], 'file': 'my-created.svg', 'size': [80.0, 80.0]},
    {'id': 'event_trigger', 'name': '事件触发', 'name_en': 'Event Trigger', 'category': 'action', 'tags': ['触发', '事件', 'trigger'], 'file': 'event-trigger.svg', 'size': [80.0, 80.0]},
    {'id': 'search', 'name': '搜索', 'name_en': 'Search', 'category': 'action', 'tags': ['搜索', '查找', 'search'], 'file': 'search.svg', 'size': [80.0, 80.0]},
    {'id': 'sort', 'name': '排序', 'name_en': 'Sort', 'category': 'action', 'tags': ['排序', '顺序', 'sort'], 'file': 'sort.svg', 'size': [36.0, 36.0]},
    {'id': 'pipeline', 'name': '流水线', 'name_en': 'Pipeline', 'category': 'action', 'tags': ['流水线', '部署', 'pipeline'], 'file': 'pipeline.svg', 'size': [80.0, 80.0]},
    {'id': 'execute', 'name': '执行', 'name_en': 'Execute', 'category': 'action', 'tags': ['执行', '运行', 'run'], 'file': 'execute.svg', 'size': [80.0, 80.0]},
    {'id': 'service', 'name': '服务', 'name_en': 'Service', 'category': 'action', 'tags': ['服务', '模块', 'service'], 'file': 'service.svg', 'size': [80.0, 80.0]},

    {'id': 'a-48px-48px-1', 'name': 'a-48px-48px-1', 'name_en': 'A 48px 48px 1', 'category': 'action', 'tags': ['a-48px-48px-1', 'A 48px 48px 1'], 'file': 'a-48px-48px-1.svg', 'size': [80.0, 80.0]},
    {'id': 'a-48px-48px', 'name': 'a-48px-48px', 'name_en': 'A 48px 48px', 'category': 'action', 'tags': ['a-48px-48px', 'A 48px 48px'], 'file': 'a-48px-48px.svg', 'size': [80.0, 80.0]},
    {'id': 'c-48px-48px-1', 'name': 'c-48px-48px-1', 'name_en': 'C 48px 48px 1', 'category': 'action', 'tags': ['c-48px-48px-1', 'C 48px 48px 1'], 'file': 'c-48px-48px-1.svg', 'size': [80.0, 80.0]},
    {'id': 'c-48px-48px-2', 'name': 'c-48px-48px-2', 'name_en': 'C 48px 48px 2', 'category': 'action', 'tags': ['c-48px-48px-2', 'C 48px 48px 2'], 'file': 'c-48px-48px-2.svg', 'size': [80.0, 80.0]},
    {'id': 'c-48px-48px', 'name': 'c-48px-48px', 'name_en': 'C 48px 48px', 'category': 'action', 'tags': ['c-48px-48px', 'C 48px 48px'], 'file': 'c-48px-48px.svg', 'size': [80.0, 80.0]},
    {'id': 'd-48px-48px', 'name': 'd-48px-48px', 'name_en': 'D 48px 48px', 'category': 'action', 'tags': ['d-48px-48px', 'D 48px 48px'], 'file': 'd-48px-48px.svg', 'size': [80.0, 80.0]},
    {'id': 'f-48px-48px', 'name': 'f-48px-48px', 'name_en': 'F 48px 48px', 'category': 'action', 'tags': ['f-48px-48px', 'F 48px 48px'], 'file': 'f-48px-48px.svg', 'size': [80.0, 80.0]},
    {'id': 'i-48px-48px-1', 'name': 'i-48px-48px-1', 'name_en': 'I 48px 48px 1', 'category': 'action', 'tags': ['i-48px-48px-1', 'I 48px 48px 1'], 'file': 'i-48px-48px-1.svg', 'size': [80.0, 80.0]},
    {'id': 'i-48px-48px', 'name': 'i-48px-48px', 'name_en': 'I 48px 48px', 'category': 'action', 'tags': ['i-48px-48px', 'I 48px 48px'], 'file': 'i-48px-48px.svg', 'size': [80.0, 80.0]},
    {'id': 'j-48px-48px', 'name': 'j-48px-48px', 'name_en': 'J 48px 48px', 'category': 'action', 'tags': ['j-48px-48px', 'J 48px 48px'], 'file': 'j-48px-48px.svg', 'size': [80.0, 80.0]},
    {'id': 'p-32x33', 'name': 'p-32x33', 'name_en': 'P 32x33', 'category': 'action', 'tags': ['p-32x33', 'P 32x33'], 'file': 'p-32x33.svg', 'size': [76.0, 76.0]},
    {'id': 's-48px-48px-1', 'name': 's-48px-48px-1', 'name_en': 'S 48px 48px 1', 'category': 'action', 'tags': ['s-48px-48px-1', 'S 48px 48px 1'], 'file': 's-48px-48px-1.svg', 'size': [80.0, 80.0]},
    {'id': 's-48px-48px', 'name': 's-48px-48px', 'name_en': 'S 48px 48px', 'category': 'action', 'tags': ['s-48px-48px', 'S 48px 48px'], 'file': 's-48px-48px.svg', 'size': [80.0, 80.0]},
    {'id': 'z-48px-48px', 'name': 'z-48px-48px', 'name_en': 'Z 48px 48px', 'category': 'action', 'tags': ['z-48px-48px', 'Z 48px 48px'], 'file': 'z-48px-48px.svg', 'size': [80.0, 80.0]},
    {'id': 'activity', 'name': 'activity', 'name_en': 'Activity', 'category': 'action', 'tags': ['activity', 'Activity'], 'file': 'activity.svg', 'size': [80.0, 80.0]},
    {'id': 'add-node', 'name': 'add-node', 'name_en': 'Add Node', 'category': 'action', 'tags': ['add-node', 'Add Node'], 'file': 'add-node.svg', 'size': [50.0, 50.0]},
    {'id': 'api', 'name': 'api', 'name_en': 'Api', 'category': 'action', 'tags': ['api', 'Api'], 'file': 'api.svg', 'size': [80.0, 80.0]},
    {'id': 'architecture', 'name': 'architecture', 'name_en': 'Architecture', 'category': 'action', 'tags': ['architecture', 'Architecture'], 'file': 'architecture.svg', 'size': [59.0, 59.0]},
    {'id': 'archived', 'name': 'archived', 'name_en': 'Archived', 'category': 'action', 'tags': ['archived', 'Archived'], 'file': 'archived.svg', 'size': [80.0, 80.0]},
    {'id': 'artifact-repo', 'name': 'artifact-repo', 'name_en': 'Artifact Repo', 'category': 'action', 'tags': ['artifact-repo', 'Artifact Repo'], 'file': 'artifact-repo.svg', 'size': [24.0, 24.0]},
    {'id': 'background-01', 'name': 'background-01', 'name_en': 'Background 01', 'category': 'action', 'tags': ['background-01', 'Background 01'], 'file': 'background-01.svg', 'size': [1505.0, 510.0]},
    {'id': 'background-02', 'name': 'background-02', 'name_en': 'Background 02', 'category': 'action', 'tags': ['background-02', 'Background 02'], 'file': 'background-02.svg', 'size': [1920.0, 458.0]},
    {'id': 'background-03', 'name': 'background-03', 'name_en': 'Background 03', 'category': 'action', 'tags': ['background-03', 'Background 03'], 'file': 'background-03.svg', 'size': [2062.0, 515.0]},
    {'id': 'background-04', 'name': 'background-04', 'name_en': 'Background 04', 'category': 'action', 'tags': ['background-04', 'Background 04'], 'file': 'background-04.svg', 'size': [466.0, 262.0]},
    {'id': 'background-05', 'name': 'background-05', 'name_en': 'Background 05', 'category': 'action', 'tags': ['background-05', 'Background 05'], 'file': 'background-05.svg', 'size': [550.0, 309.0]},
    {'id': 'background-06', 'name': 'background-06', 'name_en': 'Background 06', 'category': 'action', 'tags': ['background-06', 'Background 06'], 'file': 'background-06.svg', 'size': [1920.0, 1080.0]},
    {'id': 'background', 'name': 'background', 'name_en': 'Background', 'category': 'action', 'tags': ['background', 'Background'], 'file': 'background.svg', 'size': [1000.0, 500.0]},
    {'id': 'best-practices', 'name': 'best-practices', 'name_en': 'Best Practices', 'category': 'action', 'tags': ['best-practices', 'Best Practices'], 'file': 'best-practices.svg', 'size': [80.0, 80.0]},
    {'id': 'code-management', 'name': 'code-management', 'name_en': 'Code Management', 'category': 'action', 'tags': ['code-management', 'Code Management'], 'file': 'code-management.svg', 'size': [24.0, 24.0]},
    {'id': 'code', 'name': 'code', 'name_en': 'Code', 'category': 'action', 'tags': ['code', 'Code'], 'file': 'code.svg', 'size': [80.0, 80.0]},
    {'id': 'continuous-delivery', 'name': 'continuous-delivery', 'name_en': 'Continuous Delivery', 'category': 'action', 'tags': ['continuous-delivery', 'Continuous Delivery'], 'file': 'continuous-delivery.svg', 'size': [24.0, 24.0]},
    {'id': 'dashboard', 'name': 'dashboard', 'name_en': 'Dashboard', 'category': 'action', 'tags': ['dashboard', 'Dashboard'], 'file': 'dashboard.svg', 'size': [24.0, 24.0]},
    {'id': 'default-project', 'name': 'default-project', 'name_en': 'Default Project', 'category': 'action', 'tags': ['default-project', 'Default Project'], 'file': 'default-project.svg', 'size': [75.0, 75.0]},
    {'id': 'defect', 'name': 'defect', 'name_en': 'Defect', 'category': 'action', 'tags': ['defect', 'Defect'], 'file': 'defect.svg', 'size': [14.996094, 14.785767]},
    {'id': 'dev-requirement', 'name': 'dev-requirement', 'name_en': 'Dev Requirement', 'category': 'action', 'tags': ['dev-requirement', 'Dev Requirement'], 'file': 'dev-requirement.svg', 'size': [16.0, 16.0]},
    {'id': 'faq', 'name': 'faq', 'name_en': 'Faq', 'category': 'action', 'tags': ['faq', 'Faq'], 'file': 'faq.svg', 'size': [80.0, 80.0]},
    {'id': 'favorite', 'name': 'favorite', 'name_en': 'Favorite', 'category': 'action', 'tags': ['favorite', 'Favorite'], 'file': 'favorite.svg', 'size': [70.0, 70.0]},
    {'id': 'feature-tree', 'name': 'feature-tree', 'name_en': 'Feature Tree', 'category': 'action', 'tags': ['feature-tree', 'Feature Tree'], 'file': 'feature-tree.svg', 'size': [16.0, 16.0]},
    {'id': 'general-reference', 'name': 'general-reference', 'name_en': 'General Reference', 'category': 'action', 'tags': ['general-reference', 'General Reference'], 'file': 'general-reference.svg', 'size': [80.0, 80.0]},
    {'id': 'ic-square-lined', 'name': 'ic-square-lined', 'name_en': 'Ic Square Lined', 'category': 'action', 'tags': ['ic-square-lined', 'Ic Square Lined'], 'file': 'ic-square-lined.svg', 'size': [74.0, 74.0]},
    {'id': 'knowledge-base', 'name': 'knowledge-base', 'name_en': 'Knowledge Base', 'category': 'action', 'tags': ['knowledge-base', 'Knowledge Base'], 'file': 'knowledge-base.svg', 'size': [20.487793, 20.487793]},
    {'id': 'link-work-item', 'name': 'link-work-item', 'name_en': 'Link Work Item', 'category': 'action', 'tags': ['link-work-item', 'Link Work Item'], 'file': 'link-work-item.svg', 'size': [80.0, 80.0]},
    {'id': 'member', 'name': 'member', 'name_en': 'Member', 'category': 'action', 'tags': ['member', 'Member'], 'file': 'member.svg', 'size': [80.0, 80.0]},
    {'id': 'merge-request', 'name': 'merge-request', 'name_en': 'Merge Request', 'category': 'action', 'tags': ['merge-request', 'Merge Request'], 'file': 'merge-request.svg', 'size': [80.0, 80.0]},
    {'id': 'my-following', 'name': 'my-following', 'name_en': 'My Following', 'category': 'action', 'tags': ['my-following', 'My Following'], 'file': 'my-following.svg', 'size': [80.0, 80.0]},
    {'id': 'original-requirement', 'name': 'original-requirement', 'name_en': 'Original Requirement', 'category': 'action', 'tags': ['original-requirement', 'Original Requirement'], 'file': 'original-requirement.svg', 'size': [16.0, 16.0]},
    {'id': 'plan-management', 'name': 'plan-management', 'name_en': 'Plan Management', 'category': 'action', 'tags': ['plan-management', 'Plan Management'], 'file': 'plan-management.svg', 'size': [16.0, 16.0]},
    {'id': 'priority-medium', 'name': 'priority-medium', 'name_en': 'Priority Medium', 'category': 'action', 'tags': ['priority-medium', 'Priority Medium'], 'file': 'priority-medium.svg', 'size': [80.0, 80.0]},
    {'id': 'product-intro', 'name': 'product-intro', 'name_en': 'Product Intro', 'category': 'action', 'tags': ['product-intro', 'Product Intro'], 'file': 'product-intro.svg', 'size': [58.0, 80.0]},
    {'id': 'project-collaboration', 'name': 'project-collaboration', 'name_en': 'Project Collaboration', 'category': 'action', 'tags': ['project-collaboration', 'Project Collaboration'], 'file': 'project-collaboration.svg', 'size': [24.0, 24.0]},
    {'id': 'quick-start', 'name': 'quick-start', 'name_en': 'Quick Start', 'category': 'action', 'tags': ['quick-start', 'Quick Start'], 'file': 'quick-start.svg', 'size': [80.0, 80.0]},
    {'id': 'repo-home', 'name': 'repo-home', 'name_en': 'Repo Home', 'category': 'action', 'tags': ['repo-home', 'Repo Home'], 'file': 'repo-home.svg', 'size': [80.0, 80.0]},
    {'id': 'review-record', 'name': 'review-record', 'name_en': 'Review Record', 'category': 'action', 'tags': ['review-record', 'Review Record'], 'file': 'review-record.svg', 'size': [80.0, 80.0]},
    {'id': 'review', 'name': 'review', 'name_en': 'Review', 'category': 'action', 'tags': ['review', 'Review'], 'file': 'review.svg', 'size': [16.0, 16.0]},
    {'id': 'settings_1', 'name': 'settings', 'name_en': 'Settings', 'category': 'action', 'tags': ['settings', 'Settings'], 'file': 'settings_1.svg', 'size': [80.0, 80.0]},
    {'id': 'software-design', 'name': 'software-design', 'name_en': 'Software Design', 'category': 'action', 'tags': ['software-design', 'Software Design'], 'file': 'software-design.svg', 'size': [24.0, 24.0]},
    {'id': 'statistics', 'name': 'statistics', 'name_en': 'Statistics', 'category': 'action', 'tags': ['statistics', 'Statistics'], 'file': 'statistics.svg', 'size': [16.0, 16.0]},
    {'id': 'subtitle-settings-line', 'name': 'subtitle-settings-line', 'name_en': 'Subtitle Settings Line', 'category': 'action', 'tags': ['subtitle-settings-line', 'Subtitle Settings Line'], 'file': 'subtitle-settings-line.svg', 'size': [56.0, 56.0]},
    {'id': 'tag', 'name': 'tag', 'name_en': 'Tag', 'category': 'action', 'tags': ['tag', 'Tag'], 'file': 'tag.svg', 'size': [80.0, 80.0]},
    {'id': 'task', 'name': 'task', 'name_en': 'Task', 'category': 'action', 'tags': ['task', 'Task'], 'file': 'task.svg', 'size': [16.0, 16.0]},
    {'id': 'test-management', 'name': 'test-management', 'name_en': 'Test Management', 'category': 'action', 'tags': ['test-management', 'Test Management'], 'file': 'test-management.svg', 'size': [24.0, 24.0]},
    {'id': 'theme-toggle', 'name': 'theme-toggle', 'name_en': 'Theme Toggle', 'category': 'action', 'tags': ['theme-toggle', 'Theme Toggle'], 'file': 'theme-toggle.svg', 'size': [71.0, 71.0]},
    {'id': 'user-forum', 'name': 'user-forum', 'name_en': 'User Forum', 'category': 'action', 'tags': ['user-forum', 'User Forum'], 'file': 'user-forum.svg', 'size': [80.0, 80.0]},
    {'id': 'user-guide', 'name': 'user-guide', 'name_en': 'User Guide', 'category': 'action', 'tags': ['user-guide', 'User Guide'], 'file': 'user-guide.svg', 'size': [80.0, 80.0]},
    {'id': 'version-history', 'name': 'version-history', 'name_en': 'Version History', 'category': 'action', 'tags': ['version-history', 'Version History'], 'file': 'version-history.svg', 'size': [80.0, 80.0]},
    {'id': 'vertical-more', 'name': 'vertical-more', 'name_en': 'Vertical More', 'category': 'action', 'tags': ['vertical-more', 'Vertical More'], 'file': 'vertical-more.svg', 'size': [59.0, 59.0]},

    {'id': 'home_1', 'name': 'home', 'name_en': 'Home', 'category': 'action', 'tags': ['home', 'Home'], 'file': 'home_1.svg', 'size': [80.0, 80.0]},

    {'id': 'plus', 'name': 'plus', 'name_en': 'Plus', 'category': 'action', 'tags': ['plus', 'Plus'], 'file': 'plus.svg', 'size': [80.0, 80.0]},
    {'id': 'successful', 'name': 'successful', 'name_en': 'Successful', 'category': 'action', 'tags': ['successful', 'Successful'], 'file': 'successful.svg', 'size': [80.0, 80.0]},
    {'id': 'common-chatpush-line', 'name': 'common-chatpush-line', 'name_en': 'Common Chatpush Line', 'category': 'action', 'tags': ['common-chatpush-line', 'Common Chatpush Line'], 'file': 'common-chatpush-line.svg', 'size': [80.0, 80.0]},
    {'id': '中切英', 'name': '中切英', 'name_en': '中切英', 'category': 'action', 'tags': ['中切英', '中切英'], 'file': '中切英.svg', 'size': [80.0, 80.0]},
    {'id': '复制', 'name': '复制', 'name_en': '复制', 'category': 'action', 'tags': ['复制', '复制'], 'file': '复制.svg', 'size': [80.0, 80.0]},
    {'id': '收藏-follow', 'name': '收藏-follow', 'name_en': '收藏 Follow', 'category': 'action', 'tags': ['收藏-follow', '收藏 Follow'], 'file': '收藏-follow.svg', 'size': [80.0, 80.0]},
    {'id': '版本历程', 'name': '版本历程', 'name_en': '版本历程', 'category': 'action', 'tags': ['版本历程', '版本历程'], 'file': '版本历程.svg', 'size': [80.0, 80.0]},
    {'id': '设置-setting', 'name': '设置-setting', 'name_en': '设置 Setting', 'category': 'action', 'tags': ['设置-setting', '设置 Setting'], 'file': '设置-setting.svg', 'size': [80.0, 80.0]},
]


def _icon_path(icon: dict) -> str:
    """图标 SVG 的完整路径。"""
    return os.path.join(ICONS_DIR, icon["file"])


def _parse_svg_dimensions(svg_content: str) -> tuple[float, float] | None:
    """
    从 SVG 内容中解析宽高。
    优先使用 width/height 属性，否则从 viewBox 解析。
    返回 (width, height) 或 None（解析失败时）。
    """
    if not svg_content or not svg_content.strip().startswith("<svg"):
        return None

    # 1. 尝试 width/height 属性
    w_match = re.search(r'\bwidth\s*=\s*["\']([^"\']+)["\']', svg_content, re.I)
    h_match = re.search(r'\bheight\s*=\s*["\']([^"\']+)["\']', svg_content, re.I)
    if w_match and h_match:
        try:
            w = float(w_match.group(1).strip())
            h = float(h_match.group(1).strip())
            return (w, h)
        except ValueError:
            pass

    # 2. 回退到 viewBox: "minX minY width height"
    vb_match = re.search(r'\bviewBox\s*=\s*["\']([^"\']+)["\']', svg_content, re.I)
    if vb_match:
        parts = vb_match.group(1).strip().split()
        if len(parts) >= 4:
            try:
                w = float(parts[2])
                h = float(parts[3])
                return (w, h)
            except ValueError:
                pass

    return None


def add_svg_dimensions_to_icons(icons: list[dict], icons_dir: str = ICONS_DIR) -> list[dict]:
    """
    为每个 icon 添加 size 字段（从对应 SVG 文件读取，格式 [width, height]）。
    不修改原 dict，返回新列表；若 SVG 不存在或解析失败，则 size 为 []。
    """
    result = []
    for icon in icons:
        icon_copy = icon.copy()
        file_name = icon.get("file")
        if not file_name:
            icon_copy["size"] = []
            result.append(icon_copy)
            continue

        path = os.path.join(icons_dir, file_name)
        if not os.path.isfile(path):
            icon_copy["size"] = []
            result.append(icon_copy)
            continue

        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception:
            icon_copy["size"] = []
            result.append(icon_copy)
            continue

        dims = _parse_svg_dimensions(content)
        if dims:
            icon_copy["size"] = [dims[0], dims[1]]
        else:
            icon_copy["size"] = []

        result.append(icon_copy)

    return result


def get_icon_path(icon: dict) -> str:
    """返回该图标 SVG 的绝对路径，供调用方使用。"""
    return os.path.abspath(_icon_path(icon))


def load_svg_content(icon: dict) -> str:
    """从本地文件读取该图标的 SVG 内容。文件不存在时返回空字符串或简短错误说明。"""
    path = _icon_path(icon)
    if not os.path.isfile(path):
        return f"<!-- 未找到文件: {path} -->"
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception as e:
        return f"<!-- 读取失败: {e} -->"


def get_icon_by_id(icon_id: str) -> dict | None:
    """按 id 获取单个图标（仅元数据，不含 SVG 内容）。"""
    for icon in ICONS:
        if icon["id"] == icon_id:
            return icon
    return None


def list_icons(category: str | None = None) -> list[dict]:
    """列出图标，可按 category 筛选。"""
    if not category:
        return ICONS
    return [i for i in ICONS if i["category"] == category]


def list_icons_with_dimensions(category: str | None = None) -> list[dict]:
    """列出图标（含 SVG 尺寸 size: [width, height]），可按 category 筛选。"""
    icons = list_icons(category)
    return add_svg_dimensions_to_icons(icons)


def search_icons(keyword: str) -> list[dict]:
    """按关键词搜索（匹配 name、name_en、tags）。"""
    k = keyword.strip().lower()
    if not k:
        return ICONS
    out = []
    for icon in ICONS:
        if k in icon["name"].lower() or k in icon["name_en"].lower():
            out.append(icon)
            continue
        if any(k in t.lower() for t in icon["tags"]):
            out.append(icon)
    return out

if __name__ == "__main__":
    icons_with_sizes = add_svg_dimensions_to_icons(ICONS)

    for icon in icons_with_sizes:
        print(icon["id"], icon["size"])
        for i in ICONS:
            if i["id"] == icon["id"]:
                i["size"] = icon["size"]
    # print(ICONS)

    for i in ICONS:
        print(i)


