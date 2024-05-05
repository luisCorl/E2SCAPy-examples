syms s t V1
R1 = 0.2;
R2 = 0.2;
R3 = 1e3;
R4 = 0.2;
R5 = 0.2;
R6 = 1e3;
R7 = 0.2;
R8 = 0.2;
R9 = 0.2;
R10 = 0.2;
R11 = 0.2;
R12 = 1e3;
R13 = 1e3;
C1 = 0.0025;
f = 3;
w = 2*3.14159265358*f;
vi = 0.5*sin(w*t)*heaviside(t);
vi = laplace(vi)
v4 = C1*R3*V1*s*(R1*R2*R8*R9*(R10*R11 + R10*R12 + R11*R12)*(R5*R6 + R5*R7 + R6*R7) + R10*R12*R6*R7*(R1*R2 + R1*R4 + R2*R4)*(R13*R8 + R13*R9 + R8*R9))/(C1*R1*R3*R4*R8*R9*s*(R10*R11 + R10*R12 + R11*R12)*(R5*R6 + R5*R7 + R6*R7) + R11*R12*R6*R7*(R1*R2 + R1*R4 + R2*R4)*(R13*R8 + R13*R9 + R8*R9));
H4 = v4/V1;
v4 = vi*H4;
f4 = ilaplace(v4)

v9 = R1*R12*V1*(C1*R10*R3*R4*s + R11*R2)*(R13*R8 + R13*R9 + R8*R9)*(R5*R6 + R5*R7 + R6*R7)/(C1*R1*R3*R4*R8*R9*s*(R10*R11 + R10*R12 + R11*R12)*(R5*R6 + R5*R7 + R6*R7) + R11*R12*R6*R7*(R1*R2 + R1*R4 + R2*R4)*(R13*R8 + R13*R9 + R8*R9));
H9 = v9/V1;
v9 = vi*H9;
f9 = ilaplace(v9)

