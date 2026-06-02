#!/usr/bin/env python3
"""
Build Feasibility Assessment (Build Lens)

Scores ideas on technical buildability — separate from opportunity / passive-income scoring.
See frameworks/build-feasibility-matrix.md for criteria.
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
MODELS_DIR = REPO_ROOT / "ml-engine" / "models"
TRAINING_FILE = MODELS_DIR / "build_feasibility_training.json"

WEIGHTS = {
    "technical_viability": 0.25,
    "build_complexity": 0.25,
    "infrastructure_fit": 0.15,
    "scale_architecture": 0.20,
    "technical_risk": 0.10,
    "ops_maintainability": 0.05,
}

SCORE_PATTERNS = {
    "technical_viability": r"Technical Viability:\s*(\d+)\s*/\s*10",
    "build_complexity": r"Build Complexity:\s*(\d+)\s*/\s*10",
    "infrastructure_fit": r"Infrastructure Fit:\s*(\d+)\s*/\s*10",
    "scale_architecture": r"Scale Architecture:\s*(\d+)\s*/\s*10",
    "technical_risk": r"Technical Risk:\s*(\d+)\s*/\s*10",
    "ops_maintainability": r"Ops Maintainability:\s*(\d+)\s*/\s*10",
}


class BuildFeasibilityAssessor:
    def __init__(self, repo_root=None):
        self.repo_root = Path(repo_root) if repo_root else REPO_ROOT
        self.models_dir = self.repo_root / "ml-engine" / "models"
        self.models_dir.mkdir(parents=True, exist_ok=True)
        self.training_file = self.models_dir / "build_feasibility_training.json"
        self.training_data = self._load_training_data()

    def _load_training_data(self):
        if self.training_file.exists():
            with open(self.training_file, "r") as f:
                return json.load(f)
        return []

    def _save_training_data(self):
        with open(self.training_file, "w") as f:
            json.dump(self.training_data, f, indent=2)

    def extract_scores(self, content):
        scores = {}
        for key, pattern in SCORE_PATTERNS.items():
            match = re.search(pattern, content, re.IGNORECASE)
            scores[key] = int(match.group(1)) if match else 0
        return scores

    def extract_metadata(self, content):
        metadata = {}
        linked = re.search(r"\*\*Linked Idea:\*\*\s*\[.*?\]\((.*?)\)", content)
        if linked:
            metadata["linked_idea"] = linked.group(1)
        status = re.search(r"\*\*Status:\*\*\s*(.+)", content)
        if status:
            metadata["status"] = status.group(1).split("|")[0].strip()
        return metadata

    def calculate_score(self, scores):
        total = sum(scores.get(k, 0) * w * 10 for k, w in WEIGHTS.items())
        return round(total, 1)

    def get_verdict(self, score):
        if score >= 80:
            return {
                "verdict": "buildable",
                "action": "Proceed to MVP",
                "priority": "HIGH",
                "next_steps": [
                    "Lock MVP scope from this assessment",
                    "Create or update PLAN.md in target repo",
                    "Set up dev environment and spike any remaining unknowns in parallel",
                ],
            }
        if score >= 60:
            return {
                "verdict": "spike_first",
                "action": "Run time-boxed spike",
                "priority": "MEDIUM",
                "next_steps": [
                    "Execute spike plan in Unknowns section",
                    "Re-run assess.py after spike",
                    "Do not start full MVP until blockers cleared",
                ],
            }
        if score >= 40:
            return {
                "verdict": "defer",
                "action": "Defer build",
                "priority": "LOW",
                "next_steps": [
                    "Document blockers in Technical Risks",
                    "Revisit when infra or skills gap closes",
                    "Keep opportunity score separate — may still be worth market validation only",
                ],
            }
        return {
            "verdict": "not_buildable",
            "action": "Not buildable (now)",
            "priority": "NONE",
            "next_steps": [
                "Archive or pivot architecture",
                "Extract lessons to knowledge-base",
                "Do not invest MVP time until fundamentals change",
            ],
        }

    def analyze_dimensions(self, scores):
        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        strengths = [
            f"{k.replace('_', ' ').title()}: {v}/10"
            for k, v in sorted_scores[:2]
            if v >= 7
        ]
        blockers = [
            f"{k.replace('_', ' ').title()}: {v}/10"
            for k, v in sorted_scores
            if v <= 5 and v > 0
        ]
        missing = [k.replace("_", " ").title() for k, v in scores.items() if v == 0]
        return strengths, blockers, missing

    def assess(self, md_file):
        md_path = Path(md_file)
        if not md_path.is_absolute():
            md_path = self.repo_root / md_path

        if not md_path.exists():
            print(f"❌ Error: File not found: {md_path}")
            return None

        content = md_path.read_text()
        scores = self.extract_scores(content)
        metadata = self.extract_metadata(content)
        total = self.calculate_score(scores)
        verdict = self.get_verdict(total)
        strengths, blockers, missing = self.analyze_dimensions(scores)

        print(f"\n{'='*60}")
        print(f"🔧 BUILD FEASIBILITY: {md_path.stem}")
        print(f"{'='*60}\n")
        print(f"📈 BUILD FEASIBILITY SCORE: {total}/100")
        print(f"🎬 VERDICT: {verdict['verdict']} — {verdict['action']}")
        print(f"⚡ PRIORITY: {verdict['priority']}")

        if metadata.get("linked_idea"):
            print(f"🔗 Linked idea: {metadata['linked_idea']}")

        if strengths:
            print("\n✅ ENGINEERING STRENGTHS:")
            for s in strengths:
                print(f"   • {s}")

        if blockers:
            print("\n⚠️  BLOCKERS / WEAK DIMENSIONS:")
            for b in blockers:
                print(f"   • {b}")

        if missing:
            print("\n❓ UNSCORED (fill in template):")
            for m in missing:
                print(f"   • {m}")

        print("\n📋 NEXT STEPS:")
        for i, step in enumerate(verdict["next_steps"], 1):
            print(f"   {i}. {step}")

        entry = {
            "assessment_id": md_path.stem,
            "date_assessed": datetime.now().isoformat(),
            "linked_idea": metadata.get("linked_idea"),
            "scores": scores,
            "build_feasibility_score": total,
            "verdict": verdict["verdict"],
            "outcome": "pending",
            "actual_build_weeks": None,
        }
        self.training_data.append(entry)
        self._save_training_data()
        print(f"\n💾 Saved to {self.training_file.name}")
        print(f"{'='*60}\n")

        return {
            "build_feasibility_score": total,
            "verdict": verdict,
            "scores": scores,
            "strengths": strengths,
            "blockers": blockers,
        }

    def rank_assessments(self, directory=None):
        directory = Path(directory) if directory else self.repo_root / "ideas" / "feasibility"
        if not directory.is_absolute():
            directory = self.repo_root / directory

        if not directory.exists():
            print(f"❌ Directory not found: {directory}")
            return []

        files = sorted(
            f for f in directory.glob("*.md")
            if f.name.lower() != "readme.md"
        )
        if not files:
            print(f"No assessments in {directory}")
            return []

        print(f"\n{'='*60}")
        print("🔧 BUILD FEASIBILITY RANKINGS")
        print(f"{'='*60}\n")
        print(f"{'Rank':<6} {'Assessment':<45} {'Score':<8} {'Verdict'}")
        print(f"{'-'*6} {'-'*45} {'-'*8} {'-'*20}")

        rows = []
        for f in files:
            content = f.read_text()
            scores = self.extract_scores(content)
            total = self.calculate_score(scores)
            verdict = self.get_verdict(total)["verdict"]
            rows.append({"name": f.stem, "score": total, "verdict": verdict})

        rows.sort(key=lambda x: x["score"], reverse=True)
        for i, row in enumerate(rows, 1):
            print(f"{i:<6} {row['name'][:45]:<45} {row['score']:<8.1f} {row['verdict']}")

        print(f"\n{'='*60}\n")
        return rows


def main():
    assessor = BuildFeasibilityAssessor()
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python assess.py <build-feasibility.md>   # Assess one file")
        print("  python assess.py rank [directory]        # Rank assessments")
        sys.exit(1)

    if sys.argv[1] == "rank":
        directory = sys.argv[2] if len(sys.argv) > 2 else None
        assessor.rank_assessments(directory)
    else:
        assessor.assess(sys.argv[1])


if __name__ == "__main__":
    main()
