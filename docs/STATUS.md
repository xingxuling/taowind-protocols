# 状态与证据

核对日期：2026-10-03。核对方式：读取公开GitHub文件并锁定提交；TINP基于默认分支codex/next-internet-v01的729113b89e6dea59033b64c2aab3dca0c28f5fc3，OPP基于main的da65ab1d26c01c5e2939294e415b9fd07b7dbe5a；后续HEAD变化不回写这份快照；本轮未执行OPP/TINP代码、未重跑测试、未操作开发者电脑。

## 最新增量：第二轮已复测

2026-10-03收到有明确被测版本的第二轮记录：OPP e3dec213、TINP db6ab547。TINP干净环境225/225、原篡改探针26/26、验收绑定篡改7/7、联合链15/15。原始JSON/TAP未随附，本目录未独立复算；这不等于报告没有复测。[结果、第一轮历史和性能边界](ROUND2_VERIFICATION.md)。

下方原有源码/域表快照继续保留；不能用它覆盖较新的第二轮结果。域状态也不因测试计数自动提升。

## 三种状态分别报告

| 层级 | 观察 | 不能外推 |
|---|---|---|
| 总体域 | TINP注册表alpha.20为14 partial、2 not_implemented | 不能说16域完成 |
| 协议与工具 | OPP核心candidate.1；运行工具0.3 candidate.1 | 不能说生态标准或生产认证 |
| 实现证据 | TINP README记载alpha.29本地候选及后续SDK/托管运行增量 | 不能说最新提交全量测试已被本目录复跑 |

## 较新增量与旧注册表的关系

TINP当前提交中的registry/protocols.json仍写`0.1.0-alpha.20`，README基线为alpha.29，并附2026-09-12的SDK与远端运行信息。这是资料版本不齐，不能把目录观测日期当作上游注册表升级日期。本目录保留原状态；由上游Owner依据增量证据修订后，再同步域状态。

- OPP文档记录Python→HTTP/OpenAPI和HTTP→CLI的具体异质接口路径；三项库独立维护，但包装和操作由项目提供，不是三个独立OPP实现
- MCP目前仅能力描述导入；没有据此确认真实独立MCP server执行，gRPC等路径仍有缺口
- TINP记录OPP native receipt的结构/root核验和acceptance binding；`authorityGranted:false`、`sideEffects:false`约束不能删除
- 公开README列有GitHub托管Linux生成、Linux/Windows复核运行。托管系统多环境验证与两台真实物理设备/不同操作员验收不是同一结论
- README历史测试数量和PASS仅代表所指证据版本；不能自动应用到之后每一个提交

来源：[OPP README](https://github.com/xingxuling/OPP/blob/da65ab1d26c01c5e2939294e415b9fd07b7dbe5a/README.md)、[OPP STATUS](https://github.com/xingxuling/OPP/blob/da65ab1d26c01c5e2939294e415b9fd07b7dbe5a/STATUS.md)、[TINP README](https://github.com/xingxuling/TINP/blob/729113b89e6dea59033b64c2aab3dca0c28f5fc3/README.md)。

## 状态词义

- `partial`：域只被部分覆盖，内部可以存在已实现行为
- `not_implemented`：该域尚无登记实现，P12/P14属于此类
- `implemented`：必须说明是一个有界行为还是整个域；目录不擅自提升域状态
- `candidate`：候选，接口/格式仍可能变化
- `upstream-reported`：引用上游报告，目录作者没有独立复跑
- `unverified`：没有建立相应验证，不等同于已证伪

证据强度需分维度记录：运行环境、真实网络/回环、操作者独立性、实现独立性、故障负例、安全范围、提交与时间。不要把这些压成单一“PASS=生产可用”。

## 历史报告与当前源码

一份报告的日期、运行环境、输入与source commit缺一不可。历史故障不因后来源码补丁而消失；当前源码存在校验也不证明同一历史探针已复跑。本目录不将未绑定提交的附件、外部吞吐数字或开发者正在进行的基准当作当前提交验收证据。
