import pygame
black = (0, 0, 0) #color of frame
white = (255, 255, 255) #color of fill

red = (255, 0, 0) #marker color
WIDTH = 20 
HEIGHT = 20 
MARGIN = 5 #tickness of line
grid = [] #2D array/empty list
for row in range(9): #make grid 9x9
    grid.append([])
    for column in range(9):
        grid[row].append(0) #marge cell
grid[1][5] = 0 #marked squer, when open the game field
pygame.init()
window_size = [230, 230] #game fied size
scr = pygame.display.set_mode(window_size)
pygame.display.set_caption("Grid") #name of the window
done = False
clock = pygame.time.Clock() #screen refresh speed
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)
    scr.fill(black) #background color
    for row in range(9):
        for column in range(9):
            color = white
            if grid[row][column] == 1:
                color = red
            a=input("")
            #pygame.draw.rect(scr,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT]) #draw red squer
    clock.tick(50) #limit of the frames per second
    pygame.display.flip() #update the screen with what we have drawn
pygame.quit()