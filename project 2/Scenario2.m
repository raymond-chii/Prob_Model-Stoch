% Arav Sharma and Lei(Raymond) Chi


linear_mmse_estimator

function linear_mmse_estimator()
    % Parameters
    samples = 10000;
    u_Y = 1;
    variances_Y = [0.2, 0.4, 0.6, 0.8, 1];
    variances_R = [0.2,0.4, 0.6, 0.8, 1];
    N = 5;

    simulation = zeros(N, length(variances_Y)); % looping through each observation and pairs of variance, so N x var(Y)
    theoretical = zeros(N, length(variances_Y));% looping through each observation and pairs of variance, so N x var(Y)

    % Simulation
    for m = 1:N % looping through observation, so N can be arbitrary
        for i = 1:length(variances_Y) % calculate for each variance
            sigma_Y = variances_Y(i);
            sigma_R = variances_R(i);
            [Y, X] = gen_gaussian_sim(m, samples, u_Y, sigma_Y, sigma_R);
            a = calculate_coefficients(X, u_Y);
            Y_hat = a(1) + sum(a(2:end) .* X, 1);

            % calculating simulation MSE 
            simulation(m, i) = mean((Y - Y_hat).^2);  % using estimator to measure, which is sim
            % calculating theoretical MSE 
            theoretical(m, i) = theoretical_mse(sigma_Y, sigma_R, m); % differs depending on N, so functionize
        end
    end

    figure;
    hold on;
    colors = ['b', 'r', 'g', 'k', 'o'];

    for i = 1:length(variances_Y)
        plot(1:N, simulation(:, i), ['-' colors(i)], 'DisplayName', sprintf('simulation: varY = %.2f, varR = %.2f', variances_Y(i), variances_R(i)));
        
    end
    hold off;
    title('Linear Estimator MSE - Simulation');
    xlabel('Number of Observations');
    ylabel('MSE');
    legend('show');

    figure;
    hold on;
    colors = ['b', 'r', 'g', 'k', 'o'];

    for i = 1:length(variances_Y)
        plot(1:N, theoretical(:, i), ['-' colors(i)], 'DisplayName', sprintf('Theoretical: varY = %.2f, varR = %.2f', variances_Y(i), variances_R(i)));
        
    end
    hold off;
    title('Linear Estimator MSE - Theoretical');
    xlabel('Number of Observations');
    ylabel('MSE');
    legend('show');
end

function [Y, X] = gen_gaussian_sim(N, num_samples, u_Y, sigma_Y, sigma_R)
    Y = u_Y + sigma_Y * randn(1, num_samples); % normal gaussian distribution of Y
    R = sigma_R * randn(N, num_samples); % normal gaussian distribution of Y
    X = Y + R;
end

function a = calculate_coefficients(X, mu_Y)
    num_samples = size(X, 2); % Number of samples is the second dimension of X
    A = [ones(num_samples, 1), X']; % Concatenate a column of ones with the transposed X
    a = (A' * A) \ (A' * (mu_Y * ones(num_samples, 1))); % Solve the normal equations
end

function mse = theoretical_mse(sigma_Y, sigma_R, N)
    mse = (sigma_Y^2 * sigma_R^2) / (N * sigma_Y^2 + sigma_R^2); % using the theoretical formula in the book
end


