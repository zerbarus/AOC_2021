import strutils, sequtils

iterator diffs(values: seq[(int, int)]): bool =
  for (x, y) in values:
    yield x < y

let 
  lines = readFile("day01-test.txt").splitlines()
  depths = lines.map(parseInt)
  zipped = zip(depths[0 .. ^2], depths[1 .. ^1])
var  
  windows = newSeq[int]()
  zippedWindows: seq[(int, int)]

for i in 0 .. depths.len - 3:
  let x = depths[i] + depths[i+1] + depths[i+2]
  windows.add(x)

zippedWindows = zip(windows[0 .. ^2], windows[1 .. ^1])
echo countIt(diffs(zipped), it == true)
echo countIt(diffs(zippedWindows), it == true)
  