import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Vibestar｜企业主 AI 团队课',
  description: '从会用 AI 到搭建 AI 团队创造 ROI 的 3 小时企业主实战课。',
  lang: 'zh-CN',
  cleanUrls: true,
  base: '/vibestar/',
  head: [
    ['meta', { name: 'theme-color', content: '#071b36' }]
  ],
  themeConfig: {
    logo: '/logo.png',
    nav: [
      { text: '首页', link: '/' },
      { text: '课前准备', link: '/preflight/' },
      { text: '3小时课程', link: '/course/' },
      { text: '课堂演示', link: '/demos/' },
      { text: '90天路径', link: '/roadmap-90-days/' }
    ],
    sidebar: {
      '/preflight/': [
        {
          text: '课前准备',
          items: [
            { text: '开始前：只装两项', link: '/preflight/' },
            { text: 'Windows', link: '/preflight/windows' },
            { text: 'macOS', link: '/preflight/macos' }
          ]
        }
      ],
      '/course/': [
        {
          text: '3 小时课程路线',
          items: [
            { text: '总览｜180 分钟路线', link: '/course/' },
            { text: '0｜AI Age', link: '/course/chapter-0' },
            { text: '1｜用上最强模型', link: '/course/chapter-1' },
            { text: '2｜选择合适架构', link: '/course/chapter-2' },
            { text: '3｜让 AI 会用工具', link: '/course/chapter-3' },
            { text: '4｜Harness 到 Loop', link: '/course/chapter-4' },
            { text: '5｜Graph 与 Agent Team', link: '/course/chapter-5' }
          ]
        }
      ],
      '/demos/': [
        {
          text: '课堂演示与录屏',
          items: [
            { text: '演示总览', link: '/demos/' },
            { text: '01｜Notion 四种保存方式', link: '/demos/notion' },
            { text: '02｜小游戏公司 Harness', link: '/demos/harness' },
            { text: '03｜TradingAgents / NVDA', link: '/demos/tradingagents' }
          ]
        }
      ],
      '/roadmap-90-days/': [
        {
          text: '课后 90 天',
          items: [
            { text: '从数字员工到 AI 团队', link: '/roadmap-90-days/' },
            { text: '90 天 AI 数字员工经营手册', link: '/roadmap-90-days/ceo-agent-operating-manual' }
          ]
        }
      ]
    },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/ChannelCMT/vibestar' }
    ],
    footer: {
      message: 'Vibestar · 企业主 AI 团队实战课',
      copyright: 'Copyright © 2026 Vibestar'
    },
    outline: { level: [2, 3], label: '本页内容' },
    docFooter: { prev: '上一页', next: '下一页' },
    returnToTopLabel: '回到顶部'
  }
})
