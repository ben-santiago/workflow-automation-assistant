# Workflow Automation Assistant

This repo is where Ben and Claude design, document, and automate Ben's daily
workflows (content creation, design, social, project management).

## How to work here
- Each real workflow gets a file in `workflows/` (copy `workflows/_TEMPLATE.md`).
- When a workflow has run well by hand 2-3 times, turn its repeatable steps into
  a skill in `.claude/skills/<name>/SKILL.md`.
- Only create a subagent in `.claude/agents/` when a step needs its own
  isolated context, a restricted tool set, or should run in parallel.
- Default to read-only connector actions. Anything that publishes, schedules,
  sends, or deletes (posting to Metricool, sharing Drive files, changing a live
  website) needs Ben's explicit OK unless the workflow file says otherwise.

## Connectors
Status lives in `workflows/CONNECTORS.md`. Check it before proposing an
automation, and say plainly when a step has no connector and needs Zapier or
stays manual.
