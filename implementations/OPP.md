# OPP 入口

[实现仓库](https://github.com/xingxuling/OPP) · [固定版README](https://github.com/xingxuling/OPP/blob/da65ab1d26c01c5e2939294e415b9fd07b7dbe5a/README.md) · [原规范](https://github.com/xingxuling/OPP/blob/da65ab1d26c01c5e2939294e415b9fd07b7dbe5a/docs/SPECIFICATION.md) · [状态](https://github.com/xingxuling/OPP/blob/da65ab1d26c01c5e2939294e415b9fd07b7dbe5a/STATUS.md)

职责：描述语义和能力，判断契约兼容，规划受限适配，并在显式执行许可下运行已支持的互操作路径。核心六协议与工具链版本不同，见[层级说明](../docs/ARCHITECTURE.md)。

当前证据包括有界Python、HTTP和CLI组合。MCP描述导入不等于任意MCP执行；同操作员使用真实第三方库不等于独立实现认证。静态分析、桥接规划、显式执行、离线验收应分别对待。

适合入口：原仓库README中的Demo、CHA Session、Public SDK与Native Interop文档。本总仓库不复制运行时，也不承诺工具安装后可自动执行任意外部系统。

许可观察：[当前固定源MIT LICENSE](https://github.com/xingxuling/OPP/blob/da65ab1d26c01c5e2939294e415b9fd07b7dbe5a/LICENSE)；不自动替历史vendored快照做追溯许可裁决。
