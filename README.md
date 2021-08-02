# apple.cx

I've noticed some fun patterns in the different kinds of ways one can cut apples.
It's probably not generalizable, but I think it's fun!
So, I thought I'd make some videos of it.

## Making the video

Native install didn't work on my mac, and cost me an embarrassing amount of time.
Docker was a snap.

1. get docker running
2. `docker run -it --name my-manim-container -v "$(pwd):/manim" manimcommunity/manim /bin/bash`
3. `manim intersection_test.py IntersectionScene -ql`
