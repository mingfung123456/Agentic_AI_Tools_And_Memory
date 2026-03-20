1. update the claude code
2. brew install tmux
3. 
'''
cat > ~/.claude/settings.json << 'EOF'
{
	"env": {
	"CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
	},
	"preferences": {
	"tmuxSplitPanes": true
	}
}
EOF
'''
4. cd to your-project
5. run the command "tmux new-session -s claude-work"
6. claude
7. prepare the prompt (keyword - Create a team, ..  with 4 parallel agents )
'''
# KAN-75 Open Banking Research - Agent Team Prompt
Research direct bank connections via Plaid (US) and Flinks (Canada) for auto-importing transactions into our bookkeeping app (Next.js 14 + Supabase, Canada-first, targeting 1000 users → YC March 2026).
Create a team called 'kan-75-research' with 2 parallel agents, then aggregate their findings into
'docs/research/KAN-75-open-banking-research.md'.
And here is the JIRA ticket• number where you can access to get•the• ticket context: • KAN-75|
## Agent 1 - Business & Product
**Name:** 'business-product'
**Model:** GLM-5
**Sub-agent type:** 'product-strategy-advisor'

Use web search to gather competitor and market data. Output structured tables, not prose.
- Competitor comparison matrix: Wave, QuickBooks, FreshBooks, Bench, Hurdlr - which open banking providers each uses, pricing tier that includes bank connections, connection limits
- Plaid vs Flinks product-market fit for Canada-first strategy (coverage of Big 5 banks, credit unions, fintechs)
- User experience comparison:cnnection flow steps, re-auth frequency, failure modes, time-to-first-transaction
- Impact analysis table: projected effect on retention, paid conversion, and churn with/without bank connections
- YC narrative angle: how bank connections strengthen "AI bookkeeper" positioning vs "receipt scanner"
## Agent 2 - Financial & Cost
**Name:** 'financial-cost'
**Model:** GLM-5
**Sub-agent type:** 'general-purpose"
Use web search for current Plaid and Flinks pricing. Frame all projections for build-for-longevity - model costs at scale, not just launch.
- Plaid pricing: per-connection fees, API call costs, free tier / startup program limits, enterprise discounts
- Flinks pricing: per-connection, monthly minimums, startup deals
- Cost projection table at **100 / 1,000 / 10,000 / 1,000, 000** connected users for each provider
- Breakeven analysis: can bank connections be gated to paid tiers only? At what user count does provider cost exceed subscription revenue?
- Compare against current AI credit costs (Gemini Flash) - is open banking a larger or smaller cost line?
- Dual-provider cost model: Flinks for Canada + Plaid for US, vs single provider for both markets
## Lead Synthesis (You - GLM-5)
After all 2 agents report back, write the final report to 'docs/research/KAN-75-open-banking-
research.md' containing:
1. **GS / No-Go recommendation** with rationale
2. **Frovider recommendation** - Plaid, Flinks, both, or alternative (with reasoning)
3. **Cost summary table** - per provider, per user tier (100 / 1K / 10K / 1M)
4. **Architecture recommendation** - include the Mermaid diagram and abstraction layer design
5. **Risk register** - from Agent 4's devil's advocate analysis, with mitigations
6. **Implementation phases** - suggested rollout plan with effort estimates
'''