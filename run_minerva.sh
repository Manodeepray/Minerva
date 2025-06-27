#!/bin/bash

SESSION="project_ui"
GREEN='\033[0;32m'
NC='\033[0m'

# Define ports used
FLASK_PORT=5000
FASTAPI_PORT=8000

echo -e "${GREEN}[INFO] Starting Flask on port $FLASK_PORT...${NC}"
nohup python flask_demo_app/app.py > flask.log 2>&1 &

echo -e "${GREEN}[INFO] Starting FastAPI on port $FASTAPI_PORT...${NC}"
nohup uvicorn status_server:app --reload > fastapi.log 2>&1 &

# Wait a bit to let them start
sleep 2

# Kill previous tmux session if exists
tmux kill-session -t $SESSION 2>/dev/null

# Start new tmux session and run Minerva
tmux new-session -d -s $SESSION -n UI
tmux send-keys -t $SESSION:0.0 "echo -e '${GREEN}[Minerva] Running Minerva.py${NC}'" C-m
tmux send-keys -t $SESSION:0.0 "python Minerva.py" C-m

# Split for Dashboard
tmux split-window -h -t $SESSION:0
tmux send-keys -t $SESSION:0.1 "echo -e '${GREEN}[Dashboard] Running dashboard.py${NC}'" C-m
tmux send-keys -t $SESSION:0.1 "python dashboard.py" C-m

# Resize Dashboard pane (right side)
tmux resize-pane -t $SESSION:0.1 -x 15

# Focus back on Minerva pane
tmux select-pane -t $SESSION:0.0

# Attach to session
tmux attach-session -t $SESSION

#######################################
# AFTER tmux is closed, clean up ports
#######################################

echo -e "${GREEN}[INFO] Cleaning up ports...${NC}"

# Function to kill a port process
kill_port() {
  PORT=$1
  PID=$(lsof -t -i:$PORT)
  if [ -n "$PID" ]; then
    echo -e "${GREEN}Killing process on port $PORT (PID $PID)...${NC}"
    kill -9 $PID
  else
    echo -e "${GREEN}No process found on port $PORT.${NC}"
  fi
}

kill_port $FLASK_PORT
kill_port $FASTAPI_PORT

echo -e "${GREEN}[DONE] All services cleaned up.${NC}"
