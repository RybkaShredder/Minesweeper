clear; clc; close all;
global sprites bot_coords
addpath('img/');

fig_num = 1;

sprites = {};
sprites{1} = imread('OneCell.png');
sprites{2} = imread('TwoCell.png');
sprites{3} = imread('ThreeCell.png');
sprites{4} = imread('FourCell.png');
sprites{5} = imread('FiveCell.png');
sprites{6} = imread('SixCell.png');
sprites{7} = imread('SevenCell.png');
sprites{8} = imread('EightCell.png');
sprites{9} = imread('MineCell.png');
sprites{10} = imread('UnknownCell.png');
sprites{11} = imread('ZeroCell.png');
sprites{12} = imread('FlagCell.png');
sprites{13} = imread('UnavailableCell.png');
sprites{14} = imread('RobotCell.png');


prompt = 'How many files? ';
file_num = input(prompt)

fileID = fopen('animation.txt','r');
formatSpec = '%f';

data = fscanf(fileID,formatSpec);
transition = find(data == -66);
bot_coordinates = data(1:transition - 1);
player_board = data(transition + 1: end);
bot_coords = [];
for i = 1:2:length(bot_coordinates)
    bot_coords = [bot_coords; bot_coordinates(i) bot_coordinates(i + 1)];
end
player_board = reshape(player_board, sqrt(length(player_board)), sqrt(length(player_board)))';
bot_num = size(bot_coords, 1);
%bot_coordinate = [ceil(length(player_board)/2), ceil(length(player_board)/2)];

initializeFigureWindow(1, [length(player_board), length(player_board)], 20)
draw1([length(player_board), length(player_board)], player_board)

%saveas(gcf, strcat('MinesweeperAnimation',int2str(fig_num),'.png'))
fig_num = fig_num + 1;
len_moves = 0;

for n = 1:file_num
    
    fileID = fopen(strcat("animation",int2str(n),".txt"));
    formatSpec = '%f';
    A = fscanf(fileID, formatSpec);
    
    transition0 = find(A == -77);
    transition1 = find(A == 66);
    transition2 = find(A == -66);
    bot_coordinates = A(1:transition0 - 1);
    bot_coords = [];
    for i = 1:2:length(bot_coordinates)
        bot_coords = [bot_coords; bot_coordinates(i) bot_coordinates(i + 1)];
    end
    moves = A(transition0 + 1:transition1 - 1)';
    len = length(moves);
    h = (transition2 - transition0)/(len);
    for j = 1:h - 1
       
        moves = [moves; A(transition0 + len*j + 2: (j + 1)*len + 1 + transition0)'];
       
    end    
    len_moves = len_moves + size(moves, 2);
    
    transition = transition2 + 1;
    boards = A(transition2 + 1) - 66;
    five_by_fives = eye(5);
    heat_maps = eye(5);
    solveds = eye(5);
    finals = eye(length(player_board));
    
    for i = 1: boards
        five_by_five = A(transition + 1: transition + 25);
        heat_map = A(transition + 26: transition + 50);
        solved = A(transition + 51: transition + 75);
        final = A(transition + 76: transition + 75 + length(player_board)^2);
        
        transition = transition + 76 + length(player_board)^2;
        
        five_by_five = reshape(five_by_five, 5, 5)';
        heat_map = reshape(heat_map, 5, 5)';
        solved = reshape(solved, 5, 5)';
        final = reshape(final, length(player_board), length(player_board))';
        five_by_fives(:,:,i) = five_by_five;
        heat_maps(:,:,i) = heat_map;
        solveds(:,:,i) = solved;
        finals(:,:,i) = final;
    end
        
    

    
    for m = 1:size(moves, 2)
        pause(0.1)
        previous = bot_coords;
        for k = 1:size(bot_coords, 1)
            bot_coordinate = moving(moves(k, m), [bot_coords(k, 1), bot_coords(k, 2)]);
            bot_coords(k, 1) = bot_coordinate(1);
            bot_coords(k, 2) = bot_coordinate(2);
        %pause(0.05)

            if n == 1
                draw_move([length(player_board), length(player_board)], player_board, [previous(k, 1), previous(k, 2)], bot_coordinate)
            else
                draw_move([length(player_board), length(player_board)], true_last_board, [previous(k, 1), previous(k, 2)], bot_coordinate)   
            end
            
        end
        %saveas(gcf, strcat('MinesweeperAnimation',int2str(fig_num),'.png'))
        fig_num = fig_num + 1;
    end
    
        %final_board1 = A(transition + 1: end);
        %final_board1 = reshape(final_board1, length(player_board), length(player_board))';
    
    
    for i = 1:boards
        five_by_five = five_by_fives(:,:,i);
        heat_map = heat_maps(:,:,i);
        solved = solveds(:,:,i);
        final_board = finals(:,:,i);
        
        initializeFigureWindow(1.2, [5, 5], 650);
        draw2([5, 5], five_by_five)
        pause(0.7)
    
        figure('Position', [900, 200, 600, 500])
        contourf(heat_map, 'LineColor', 'none')
        axis([1 5 1 5])
        set (gca,'Ydir','reverse')
        yticks([1:1:5])
        xticks([1:1:5])
        title("PDF of Mine in the Given 5x5 Map")
        xlabel("Column")
        ylabel("Row")
        grid on
        colorbar
        pause(0.7)
    
    
        initializeFigureWindow(1.2, [5, 5], 650);
        draw2([5, 5], solved)
        pause(0.7)
    
    
    
        initializeFigureWindow(1, [length(player_board), length(player_board)], 20)
        draw1([length(player_board), length(player_board)], final_board)
        figs = get(0,'children');
        figs(figs == gcf) = []; % delete your current figure from the list
        close(figs)
    end
    %saveas(gcf, strcat('MinesweeperAnimation',int2str(fig_num),'.png'))
    fig_num = fig_num + 1;
    fig = gcf;
    
    
    
    
    fclose('all');
    true_last_board = finals(:,:,size(finals, 3));
end
len_moves
fig_num
%{
moves = A(transition1 + 1: transition2 - 1);
five_by_five = A(transition2 + 1: transition2 + 25);
heat_map = A(transition2 + 26: transition2 + 50);
solved = A(transition2 + 51: transition2 + 75);
final_board = A(transition2 + 76: end);

player_board = reshape(player_board, sqrt(transition1 - 1), sqrt(transition1 - 1))';
five_by_five = reshape(five_by_five, 5, 5)';
heat_map = reshape(heat_map, 5, 5)';
solved = reshape(solved, 5, 5)';
final_board = reshape(final_board, sqrt(transition1 - 1), sqrt(transition1 - 1))'

bot_coordinate = [ceil(sqrt(transition1 - 1) / 2), ceil(sqrt(transition1 - 1) / 2)]

initializeFigureWindow(1, [sqrt(transition1 - 1), sqrt(transition1 - 1)], 20)

draw1([sqrt(transition1 - 1), sqrt(transition1 - 1)], player_board)

for n = 1:length(moves)
    moving(moves(n))
    pause(0.6)
    draw1([sqrt(transition1 - 1), sqrt(transition1 - 1)], player_board)
end

initializeFigureWindow(1.2, [5, 5], 420);
draw2([5, 5], five_by_five)
pause(1.5)

% figureSize = [minefieldDim(1) * multiplier*44, minefieldDim(2) * multiplier*44];

figure('Position', [700, 200, 600, 500])
contourf(heat_map, 'LineColor', 'none')
axis([1 5 1 5])
set (gca,'Ydir','reverse')
yticks([1:1:5])
xticks([1:1:5])
title("Heat Map for Likelihood of Mine in the Given 5x5 Map")
xlabel("Column")
ylabel("Row")
grid on
colorbar
pause(2)

initializeFigureWindow(1.2, [5, 5], 420);
draw2([5, 5], solved)
pause(1.5)
close(2)

initializeFigureWindow(1, [sqrt(transition1 - 1), sqrt(transition1 - 1)], 20)

draw1([sqrt(transition1 - 1), sqrt(transition1 - 1)], final_board)

close(1)
%}
    
function bot_coordinate = moving(move, bot_coordinate)
    if move == 0
        bot_coordinate(1) = bot_coordinate(1) - 1;
    elseif move == 1
        bot_coordinate(2) = bot_coordinate(2) - 1;
    elseif move == 2
        bot_coordinate(1) = bot_coordinate(1) + 1;
    else
        bot_coordinate(2) = bot_coordinate(2) + 1;
    end
    return
end

function draw_move(minefieldDim, board, previous, bot_coordinate)
    global sprites bot_coords
    image([(bot_coordinate(2)-1)*35,(bot_coordinate(2))*35],[(minefieldDim(1)-(bot_coordinate(1))+1)*35,(minefieldDim(1)-(bot_coordinate(1)))*35], sprites{14});
    x = [(previous(2)-1)*35,(previous(2))*35];
    y = [(minefieldDim(1)-(previous(1))+1)*35,(minefieldDim(1)-(previous(1)))*35];
    z = board(previous(1), previous(2));
    if board(previous(1), previous(2)) == 0
        image([(previous(2)-1)*35,(previous(2))*35],[(minefieldDim(1)-(previous(1))+1)*35,(minefieldDim(1)-(previous(1)))*35], sprites{11})
    else
        image([(previous(2)-1)*35,(previous(2))*35],[(minefieldDim(1)-(previous(1))+1)*35,(minefieldDim(1)-(previous(1)))*35], sprites{board(previous(1), previous(2))});
    end
    for n = 1:size(bot_coords, 1)
        if previous(1) == bot_coords(n, 1) && previous(2) == bot_coords(n, 2)
            image([(previous(2)-1)*35,(previous(2))*35],[(minefieldDim(1)-(previous(1))+1)*35,(minefieldDim(1)-(previous(1)))*35], sprites{14})
        end
    end
        
    
end

function draw1(minefieldDim, board)
    global sprites bot_coords
    for i = 1:minefieldDim(1)
        for j = 1:minefieldDim(2)
            for k = 1:size(bot_coords, 1)
                if (i == bot_coords(k, 1) && j == bot_coords(k, 2))
                    image([(j-1)*35,j*35],[(minefieldDim(1)-i+1)*35,(minefieldDim(1)-i)*35], sprites{14});
                elseif board(i, j) == -1
                    image([(j-1)*35,j*35],[(minefieldDim(1)-i+1)*35,(minefieldDim(1)-i)*35], sprites{10});
                elseif board(i, j) == -2
                    image([(j-1)*35,j*35],[(minefieldDim(1)-i+1)*35,(minefieldDim(1)-i)*35], sprites{12});
                elseif board(i, j) == 0
                    image([(j-1)*35,j*35],[(minefieldDim(1)-i+1)*35,(minefieldDim(1)-i)*35], sprites{11});
                elseif board(i, j) == -3
                    image([(j-1)*35,j*35],[(minefieldDim(1)-i+1)*35,(minefieldDim(1)-i)*35], sprites{13});
                else
                    image([(j-1)*35,j*35],[(minefieldDim(1)-i+1)*35,(minefieldDim(1)-i)*35], sprites{board(i, j)});
                end
            end
        end
    end
    for k = 1:size(bot_coords, 1)
        image([(bot_coords(k,2)-1)*35,(bot_coords(k,2))*35],[(minefieldDim(1)-(bot_coords(k,1))+1)*35,(minefieldDim(1)-(bot_coords(k,1)))*35], sprites{14});

    end
end

function draw2(minefieldDim, board)
    global sprites
    for i = 1:minefieldDim(1)
        for j = 1:minefieldDim(2)
            if board(i, j) == -1
                image([(j-1)*35,j*35],[(minefieldDim(1)-i+1)*35,(minefieldDim(1)-i)*35], sprites{10});
            elseif board(i, j) == -2
                image([(j-1)*35,j*35],[(minefieldDim(1)-i+1)*35,(minefieldDim(1)-i)*35], sprites{12});
            elseif board(i, j) == 0
                image([(j-1)*35,j*35],[(minefieldDim(1)-i+1)*35,(minefieldDim(1)-i)*35], sprites{11});
            elseif board(i, j) == -3
                image([(j-1)*35,j*35],[(minefieldDim(1)-i+1)*35,(minefieldDim(1)-i)*35], sprites{13});
            else
                image([(j-1)*35,j*35],[(minefieldDim(1)-i+1)*35,(minefieldDim(1)-i)*35], sprites{board(i, j)});
            end

        end
    end
end





function initializeFigureWindow(multiplier, minefieldDim, xcoord)
    %Creates a figure window with defined properties
    
    %Get the screensize and figure size
    screenSize = get(0, 'ScreenSize');
    %44x44 for full size
    figureSize = [minefieldDim(1) * multiplier*44, minefieldDim(2) * multiplier*44];
    
    %Get the centered offset for the figure window
    xpos = (screenSize(3)-figureSize(1))/2;
    ypos = (screenSize(4)-figureSize(2))/2;
    
    figure('Position', [xcoord, ypos, figureSize(1), figureSize(2)])  %Center and size the figure windo);              %Set figure title
       
    hold('on');
    axis([0, minefieldDim(1)*35, 0, minefieldDim(2)*35]);
    axis('off');
end


function full_board(multiplier, minefieldDim, xcoord, k)
    %Creates a figure window with defined properties
    
    %Get the screensize and figure size
    screenSize = get(0, 'ScreenSize');
    %44x44 for full size
    figureSize = [minefieldDim(1) * multiplier*44, minefieldDim(2) * multiplier*44];
    
    %Get the centered offset for the figure window
    xpos = (screenSize(3)-figureSize(1))/2;
    ypos = (screenSize(4)-figureSize(2))/2;
    name = 'Board' + int2str(k);
    
    figure('Position', [xcoord, ypos, figureSize(1), figureSize(2)], 'Name', name)  %Center and size the figure windo);              %Set figure title
       
    hold('on');
    axis([0, minefieldDim(1)*35, 0, minefieldDim(2)*35]);
    axis('off');
end