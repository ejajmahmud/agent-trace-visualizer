"""Tests for agent-trace-visualizer."""
import unittest
from agent_trace_visualizer.visualizer import TraceVisualizer


class TestTraceVisualizer(unittest.TestCase):
    def setUp(self):
        self.v = TraceVisualizer()

    def test_svg_generation(self):
        spans = [{"name": "tool_a", "start_ms": 10, "end_ms": 50}]
        svg = self.v.generate_svg_timeline(spans)
        self.assertIn("<svg", svg)
        self.assertIn("tool_a", svg)
        self.assertIn("40ms", svg)


if __name__ == "__main__":
    unittest.main()
