# Overwatch Counter

当前版本：**v3.7.0**

## v3.7.0 更新

地图页新增“多套参考阵容 + 对应打法推荐”。

每张地图现在提供 **3 套参考阵容**，不再只有一套。每套阵容都会分别说明：

- 阵容名称
- 5 人英雄组合
- 适用场景
- 核心打法
- 开团方式
- 注意点

### Excel

新增 `map_comps` Sheet。

字段：

```text
map
rank
style_name
tank
dps1
dps2
support1
support2
lineup
use_when
core_play
engage
caution
```

当前 24 张地图 × 3 套阵容，共 **72 套参考阵容**。

阵容不是固定答案，而是根据地图的长枪、高台、拐角、机动、控制点和转点特点提供不同思路。例如同一张地图可以在默认稳定、远程消耗、快速冲阵、机动切后之间切换。

### 自动构建

仍然保持：

```text
data.xlsx
→ build.py
→ index.html
```

后续你只需要改 `map_comps` Sheet，就能增加、删除或修改某张地图的参考阵容和打法说明。

## 版本规则

本次新增多阵容与打法卡片，属于功能更新：

```text
v3.6.1 → v3.7.0
```
