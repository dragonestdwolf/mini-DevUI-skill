#!/bin/bash
LOG="/Users/zlm/code/.cursor/debug.log"
echo "{\"id\":\"wrap_1\",\"timestamp\":$(($(date +%s)*1000)),\"message\":\"run_mcp.sh started\",\"hypothesisId\":\"H1\"}" >> "$LOG"
cd /Users/zlm/code/icon-feed-mcp
exec python server.py
