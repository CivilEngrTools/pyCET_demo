### 1 Summary
 
To demonstrate the calcuations from AISC 14th Design Examples 
II.A-17, SINGLE-PLATE CONNECTION (CONVENTIONALBEAM-TO-COLUMN FLANGE). Origianl information

Given:

Design a single-plate connection between an ASTM A992 W1650 beam and an ASTM A992 W1490 column
flange to support the following beam end reactions:

RD = 8.0 kips 

RL = 25 kips 

Rn = 33 kips (ASD method) 

Use 3/4-in.-diameter ASTM A325-N or F1852-N bolts in standard holes, 70-ksi electrode welds and an ASTM A36 plate 

#### Capacity Table
Beam Web
| Limit State    | Design Value | Check value | Ratio | Check Result | Reference |
|----------------|-------|-------------|-------|-------|-------|
| Shear Yielding | 123.88 Kips | 60 Kips | 0.484 | o.k. | AISC G2 |
| Hole Bearing | 79.07 Kips | 60 Kips | 0.759 | o.k. | AISC J3.10 |

Beam Web Connection
| Limit State    | Design Value | Check value | Ratio | Check Result | Reference |
|----------------|-------|-------------|-------|-------|-------|
| Bolt Shear | 42.43 Kips | 60 Kips | 1.414 | no good | AISC J3.2 |
| Shear Yielding | 41.40 Kips | 60 Kips | 1.449 | no good | AISC J4.2 |
| Shear Rupture | 34.80 Kips | 60 Kips | **1.724** | no good | AISC J4.2 |
| Block Shear | 35.38 Kips | 60 Kips | 1.696 | no good | AISC J4.3 |
| Hole Bearing | 41.34 Kips | 60 Kips | 1.451 | no good | AISC J3.10 |
| Welds | 64.03 Kips | 60 Kips | 0.937 | o.k. | AISC J2 |
### 2 Beam web check
#### Shear Yielding
$$
\begin{align}
\frac{h}{t_w} & = \frac{16.3 \text{ in.} -2(1.03 \text{ in.} )}{0.38 \text{ in.} } \\
  & = 37.47
\end{align}
$$
$$
\begin{align}
2.24\sqrt{\frac{E}{F_y}} & = 2.24\sqrt{\frac{29000 \text{ ksi} }{50 \text{ ksi} }} \\
  & = 53.95
\end{align}
$$
$$
\begin{align}
\frac{h}{t_w} \le 2.24\sqrt{E/F_y}
\end{align}
$$
$$
\begin{align}
\frac{R_{n}}{\Omega} & = \frac{1}{\Omega} 0.6 F_y A_w C_v \\
  & = \frac{1}{1.5}(0.6)(50 \text{ ksi} )(16.3 \text{ in.} )(0.38 \text{ in.} )(1) \\
  & = 123.9 \text{ kips} \tag{AISC Equ. G2-1}>33 \text{ kips}  \text{ O.K.}
\end{align}
$$
#### Hole Bearing
Bearing/tearout of inner bolts
$$
\begin{align}
\frac{R_{n,i}}{\Omega} & = \frac{1}{\Omega} 1.2 L_c t F_u \le \frac{1}{\Omega} 2.4 d t F_u \\
  & = \frac{1}{2}(1.2)(3 \text{ in.}  - 0.8125 \text{ in.} )(0.38 \text{ in.} )(65 \text{ ksi} ) \le \frac{1}{2}(2.4)(0.75 \text{ in.} )(0.38 \text{ in.} )(65 \text{ ksi} ) \\
  & = 32.42 \text{ kips} \le22.23 \text{ kips}  \\
  & = 22.23 \text{ kips} \tag{AISC Equ. J3-6a}
\end{align}
$$
Bearing of edge bolts
$$
\begin{align}
\frac{R_{n,e}}{\Omega} & = \frac{1}{\Omega} 2.4 d t F_u \\
  & = \frac{1}{2}(2.4)(0.75 \text{ in.} )(0.38 \text{ in.} )(65 \text{ ksi} ) \\
  & = 22.23 \text{ kips}  \\
  & = 22.23 \text{ kips} \tag{AISC Equ. J3-6a}
\end{align}
$$
Bolts bearing/tearout capacity
$$
\begin{align}
\frac{R_n}{\Omega} & = \left[\frac{1}{\Omega} R_{n,e} + (\frac{1}{\Omega} R_{n,i})(n -1) \right] C / n \\
  & = \left[22.23 \text{ kips}  + (22.23 \text{ kips} )(4-1) \right](3.557)/(4) \\
  & = 79.07 \text{ kips} >33 \text{ kips}  \text{ O.K.}
\end{align}
$$
### 3 Beam web connection check
#### Bolt Shear
The nominal shear stress of A325N bolt: $F_{n} = 54 \text{ kips} \text{ (AISC 13th Table J3.2)}$

$$
\begin{align}
r_n & =  F_n A_b \\
  & = (54 \text{ kips} )\left( \frac{3.1416(0.75 \text{ in.} )^2}{4} \right) \\
  & = 23.86 \text{ kips} 
\end{align}
$$
$$
\begin{align}
\frac{R_n}{\Omega} & = \frac{1}{\Omega} C r_n \\
  & = \frac{1}{2} (3.557)(23.8565 \text{ kips} ) \\
  & = 42.43 \text{ kips} \tag{AISC 13th Equ. J3-1}>33 \text{ kips}  \text{ O.K.}
\end{align}
$$
#### Shear Yielding
$$
\begin{align}
\frac{R_{n}}{\Omega} & = \frac{1}{\Omega} 0.6 F_y A_g \\
  & = \frac{1}{1.5}(0.6)(36 \text{ ksi} )(11.5 \text{ in.} )(0.25 \text{ in.} ) \\
  & = 41.4 \text{ kips} \tag{AISC Equ. J4-3}>33 \text{ kips}  \text{ O.K.}
\end{align}
$$
#### Shear Rupture
$$
\begin{align}
\frac{R_{n}}{\Omega} & = \frac{1}{\Omega} 0.6 F_u A_{nv} \\
  & = \frac{1}{2}(0.6)(58 \text{ ksi} )[(11.5 \text{ in.} )( 0.25 \text{ in.} ) - (0.8125 \text{ in.} + 0.0625 \text{ in.} )(4)(0.25 \text{ in.} )] \\
  & = 34.8 \text{ kips} \tag{AISC Equ. J4-4}>33 \text{ kips}  \text{ O.K.}
\end{align}
$$
#### Block Shear
Force direction, L shape
$$
\begin{align}
 A_{gv}  & = ((n - 1)s+l_{ev})t \\
  & = ((4 - 1)(3 \text{ in.} )+1.25 \text{ in.} )(0.25 \text{ in.} ) \\
  & = 2.562 \text{ }\mathrm{in.^2} 
\end{align}
$$
$$
\begin{align}
 A_{nv}  & = A_{gv} - (n-0.5) d_h^\prime t \\
  & = 2.5625 \text{ }\mathrm{in.^2}  - (4-0.5)(0.8125 \text{ in.}  + 0.0625 \text{ in.} )(0.25 \text{ in.} ) \\
  & = 1.797 \text{ }\mathrm{in.^2} 
\end{align}
$$
$$
\begin{align}
 A_{nt}  & = (l_{eh} + (n_h-1)s -(n_h - 0.5) d_h^\prime )t \\
  & = (1.5 \text{ in.}  + (1-1)(3 \text{ in.} ) -(1 - 0.5)(0.8125 \text{ in.}  + 0.0625 \text{ in.} ) )(0.25 \text{ in.} ) \\
  & = 0.2656 \text{ }\mathrm{in.^2} 
\end{align}
$$
$$
\begin{align}
\frac{1}{\Omega} R_{n} & = \frac{1}{\Omega} (0.6 F_{u} A_{nv} + U_{bs} F_{u} A_{nt}) \le \frac{1}{\Omega} (0.6 F_{y} A_{gv} + U_{bs} F_{u} A_{nt}) \\
  & = \frac{1}{2} (0.6(58 \text{ ksi} )(1.79688 \text{ }\mathrm{in.^2} ) + 1(58 \text{ ksi} )(0.265625 \text{ }\mathrm{in.^2} )) \\ 
 &\quad\le \frac{1}{2} (0.6(36 \text{ ksi} )(2.5625 \text{ }\mathrm{in.^2} ) + 1(58 \text{ ksi} )(0.265625 \text{ }\mathrm{in.^2} )) \\
  & = 38.97 \text{ kips} \le35.38 \text{ kips}  \\
  & = 35.38 \text{ kips} \tag{AISC Equ. J4-5}>33 \text{ kips}  \text{ O.K.}
\end{align}
$$
Using 35.38 kips to check.
#### Hole Bearing
Bearing/tearout of inner bolts
$$
\begin{align}
\frac{R_{n,i}}{\Omega} & = \frac{1}{\Omega} 1.2 L_c t F_u \le \frac{1}{\Omega} 2.4 d t F_u \\
  & = \frac{1}{2}(1.2)(3 \text{ in.}  - 0.8125 \text{ in.} )(0.25 \text{ in.} )(58 \text{ ksi} ) \le \frac{1}{2}(2.4)(0.75 \text{ in.} )(0.25 \text{ in.} )(58 \text{ ksi} ) \\
  & = 19.03 \text{ kips} \le13.05 \text{ kips}  \\
  & = 13.05 \text{ kips} \tag{AISC Equ. J3-6a}
\end{align}
$$
Bearing/tearout of edge bolts
$$
\begin{align}
\frac{R_{n,e}}{\Omega} & = \frac{1}{\Omega} 1.2 L_c t F_u \le \frac{1}{\Omega} 2.4 d t F_u \\
  & = \frac{1}{2}(1.2)(1.25 \text{ in.}  - \frac{0.8125 \text{ in.} }{2})(0.25 \text{ in.} )(58 \text{ ksi} ) \le \frac{1}{2}(2.4)(0.75 \text{ in.} )(0.25 \text{ in.} )(58 \text{ ksi} ) \\
  & = 7.341 \text{ kips} \le13.05 \text{ kips}  \\
  & = 7.341 \text{ kips} \tag{AISC Equ. J3-6a}
\end{align}
$$
Bolts bearing/tearout capacity
$$
\begin{align}
\frac{R_n}{\Omega} & = \left[\frac{1}{\Omega} R_{n,e} + (\frac{1}{\Omega} R_{n,i})(n -1) \right] C / n \\
  & = \left[7.34062 \text{ kips}  + (13.05 \text{ kips} )(4-1) \right](3.557)/(4) \\
  & = 41.34 \text{ kips} >33 \text{ kips}  \text{ O.K.}
\end{align}
$$
#### Welds
$$
\begin{align}
\frac{R_{n}}{\Omega} & = \frac{1}{\Omega} 0.6F_{EXX}A_w \\
  & = \frac{1}{2}(0.6)(70 \text{ ksi} )(0.707)(11.5 \text{ in.} )(0.1875 \text{ in.} )(2) \\
  & = 64.03 \text{ kips} \tag{AISC 13th Equ. J2-5}>33 \text{ kips}  \text{ O.K.} \text{ O.K.}
\end{align}
$$
