function [xe, ye] = xymatrix (th1, th2, th3, l1, l2, l3)
r1 = [cos(th1) -sin(th1) 0 0;sin(th1) cos(th1) 0 0;0 0 1 0;0 0 0 1];
t1 = [1 0 0 l1;0 1 0 0;0 0 1 0;0 0 0 1];
q1 = r1*t1;
r2 = [cos(th2) -sin(th2) 0 0;sin(th2) cos(th2) 0 0;0 0 1 0;0 0 0 1];
t2 = [1 0 0 l2;0 1 0 0;0 0 1 0;0 0 0 1];
q2 = r2*t2;
r3 = [cos(th3) -sin(th3) 0 0;sin(th3) cos(th3) 0 0;0 0 1 0;0 0 0 1];
t3 = [1 0 0 l3;0 1 0 0;0 0 1 0;0 0 0 1];
q3 = r3*t3;
qe = q1*q2*q3;
xe=qe(1,4);
ye=qe(2,4);
end