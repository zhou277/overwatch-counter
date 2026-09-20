# Overwatch Counter

当前版本：**v3.1.0**

## v3.1.0 更新

新增 **GitHub Actions 自动构建**。

现在不再要求每次都在本地运行 `python build.py`。

以后修改网页数据时，只需要：

```text
修改 data.xlsx
      ↓
上传 / 提交到 GitHub
      ↓
GitHub Actions 自动运行 build.py
      ↓
自动更新 index.html
      ↓
GitHub Pages 自动显示新内容
```

## 项目结构

```text
overwatch-counter/
├── .github/
│   └── workflows/
│       └── build.yml
├── data.xlsx
├── template.html
├── build.py
├── index.html
└── README.md
```

## 第一次部署

把以上文件完整上传到 GitHub 仓库根目录。

GitHub Pages 保持：

```text
Settings
→ Pages
→ Deploy from a branch
→ main
→ /(root)
```

## 以后怎么更新

### 只修改英雄、克制、地图或上分建议

你只需要编辑：

```text
data.xlsx
```

然后把新版 `data.xlsx` 上传到 GitHub 覆盖旧文件。

当 `data.xlsx` 被提交到 `main` 分支后，GitHub Actions 会自动：

1. 下载仓库
2. 安装 Python 3.12
3. 安装 `openpyxl`
4. 运行 `python build.py`
5. 生成新的 `index.html`
6. 自动 commit 并 push `index.html`

因此不需要你手动运行 Python。

## 查看自动构建状态

进入 GitHub 仓库：

```text
Actions
→ Build Overwatch Counter
```

绿色勾表示构建成功。

如果构建失败，可以点击失败的任务查看错误日志。

## 为什么不会无限循环

自动构建生成的 commit 只修改：

```text
index.html
```

而 workflow 只在以下文件变化时触发：

```text
data.xlsx
template.html
build.py
.github/workflows/build.yml
```

所以 Actions 自动提交 `index.html` 后不会再次触发自身。

## data.xlsx

### settings

项目版本等设置。

### heroes

英雄列表：

- `order`
- `name`
- `role`
- `aliases`
- `note`

位置统一使用：

```text
T = 坦克
C = 输出
S = 辅助
```

### counters

克制关系：

- `weak`：谁克制我
- `strong`：我克制谁

包含 TOP 排名和克制原因。

### maps

地图推荐、推荐英雄、阵容和打法说明。

### tips

Top 22 上分建议。

## 什么时候还需要改其他文件

普通数据更新：

```text
只改 data.xlsx
```

网页样式或功能改变：

```text
修改 template.html
```

生成逻辑改变：

```text
修改 build.py
```

## 版本规则

统一使用：

```text
vX.Y.Z
```

- **X**：架构级更新
- **Y**：功能更新
- **Z**：小调整、文案、样式优化、Bug 修复

本次加入 GitHub Actions 自动构建属于功能更新：

```text
v3.0.0 → v3.1.0
```
