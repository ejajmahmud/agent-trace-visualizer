"""CLI for agent-trace-visualizer."""
import sys
import argparse
from .visualizer import TraceVisualizer


def main():
    parser = argparse.ArgumentParser(description="Agent Trace Visualizer")
    parser.add_argument("--demo", action="store_true", help="Generate demo SVG")
    args = parser.parse_args()

    v = TraceVisualizer()
    spans = [
        {"name": "fetch_doc", "start_ms": 0, "end_ms": 120},
        {"name": "parse_sql", "start_ms": 130, "end_ms": 250}
    ]
    svg = v.generate_svg_timeline(spans)
    print(svg)
    sys.exit(0)


if __name__ == "__main__":
    main()
