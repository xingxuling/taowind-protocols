# TaoWind Protocols · 协议总仓库

TaoWind 协议、套件、实现与证据的统一入口。先看全貌，再进入各自Owner仓库。

**当前是资料目录候选（informative catalog），不替代原始工程规范，不宣布16域已完成，也不合并OPP与TINP的实现仓库。**

## 从哪里开始

- 想理解总体结构：读 [层级与职责](docs/ARCHITECTURE.md)
- 想知道16个域具体干什么：看下表与 `domains/` 逐域页面
- 想看正式来源：读 [规范来源与公开状态](specifications/README.md)
- 想接系统：进入 [OPP](implementations/OPP.md) 或 [TINP](implementations/TINP.md)
- 想确认做到哪一步：读 [状态与证据](docs/STATUS.md)
- 想继续建设：读 [差距清单](docs/GAPS.md) 与 [贡献约定](CONTRIBUTING.md)

## 四个层级

1. **原始规格**：定义长期目标、结构和要求；原件未收录，来源与哈希已登记
2. **能力域 P00–P15**：总体路线图的16个关注领域；一个域可以由多个协议或实现协作承担
3. **协议族/套件/Profile**：OPP拥有六个语义交换核心协议；TINP组合身份、准入、传输、恢复和证据；Session是OPP可选Profile
4. **实现与验证**：源码、测试、回执和运行证据；不能用“有规范”代替实现，也不能用本机PASS代替生产成熟

## P00–P15 总表

截至2026-10-03，当前公开注册表的自身版本仍为`0.1.0-alpha.20`：**14项partial、2项not_implemented、0项整域implemented**。TINP README及后续证据比该注册表更新，两者分开记录。

| 域 | 中文解释 | 域状态 | 主要问题 |
|---|---|---|---|
| [P00](domains/P00.md) | 共享语义核心 | `partial` | 让不同协议对主体、请求、会话、权限和证据使用可对应的语义结构 |
| [P01](domains/P01.md) | 主体与身份 | `partial` | 回答是谁，以及换节点后是否仍是同一主体 |
| [P02](domains/P02.md) | 命名与寻址 | `partial` | 将稳定主体引用与当次访问节点的地址分开 |
| [P03](domains/P03.md) | 发现与在线状态 | `partial` | 查找有哪些可调用服务，并判断其声明是否仍有效 |
| [P04](domains/P04.md) | 意图与能力协商 | `partial` | 把请求意图落到明确能力契约，判断双方能否协作 |
| [P05](domains/P05.md) | 权限与主权 | `partial` | 界定谁能做什么、有效多久，以及撤销后如何拒绝执行 |
| [P06](domains/P06.md) | 信任证据与溯源 | `partial` | 把执行结果与请求、权限和路径绑定，并保留可复核来源 |
| [P07](domains/P07.md) | 路由与路径选择 | `partial` | 在成本、时延、能耗、地区与带宽约束下选择合法路径 |
| [P08](domains/P08.md) | 会话与连续性 | `partial` | 故障、迁移或重启后保持主体、权限、证据的关联 |
| [P09](domains/P09.md) | 传输适配 | `partial` | 把有边界的协议消息交给实际传输实现 |
| [P10](domains/P10.md) | 资源、SLA与价值 | `partial` | 表达调用预算和资源限制，并区分声明与实际保障 |
| [P11](domains/P11.md) | 世界与数据上下文 | `partial` | 指明请求属于哪个世界/数据上下文，保持既有权威归属 |
| [P12](domains/P12.md) | 应用种子 | `not_implemented` | 描述可分发、可验证并能安装的应用初始工件 |
| [P13](domains/P13.md) | 运行时能力与Lowering | `partial` | 把抽象约束落到具体编译器、运行时和设备能力 |
| [P14](domains/P14.md) | 私网与隔离 | `not_implemented` | 按主体或世界建立实际的网络隔离边界 |
| [P15](domains/P15.md) | 旧网互操作 | `partial` | 在保留现有互联网协议职责的前提下形成受控兼容路径 |

中文名称用于帮助理解，英文登记名与Owner边界保留在逐域页。原始状态见[固定版本TINP注册表](https://github.com/xingxuling/TINP/blob/729113b89e6dea59033b64c2aab3dca0c28f5fc3/registry/protocols.json)。

## 协议族与实现入口

| 入口 | 职责 | 当前边界 |
|---|---|---|
| [OPP](https://github.com/xingxuling/OPP) | 能力描述、协商、有限转换、互操作回执 | Candidate；独立实现/操作员互操作仍未验证 |
| [TINP](https://github.com/xingxuling/TINP) | 执行前准入、路由、会话、失败恢复、执行后核对 | 已有受控候选证据；生产、真实双机等门仍开放 |

OPP与TINP可以独立演进；验收一条OPP回执不会自动授予TINP执行权限。

## 机器可读目录

- [域注册表](registry/domains.json)：16域、Owner边界、实现摘要、缺口
- [协议索引](registry/protocols.json)：OPP六协议及可选Profile
- [实现登记](registry/implementations.json)：仓库、固定提交、成熟度与许可观察
- [来源锁定表](registry/sources.json)：已读取文件的固定提交、Git blob SHA与链接

## 许可和公开边界

本目录只整理已公开事实与来源链接，不复制DOCX原件、vendor源码、密钥或私有项目内容。OPP当前源为MIT；TINP仍为`NOT_ADJUDICATED`；原始规格的全文公开/再分发权限未确认。详见[权利说明](RIGHTS.md)。本目录本身尚未选定开放许可证，不能把来源项目许可证套用到所有材料。
