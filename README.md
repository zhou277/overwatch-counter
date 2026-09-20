# Overwatch Counter

当前版本：**v3.0.0**

## v3.0.0 架构更新

项目已经改成 **Excel 数据驱动**。以后主要修改 `data.xlsx`，然后运行：

```bash
python build.py
```

自动重新生成 `index.html`。

## 项目结构

```text
overwatch-counter/
├── data.xlsx
├── template.html
├── build.py
├── index.html
└── README.md
```

## data.xlsx

- `settings`：版本号等设置
- `heroes`：英雄、T/C/S、搜索别名、说明
- `counters`：克制关系、TOP 排名、克制原因
- `maps`：地图推荐、阵容、打法说明
- `tips`：Top 22 上分建议

### counters 的 relation

- `weak`：谁克制我
- `strong`：我克制谁

### 位置缩写

- `T`：坦克
- `C`：输出
- `S`：辅助

## 使用方式

安装依赖：

```bash
pip install openpyxl
```

修改 `data.xlsx` 后运行：

```bash
python build.py
```

然后本地打开新生成的 `index.html` 检查，确认后上传 GitHub Pages。

## 推荐 Git 流程

```bash
python build.py
git add data.xlsx index.html
git commit -m "update counter data"
git push
```

`template.html` 和 `build.py` 只有在网页结构或生成功能发生变化时才需要改。

## 版本规则

统一使用 `vX.Y.Z`：

- X：架构级更新
- Y：功能更新
- Z：小调整、文案、样式或 Bug 修复

本次从静态 HTML 数据改成 Excel 数据源，因此为 **v3.0.0**。
