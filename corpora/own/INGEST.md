# Ingest report

Written by `uv run p2 ingest`.
It lists every document in this corpus that ingest added, with what the cleaning pass did and anything that looks wrong.
Running ingest again adds to the table and replaces the "last run" section, and `uv run p2 ingest --report` rewrites it for the documents in docs/ now, after you removed some.

## Summary

- Documents: 310 (the final check needs at least 200)
- Words: 365,128
- Estimated tokens (words times 1.4): 511,179 (`p2 check` warns above 800,000 and fails above 1,000,000)
- Flagged documents: 51

## Documents

| docid | words | characters per page | flags | cleaning |
|---|---:|---:|---|---|
| `cfr29-1926.1` | 73 | - | - | - |
| `cfr29-1926.10` | 137 | - | - | - |
| `cfr29-1926.100` | 219 | - | - | - |
| `cfr29-1926.1000` | 455 | - | - | - |
| `cfr29-1926.1001` | 258 | - | - | - |
| `cfr29-1926.1002` | 358 | - | - | - |
| `cfr29-1926.1003` | 272 | - | - | - |
| `cfr29-1926.101` | 64 | - | - | - |
| `cfr29-1926.102` | 690 | - | - | - |
| `cfr29-1926.103` | 25 | - | very short (25 words) | - |
| `cfr29-1926.104` | 234 | - | - | - |
| `cfr29-1926.105` | 233 | - | - | - |
| `cfr29-1926.1050` | 867 | - | - | - |
| `cfr29-1926.1051` | 247 | - | - | - |
| `cfr29-1926.1052` | 989 | - | - | - |
| `cfr29-1926.1053` | 2,885 | - | - | - |
| `cfr29-1926.106` | 114 | - | - | - |
| `cfr29-1926.1060` | 170 | - | - | - |
| `cfr29-1926.107` | 144 | - | - | - |
| `cfr29-1926.1071` | 25 | - | very short (25 words) | - |
| `cfr29-1926.1072` | 23 | - | very short (23 words) | - |
| `cfr29-1926.1076` | 26 | - | very short (26 words) | - |
| `cfr29-1926.1080` | 25 | - | very short (25 words) | - |
| `cfr29-1926.1081` | 24 | - | very short (24 words) | - |
| `cfr29-1926.1082` | 25 | - | very short (25 words) | - |
| `cfr29-1926.1083` | 24 | - | very short (24 words) | - |
| `cfr29-1926.1084` | 24 | - | very short (24 words) | - |
| `cfr29-1926.1085` | 25 | - | very short (25 words) | - |
| `cfr29-1926.1086` | 24 | - | very short (24 words) | - |
| `cfr29-1926.1087` | 23 | - | very short (23 words) | - |
| `cfr29-1926.1090` | 23 | - | very short (23 words) | - |
| `cfr29-1926.1091` | 24 | - | very short (24 words) | - |
| `cfr29-1926.11` | 223 | - | - | - |
| `cfr29-1926.1101__part01` | 4,009 | - | - | reference list dropped, 2,970 characters (heading) |
| `cfr29-1926.1101__part02` | 4,100 | - | - | reference list dropped, 2,970 characters (heading) |
| `cfr29-1926.1101__part03` | 4,002 | - | - | reference list dropped, 2,970 characters (heading) |
| `cfr29-1926.1101__part04` | 4,001 | - | - | reference list dropped, 2,970 characters (heading) |
| `cfr29-1926.1101__part05` | 4,004 | - | - | reference list dropped, 2,970 characters (heading) |
| `cfr29-1926.1101__part06` | 4,021 | - | - | reference list dropped, 2,970 characters (heading) |
| `cfr29-1926.1101__part07` | 4,015 | - | - | reference list dropped, 2,970 characters (heading) |
| `cfr29-1926.1101__part08` | 4,032 | - | - | reference list dropped, 2,970 characters (heading) |
| `cfr29-1926.1101__part09` | 3,931 | - | - | reference list dropped, 2,970 characters (heading) |
| `cfr29-1926.1102` | 29 | - | very short (29 words) | - |
| `cfr29-1926.1103` | 26 | - | very short (26 words) | - |
| `cfr29-1926.1104` | 23 | - | very short (23 words) | - |
| `cfr29-1926.1106` | 25 | - | very short (25 words) | - |
| `cfr29-1926.1107` | 26 | - | very short (26 words) | - |
| `cfr29-1926.1108` | 24 | - | very short (24 words) | - |
| `cfr29-1926.1109` | 23 | - | very short (23 words) | - |
| `cfr29-1926.1110` | 23 | - | very short (23 words) | - |
| `cfr29-1926.1111` | 23 | - | very short (23 words) | - |
| `cfr29-1926.1112` | 23 | - | very short (23 words) | - |
| `cfr29-1926.1113` | 23 | - | very short (23 words) | - |
| `cfr29-1926.1114` | 23 | - | very short (23 words) | - |
| `cfr29-1926.1115` | 23 | - | very short (23 words) | - |
| `cfr29-1926.1116` | 23 | - | very short (23 words) | - |
| `cfr29-1926.1117` | 24 | - | very short (24 words) | - |
| `cfr29-1926.1118` | 24 | - | very short (24 words) | - |
| `cfr29-1926.1124` | 5,759 | - | - | - |
| `cfr29-1926.1126` | 3,416 | - | - | - |
| `cfr29-1926.1127` | 10,720 | - | - | - |
| `cfr29-1926.1128` | 23 | - | very short (23 words) | - |
| `cfr29-1926.1144` | 23 | - | very short (23 words) | - |
| `cfr29-1926.1145` | 23 | - | very short (23 words) | - |
| `cfr29-1926.1147` | 24 | - | very short (24 words) | - |
| `cfr29-1926.1148` | 23 | - | very short (23 words) | - |
| `cfr29-1926.1152` | 22 | - | very short (22 words) | - |
| `cfr29-1926.1153` | 11,264 | - | - | reference list dropped, 5,491 characters (heading) |
| `cfr29-1926.12` | 4,197 | - | - | - |
| `cfr29-1926.1201` | 222 | - | - | - |
| `cfr29-1926.1202` | 2,284 | - | - | - |
| `cfr29-1926.1203` | 1,990 | - | - | - |
| `cfr29-1926.1204` | 1,476 | - | - | - |
| `cfr29-1926.1205` | 303 | - | - | - |
| `cfr29-1926.1206` | 375 | - | - | - |
| `cfr29-1926.1207` | 291 | - | - | - |
| `cfr29-1926.1208` | 166 | - | - | - |
| `cfr29-1926.1209` | 389 | - | - | - |
| `cfr29-1926.1210` | 193 | - | - | - |
| `cfr29-1926.1211` | 846 | - | - | - |
| `cfr29-1926.1212` | 53 | - | - | - |
| `cfr29-1926.1213` | 35 | - | very short (35 words) | - |
| `cfr29-1926.13` | 548 | - | - | - |
| `cfr29-1926.14` | 156 | - | - | - |
| `cfr29-1926.1400` | 999 | - | - | - |
| `cfr29-1926.1401` | 3,329 | - | - | - |
| `cfr29-1926.1402` | 351 | - | - | - |
| `cfr29-1926.1403` | 85 | - | - | - |
| `cfr29-1926.1404` | 1,497 | - | - | - |
| `cfr29-1926.1405` | 178 | - | - | - |
| `cfr29-1926.1406` | 86 | - | - | - |
| `cfr29-1926.1407` | 784 | - | - | - |
| `cfr29-1926.1408` | 1,500 | - | - | - |
| `cfr29-1926.1409` | 81 | - | - | - |
| `cfr29-1926.1410` | 1,305 | - | - | - |
| `cfr29-1926.1411` | 353 | - | - | - |
| `cfr29-1926.1412` | 2,085 | - | - | - |
| `cfr29-1926.1413` | 1,350 | - | - | - |
| `cfr29-1926.1414` | 1,040 | - | - | - |
| `cfr29-1926.1415` | 299 | - | - | - |
| `cfr29-1926.1416` | 1,523 | - | - | - |
| `cfr29-1926.1417` | 1,449 | - | - | - |
| `cfr29-1926.1418` | 37 | - | very short (37 words) | - |
| `cfr29-1926.1419` | 532 | - | - | - |
| `cfr29-1926.1420` | 115 | - | - | - |
| `cfr29-1926.1421` | 123 | - | - | - |
| `cfr29-1926.1422` | 24 | - | very short (24 words) | - |
| `cfr29-1926.1423` | 1,144 | - | - | - |
| `cfr29-1926.1424` | 333 | - | - | - |
| `cfr29-1926.1425` | 343 | - | - | - |
| `cfr29-1926.1426` | 556 | - | - | - |
| `cfr29-1926.1427` | 2,630 | - | - | - |
| `cfr29-1926.1428` | 388 | - | - | - |
| `cfr29-1926.1429` | 112 | - | - | - |
| `cfr29-1926.1430` | 412 | - | - | - |
| `cfr29-1926.1431` | 4,251 | - | - | - |
| `cfr29-1926.1432` | 146 | - | - | - |
| `cfr29-1926.1433` | 1,725 | - | - | - |
| `cfr29-1926.1434` | 435 | - | - | - |
| `cfr29-1926.1435` | 2,585 | - | - | - |
| `cfr29-1926.1436` | 2,260 | - | - | - |
| `cfr29-1926.1437` | 2,766 | - | - | - |
| `cfr29-1926.1438` | 284 | - | - | - |
| `cfr29-1926.1439` | 63 | - | - | - |
| `cfr29-1926.1440` | 203 | - | - | - |
| `cfr29-1926.1441` | 698 | - | - | - |
| `cfr29-1926.1442` | 328 | - | - | - |
| `cfr29-1926.1443` | 28 | - | very short (28 words) | - |
| `cfr29-1926.15` | 375 | - | - | - |
| `cfr29-1926.150` | 931 | - | - | - |
| `cfr29-1926.151` | 703 | - | - | - |
| `cfr29-1926.152` | 9,899 | - | - | - |
| `cfr29-1926.153` | 2,029 | - | - | - |
| `cfr29-1926.154` | 377 | - | - | - |
| `cfr29-1926.155` | 658 | - | - | - |
| `cfr29-1926.16` | 270 | - | - | - |
| `cfr29-1926.2` | 181 | - | - | - |
| `cfr29-1926.20` | 565 | - | - | - |
| `cfr29-1926.200` | 568 | - | - | - |
| `cfr29-1926.201` | 53 | - | - | - |
| `cfr29-1926.21` | 224 | - | - | - |
| `cfr29-1926.23` | 48 | - | very short (48 words) | - |
| `cfr29-1926.24` | 58 | - | - | - |
| `cfr29-1926.25` | 120 | - | - | - |
| `cfr29-1926.250` | 542 | - | - | - |
| `cfr29-1926.251` | 2,529 | - | - | - |
| `cfr29-1926.252` | 200 | - | - | - |
| `cfr29-1926.26` | 43 | - | very short (43 words) | - |
| `cfr29-1926.27` | 17 | - | very short (17 words) | - |
| `cfr29-1926.28` | 69 | - | - | - |
| `cfr29-1926.29` | 106 | - | - | - |
| `cfr29-1926.3` | 155 | - | - | - |
| `cfr29-1926.30` | 60 | - | - | - |
| `cfr29-1926.300` | 1,006 | - | - | - |
| `cfr29-1926.301` | 78 | - | - | - |
| `cfr29-1926.302` | 823 | - | - | - |
| `cfr29-1926.303` | 834 | - | - | - |
| `cfr29-1926.304` | 620 | - | - | - |
| `cfr29-1926.305` | 232 | - | - | - |
| `cfr29-1926.306` | 409 | - | - | - |
| `cfr29-1926.307` | 3,655 | - | - | - |
| `cfr29-1926.32` | 511 | - | - | - |
| `cfr29-1926.33` | 29 | - | very short (29 words) | - |
| `cfr29-1926.34` | 155 | - | - | - |
| `cfr29-1926.35` | 375 | - | - | - |
| `cfr29-1926.350` | 1,645 | - | - | - |
| `cfr29-1926.351` | 792 | - | - | - |
| `cfr29-1926.352` | 544 | - | - | - |
| `cfr29-1926.353` | 1,025 | - | - | - |
| `cfr29-1926.354` | 225 | - | - | - |
| `cfr29-1926.4` | 212 | - | - | - |
| `cfr29-1926.400` | 169 | - | - | - |
| `cfr29-1926.402` | 169 | - | - | - |
| `cfr29-1926.403` | 2,229 | - | - | - |
| `cfr29-1926.404` | 3,781 | - | - | - |
| `cfr29-1926.405` | 3,305 | - | - | - |
| `cfr29-1926.406` | 700 | - | - | - |
| `cfr29-1926.407` | 658 | - | - | - |
| `cfr29-1926.408` | 1,546 | - | - | - |
| `cfr29-1926.416` | 333 | - | - | - |
| `cfr29-1926.417` | 75 | - | - | - |
| `cfr29-1926.431` | 48 | - | very short (48 words) | - |
| `cfr29-1926.432` | 116 | - | - | - |
| `cfr29-1926.441` | 204 | - | - | - |
| `cfr29-1926.449` | 4,711 | - | - | - |
| `cfr29-1926.450` | 2,311 | - | - | - |
| `cfr29-1926.451` | 6,930 | - | - | - |
| `cfr29-1926.452` | 4,274 | - | - | - |
| `cfr29-1926.453` | 992 | - | - | - |
| `cfr29-1926.454` | 370 | - | - | - |
| `cfr29-1926.5` | 350 | - | - | - |
| `cfr29-1926.50` | 664 | - | - | - |
| `cfr29-1926.500` | 2,000 | - | - | - |
| `cfr29-1926.501` | 1,626 | - | - | - |
| `cfr29-1926.502` | 5,045 | - | - | - |
| `cfr29-1926.503` | 468 | - | - | - |
| `cfr29-1926.51` | 870 | - | - | - |
| `cfr29-1926.52` | 401 | - | - | - |
| `cfr29-1926.53` | 142 | - | - | - |
| `cfr29-1926.54` | 304 | - | - | - |
| `cfr29-1926.55` | 6,497 | - | - | - |
| `cfr29-1926.551` | 702 | - | - | - |
| `cfr29-1926.552` | 1,599 | - | - | - |
| `cfr29-1926.553` | 170 | - | - | - |
| `cfr29-1926.554` | 174 | - | - | - |
| `cfr29-1926.555` | 216 | - | - | - |
| `cfr29-1926.56` | 191 | - | - | - |
| `cfr29-1926.57` | 12,494 | - | - | - |
| `cfr29-1926.58` | 23 | - | very short (23 words) | - |
| `cfr29-1926.59` | 24 | - | very short (24 words) | - |
| `cfr29-1926.6` | 3,044 | - | - | - |
| `cfr29-1926.60` | 7,854 | - | - | - |
| `cfr29-1926.600` | 723 | - | - | - |
| `cfr29-1926.601` | 591 | - | - | - |
| `cfr29-1926.602` | 1,313 | - | - | - |
| `cfr29-1926.603` | 543 | - | - | - |
| `cfr29-1926.604` | 132 | - | - | - |
| `cfr29-1926.605` | 564 | - | - | - |
| `cfr29-1926.606` | 81 | - | - | - |
| `cfr29-1926.61` | 29 | - | very short (29 words) | - |
| `cfr29-1926.62__part01` | 4,026 | - | - | - |
| `cfr29-1926.62__part02` | 4,096 | - | - | - |
| `cfr29-1926.62__part03` | 4,079 | - | - | - |
| `cfr29-1926.62__part04` | 4,037 | - | - | - |
| `cfr29-1926.62__part05` | 4,019 | - | - | - |
| `cfr29-1926.62__part06` | 2,941 | - | - | - |
| `cfr29-1926.64` | 32 | - | very short (32 words) | - |
| `cfr29-1926.650` | 1,040 | - | - | - |
| `cfr29-1926.651` | 1,611 | - | - | - |
| `cfr29-1926.652` | 1,721 | - | - | - |
| `cfr29-1926.65__part01` | 4,002 | - | - | - |
| `cfr29-1926.65__part02` | 4,005 | - | - | - |
| `cfr29-1926.65__part03` | 4,016 | - | - | - |
| `cfr29-1926.65__part04` | 4,002 | - | - | - |
| `cfr29-1926.65__part05` | 4,012 | - | - | - |
| `cfr29-1926.65__part06` | 4,003 | - | - | - |
| `cfr29-1926.65__part07` | 4,469 | - | - | - |
| `cfr29-1926.66` | 3,821 | - | - | - |
| `cfr29-1926.700` | 350 | - | - | - |
| `cfr29-1926.701` | 217 | - | - | - |
| `cfr29-1926.702` | 441 | - | - | - |
| `cfr29-1926.703` | 855 | - | - | - |
| `cfr29-1926.704` | 149 | - | - | - |
| `cfr29-1926.705` | 1,000 | - | - | - |
| `cfr29-1926.706` | 225 | - | - | - |
| `cfr29-1926.750` | 536 | - | - | - |
| `cfr29-1926.751` | 1,673 | - | - | - |
| `cfr29-1926.752` | 368 | - | - | - |
| `cfr29-1926.753` | 816 | - | - | - |
| `cfr29-1926.754` | 999 | - | - | - |
| `cfr29-1926.755` | 201 | - | - | - |
| `cfr29-1926.756` | 438 | - | - | - |
| `cfr29-1926.757` | 2,099 | - | - | - |
| `cfr29-1926.758` | 289 | - | - | - |
| `cfr29-1926.759` | 57 | - | - | - |
| `cfr29-1926.760` | 644 | - | - | - |
| `cfr29-1926.761` | 358 | - | - | - |
| `cfr29-1926.800` | 7,759 | - | - | - |
| `cfr29-1926.801` | 256 | - | - | - |
| `cfr29-1926.802` | 84 | - | - | - |
| `cfr29-1926.803` | 4,376 | - | - | - |
| `cfr29-1926.804` | 440 | - | - | - |
| `cfr29-1926.850` | 531 | - | - | - |
| `cfr29-1926.851` | 128 | - | - | - |
| `cfr29-1926.852` | 265 | - | - | - |
| `cfr29-1926.853` | 68 | - | - | - |
| `cfr29-1926.854` | 326 | - | - | - |
| `cfr29-1926.855` | 267 | - | - | - |
| `cfr29-1926.856` | 73 | - | - | - |
| `cfr29-1926.857` | 162 | - | - | - |
| `cfr29-1926.858` | 82 | - | - | - |
| `cfr29-1926.859` | 246 | - | - | - |
| `cfr29-1926.860` | 24 | - | very short (24 words) | - |
| `cfr29-1926.900` | 1,126 | - | - | - |
| `cfr29-1926.901` | 124 | - | - | - |
| `cfr29-1926.902` | 420 | - | - | - |
| `cfr29-1926.903` | 438 | - | - | - |
| `cfr29-1926.904` | 160 | - | - | - |
| `cfr29-1926.905` | 587 | - | - | - |
| `cfr29-1926.906` | 677 | - | - | - |
| `cfr29-1926.907` | 377 | - | - | - |
| `cfr29-1926.908` | 291 | - | - | - |
| `cfr29-1926.909` | 230 | - | - | - |
| `cfr29-1926.910` | 109 | - | - | - |
| `cfr29-1926.911` | 188 | - | - | - |
| `cfr29-1926.912` | 242 | - | - | - |
| `cfr29-1926.913` | 290 | - | - | - |
| `cfr29-1926.914` | 1,020 | - | - | - |
| `cfr29-1926.95` | 459 | - | - | - |
| `cfr29-1926.950` | 1,489 | - | - | - |
| `cfr29-1926.951` | 153 | - | - | - |
| `cfr29-1926.952` | 325 | - | - | - |
| `cfr29-1926.953` | 1,069 | - | - | - |
| `cfr29-1926.954` | 1,696 | - | - | - |
| `cfr29-1926.955` | 215 | - | - | - |
| `cfr29-1926.956` | 577 | - | - | - |
| `cfr29-1926.957` | 500 | - | - | - |
| `cfr29-1926.958` | 182 | - | - | - |
| `cfr29-1926.959` | 663 | - | - | - |
| `cfr29-1926.96` | 23 | - | very short (23 words) | - |
| `cfr29-1926.960` | 2,921 | - | - | - |
| `cfr29-1926.961` | 1,137 | - | - | - |
| `cfr29-1926.962` | 803 | - | - | - |
| `cfr29-1926.963` | 1,262 | - | - | - |
| `cfr29-1926.964` | 2,172 | - | - | - |
| `cfr29-1926.965` | 776 | - | - | - |
| `cfr29-1926.966` | 988 | - | - | - |
| `cfr29-1926.967` | 862 | - | - | - |
| `cfr29-1926.968` | 2,406 | - | - | - |
| `cfr29-1926.97` | 2,804 | - | - | - |

## Not added in the last run

Nothing was left out.

## What to check by eye

Ingest cleans text by rules, and rules miss things.
Take five minutes to open the shortest, a middle one and the longest document next to its original and read one page of each.

- Search the documents for `þ`, `¼`, `(cid:` and the replacement character.
  A hit usually means the PDF's font map is wrong, which no tool can repair, so treat it as a defect and leave that document out.
- Look at the end of a few papers.
  Ingest drops a trailing reference list when it finds a References heading or a run of numbered entries.
  A paper whose list has neither can keep it, and then every author and journal name matches queries it should not.
- Open the first lines of a few documents.
  Author lists, copyright pages and tables of contents are not removed automatically, and you may want to cut them.
- Compare one table with the PDF.
  A PDF prints footnote marks as small raised digits, and the converter glues them onto the word or number next to them: `ALUMINUM1` is the heading ALUMINUM with footnote 1, and `11210,000` can be 210,000 with footnote 11.
  Quotes still match the stored text, but a number read from it can be wrong, so check before you trust a figure in a query, a judgment or an answer.
- Fix the `license` column in the manifest for every document, then run `uv run p2 license`.
  It is `unknown` until you do, and `unknown` does not pass.

## If a document is flagged as scanned

A scan is a picture of a page, so there is no text for ingest to read.
This template does not install an OCR tool, because it is large and most students never need it.
If you do need one, the opt-in route is pymupdf4llm with rapidocr, run on its own outside the template's environment:

```
uv run --no-project --with pymupdf4llm --with rapidocr python -c "import pymupdf4llm, sys, pathlib; pathlib.Path(sys.argv[2]).write_text(pymupdf4llm.to_markdown(sys.argv[1], use_ocr=True, force_ocr=True), encoding='utf-8')" scan.pdf scan.md
```

Put the resulting `.md` file in your folder and ingest the folder again.
It costs about 2 seconds a page, and OCR text needs a second look: it misreads ligatures, hyphens and numbers.
pymupdf4llm is AGPL-3.0 software, so use it only as a tool on your own machine, and do not add it to this repo's dependencies or copy its code into the repo.
