<h1 align="center">Mathematical Table Program</h1>
<h3 align = "center">By Muhammad Ali</h3>

<hr>

<p>This is a mathematical table program i built using Python. It has a simple for loop algorithm that gets the mathematical table for a number. For Example, if the number is 10 and the times variable is 4 then the output will print: <br>10x1=10<br>10x2=20<br>10x3=30<br>10x4=40</p>

<h4>How the algorithm works</h4>
<pre>for i in range(num, num*tms+1, num):
            print(str(num)+"x"+str(int(i/num))+"="+str(i))</pre>

<p>This is a very simple 2 line algorithm that i have used to make this program. If you have worked with loops before it must be fairly simple to understand. Here's how it works:
  <ol>
    <li>We are using the "range" function for this loop which should be available if you are using Python 3 or 3+. We have a start index as the number, a       stop index as the number multiplied by the times variable added by 1 because computers start with 0 and then as a step we have the number.
    <li>We print the number followed by "x" then we divide the index by the number, followed by "=" then we have the index as an answer.
  </ol></p>
  
  <h4>Facts about the Program</h4>
  <ul>
    <li>The program is fully exception proof, that means even if you give the wrong input it won't crash.
    <li>The program can show the table of litteraly any number followed by any number for the times variable.
  </ul>
