# Burtle

## Functions
move({u, l , d, r} || {ul, ur, dl, dr}, steps)
  - manhattan distance
for loops
while loops
bomb(color)
  - color all around it
chg_color(color [rgb])
  - changes the color of the burtle
rainbow(starting_color [default red])
  - colors line in a rainbow
draw_pic(picture source)
  - draws the picture (albeit pixelated most likely)
jump(x, y)
  - jumps burtle to x,y
rect(dx, dy)
  - makes a rectangle of dx length and dy height
circle(r)
  - makes a circle with r radius

## Syntax
- semicolon to end command
- don't need semicolon on new line
- no parantheses
- double back slash for comments
- # and # for beginning and ending multiline comments
- handle out of bounds

## Example
//draws a house
color(yellow);
rect(5, 6);
jump(0, 6);
color(brown);
diag(ul, 3);
diag(dl, 3);

