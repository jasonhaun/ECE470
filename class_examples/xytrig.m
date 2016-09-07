function [xe, ye] = xytrig(th1, th2, th3, l1, l2, l3)
xe = l1*cos(th1) + l2*cos(th1+th2) + l3*cos(th1+th2+th3);
ye = l1*sin(th1) + l2*sin(th1+th2) + l3*sin(th1+th2+th3);
end
