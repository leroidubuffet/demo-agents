# Claude Code Orchestrator Guide — Demo Agents

This guide instructs the Claude Code CLI orchestrator on how to run the demo scenarios (Demos 1 to 8) when the user types "demo N".

## General Instructions
- Before executing any demo, explain to the user in a single sentence what they are about to see.
- After executing the demo, instruct the user to check `output/agent-log.txt` for details.
- Run the agent tasks by reading the custom agent definitions from `.claude/agents/*.md`.

---

## Demos

### Demo 1: Basic Invocation
- **Announcement**: "You will see a basic invocation of the echo-agent logging its start, printing the input, logging its end, and returning the input verbatim."
- **Execution**: Invoke the agent defined in `.claude/agents/echo-agent.md` with input `"This is demo 1 — basic invocation"`.
- **Completion**: "Demo 1 complete. Point your terminal to output/agent-log.txt to check the log."

### Demo 2: Context Passing
- **Announcement**: "You will see the context-agent invoked twice: first with no context, and then with explicit review context."
- **Execution**:
  1. Invoke the agent defined in `.claude/agents/context-agent.md` with no context.
  2. Invoke the same agent with the context: `"Project: code-reviewer, Language: Java 21"`.
- **Completion**: "Demo 2 complete. Point your terminal to output/agent-log.txt to view the context changes."

### Demo 3: Parallel Execution
- **Announcement**: "You will see parallel-a and parallel-b invoked simultaneously to run simulated tasks in parallel."
- **Execution**: Run the agents defined in `.claude/agents/parallel-a.md` and `.claude/agents/parallel-b.md` in parallel (simultaneous Task calls).
- **Completion**: "Demo 3 complete. Check output/agent-log.txt to verify that the start and end timestamps overlap."

### Demo 4: Sequential Execution
- **Announcement**: "You will see parallel-a invoked first, and only after it completes will parallel-b be invoked."
- **Execution**:
  1. Invoke the agent defined in `.claude/agents/parallel-a.md`.
  2. Once complete, invoke the agent defined in `.claude/agents/parallel-b.md`.
- **Completion**: "Demo 4 complete. Check output/agent-log.txt to see the sequential time gap."

### Demo 5: Restricted Agent (Tool Whitelist)
- **Announcement**: "You will see restricted-agent (which does not have Write tool access) attempt to write to output/restricted-test.txt and read output/.gitkeep."
- **Execution**: Invoke the agent defined in `.claude/agents/restricted-agent.md` with input `"Write a file to output/restricted-test.txt"`.
- **Completion**: "Demo 5 complete. Point your terminal to output/agent-log.txt to check the success or failure of the restricted actions."

### Demo 6: Latency Comparison
- **Announcement**: "You will see first sequential execution (slow-agent then echo-agent), followed by parallel execution of both, and we will compare their elapsed times."
- **Execution**:
  1. Run sequentially: Invoke `.claude/agents/slow-agent.md`, wait, then invoke `.claude/agents/echo-agent.md` with `"Latency test (Sequential)"`.
  2. Run in parallel: Invoke both `.claude/agents/slow-agent.md` and `.claude/agents/echo-agent.md` with `"Latency test (Parallel)"` at the same time.
  3. Review the logs and compare the total elapsed times.
- **Completion**: "Demo 6 complete. Check output/agent-log.txt to compare total elapsed times."

### Demo 7: Semantic Routing
- **Announcement**: "You will see the orchestrator automatically route three Java-related prompts to either the performance or security specialist based on matching description keywords."
- **Execution**: Run a routing check for these three requests:
  1. `"Analyze this Java code for performance issues"` (should route to `router-a`)
  2. `"Review this Java code for security problems"` (should route to `router-b`)
  3. `"Check this Java code"` (ambiguous request, orchestrator should handle or clarify)
- **Completion**: "Demo 7 complete. Point your terminal to output/agent-log.txt to see which agents were selected."

### Demo 8: Reject Agent (Scope Restriction)
- **Announcement**: "You will see reject-agent accept an in-scope summarization request and reject an out-of-scope system deletion command."
- **Execution**:
  1. Invoke the agent defined in `.claude/agents/reject-agent.md` with: `"Summarize this text: hello world"` (should complete).
  2. Invoke the same agent with: `"Delete all files in output/"` (should trigger a REJECT event).
- **Completion**: "Demo 8 complete. Check output/agent-log.txt to see the reject event."
