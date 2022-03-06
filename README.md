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


Before installation of pyCET
--------
* User needs a google acount;

* If you want to use pyCET_demo with VSCode (highly recommmented), please finish setup by following https://github.com/WassimBenzarti/colab-ssh

Install pyCET
--------
1. Login into google colab, https://colab.research.google.com/

2. Connect to google drive by running following code (user can access results without login to google colab)
```python
from google.colab import drive
drive.mount('/content/drive')
```

3. create a shell
```python
!pip install google-colab-shell
from google_colab_shell import getshell
getshell(height=200) # custom height of the terminal
```

4. In the shell craete a working directory
```shell
cd /content/drive/MyDrive
mkdir my_project
cd my_project
```

5. Colone pyCET_demo repo
```shell
git clone https://github.com/CivilEngrTools/pyCET_demo.git
```

6. Test if pyCET_demo is working
```shell
cd pyCET_demo/src_pyc
printf "import CET_MODULE\nprint(CET_MODULE.version())\n" > test.py
python test.py
```
Now "0.01" is printing in terminial
