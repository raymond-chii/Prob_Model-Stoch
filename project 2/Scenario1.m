% Arav Sharma and Lei(Raymond) Chi


%%%% Linear MMSE estimator implementation %%%%

%%% Simulation %%%
N = 10000;

Y = 2 * rand(N, 1) - 1; % Uniformly distributed in [-1, 1]
W = 4 * rand(N, 1) - 2; % Uniformly distributed in [-2, 2]

X = Y + W; % Form X
Y_hat = (1/5) * X;% Linear MMSE estimator for Y given X
MSE_simulated = mean((Y - Y_hat).^2);% Compute the simulated MSE

fprintf('Simulated MSE: %f\n', MSE_simulated);

%%% Theoretical %%%

% Y --> E[Y] = 0 and Var(Y) = 1/3.
% W --> E[W] = 0 and Var(W) = 4/3.
% Var(X) = Var(Y) + Var(W) = 5/3.
% Y_hat = (Cov(Y, X) / Var(X)) * X
% Cov(Y, X) = Var(Y) = 1/3
% Y_hat = (1/3) / (5/3) * X = (1/5) * X
% MSE = E[(Y - Y_hat)^2] = Var(Y) - (Cov(Y, X)^2 / Var(X)) = 1/3 - (1/3)^2 / (5/3) = 1/3 - 1/15 = 4/15

fprintf('Theoretical MSE: %f\n', 4/15);

%%%% Bayes MMSE estimator implementation %%%%

%%% Simulation %%%

% y_hat(x) = E[ Y | X = x ]
% bayes MMSE estimator = E[ Y | X = x ]
idx1 = X>-1 & X<1;
idx2 = X<-1;
idx3 = X>1;
X(idx1) = 0;
X(idx2) = 0.5 + X(idx2)*0.5;
X(idx3) = -0.5 + X(idx3)*0.5;

Y_hat_bayes = X;
Bayes_MSE_simulated = mean((Y - Y_hat_bayes).^2);


fprintf('Simulated Bayes MMSE MSE: %f\n', Bayes_MSE_simulated);

%%% Theoretical %%%



