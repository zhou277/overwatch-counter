# Overwatch Counter

当前版本：**v3.8.0**

## v3.8.0 更新：英雄头像

本版为全部 53 个英雄加入头像显示。

头像会出现在：

- 左侧英雄列表
- 当前英雄详情标题
- 克制查询 Top 1 / Top 2 / Top 3
- 地图 T / C / S 推荐英雄
- 每套地图参考阵容的 5 个英雄

## 数据维护

`heroes` Sheet 新增：

```text
avatar_url
```

每个英雄对应一条头像地址。

当前头像使用 Blizzard 托管的 Overwatch 英雄 portrait CDN 地址。网页本身不打包几十张图片，因此项目体积基本不增加。

如果某个头像网络加载失败，会自动退化为英雄名字首字符的本地占位头像，不会破坏页面布局。

## 后续替换成本地头像

如果以后希望完全离线，也可以把 `avatar_url` 改成：

```text
assets/heroes/genji.webp
assets/heroes/ana.webp
...
```

网页代码不需要再修改。

## 自动构建

仍然保持：

```text
data.xlsx
→ build.py
→ index.html
```

## 版本

本次增加完整英雄头像系统，属于功能更新：

```text
v3.7.0 → v3.8.0
```
