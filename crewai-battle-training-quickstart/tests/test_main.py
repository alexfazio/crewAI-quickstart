import json
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from unittest.mock import patch

import main


class ArenaExampleTests(unittest.TestCase):
    def test_ladder_limits_output_and_preserves_observations(self):
        fixture = {"updated_at": 123, "entries": [
            {"rank": 1, "bot": "a", "rating": 1500, "wins": 2, "private": "omit"},
            {"rank": 2, "bot": "b", "rating": 1400},
        ]}
        with patch.object(main, "fetch_json", return_value=fixture):
            result = main.ladder_snapshot(1)
        self.assertEqual(len(result["entries"]), 1)
        self.assertEqual(result["entries"][0]["rating"], 1500)
        self.assertNotIn("private", result["entries"][0])
        self.assertEqual(result["updated_at"], 123)

    def test_rejects_invalid_name_before_request(self):
        with patch.object(main, "fetch_json") as fetch:
            with self.assertRaises(ValueError):
                main.bot_snapshot("../api/me")
            fetch.assert_not_called()

    def test_bot_preserves_house_status_and_does_not_guess_missing_status(self):
        fixture = {"name": "house-starter", "house": True, "ladders": [], "theaters": {}}
        with patch.object(main, "fetch_json", return_value=fixture):
            self.assertTrue(main.bot_snapshot("house-starter")["house"])
        fixture.pop("house")
        with patch.object(main, "fetch_json", return_value=fixture):
            self.assertIsNone(main.bot_snapshot("house-starter")["house"])

    def test_malformed_rows_are_reported_to_the_agent(self):
        with patch.object(main, "fetch_json", return_value={"entries": [None]}):
            result = json.loads(main.LadderTool()._run())
        self.assertIn("must be a list of objects", result["error"])

    def test_arena_redirect_is_not_followed(self):
        requested_paths = []

        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                requested_paths.append(self.path)
                if self.path == "/redirect":
                    self.send_response(302)
                    self.send_header("Location", "/other-origin-like-target")
                    self.end_headers()
                else:
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(b"{}")

            def log_message(self, *_args):
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            with patch.object(main, "BASE", f"http://127.0.0.1:{server.server_port}"):
                with self.assertRaisesRegex(RuntimeError, "Arena request failed"):
                    main.fetch_json("/redirect")
        finally:
            server.shutdown()
            thread.join()
            server.server_close()
        self.assertEqual(requested_paths, ["/redirect"])

    def test_cup_output_includes_real_qualification_fields(self):
        fixture = {"name": "Cup", "status": "open", "entry": {"min_sets_to_qualify": 100},
                   "standings": [{"bot": "a", "qualified": False, "sets_to_qualify": 88}]}
        with patch.object(main, "fetch_json", return_value=fixture):
            result = main.cup_snapshot()
        self.assertEqual(result["entry"]["min_sets_to_qualify"], 100)
        self.assertEqual(result["standings"][0]["sets_to_qualify"], 88)
        self.assertFalse(result["standings"][0]["qualified"])

    def test_tool_returns_error_instead_of_fabricating_data(self):
        with patch.object(main, "fetch_json", side_effect=RuntimeError("Arena request failed")):
            result = json.loads(main.BotTool()._run("house-starter"))
        self.assertEqual(result, {"error": "Arena request failed"})

    def test_ladder_limit_is_validated(self):
        with self.assertRaises(ValueError):
            main.ladder_snapshot(21)

    def test_crew_registers_tools_without_making_requests(self):
        with patch.object(main, "fetch_json") as fetch:
            crew = main.build_crew("house-starter")
        self.assertEqual({t.name for t in crew.agents[0].tools}, {"arena_bot", "arena_ladder", "arena_november_cup"})
        self.assertIn("house bots", crew.tasks[0].description)
        self.assertIn("rated sets", crew.tasks[0].description)
        fetch.assert_not_called()


if __name__ == "__main__":
    unittest.main()
