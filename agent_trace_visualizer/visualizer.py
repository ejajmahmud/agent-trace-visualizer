"""Interactive SVG Gantt timeline visualizer for agent traces."""
from typing import List, Dict, Any


class TraceVisualizer:
    def generate_svg_timeline(self, spans: List[Dict[str, Any]]) -> str:
        if not spans:
            return '<svg width="400" height="100"><text x="20" y="50" fill="#fff">No spans</text></svg>'

        min_time = min(s.get("start_ms", 0) for s in spans)
        max_time = max(s.get("end_ms", 100) for s in spans)
        total_duration = max(1, max_time - min_time)

        svg_bars = []
        chart_width = 600
        y = 40

        for i, s in enumerate(spans):
            start = s.get("start_ms", 0) - min_time
            dur = max(10, s.get("end_ms", 10) - s.get("start_ms", 0))
            x = 100 + int((start / total_duration) * (chart_width - 120))
            w = max(10, int((dur / total_duration) * (chart_width - 120)))
            name = s.get("name", f"span_{i}")

            svg_bars.append(f"""
            <text x="10" y="{y + 14}" fill="#94a3b8" font-size="11" font-family="sans-serif">{name}</text>
            <rect x="{x}" y="{y}" width="{w}" height="20" rx="4" fill="#38bdf8"/>
            <text x="{x + 6}" y="{y + 14}" fill="#0f172a" font-size="10" font-weight="700" font-family="sans-serif">{dur}ms</text>
            """)
            y += 32

        svg_height = y + 20
        return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{chart_width}" height="{svg_height}" style="background:#0f172a">
        <text x="20" y="24" fill="#f8fafc" font-size="14" font-weight="700" font-family="sans-serif">Agent Execution Timeline</text>
        {''.join(svg_bars)}
        </svg>"""
