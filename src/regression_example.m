%% Clean Up
close all; clear; clc;

%% Data
x = linspace(0, 5, 10000);
y = round(x);
x_train = x(1:250:end);
y_train = y(1:250:end);

%% Linear
p = polyfit(x_train, y_train, 1);
y_linear = polyval(p, x);

%% Poly 5
p = polyfit(x_train, y_train, 5);
y_poly_5 = polyval(p, x);

%% Poly 10
p = polyfit(x_train, y_train, 10);
y_poly_10 = polyval(p, x);

%% Poly 15
p = polyfit(x_train, y_train, 15);
y_poly_15 = polyval(p, x);

%% Poly 20
p = polyfit(x_train, y_train, 20);
y_poly_20 = polyval(p, x);

%% Random Forest
n_trees = 500;
myRF = TreeBagger(n_trees, x_train.', y_train.', 'Method', 'regression');
y_rf = predict(myRF, x.');

%% Plot
figure; hold on; grid on;
plot(x, y, 'b', 'LineWidth', 2, 'DisplayName', 'Underlying Function: $y = \mathrm{round}(x)$')
scatter(x_train, y_train, 40, 'bo', 'filled', 'DisplayName', 'Training Data')
plot(x, y_linear, 'LineWidth', 2, 'DisplayName', 'Best-Fit Linear Model')
plot(x, y_poly_5, 'LineWidth', 2, 'DisplayName', 'Best-Fit Polynomial Model: Degree 5')
plot(x, y_poly_10, 'LineWidth', 2, 'DisplayName', 'Best-Fit Polynomial Model: Degree 10')
plot(x, y_poly_15, 'LineWidth', 2, 'DisplayName', 'Best-Fit Polynomial Model: Degree 15')
plot(x, y_poly_20, 'LineWidth', 2, 'DisplayName', 'Best-Fit Polynomial Model: Degree 20')
plot(x, y_rf, 'r', 'LineWidth', 2, 'DisplayName', 'Best-Fit Random Forest Regression Model')
xlabel('$x$'); ylabel('$y$')
title('Comparison of Linear, Polynomial, and Random Forest Regression on 1D, Quantized Data')
legend('visible', 'on', 'location', 'northwest')
prettyPlot(gcf, gca)

%% Function: prettyPlot()
function prettyPlot(gcf, gca)
set(gcf, 'units', 'normalized', 'outerposition', [0 0 0.5 1]);

% Tick Labels
set(gca, 'TickLabelInterpreter', 'latex', 'FontSize', 16);

% Axis Labels
set(gca.XLabel, 'interpreter', 'latex', 'FontSize', 16);
set(gca.YLabel, 'interpreter', 'latex', 'FontSize', 16);
set(gca.ZLabel, 'interpreter', 'latex', 'FontSize', 16);

% Title
set(gca.Title, 'interpreter', 'latex', 'FontSize', 16);

% Legend
set(gca.Legend, 'interpreter', 'latex', 'FontSize', 14);

% Subplot Group Title
myChildren = get(gcf, 'Children');
for i = 1:length(myChildren)
    if (strcmp(class(myChildren(i)), 'matlab.graphics.illustration.subplot.Text'))
        set(myChildren(i), 'interpreter', 'latex', 'FontSize', 18)
    end
end
end
