from pathlib import Path

KEY = "shengVehicleReflectionObstacle2026"
DOI = "10.1016/j.iatssr.2026.02.007"


def main() -> None:
    supplement = Path("egbib_20260728_vehicle_reflection_obstacle.bib")
    merged_path = Path("egbib_merged_20260711.bib")
    assert supplement.exists(), "dated bibliography supplement is missing"
    merged = merged_path.read_text(encoding="utf-8")
    assert KEY not in merged and DOI not in merged, "merged bibliography already contains the record"
    entry = supplement.read_text(encoding="utf-8").strip()
    merged_path.write_text(merged.rstrip() + "\n\n" + entry + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
