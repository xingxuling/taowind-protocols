# TaoWind 协议总仓库

**把两个系统接起来：先说清各自能做什么，再检查怎么转换、能不能执行，最后留下这次调用的记录。**

比如，旧预约表单叫 `name`，新 CRM 要 `customer_name`。谁来改字段？转换规则被改过怎么办？调用失败后怎么知道卡在哪一步？

这里把解决这些问题的协议和实现放在一起，方便你找到能用的部分。**这个仓库是说明和入口；可运行的代码在 [OPP](https://github.com/xingxuling/OPP) 和 [TINP](https://github.com/xingxuling/TINP)。**

## 先看一个能跑的例子：旧预约表单接新 CRM

OPP仓库里已有本地演示。下面摘出几个字段，电话号码和备注没有展开：

| 步骤 | 实际发生什么 |
|---|---|
| 1. 收到旧表单 | `name: "陈小姐"`、`service: "physio-first-visit"`、`slot: "2026-09-15 14:30"` |
| 2. 按明确规则转换 | `name → customer_name`、`service → service_code`、`slot → preferred_time` |
| 3. 补上/去掉字段 | 原样保留 `phone`、`notes`；补 `channel: "legacy-web-form"`；不把 `debug_source` 传给 CRM |
| 4. 调用接收函数 | 本地模拟 CRM 收到新字段，返回 `accepted: true` |
| 5. 留下记录 | 返回转换后的数据、接收结果、`PASS/FAIL` 和可核对的回执根 |

**转换规则是示例作者明确写好的，不是程序自动猜出任意 CRM 的业务含义。** 两端都是本地模拟函数，不连接真实预约系统或真实 CRM。

### 这条链怎么决定继续还是停下？

- 没有明确允许执行，运行器会拒绝，报 `EXECUTION_CONSENT_REQUIRED`
- 转换计划的内容与记录的哈希不一致，报 `BRIDGE_PLAN_ROOT_INVALID`，不调用两端函数
- 旧表单函数失败，或字段转换失败，不继续调用 CRM
- CRM 函数执行失败，这次结果记为 `FAIL`；不会暗中不断重试
- 两端运行成功，记录这次输入、转换计划、转换结果和最终结果之间的对应关系

这些分支来自 [互操作运行器](https://github.com/xingxuling/OPP/blob/da65ab1d26c01c5e2939294e415b9fd07b7dbe5a/src/opp/runtime/interop.py)。示例正常运行走的是成功路径，**不能把上面的源码分支都算成这次示例已跑过的负例测试**。

### 怎样试？

需要 Git 和 Python 3.10 或更新版本。建议在单独的 Python 虚拟环境中运行：

```bash
git clone https://github.com/xingxuling/OPP.git
cd OPP
git checkout da65ab1d26c01c5e2939294e415b9fd07b7dbe5a
python -m pip install -e .
python examples/business_demo.py
```

这会安装声明的依赖并运行本地示例函数，不会连接真实 CRM。`business_demo.py` 已在脚本内设置 `allow_execution=True`：运行脚本即会启动两端本地函数，不会另弹确认。输出里看三个位置：`OPP 转换后`、`新系统结果`、`状态`。

不想先安装，可以直接看 [示例源码](https://github.com/xingxuling/OPP/blob/da65ab1d26c01c5e2939294e415b9fd07b7dbe5a/examples/business_demo.py) 和 [已归档的完整输入输出](https://github.com/xingxuling/OPP/blob/da65ab1d26c01c5e2939294e415b9fd07b7dbe5a/evidence/business-demo-output.json)。这份运行记录生成于 2026-09-12，标记的运行源码是 `643e392...`；上面的命令固定到本目录查阅的较新源码 `da65ab1...`。**本目录没有重跑这个示例，不把旧回执当成新提交的验收结果。**

## OPP 和 TINP 各管哪一段？

| 你遇到的问题 | 从哪里看 | 当前能拿到什么 |
|---|---|---|
| 两边字段不一样，需要明确怎么转 | [OPP 业务示例](https://github.com/xingxuling/OPP/blob/da65ab1d26c01c5e2939294e415b9fd07b7dbe5a/BUSINESS_DEMO.md) | 一条明确的字段映射、本地执行结果和回执 |
| 两边先描述能力，再判断直接接、转换、继续协商、接受降级还是拒绝 | [OPP Session](https://github.com/xingxuling/OPP/blob/da65ab1d26c01c5e2939294e415b9fd07b7dbe5a/docs/CHA_SESSION.md) | 有界能力协商、绑定接口版本的会话契约；这与上面的预写映射示例是不同路径 |
| 请求要在几个节点之间执行，需要先查身份和权限，节点坏了还要处理失败 | [TINP 入口](implementations/TINP.md) | 受控调用的准入、路由、会话、恢复和回执实现；生产、多机与安全验证仍有明确缺口 |

**上面的预约→CRM演示调用的是 OPP 的 `run_interop`，没有接入 TINP，也没有把下面六个协议逐一端到端跑一遍。** 其运行回执使用 `taowind.opp.interop-receipt.v0.1` 格式，不能直接称为REP报文。 如需查看 TINP，再到它的仓库读独立示例和证据，不要把两份结果拼成一次不存在的完整运行。

## 具体有哪些协议？什么时候用？

下面六项属于 OPP。正式名称保留，旁边说明它在一次接入工作中要表达什么。

| 简称与正式全名 | 什么时候用 / 具体写什么 | 现在有哪种实现 |
|---|---|---|
| **RXP** · Reality Exchange Protocol · 现实交换协议 | 需要统一消息外壳时：写消息来自谁、装的是什么、附带哪些约束 | [数据格式](https://github.com/xingxuling/OPP/blob/da65ab1d26c01c5e2939294e415b9fd07b7dbe5a/schemas/rxp.schema.json)与[结构检查](https://github.com/xingxuling/OPP/blob/da65ab1d26c01c5e2939294e415b9fd07b7dbe5a/src/opp/validation.py)；信封不自行执行动作 |
| **RCP** · Reality Capability Protocol · 现实能力协议 | 对接前说明“我能做什么”：例如接收哪些字段、返回什么结果、是否有副作用 | [能力格式](https://github.com/xingxuling/OPP/blob/da65ab1d26c01c5e2939294e415b9fd07b7dbe5a/schemas/rcp.schema.json)与[参考协商器](https://github.com/xingxuling/OPP/blob/da65ab1d26c01c5e2939294e415b9fd07b7dbe5a/src/opp/capability.py)；不是任意业务含义自动匹配 |
| **RAP** · Reality Artifact Protocol · 现实工件协议 | 交换一个文件、模型或软件包时：说清它是哪一版、依赖什么、从哪来、怎么验收 | [数据格式](https://github.com/xingxuling/OPP/blob/da65ab1d26c01c5e2939294e415b9fd07b7dbe5a/schemas/rap.schema.json)与[结构检查](https://github.com/xingxuling/OPP/blob/da65ab1d26c01c5e2939294e415b9fd07b7dbe5a/src/opp/validation.py)；不等于已实现通用安装分发 |
| **REP** · Reality Evidence Protocol · 现实证据协议 | 别人说“测试通过”时：让其附上测了什么、用什么方法、怎么复现、哪里还没证明 | [数据格式](https://github.com/xingxuling/OPP/blob/da65ab1d26c01c5e2939294e415b9fd07b7dbe5a/schemas/rep.schema.json)与[结构检查](https://github.com/xingxuling/OPP/blob/da65ab1d26c01c5e2939294e415b9fd07b7dbe5a/src/opp/validation.py)；格式通过不等于主张真实 |
| **RSP** · Reality State Protocol · 现实状态协议 | 交换状态时：分清“实际观察到”与“预测可能发生”，并记录是哪个版本 | [数据格式](https://github.com/xingxuling/OPP/blob/da65ab1d26c01c5e2939294e415b9fd07b7dbe5a/schemas/rsp.schema.json)与[结构检查](https://github.com/xingxuling/OPP/blob/da65ab1d26c01c5e2939294e415b9fd07b7dbe5a/src/opp/validation.py)；不等于已实现跨设备状态同步 |
| **CHP** · Civilization Handshake Protocol · 文明握手协议 | 两端开始合作前：核对支持的版本、能力和限制，能接受才继续，否则拒绝 | [握手格式](https://github.com/xingxuling/OPP/blob/da65ab1d26c01c5e2939294e415b9fd07b7dbe5a/schemas/chp.schema.json)与[参考协商器](https://github.com/xingxuling/OPP/blob/da65ab1d26c01c5e2939294e415b9fd07b7dbe5a/src/opp/handshake.py)；不会自动给对方增加权限 |

这六项都还是候选规范。RXP/RAP/REP/RSP这里列出的落地范围是**格式和校验**，RCP/CHP另有**参考协商实现**；不能一概写成六项都只有想法，也不能一概写成六项都已有完整业务系统。

完整定义：[OPP 原规范](https://github.com/xingxuling/OPP/blob/da65ab1d26c01c5e2939294e415b9fd07b7dbe5a/docs/SPECIFICATION.md)。

## 哪些能试，哪些还只是目标？

| 项目 | 目前应怎么理解 |
|---|---|
| 预约表单→CRM | 有源码和固定输入输出记录，可按上面命令试；两端为本地模拟函数 |
| OPP 能力协商、Session、受限桥接 | 有参考实现与具体示例；不保证任意系统自动兼容 |
| OPP 六个核心协议 | 有规范、Schema与校验；具体协商实现见上表，仍是候选版本 |
| TINP | 有准入、路由、恢复和回执等有界实现与证据；不能直接当成成熟公网产品 |
| 应用种子（P12） | 格式、安装分发和验证尚未实现 |
| 私网隔离（P14） | VPN/隧道和主体级隔离尚未实现；测试断链不等于网络隔离 |
| 独立第三方互操作、生产级密钥管理、可信时间等 | 仍须补足对应证据；详见[差距清单](docs/GAPS.md) |

## 如果你要看整体规划

**P00–P15是16个要覆盖的问题，不是16个已经做好的协议。** 当前引用的 TINP 域表版本为 `0.1.0-alpha.20`：14项部分实现、P12/P14未实现。TINP的较新README和运行记录另外登记，不自动改变这个域表。

- 基础： [共享语义](domains/P00.md) · [身份](domains/P01.md) · [寻址](domains/P02.md) · [发现](domains/P03.md)
- 调用： [能力协商](domains/P04.md) · [权限](domains/P05.md) · [证据](domains/P06.md) · [路由](domains/P07.md)
- 运行： [会话与恢复](domains/P08.md) · [传输](domains/P09.md) · [资源与SLA](domains/P10.md) · [数据上下文](domains/P11.md)
- 后续： [应用种子](domains/P12.md) · [运行时适配](domains/P13.md) · [私网隔离](domains/P14.md) · [旧系统兼容](domains/P15.md)

OPP是包含六协议的协议族；OPP Session是可选会话方案，不是第七个核心协议；TINP是另一个网络执行治理套件。详细分工见[层级与职责](docs/ARCHITECTURE.md)。

## 版本、来源和公开范围

- [状态与证据](docs/STATUS.md)：区分历史运行记录、当前源码和独立复测
- [原始规格来源](specifications/README.md)：原始工程规范及宪法文档只登记来源与哈希，未收录全文
- [机器可读协议索引](registry/protocols.json) · [16域登记](registry/domains.json) · [实现版本](registry/implementations.json) · [来源锁定](registry/sources.json)
- [贡献约定](CONTRIBUTING.md)：增加声明时，应附准确版本、证据和未覆盖范围
- [权利说明](RIGHTS.md)：OPP当前源为MIT；TINP历史组件的对外分发许可仍待裁决；本目录未给所有材料套统一许可证

本目录整理公开资料，没有复制私有原件或上游实现代码。协议候选、运行示例和长期目标分别列明，不把它们当成同一件事。
