# Basic-2-Dimensional-Gradient-Descent-Python
#The code in this repository is a basic 2d model of gradient descent with fixed learning rate.

How to use:

A number of variables are available at the top of the code. These control the input equation, learning rate, range of starting points, number of starting points and the limit value, values with a co-ordinate above the limit value will cause the code to abort and class the gradient descent as divergent. This is necessary due to the fact that a fixed learning rate causes the iteration to shoot away from the origin incredibly fast.

Setting the function variable, F and it's order, order:

In the code, F is created as a square np.array of side length 'order+1'. This array directly corresponds to a polynomial equation in 2 variables (X, Y) with powers from 0 up to the value of order. To find the equation from the array, multiply each element by its position according to the following formula: F[i][j] = k ===> equation contains the value k(X^j)(Y^i). Some examples:

F[0][2] = 2 

F[0][0] = 1

F[2][0] = 4

F[2][1] = 1 

Corresponds to the equation F(X,Y) = 2X^2 + 1 + 4Y^2 + XY^2, and the order is 2.

F[1][1] = -3

F[0][2] = 1

F[2][2] = 1

Corresponds to the equation F(X,Y) = -3XY + X^2 + X^2Y^2, and the order is 2.

