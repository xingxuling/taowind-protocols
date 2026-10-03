# TINP 入口

[实现仓库](https://github.com/xingxuling/TINP) · [固定版README](https://github.com/xingxuling/TINP/blob/729113b89e6dea59033b64c2aab3dca0c28f5fc3/README.md) · [域表](https://github.com/xingxuling/TINP/blob/729113b89e6dea59033b64c2aab3dca0c28f5fc3/registry/protocols.json) · [偏差记录](https://github.com/xingxuling/TINP/blob/729113b89e6dea59033b64c2aab3dca0c28f5fc3/docs/SPEC_DEVIATIONS.md)

职责：受控调用的身份、会话、权限、路由、恢复及执行证据。执行前准入与执行后核对分工明确；并非给任意操作系统进程加全局拦截。

组合OPP时，TINP核对OPP的具体回执并产生验收绑定。离线绑定不是主动业务调用，验收成功不会授予新权限。P04继续由OPP拥有协商语义；世界权威等外部Owner也保持边界。

当前有本地候选、只读SDK及托管异环境验证记录。真实物理多机、生产Authority和完整密钥生命周期、可信时间、独立操作员等门仍然开放。目录没有重新运行这些测试。

许可观察：[LICENSE_AUDIT](https://github.com/xingxuling/TINP/blob/729113b89e6dea59033b64c2aab3dca0c28f5fc3/docs/LICENSE_AUDIT.md)仍为`NOT_ADJUDICATED`。不要打包vendor目录或用当前OPP的MIT覆盖旧快照。
