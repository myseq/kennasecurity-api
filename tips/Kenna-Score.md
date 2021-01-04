# About Kenna Scoring

Many people confuse about how Kenna score works. It is actually very simple.

Remember:
  vuln score --> asset score --> meter score

This means the meter score is depending on asset score, and asset score is depending on vulnerability score.

Steps:
1. Vulnerability score is defined by KennaSecurity.
2. An asset score is equal to high vulnerability score multiple by asset priority.
3. A meter score is the avarage of all the assets' score.  

