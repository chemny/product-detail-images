# 商品详情页图片

[English](./README.md) | 中文

把一张或多张商品素材，转化为一套完整、以成交为目标的商品详情页图片。这个 Skill 不只负责生成好看的单图，还会先规划商品叙事、推荐视觉风格、编写逐页文案、设计图文关系，并对整套图片做生成后质检。

## 效果预览

### 女装详情图片系列

<p align="center">
  <img src="./assets/fashion-series-hero.png" width="31%" alt="女装系列头图与颜色总览">
  <img src="./assets/fashion-series-lifestyle.png" width="31%" alt="女装系列场景页">
  <img src="./assets/fashion-series-detail.png" width="31%" alt="女装系列腰头与结构细节页">
</p>

女装案例展示了同一个商品如何从商品认知推进到使用想象与结构细节，同时避免重复人物姿态和重复版式。

### 商品系列总览

![为虚构陶瓷手冲咖啡套装生成的三页商品详情图片系列](./assets/product-detail-series-preview.png)

咖啡预览图是专门为本仓库生成的原创虚构商品案例。两个品类共同展示了不同页面任务、景别、构图、文案层级与背景世界的变化。

## 适合谁使用？

- 需要制作电商商品详情页的运营人员
- 希望把有限素材扩展成完整视觉方案的产品与品牌团队
- 需要统一生成提示词、文案和质检标准的设计师与内容创作者
- 不满足于生成几张独立海报，希望完成整套成交叙事的 Agent 用户

## 它能做什么？

Skill 会先确认主商品与可用事实，再建立完整的商品成交叙事，最后决定图片数量。它会展示七种视觉风格并给出推荐，将每一页对应到明确的成交任务，经过一次集中确认后分批生成，并从单图和整套节奏两个层面完成质检。

## 核心能力

| 能力 | 它能帮你做什么 |
| --- | --- |
| 商品与事实分析 | 区分肉眼可见的商品事实、用户提供的信息和不可凭空编造的客观主张 |
| 品类路由与适配 | 自动识别商品的主要决策类型；结构耐用品、包装消费品和数码电子会分别加载对应的结构、包装标签、感官表达、功能与证据规则 |
| 完整页面规划 | 覆盖商品认知、核心价值、优势表达、证据、使用想象与购买决策 |
| 稳定的图片数量规则 | 根据叙事深度与素材丰富度选择 6、8 或 10 张，避免随意变化 |
| 七种视觉方向 | 同时比较七种适配商品的视觉风格，并推荐一套统一方向 |
| 逐页商业文案 | 每张图都有有效信息，不生成无字空图，也不在详情页里使用 CTA 按钮 |
| 构图与排版控制 | 改变构图、景别、姿态、商品比例与文字层级，同时保持系列一致性 |
| 背景重构 | 把原图当作商品证据，根据商品特点重新建立更合适的视觉世界 |
| 生成后质检 | 检查商品一致性、人体、裁切、文字、事实、页面意义和整套节奏 |

## 平台兼容性

已通过 Codex Skill 格式校验，并在 macOS 的 Codex 中完成测试。Skill 核心使用可移植的 Markdown 指令和相对路径；Claude Code、OpenClaw、Linux 与 Windows 已完成静态检查，但尚未进行真实运行测试。

完整生图需要宿主 Agent 提供图片生成工具。可选的结构化方案校验器需要 Python 3.9 或更高版本；Windows 使用 `py -3 scripts\validate_product_brief.py <brief.json>`，macOS 与 Linux 使用 `python3 scripts/validate_product_brief.py <brief.json>`。

## 安装

把下面这句话发送给你的 Agent：

```text
帮我安装这个 Skill：
https://github.com/chemny/product-detail-images
```

Agent 会根据当前客户端完成安装、依赖检查和加载验证。

## 快速开始

安装后新建一个任务，发送：

```text
请用 $product-detail-images 处理这些商品图片。先识别主商品，推荐完整的图片数量和视觉风格，再把整套页面规划与文案给我确认，确认前不要生成图片。
```

Skill 会在正式生成前进行一次集中确认，不会把常规设计细节拆成多轮选择。

## 使用示例

```text
请用 $product-detail-images 为这条连衣裙规划完整的详情页图片。展示七种风格，推荐其中一种，并说明每一页承担什么成交任务。
```

```text
请用 $product-detail-images 处理这三张商品图，主商品是手提包。重新设计背景世界，在我确认方案后生成一套 8 张详情页图片。
```

```text
请用 $product-detail-images 为这款数码产品规划完整详情页。先盘点外观、接口、功能、配件、参数与兼容性证据，展示七种风格，并在我确认方案后生成。
```

```text
请用 $product-detail-images 复查这套已经生成的商品详情图，只指出失败的维度，并给出针对性的提示词修改方案。
```

## 工作流程

1. 锁定主商品，排除容易混淆的陪衬商品。
2. 分析可见特征、素材丰富度、证据与客观事实边界，并自动路由到适用的品类规则。
3. 建立完整成交叙事，选择最小但完整的 6、8 或 10 张页面骨架。
4. 比较七种视觉风格，推荐一套方向，并规划每页的图文关系。
5. 集中确认一次，再从头图开始分批生成。
6. 检查单图交付质量与整套创意质量，只修改失败的维度。

## 仓库结构

```text
product-detail-images/
├── SKILL.md
├── README.md
├── README.zh.md
├── LICENSE
├── agents/
│   └── openai.yaml
├── assets/
│   ├── fashion-series-hero.png
│   ├── fashion-series-lifestyle.png
│   ├── fashion-series-detail.png
│   └── product-detail-series-preview.png
├── references/
│   ├── background-system.md
│   ├── category-routing.md
│   ├── packaged-consumable-adapter.md
│   ├── electronics-adapter.md
│   ├── structured-durable-adapter.md
│   ├── poster-sequence.md
│   ├── style-packs.md
│   └── ...
└── scripts/
    └── validate_product_brief.py
```

## 使用要求

- 能够加载本地 Skill 的 Agent 客户端
- 用于最终出图的图片生成能力
- 商品图片，或足够具体的商品描述
- 仅在使用可选的结构化商品简报校验脚本时需要 Python 3

不使用校验脚本也可以完成主要规划流程。最终图片生成能力与具体表现取决于当前 Agent 客户端。

## 许可证

本项目使用 [MIT License](./LICENSE)。预览图是本仓库的原创虚构案例；用户上传的商品图片仍受其原始版权与使用授权约束。
