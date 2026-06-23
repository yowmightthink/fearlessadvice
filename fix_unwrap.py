import re

js = open("src/engine/game.js").read()

start_str1 = """(function() {
// --- Fearless Advice Engine ---
// Unified and isolated environment
"""

start_str2 = """
(function() {
// --- Fearless Advice Engine ---
// Unified and isolated environment
"""

if js.startswith(start_str1):
    js = js[len(start_str1):]
if js.startswith(start_str2):
    js = js[len(start_str2):]

open("src/engine/game.js", "w").write(js)
print("Fixed unwrap!")
