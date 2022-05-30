<h1>Table Program</h1>
<h4>By Muhammad Ali</h4>

<p>This is a mathematical table program i made using Python which can basically show the table of any number. It usses an algorithm that takes in two numbers. The number who's table you want to show and how many times. Like 10 times 12. This will output:
<br>
10x1=10
10x2=20
10x3=30
.......
10x12=120
<br>
</p>

<h3>How to use the program</h3>
<p>Download the code or copy it and paste it in your Python file. Make sure you have Python version 3 or 3+. To check your version <em>python -version</em>. Run the program. If you don't know how to run it follow these steps: <br>
1. Change the directory to the project folder by typing <em>cd name\Directory_where_your_file_is_created</em>. You can copy the file directory by right clicking it. Click on properties and you will see the directory. Copy it and paste it in the text where it says Directory_where_your_file_is_created. (This is the process for Windows).
2. Type <em>python filename.py</em>. Make sure to add your file name where the text says filename.py
3. The file should run and it should ask you to input a number.
</p>

<h3How the algorithm works</h3>
<em>for i in range(num, num*tms+1, num):
            print(str(num)+"x"+str(int(i/num))+"="+str(i))
            time.sleep(1)</em>
<p>If you have worked with loops before this should be pretty simple. Here's how the table algorithm works:
First we create a for loop that has 3 arguments. The number as a starting index. The number multiplied by the times variable added by 1 because computers always start at 0 and lastly a the number as a step so we add the number each time we iterate. Now we just have to print the output. First we print the number followed by "x". Then we divide the index with the number and add it to our string. Lastly we just print out the iteration from the loop. For example, lets say we have entered the number 5 and the times variable is set to 10. So the for loop will look kind of like this: <br>
<em>for i in range(5,51,5):</em>
You might get an idea of the loop now. We start from 5 and end at 50 because if we entered 50 we would get an ending point of 49. Thats because computers always start with 0. For every iteration we also add 5 to the index. for example: index 1: 5, index 2: 10, index 3: 15 ......
<br>
Now we just print the output. For the first iteration you can imagine the print statement like this: <em>print(str(5n)+"x"+str(int(5i/5n))+"="+str(5i)) </em>
The i stands for index and n for number just so you dont mix up the things.
</p>

<h3>Facts about the program</h3>
<p>The program can take in basically any number and any umber acting for the times value. Just make sure the number is not a float.<br>
The program is fully exception proof, that means even if you enter the wrong number it won't crash.<br>
The program is in an infinite while loop so you can run it over and over again without having to reopen the file.<br></p>
