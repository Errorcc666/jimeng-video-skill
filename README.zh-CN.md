# jimeng-video-skill

这是一个给 **即梦（Jimeng）图生视频** 工作流使用的开源 Agent Skill。

它不是为了节省 GPT 的 token，而是把更多规划、连续性检查和风险判断放在生成之前，尽量减少昂贵的即梦重做次数。

## 默认流程

```text
故事题材 / 参考图
      ↓
GPT 完整故事大纲
      ↓
按自然剧情拆段（默认每段 15 秒）
      ↓
前后段连续性检查
      ↓
首帧图片 Prompt
      ↓
即梦图生视频 Prompt
      ↓
Cost Guard：LOW / MEDIUM / HIGH
      ↓
人工确认
      ↓
再交给即梦生成
```

## 主要能力

- 故事总长度不固定。
- 默认每个视频片段 15 秒，也可指定其他时长。
- 不机械切时间，优先按自然剧情节点拆段。
- 记录上一段 Ending State 与下一段 Beginning State。
- 首帧图片 Prompt 与视频 Prompt 分开。
- 检查多人复杂动作、手部/物体互动、复杂运镜、状态跳变等高风险因素。
- HIGH 风险默认先简化，再推荐送进即梦。
- 可选配合 `full-aigc-skills/jimeng-skills` 的 `jimeng-prompt-image2video` 使用。

## 安装

```bash
npx skills add Errorcc666/jimeng-video-skill --skill jimeng-video
```

也可以手动把：

```text
skills/jimeng-video/
```

复制到：

```text
~/.agents/skills/jimeng-video/
```

## 推荐安装即梦 Prompt Skill

```bash
npx skills add full-aigc-skills/jimeng-skills --skill jimeng-prompt-image2video
```

本项目负责“导演层”：大纲、15 秒拆段、连续性、风险判断；上游 Skill 可负责最终的即梦 Prompt wording。

## 使用

```text
jimeng-video outline
jimeng-video split
jimeng-video prompt 1
```

改变默认时长：

```text
jimeng-video split --seconds 10
```

## License

MIT。
