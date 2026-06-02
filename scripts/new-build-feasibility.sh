#!/usr/bin/env bash
# Create a Build Feasibility Assessment from an existing idea file or slug.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TEMPLATE="$REPO_ROOT/frameworks/build-feasibility-template.md"
FEASIBILITY_DIR="$REPO_ROOT/ideas/feasibility"
DATE="$(date +%Y-%m-%d)"

usage() {
  echo "Usage: $0 <idea-slug-or-path> [assessment-name]"
  echo ""
  echo "Examples:"
  echo "  $0 2026-01-05-passive-income-lab-as-saas"
  echo "  $0 ideas/evaluated/2026-01-29-bni-chapter-toolkit.md"
  exit 1
}

[[ $# -ge 1 ]] || usage

INPUT="$1"
CUSTOM_NAME="${2:-}"

# Resolve source idea path
if [[ -f "$INPUT" ]]; then
  IDEA_PATH="$INPUT"
  SLUG="$(basename "$INPUT" .md)"
elif [[ -f "$REPO_ROOT/ideas/evaluated/$INPUT.md" ]]; then
  IDEA_PATH="ideas/evaluated/$INPUT.md"
  SLUG="$INPUT"
elif [[ -f "$REPO_ROOT/ideas/brainstorm/$INPUT.md" ]]; then
  IDEA_PATH="ideas/brainstorm/$INPUT.md"
  SLUG="$INPUT"
elif [[ -f "$REPO_ROOT/ideas/in-progress/$INPUT.md" ]]; then
  IDEA_PATH="ideas/in-progress/$INPUT.md"
  SLUG="$INPUT"
else
  echo "❌ Idea not found: $INPUT"
  echo "   Looked in ideas/evaluated, brainstorm, in-progress"
  exit 1
fi

# Derive idea title from first heading
IDEA_TITLE="$(grep -m1 '^# ' "$REPO_ROOT/$IDEA_PATH" 2>/dev/null | sed 's/^# //' || echo "$SLUG")"
ASSESSMENT_SLUG="${CUSTOM_NAME:-${SLUG}-build-feasibility}"
OUT="$FEASIBILITY_DIR/$ASSESSMENT_SLUG.md"

mkdir -p "$FEASIBILITY_DIR"

if [[ -f "$OUT" ]]; then
  echo "❌ Assessment already exists: $OUT"
  exit 1
fi

cp "$TEMPLATE" "$OUT"

# Portable sed (macOS + Linux)
sed_inplace() {
  if sed --version >/dev/null 2>&1; then
    sed -i "$@"
  else
    sed -i '' "$@"
  fi
}

sed_inplace "s/\\[Idea Name\\]/$IDEA_TITLE/" "$OUT"
sed_inplace "s/YYYY-MM-DD/$DATE/g" "$OUT"
sed_inplace "s|ideas/evaluated/YYYY-MM-DD-idea-name.md|$IDEA_PATH|g" "$OUT"
sed_inplace "s|../evaluated/YYYY-MM-DD-idea-name.md|../${IDEA_PATH#ideas/}|g" "$OUT"

echo "✅ Created: $OUT"
echo ""
echo "Next steps:"
echo "  1. Fill in technical sections and scores in the new file"
echo "  2. python3 ml-engine/build-feasibility/assess.py $OUT"
echo ""
echo "Reminder: Run opportunity evaluation separately:"
echo "  python3 ml-engine/idea-scorer/evaluate.py $IDEA_PATH"
