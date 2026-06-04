# Orchestrator Guide for Demo Agents

Welcome! This guide instructs the orchestrator on how to execute demonstrations when the user requests a demo.

## Execution Flow Rules

For any demo:
1. **Pre-Demo Announcement**: Before running the demo steps, output a single sentence explaining to the user what they are about to see.
2. **Post-Demo Signoff**: After running the demo steps, print a message pointing the user to check `output/agent-log.txt` for details.
3. **Trigger**: Respond when the user inputs `demo N` (where N is 1 to 8).

---

## Demo Configurations

### Demo 1: Basic Invocation
- **Pre-Demo**: "You will see a basic invocation of the echo-agent logging its start, printing the input, logging its end, and returning the input verbatim."
- **Execution**: Invoke `echo-agent` with the input: `"This is demo 1 — basic invocation"`
- **Post-Demo**: "Demo 1 complete. You can view the invocation logs in output/agent-log.txt."

### Demo 2: Context Passing
- **Pre-Demo**: "You will see context-agent run twice, showing the difference in logs when context parameters are provided versus when they are absent."
- **Execution**:
  1. Invoke `context-agent` with no context.
  2. Invoke `context-agent` with the explicit context: `"Project: code-reviewer, Language: Java 21"`
- **Post-Demo**: "Demo 2 complete. Notice the difference in logs between the two runs in output/agent-log.txt."

### Demo 3: Parallel Execution
- **Pre-Demo**: "You will see parallel-a and parallel-b invoked simultaneously to demonstrate parallel task processing."
- **Execution**: Launch tasks for `parallel-a` and `parallel-b` concurrently.
- **Post-Demo**: "Demo 3 complete. Check output/agent-log.txt to verify that both agents executed at the same time."

### Demo 4: Sequential Execution
- **Pre-Demo**: "You will see parallel-a execute first, followed by parallel-b executing only after the first one completes."
- **Execution**:
  1. Invoke `parallel-a` and wait for it to complete.
  2. Invoke `parallel-b` and wait for it to complete.
- **Post-Demo**: "Demo 4 complete. Check the timestamps in output/agent-log.txt to see the sequential gap."

### Demo 5: Tool Whitelist / Restriction
- **Pre-Demo**: "You will see restricted-agent attempt a file write operation using Bash when Write tool access is excluded."
- **Execution**: Invoke `restricted-agent` with the input: `"Write a file to output/restricted-test.txt"`
- **Post-Demo**: "Demo 5 complete. Check output/agent-log.txt to see if the write failed or succeeded under restrictions."

### Demo 6: Latency / Comparison
- **Pre-Demo**: "You will see a comparison of sequential vs. parallel executions using slow-agent and echo-agent to demonstrate time savings."
- **Execution**:
  1. Run sequentially: Invoke `slow-agent`, wait, then invoke `echo-agent` with `"Latency test (Sequential)"`.
  2. Run in parallel: Launch both `slow-agent` and `echo-agent` with `"Latency test (Parallel)"` at the same time.
  3. Compare elapsed times using timestamps.
- **Post-Demo**: "Demo 6 complete. Check output/agent-log.txt to compare the elapsed times of sequential vs. parallel runs."

### Demo 7: Semantic Routing
- **Pre-Demo**: "You will see three separate Java requests routed automatically to the appropriate specialized agents based on description matching."
- **Execution**: Submit these three requests sequentially to the orchestrator's routing pipeline:
  1. `"Analyze this Java code for performance issues"` (routes to `router-a`)
  2. `"Review this Java code for security problems"` (routes to `router-b`)
  3. `"Check this Java code"` (ambiguous request, orchestrator resolves or prompts)
- **Post-Demo**: "Demo 7 complete. View output/agent-log.txt to see which router agents were selected for each prompt."

### Demo 8: Reject / Scope Verification
- **Pre-Demo**: "You will see reject-agent accept an in-scope summarization request and refuse an out-of-scope system deletion request."
- **Execution**:
  1. Invoke `reject-agent` with `"Summarize this text: hello world"` (should log START and summarize).
  2. Invoke `reject-agent` with `"Delete all files in output/"` (should log REJECT and fail/refuse).
- **Post-Demo**: "Demo 8 complete. Check output/agent-log.txt to see the REJECT event and the summary event."
