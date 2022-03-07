# pyCET_demo

### To demonstrate of the power of **pyCET** software.
--------

Overview of pyCET
--------

* **The First Steel Member/Connection Calcution API in the World** pyCET is the set of python APIs to do member/connection caclcuations and create Markdown reports. So far pyCET concentrates on AISC 14th manumul and will cover AISC 15th and later versions. 

* **Create Perfessional Calcuations** pyCET creates equstions in Latex and drawings in SVG format (under development).

* **Powerful APIs** Users can use pyCET APIs to write their own code to do steel structure designs, espcially about loops for different possibilies.

* **Developed and Maintained by Professionals** pyCET is developed and maintained by professional engineers across the world.

* **Not Open Source Software** But the price is very reasonable, under 1k per seat per year. Please contact civilengrtools@gmail.com if you want to buy. 

* **Still Under Development** We are planning to finish most funtionalities by the end of 2024.

Overview of pyCET_demo
--------
* **Demo Version of pyCET** pyCET_demo itself is open-source. However, files under src_pyc are compiled/binary files.

* **Limits** pyCET_demo only supports follwing beam/column and loads combiniations. If member size or laods are not in following table, pyCET_demo will use arbitary values and the calulations are not correct.

| Beam Size | Column Size | Shear Force | Moment | Comments |
| --- | :-- | --: | :-: |:-: |
| W16X50 |  | 33 kips |  | AISC_14th_Example_IIA-17 |

* **Web Host** pyCET_demo only runs inside google colab. pyCET could run udner Windows/Linux/Macos.


Before installation of pyCET_demo
--------
* User needs a google acount;

* If you want to use pyCET_demo with VSCode (highly recommmented), please finish setup by following https://github.com/WassimBenzarti/colab-ssh

Install pyCET_demo
--------
1. Login into google colab, https://colab.research.google.com/

2. In the code cell, connect to google drive by running following code (user can access results without login to google colab)
```python
from google.colab import drive
drive.mount('/content/drive')
```

3. In the code cell, create a shell
```python
!pip install google-colab-shell
from google_colab_shell import getshell
getshell(height=200) # custom height of the terminal
```

4. In the shell, craete a working directory
```shell
cd /content/drive/MyDrive
mkdir my_project
cd my_project
```

5. In the shell, clone pyCET_demo repo
```shell
git clone https://github.com/CivilEngrTools/pyCET_demo.git
```

6. In the shell, test if pyCET_demo is working
```shell
cd pyCET_demo/src_pyc
printf "import CET_MODULE\nprint(CET_MODULE.version())\n" > test.py
python test.py
```
Now "0.01" is printing in terminial

First example: Basic of pyCET_demo
--------

1. In google colab create a notebook by menu: File -> New notebook
2. Menu: File -> Save a copy in Drive
3. Use google colab file "Files" pannel (left side), rename drive/MyDrive/Colab Notebooks/Copy of Untitled0.ipynb as drive/MyDrive/Colab Notebooks/my_project.ipynb
4. Menu: File -> Open Notebook. Select the "Google Drive" tab and my_project.ipynb. The notebook will like this
![colab](https://user-images.githubusercontent.com/100242816/157124568-aef64b35-e846-434d-9674-5e9a4832edd4.JPG)
5. Connection to google drive again.
```python
from google.colab import drive
drive.mount('/content/drive')
```
6. Inside my_project.ipynb, type

```python
% cd /content/drive/MyDrive/my_project/
import copy
import sys

sys.path.append("./pyCET_demo")
sys.path.append("./pyCET_demo/src_pyc")

from src_pyc.connection import Connection
from src.civil_engr_tool import check_shear_yield
from src.civil_engr_tool import init_tool
from src.report import Report

from src.calculation import Calculation

common_data = {
    "design method": "ASD",
    "code": "AISC 14th"
}

# Need to initialize the module
init_tool(common_data)

web_conn = Connection()
# default as shear plate connection
web_conn.set_default("web conn")
web_conn.grade = "A36"
web_conn.Fy = 36
web_conn.Fu = 58
web_conn.length = 11.5
web_conn.thickness = 0.25
web_conn.check_force = 33.0

# pass data to the CET_MODULE 
web_conn.set_data()
shear_yield = check_shear_yield()

print(shear_yield['result'])
print(shear_yield['equations'][0]['content'])
```

Now the results will be printed as 

```text
/content/drive/MyDrive/my_project
41.39999999999999
$$
\begin{align}
\frac{R_{n}}{\Omega} & = \frac{1}{\Omega} 0.6 F_y A_g \\
  & = \frac{1}{1.5}(0.6)(36 \text{ ksi} )(11.5 \text{ in.} )(0.25 \text{ in.} ) \\
  & = 41.4 \text{ kips} \tag{AISC Equ. J4-3}>33 \text{ kips}  \text{ O.K.}
\end{align}
$$
```
Note that shear_yield is a dict object. shear_yield['result'] will give the result as 41.4 kips, the shear yield capacity of the plate. shear_yield['equations'] is a list of equstions. For the detailed calcualations, users can create a new Text cell and paste as

```text
%%latex
$$
\begin{align}
\frac{R_{n}}{\Omega} & = \frac{1}{\Omega} 0.6 F_y A_g \\
  & = \frac{1}{1.5}(0.6)(36 \text{ ksi} )(11.5 \text{ in.} )(0.25 \text{ in.} ) \\
  & = 41.4 \text{ kips} \tag{AISC Equ. J4-3}>33 \text{ kips}  \text{ O.K.}
\end{align}
$$
```
And the equation will be rendered as 

![shear yield](https://user-images.githubusercontent.com/100242816/156947976-7e1eb46d-c5d1-4309-bb6d-86458eaae044.JPG)

Second example: design connection by pyCET
--------

This example is to show how to use pyCET to design a connection. pyCET itself is a caluction software. But it is very powerful and the users could use it for more complicate calculations and designs.


```python
% cd /content/drive/MyDrive/my_project/
import copy
import sys

sys.path.append("./pyCET_demo")
sys.path.append("./pyCET_demo/src_pyc")

from src_pyc.connection import Connection
from src.civil_engr_tool import check_shear_yield
from src.civil_engr_tool import check_shear_rupture
from src.civil_engr_tool import init_tool
from src.report import Report

from src.calculation import Calculation

common_data = {
    "design method": "ASD",
    "code": "AISC 14th"
}

# Need to initialize the module
init_tool(common_data)

web_conn = Connection()
web_conn.set_default("web conn")
web_conn.grade = "A36"
web_conn.Fy = 36
web_conn.Fu = 58
web_conn.length = 11.5
web_conn.thickness = 0.25
web_conn.check_force = 33.0
web_conn.bolt.row = 4
web_conn.bolt.diameter = 0.75
web_conn.bolt.type = "A325N"
web_conn.bolt.hole_type = "Standard"

dia_list = [0.5, 0.625, 0.75, 0.875, 1.0, 1.25, 1.5]
t_list = [0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1.0, 1.25, 1.5, 2.0]

found = False;

for dia in dia_list:
  if found == False:
    for t in t_list:
      web_conn.bolt.diameter = dia
      web_conn.thickness = t
      web_conn.set_data()
      shear_yield = check_shear_yield()
      shear_rupture = check_shear_rupture()

      if( shear_yield['result'] > web_conn.check_force 
        and shear_rupture['result'] > web_conn.check_force ):
        found = True
        break

# call again to make sure the equations are created
web_conn.set_data()
shear_yield = check_shear_yield()
shear_rupture = check_shear_rupture()
print(shear_yield['equations'][0]['content'])
print(shear_rupture['equations'][0]['content'])
```

Above code find 0.25 inch as plate thickness and 0.5 inch as bolt diameter. Comparing to AISC 14th Example II-17, the bolt diamter is smaller because we only check shear yield and shear ruputer of the plate.

Third example: AISC 14th Design Example II.A-17
--------

The source code are in ./regression/AISC_14th_Example_IIA-17.py and the generated file is ./regression/test/AISC_14th_Example_IIA-17.md. If users want to run outside of regression folder, following code could be changed:

```python
sys.path.append("./pyCET_demo")
sys.path.append("./pyCET_demo/src_pyc")
```

It is highly recommended to use [Typora](https://typora.io/) to render the Markdown file, AISC_14th_Example_IIA-17.md. To align the equations to the left side, Typora users could make change to (aboule line 120)

**resources/window.html**

by adding

```javascript
window.MathJax = {
  ....
  svg: {
    displayAlign: 'left',
    scale: 0.9,
    minScale: 80,
  },
...
};

```

Users also could change the rendering scale. The final dispaly in Typora is:

![shear yield](https://user-images.githubusercontent.com/100242816/157089471-176b8bbf-9419-429c-9af5-342b04453bc4.JPG)

