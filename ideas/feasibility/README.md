# Build Feasibility Assessments

**Build Lens** artifacts live here — separate from opportunity scoring in `ideas/evaluated/`.

Each file assesses: *Can we build and operate this?* (not *Will it make money?*)

## Create

```bash
./scripts/new-build-feasibility.sh <idea-slug-or-path>
```

## Score

```bash
python3 ml-engine/build-feasibility/assess.py ideas/feasibility/<name>.md
python3 ml-engine/build-feasibility/assess.py rank
```

## Workflow

See [docs/build-feasibility-workflow.md](../docs/build-feasibility-workflow.md).
