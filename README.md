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

First example of pyCET_demo
--------

1. In google colab create a notebook by menu: File -> New notebook
2. Menu: File -> Save a copy in Drive
3. Use google colab file "Files" pannel (left side), rename drive/MyDrive/Colab Notebooks/Copy of Untitled0.ipynb as drive/MyDrive/Colab Notebooks/my_project.ipynb
4. Menu: File -> Open Notebook. Select the "Google Drive" tab and my_project.ipynb.
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
from src.civil_engr_tool import check_shear_rupture
from src.civil_engr_tool import init_tool
from src.report import Report

from src.calculation import Calculation

common_data = {
    "design method": "ASD",
    "code": "AISC 14th"
}

init_tool(common_data)

web_conn = Connection()
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
Note that shear_yield is a dict object. shear_yield['result'] will give the result as 41.4 kips, the shear yield capacity of the plate. shear_yield['equations'][0]['content'] is a list of equstions. For the detailed calcualations, users can create a new Text cell and paste as

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


