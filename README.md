# Overwatch Counter

一个用于查询《守望先锋》英雄克制关系和地图推荐阵容的轻量级网页工具。

当前版本：**v2.2**

## 功能

- 查询每个英雄的克制关系
- 按位置区分：
  - T：坦克
  - C：输出
  - 辅助
- 每个英雄显示：
  - 克制我的 T / C / 辅助 TOP 3
  - 我克制的 T / C / 辅助 TOP 3
- 支持地图推荐
  - 推荐坦克
  - 推荐输出
  - 推荐辅助
  - 推荐阵容
  - 地图打法思路
- 支持英雄搜索和位置筛选
- 同时适配电脑和手机
- 单 HTML 文件，无额外前端依赖

## 当前英雄

英雄列表已更新到 **2026-09-19** 的当前版本，共 **53 名英雄**。

v2.2 新增：

- D.Mon
- 安燃（Anran）
- Domina
- Emre
- Freja
- Hazard
- Jetpack Cat
- Mauga
- Mizuki
- Shion
- Sierra
- 索杰恩（Sojourn）
- Vendetta
- Venture
- Wuyang

## 项目结构

```text
overwatch-counter/
├── index.html
└── README.md
```

## 本地使用

直接用浏览器打开：

```text
index.html
```

如果浏览器对本地 HTML 的 JavaScript 有限制，也可以启动一个简单的本地 HTTP 服务：

```bash
python3 -m http.server 7000
```

然后访问：

```text
http://localhost:7000
```

## GitHub Pages 部署

将项目上传到 GitHub 仓库，并确保仓库根目录中存在：

```text
index.html
README.md
```

然后进入：

```text
Settings
→ Pages
```

设置：

```text
Source: Deploy from a branch
Branch: main
Folder: / (root)
```

保存后等待 GitHub Pages 完成部署。

访问地址通常为：

```text
https://你的GitHub用户名.github.io/overwatch-counter/
```

## 更新网站

修改 `index.html` 后提交到 `main` 分支：

```bash
git add index.html
git commit -m "update app"
git push
```

GitHub Pages 会自动重新部署。

## 关于克制关系

本项目中的克制关系用于**快速实战参考**，不是暴雪官方发布的胜率或克制排名。

实际对局结果还会受到以下因素影响：

- 当前版本平衡性
- 地图
- 阵容组合
- 技能交换
- 玩家熟练度
- 段位和团队配合

因此 TOP 3 更适合作为换英雄和判断对位的参考，而不是绝对结论。

## 版本记录

### v2.2

- 英雄数量更新到 53
- 新增 15 名当前版本英雄
- 为新增英雄补全 T / C / 辅助克制 TOP 3
- 保持手机和电脑响应式布局
- 保持单 HTML 部署方式

### v2.1

- 调整英雄详情页显示顺序
- 优先显示“谁比较克制我”
- 再显示“我比较克制谁”

### v2.0

- 整理为单 HTML 发布版
- 移除图片和额外资源依赖
- 适合直接部署到 GitHub Pages
