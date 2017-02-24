c=" "
def format_line(words, L):
  if len(words) == 0:
    return c*L
  if len(words) == 1:
    return words[0] + c*(L-len(words[0]))
  wsum=0
  for w in words:
    wsum = wsum + len(w)
  deficit = L - wsum
  gaps = len(words) - 1
  even_space = deficit / gaps
  extra_space = deficit % gaps
  line=words[0]
  i=0
  for w in words[1:]:
    line = line + c*even_space
    if i < extra_space:
      line = line + c
    line = line + w
    i = i + 1
  return line

def format_last_line(words, L):
  if len(words) == 0:
    return c*L
  line=words[0]
  for w in words[1:]:
    line = line + c + w
  s=len(line)
  return line + c*(L-s)

def textJustification(words, L):
  lines=[]
  curline=[]
  cursum=0
  for w in words:
    if len(w) == 0:
      continue
    if cursum == 0:
      newsum = len(w)
    else:
      newsum = cursum + 1 + len(w)
    if newsum <= L:
      curline.append(w)
      cursum = newsum
    else:
      lines.append(format_line(curline, L))
      curline=[w]
      cursum=len(w)
  lines.append(format_last_line(curline, L))
  return lines

words = ["This", "is", "an", "example", "of", "text", "justification."]
print "\n".join(textJustification(words, 16))

print "\n".join(textJustification(["Two", "words."], 10))
print "\n".join(textJustification([""],2))

words = ["Given", "an", "array", "of", "words", "and", "a", "length"]
print "\n".join(textJustification(words,9))
