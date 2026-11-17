#!/bin/sh
# Start FigCraft with local control port so an agent can attach (live).
# Usage: ./start-figcraft-collab.sh
# Then tell the agent: "control poort 7979 staat open"

set -u
DESIGN_DIR="$(cd "$(dirname "$0")" && pwd)"
# design/ -> frontend/ -> repo root
ROOT="$(cd "$DESIGN_DIR/../.." && pwd)"
FILE="$DESIGN_DIR/figcraft/vrijzaak-storefront.figcraft"
PORT="${FIGCRAFT_CONTROL_PORT:-7979}"
APP="/Applications/FigCraft.app/Contents/MacOS/FigCraft"

if [ ! -x "$APP" ]; then
  echo "FigCraft niet gevonden: $APP" >&2
  exit 1
fi

if [ ! -f "$FILE" ]; then
  echo "Designbestand ontbreekt: $FILE" >&2
  exit 1
fi

echo "Start FigCraft (collab)"
echo "  file:    $FILE"
echo "  control: 127.0.0.1:$PORT (alleen deze Mac)"
echo "  read:    $ROOT"
echo "  write:   $DESIGN_DIR"
echo ""
echo "Laat dit terminalvenster open. Zeg in Warp: poort $PORT is actief."
echo ""

exec "$APP" \
  --control "$PORT" \
  --automation-read-root "$ROOT" \
  --automation-write-root "$DESIGN_DIR" \
  "$FILE"
