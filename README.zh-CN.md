<div align="center">

[日本語](README.md) | [English](README.en.md) | [한국어](README.ko.md) | **简体中文**

</div>

# ygo-small-world-transit

[游戏王小世界检索路径查询](https://ygo-small-world-transit.streamlit.app/?lang=zh-CN)可根据[游戏王 Neuron](https://www.db.yugioh-card.com/yugiohdb/?request_locale=cn)的公开牌组 URL，搜索**小世界**的检索路径。

## 使用方法

YouTube 上提供了[使用说明视频](https://www.youtube.com/watch?v=VVvS8u706BM&t=6s)。

1. 输入牌组页面顶部显示的公开牌组 URL，然后点击**加载牌组**；也可以在初始页面点击**试用示例**。
2. 选择从手牌展示的怪兽。检索目标为可选项。留空时会查找当前牌组中所有可到达的检索目标。
3. 点击**查找路径**。结果按检索目标分组。选择**按中转怪兽排序**可改为按中转怪兽分组。
4. 展开**查看匹配信息**，即可查看手牌 → 中转怪兽 → 检索目标的路径及每一步的匹配项目。

加载牌组后，点击**更换牌组**打开 URL 输入框，以加载其他牌组或重新加载当前牌组。加载后收藏此页面，下次即可加载相同牌组。搜索选择和结果不会保存。

## 语言

[日本語](https://ygo-small-world-transit.streamlit.app/?lang=ja) / [English](https://ygo-small-world-transit.streamlit.app/?lang=en) / [한국어](https://ygo-small-world-transit.streamlit.app/?lang=ko) / [简体中文](https://ygo-small-world-transit.streamlit.app/?lang=zh-CN)

默认界面语言为日语。点击应用标题上方的地球图标菜单即可切换界面语言。界面语言与牌组数据语言相互独立。指定 `request_locale` 时按该语言获取牌组数据，未指定时使用界面语言。简体中文对应的数据库语言代码为 `cn`。

## 本地运行

需要 Python 3.12 或更高版本。

1. 克隆此仓库并进入项目根目录。
2. 安装所需依赖。

   ```bash
   python -m pip install -r requirements.txt
   ```

3. 启动应用。

   ```bash
   python -m streamlit run ./src/ui.py
   ```

建议使用虚拟环境，避免与其他 Python 项目的依赖冲突。若找不到 `streamlit` 命令，请使用 `python -m streamlit` 启动。若出现 `No module named streamlit`，请使用启动应用的同一 Python 解释器安装依赖。

## 开发

在项目根目录运行测试。

```bash
python -m pytest
```

需求和架构请参阅[设计文档](docs/ygo-small-world-transit.md)。

### 依赖管理

在 `requirements.in` 中声明依赖。`requirements.txt` 是包含直接及间接依赖固定版本的生成文件。请将两个文件都提交到 Git，并使用 `requirements.txt` 安装依赖。生成工具 `uv` 的版本固定在 `requirements-tools.txt` 中。

```bash
python -m pip install -r requirements-tools.txt
python -m uv pip compile requirements.in --output-file requirements.txt
```

修改依赖时，请编辑 `requirements.in` 并重新生成 `requirements.txt`，不要直接修改生成文件。在声明范围内更新单个包时添加 `--upgrade-package PACKAGE`，更新所有包时添加 `--upgrade`。

```bash
python -m uv pip compile requirements.in --output-file requirements.txt --upgrade-package streamlit
python -m uv pip compile requirements.in --output-file requirements.txt --upgrade
```

CI 会在运行测试前确认重新生成锁定文件不会产生差异。

### 依赖安全扫描

[Dependency security 工作流](https://github.com/ikishichi/ygo-small-world-transit/actions/workflows/dependency-security.yml)每周六以及面向 `main` 的 PR 创建、更新或重新打开时，使用 Trivy 扫描 `requirements.txt`。也可以在 Actions 页面手动运行。应用排除规则后仍有 High 或 Critical 漏洞、无法下载数据库、报告缺失或损坏、排除设置无效时，检查会失败。尚未发布修复版本的漏洞也会纳入检查。

工作流摘要会显示检测、临时排除和评估的问题数量、导致检查失败的 High 和 Critical 漏洞，以及排除原因和到期日。数据库下载失败、报告缺失或损坏、排除设置无效、Trivy 漏检固定依赖包时，均视为检查错误。`dependency-security-report` 工件会保存排除前后 JSON 报告、摘要、扫描所用锁定文件和排除设置，共保留 14 天。临时排除漏洞时，请将漏洞 ID 写入 `.trivyignore`，升级到修复版本后删除该排除项。排除前的结果保留在原始 JSON 报告中。

## 保持托管应用唤醒

[Keep Streamlit app awake 工作流](https://github.com/ikishichi/ygo-small-world-transit/actions/workflows/keep_alive.yml)每三小时使用 Playwright Chromium 打开托管应用，并将浏览器语言固定为 `ja-JP`。若出现休眠页面，工作流会尝试解除休眠，并确认标题、可编辑的牌组 URL 输入框和已启用的**デッキ取得**按钮均已显示。它不会加载牌组或执行搜索。此定时工作流不会在 fork 仓库中运行。

### 确认恢复及故障处理

工作流最多等待 120 秒确认恢复，并重试一次。每次页面跳转另有最多 30 秒等待时间。若未能确认恢复，工作流会失败，并将截图和各 iframe 的 HTML 作为工件保存 7 天。请结合日志和工件检查网络故障、Streamlit 服务异常或页面及按钮变化。此检查只验证界面，不验证牌组加载和搜索功能。

GitHub[定时工作流](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule)可能延迟或漏跑。公开仓库连续 60 天没有活动时，GitHub 会自动禁用工作流，届时可在 Actions 页面重新启用。[Streamlit Community Cloud 休眠条件](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app#app-hibernation)和界面都可能变化，因此无法保证始终在线。

### 在本地测试唤醒脚本

按需安装可选测试依赖和 Chromium。

```bash
python -m pip install playwright==1.63.0
python -m playwright install chromium
python scripts/keep_alive.py
python -m pytest test/keep_alive_test.py
```

`python scripts/keep_alive.py` 会实际访问托管应用以确认恢复。测试会在本地模拟页面中运行 Chromium，不会访问托管应用。未安装 Playwright 时会跳过测试。

## 许可证

本仓库代码以 MIT 许可证发布。详情请参阅 [LICENSE.txt](LICENSE.txt)。
